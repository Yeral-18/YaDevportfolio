# System Diagram — YaDev CMS

> Producción real desde Phase 3 cierre (2026-05-06). Tres servicios live en
> Railway (`api`, `studio`, `runner`) más un cron de backups (`cms-backups`),
> consumidos por tres sitios cliente publicados en Hostinger shared. Para la
> variante local-first ver [`../infra/README.md`](../infra/README.md).

## Topología actual

```mermaid
graph TB
  subgraph Railway["Railway Cloud (yadev-cms project)"]
    API[yadev-cms-api<br/>Laravel 11 + PHP 8.3<br/>api.yadev.co]
    STUDIO[yadev-cms-studio<br/>SvelteKit static SPA<br/>studio.yadev.co]
    RUNNER[yadev-cms-runner<br/>Node 22 + Fastify + BullMQ]
    MYSQL[(MySQL 8<br/>yadev_cms_central<br/>+ tenant_* DBs)]
    REDIS[(Redis 7<br/>BullMQ queue + cache)]
    BACKUPS[cms-backups<br/>cron 0 8 UTC<br/>mysqldump + mc cp]
  end

  subgraph Hostinger["Hostinger Static Hosting"]
    LUQRA[luqra-web<br/>luqraingenieria.com]
    ECOMAG[ecomag-web<br/>ecomagsas.com]
    MULTI[multiservicios-web<br/>multiserviciospj.com]
  end

  subgraph External["External services"]
    B2[(BackBlaze B2<br/>yadev-cms-backups bucket<br/>retention 30d)]
    SENTRY[Sentry<br/>3 projects: api / studio / runner]
    M365[Microsoft 365<br/>SMTP outbound<br/>per-tenant]
  end

  STUDIO -->|REST /v1<br/>Bearer Sanctum| API
  API --> MYSQL
  API --> REDIS
  API -->|POST /webhook/build<br/>HMAC-SHA256| RUNNER
  RUNNER -->|GET /v1/runner/build-bundle<br/>HMAC-SHA256| API
  RUNNER -->|rsync over SSH| LUQRA
  RUNNER -->|rsync over SSH| ECOMAG
  RUNNER -->|rsync over SSH| MULTI
  RUNNER -->|POST /v1/.../publishes/{id}/complete<br/>HMAC-SHA256| API
  BACKUPS -->|mysqldump| MYSQL
  BACKUPS -->|mc cp| B2
  API -.->|errors 5xx + unhandled| SENTRY
  STUDIO -.->|window.onerror + unhandledrejection| SENTRY
  RUNNER -.->|worker.failed events| SENTRY
  API -->|password reset, verify-email,<br/>form notifications| M365
```

## Sitios cliente vivos

| Tenant | Dominio | Hosting | Correo | Estado | Última publicación |
|--------|---------|---------|--------|--------|--------------------|
| Luqra Ingeniería | luqraingenieria.com | Hostinger shared | M365 | Live (rebrand de Multiservicios) | Phase 3 |
| ECOMAG S.A.S | ecomagsas.com | Hostinger shared | M365 | Live | Phase 2 cutover |
| Multiservicios P&J | multiserviciospj.com | Hostinger shared | M365 | Live (legacy, pendiente DNS cutover a Luqra) | Phase 1 |

Los tres sitios consumen el API en build time (no en runtime). El Runner
empuja `dist/` por rsync sobre SSH al `public_html/` de Hostinger;
Hostinger sirve solo estático + el `contact.php` heredado.

## Servicios Railway

| Servicio | Tipo | Responsabilidad | Tests | Notas |
|----------|------|-----------------|-------|-------|
| `yadev-cms-api` | Web (Dockerfile, php-fpm + nginx) | API REST `/v1`, multi-tenant DB-per-tenant, 2FA TOTP, Forms, Activity log, Search | ~390 feature tests | `api.yadev.co`, healthcheck `/health` |
| `yadev-cms-studio` | Web (static, Vite build) | SPA admin SvelteKit + shadcn-svelte | 973 vitest + 8 specs Playwright e2e (WCAG AA) | `studio.yadev.co`, healthcheck `/` |
| `yadev-cms-runner` | Worker (Node + Fastify) | Webhook `/webhook/build`, BullMQ pipeline 6 pasos (clone → fetch JSON → render → image variants `sharp` → sitemap → rsync) | 146 tests (unit + integration) | Privado, alcanzado por API vía red interna Railway |
| `MySQL` | Plugin Railway | DB central + tenant DBs | — | Sólo accesible desde la red interna del proyecto |
| `Redis` | Plugin Railway | BullMQ queue + Laravel cache | — | Mismo aislamiento |
| `cms-backups` | Cron (0 8 * * *) | mysqldump → gzip → mc cp a B2 | — | Retention 30d, ver [`../infra/scripts/setup-backups-railway.md`](../infra/scripts/setup-backups-railway.md) |

## Flujo: editar bloque → publicar

```
Cliente (Luqra)
  │
  │ 1. POST https://api.yadev.co/v1/auth/login
  │    body { email, password, device_name }
  │    respuesta { token, user, tenants[] }
  │    (si 2FA enabled: 200 { challenge_id } → POST /v1/auth/2fa/challenge)
  │
  ▼
Studio (studio.yadev.co)
  │
  │ 2. GET /v1/tenants/{tenant_id}/pages?with=sections.blocks
  │    middleware: auth:sanctum + tenant.path
  │
  │ 3. PUT /v1/tenants/{tenant_id}/blocks/{id}
  │    body { data: { ... } } → BlockSchema valida → guarda en tenant DB
  │    BlockVersion auto-creado (versioning BBC)
  │    ActivityLog graba quién/qué/cuándo
  │
  │ 4. POST /v1/tenants/{tenant_id}/publishes
  │    body { page_ids?: [int], commit_sha?: string }   ← page_ids opcional para parcial
  │    INSERT publishes status=pending
  │
  ▼
API → Runner (HMAC)
  │
  │ 5. POST runner.internal/webhook/build
  │    body { publishId, tenantId, pageIds, callbackUrl }
  │    Runner valida HMAC → enqueue BullMQ → 202 { jobId }
  │    API: UPDATE publishes status=queued, runner_job_id=jobId
  │
  ▼
Runner BullMQ worker (6 pasos)
  │
  │ 6. clone/pull repo del sitio → fetch content tree del API
  │    → render Astro → sharp image variants → sitemap.xml
  │    → rsync -az --delete dist/ user@hostinger:/public_html/
  │
  │ 7. POST https://api.yadev.co/v1/tenants/{tenant_id}/publishes/{id}/complete
  │    headers: X-YaDev-Signature: sha256=…
  │    body { status: success|failed, build_log_url, commit_sha, error_message? }
  │
  ▼
API
  │
  │ 8. tenancy()->initialize($tenant_id)
  │    UPDATE publishes status=completed|failed completed_at=now
  │    Studio polea cada 2-3s y ve el resultado
```

## Resolución de tenant (recordatorio)

| Fuente | Middleware | Caso de uso |
|--------|-----------|-------------|
| `Authorization: Bearer {token}` con ability `tenant:{id}:*` | `auth:sanctum` + `tenant.path` | Studio → API |
| `tenant_id` en URL path | `tenant.path` valida que coincida con la ability del token | Todas las rutas tenant-scoped |
| HMAC `X-YaDev-Signature` sin bearer | Validado en controller (`PublishController::complete`) | Runner → API callback |
| `Origin` header contra `central.domains` | `ResolveTenantFromOrigin` | Form submits públicos (`/v1/public/forms/{id}/submit`) |

Inconsistencia entre fuentes ⇒ 404 (no 403, evita leak), log
`cross_tenant_attempt`. Detalle en [`security-model.md`](security-model.md) §1.

## Redes y puertos

| Servicio | Puerto público | Acceso interno | TLS |
|---------|---------------|----------------|-----|
| `api.yadev.co` | 443 (Railway edge) | http://api.railway.internal:8080 | Edge (Railway-managed) |
| `studio.yadev.co` | 443 (Railway edge) | static, sin backend propio | Edge |
| `yadev-cms-runner` | — | http://runner.railway.internal:8080 | sólo red interna |
| `MySQL` | — | mysql.railway.internal:3306 | sólo red interna |
| `Redis` | — | redis.railway.internal:6379 | sólo red interna |
| Hostinger shared (3 sitios) | 443 | — | Hostinger-managed (incluye www) |

Producción nunca expone MySQL/Redis a internet — sólo al network privado
de Railway. Los sitios cliente reciben rsync por SSH (autenticación por
key, sin password) desde el Runner.

## Backups y resiliencia

- **MySQL**: cron `cms-backups` a las 08:00 UTC = 03:00 Bogotá, todas las
  DBs (central + tenants) con `mysqldump --single-transaction`, gzip,
  upload a `s3://yadev-cms-backups/yadev-cms/backups/YYYY-MM-DD/`.
  Retention 30 días (objetos viejos borrados por el script).
  Ver [`../infra/scripts/setup-backups-railway.md`](../infra/scripts/setup-backups-railway.md).
- **Redis**: efímero (queue + cache). No se respalda.
- **Media**: en Phase 3 vive en MinIO local (dev) y en B2 (prod) bajo
  `s3://yadev-cms-media/`, atrás del CDN de Hostinger en cada sitio.
- **Sitios cliente**: Hostinger shared incluye snapshots semanales nativos.
- **Sentry**: 3 proyectos (`yadev-cms-api`, `yadev-cms-studio`,
  `yadev-cms-runner`), free tier 5k events/mes con `before_send` que
  filtra 401/403/404/422 para mantener la señal limpia. Setup completo en
  [`../infra/MONITORING.md`](../infra/MONITORING.md).
- **DR plan**: restaurar desde B2 (`gunzip | mysql`) sobre Railway MySQL
  + redeploy de api/studio/runner desde GitHub. RTO ~30 min, RPO 24 h.

## Variante local-first (dev)

Idéntica a producción pero todos los servicios corren en Docker Compose
(`infra/docker-compose.yml`): `mysql:8.0`, `redis:7-alpine`, `mailpit`
(SMTP capture), `minio` (S3-compatible) y `api` (Laravel bind-mounted).
El Studio corre fuera del compose con `pnpm dev`. Subdominios fake via
`hosts`: `api.yadev.local`, `studio.yadev.local`, `{slug}.yadev.local`.
No hay TLS, no se hace rsync — el Runner se invoca con
`RUNNER_DRY_RUN=1` para validar el pipeline sin tocar Hostinger.

## Componentes pendientes / opcionales

- **VPS Hostinger KVM2**: ya no es necesario en el plan actual (Railway
  reemplazó el VPS); la doc `phases/phase-vps-migration.md` queda como
  referencia histórica.
- **AI endpoints (Phase 3)**: `/v1/tenants/{id}/ai/seo-audit`,
  `/suggest-copy`, `/rewrite-tone`. Código mergeado, deshabilitado en
  prod (degrada a 503 cuando `ANTHROPIC_API_KEY` está vacío).
- **DNS cutover Multiservicios → Luqra**: pendiente manual (Angel).
- **Marketing landing yadev.co**: el dominio raíz sirve el Studio hoy;
  la landing pública es opcional post-MVP.
