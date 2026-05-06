# YADEV CMS — CLAUDE.md

> Instrucciones para sesiones futuras de Claude Code que trabajen dentro de `yadev-cms/`.
> Este archivo es el reemplazo del CLAUDE.md raíz cuando el CWD está aquí dentro.

---

## Contexto rápido

Proyecto: **YaDev CMS** — gestor de contenidos multi-tenant headless para clientes de YA Dev.
Fundador y único operador: **Angel** (`angelpelaezca@gmail.com`).
Objetivo: reemplazar edición manual de componentes `.astro` por panel web self-service.
Modelo de referencia: Damos.co (pero con look YaDev y stack propio).
Estado actual (2026-05-06): **Phase 3 cerrada**. Stack producción completo.
- API Laravel 11 con ~390 feature tests, multi-tenant DB-per-tenant, 2FA TOTP, Forms, Activity log, Search, Block templates + versioning, Page duplicate + bulk publish (`page_ids[]`).
- Studio SvelteKit con 973 vitest + 8 specs Playwright e2e, WCAG AA pass.
- Runner Node con 146 tests, sharp image variants, sitemap, pipeline de 6 pasos.
- 3 sitios cliente live: Luqra (`luqraingenieria.com`), ECOMAG (`ecomagsas.com`), Multiservicios (`multiserviciospj.com`) — todos en Hostinger shared, deploy por rsync desde el Runner.
- Hosting de la plataforma: Railway (`api.yadev.co`, `studio.yadev.co`, `yadev-cms-runner` interno, MySQL plugin, Redis plugin, cron `cms-backups`).
- Infra: Backups B2 cron daily 08:00 UTC, Sentry monitoring 3 servicios con `before_send` filtrando 401/403/404/422, MinIO local + B2 prod.

Pendientes manuales (Angel, no automatizables desde Claude):
1. Comprar `yadev.co` (si todavía no) + opcional Hostinger KVM2 VPS si se quiere reemplazar Railway.
2. `ANTHROPIC_API_KEY` + billing (Phase 3 AI dormant, endpoints degradan a 503 sin la key).
3. DNS cutover Multiservicios → Luqra.
4. `RAILWAY_API_TOKEN` env del runner para auto-redeploys de sitios cliente.
5. BackBlaze B2 + Railway cron `cms-backups` — guía: [`infra/scripts/setup-backups-railway.md`](infra/scripts/setup-backups-railway.md).
6. Sentry org + 3 DSNs — guía: [`infra/MONITORING.md`](infra/MONITORING.md).

Detalle topológico: [`architecture/system-diagram.md`](architecture/system-diagram.md). Detalle de deploy: [`architecture/deployment.md`](architecture/deployment.md).

> **Scope del CMS (importante):** Este subproyecto lo desarrolla Angel solo. Yeral (Lead Developer listado en el portfolio raíz `index.html`) colabora en los sitios de clientes del monorepo `YaDevportfolio/`, pero **NO participa** en `yadev-cms/`. Cualquier decisión, acceso, tenant admin, clave o credencial del CMS pertenece únicamente a Angel.

### Arquitectura de dominios (decidida)

**Dev local-first (Docker Compose):**
- Stack via Docker Compose (`infra/docker-compose.yml`): mysql, redis, mailpit, minio, api.
- Subdominios fake via `C:\Windows\System32\drivers\etc\hosts`:
  - `api.yadev.local` → Laravel API (puerto 8000).
  - `studio.yadev.local` → SvelteKit studio (puerto 5173).
  - `{tenant}.yadev.local` → testing multi-tenant.
- SSL no aplica en dev — HTTP plano, CORS permite `http://studio.yadev.local:5173` explícitamente.
- Studio se levanta fuera del compose con `pnpm dev`.

**Producción (Railway, ya activa):**
- Dominio maestro: **`yadev.co`** y **`studio.yadev.co`** → servicio `yadev-cms-studio` (SvelteKit static SPA).
- **`api.yadev.co`** → servicio `yadev-cms-api` (Laravel 11 + php-fpm + nginx, Dockerfile).
- **`yadev-cms-runner`** → servicio interno (Node + Fastify + BullMQ), sólo accesible vía red interna Railway desde la API.
- **`MySQL`** y **`Redis`** plugins Railway dentro del mismo proyecto.
- **`cms-backups`** cron (`0 8 * * *` UTC) → mysqldump + mc cp a BackBlaze B2.
- **Dominios cliente** (`luqraingenieria.com`, `ecomagsas.com`, `multiserviciospj.com`) — siguen en Hostinger shared, sitios Astro estáticos, hacen fetch al API en build time, deploy por rsync sobre SSH desde el Runner.
- **Resolución de tenant:** por token Sanctum (panel) o por `tenant_id` en la URL (`api.yadev.co/v1/tenants/{tenant_id}/...`). Origin header validado contra whitelist `central.domains` para form submits públicos. Runner→API usa HMAC sin Sanctum.

### Repositorios GitHub (decididos)

Organización: **`yadevOs/`** (con esa capitalización exacta, ya creada).

Los 3 repos están clonados como subcarpetas de este subproyecto:

- `yadevOs/yadev-cms-api` → `yadev-cms/api/` — backend Laravel 11 (DB-per-tenant con stancl/tenancy v3).
- `yadevOs/yadev-cms-studio` → `yadev-cms/studio/` — panel admin SvelteKit + shadcn-svelte (look YaDev dark glassmorphism).
- `yadevOs/yadev-cms-infra` → `yadev-cms/infra/` — Docker Compose (local-first), nginx vhosts, scripts, deploy pipelines (activados en Fase VPS-migration).

Repos de sitios cliente (`yadevOs/site-multiservicios`, `yadevOs/site-ecomag`, etc.) siguen separados, uno por cliente.

### Pricing

Pricing del servicio: **TBD post-MVP**. Se define cuando haya data real de costos de operación (VPS, storage, ancho de banda, tiempo de soporte). No tomar decisiones de arquitectura basadas en tiers actuales.

**NO tocar fuera de `yadev-cms/`.** Los proyectos de producción viven en:
- `internal/PROYECTOS/2026/ECOMAG02/`
- `internal/PROYECTOS/2026/MULTISERVICIOS P&J/`
- `index.html`, `main.js`, `proyectos/`, `Modelos/`, `design-system/`

Trátalos como read-only excepto si Angel pide explícitamente "migra Multiservicios al CMS" y ya estás en Fase 1+.

---

## Stack técnico (decidido, no cuestionar)

```
Backend:       Laravel 11 + PHP 8.3
DB:            MySQL 8 (central + una por tenant vía stancl/tenancy v3)
Auth:          Laravel Sanctum (token SPA)
RBAC:          spatie/laravel-permission
Mediateca:     spatie/medialibrary + Intervention Image
Object store:  MinIO local (S3-compatible, Fase 0-2) → BackBlaze B2 en producción
SMTP testing:  Mailpit local (puerto 1025 SMTP + 8025 UI) en Fase 0-2
Email prod:    Resend o Amazon SES (post Fase VPS-migration)
Queue:         Redis + Laravel Horizon
API:           REST versionado (/v1/...)
Panel:         SvelteKit + Tailwind + shadcn-svelte
Editor:        TipTap
Frontend cliente: Astro 5.18 + Svelte 5.53 (existente, se refactoriza)
Runner:        Node + PM2 (webhook → build → rsync)
Hosting:       Local Docker Compose (Fase 0-2) → VPS Hostinger KVM2 $8/mes (producción)
Sitios cliente: Hostinger shared (no cambia entre fases)
IA:            Anthropic SDK (Claude Haiku 4.5 por defecto, Sonnet 4.6 para tareas complejas, con prompt caching)
```

---

## Estructura del subproyecto

```
yadev-cms/
├── BLUEPRINT.md                  ← Plan ejecutivo (histórico)
├── CLAUDE.md                     ← ESTE ARCHIVO
├── READY-FOR-REVIEW.md           ← Preguntas históricas para Angel
├── architecture/
│   ├── system-diagram.md         ← Topología Railway + Hostinger
│   ├── deployment.md             ← Env vars, smoke tests, rollback, DNS
│   ├── multi-tenancy-strategy.md
│   ├── api-contract.md           ← /v1/* completo
│   ├── auth-decision.md          ← Sanctum bearer Phase 1 → cookies Phase 2
│   ├── publish-flow.md           ← Handshake API ↔ Runner
│   ├── security-model.md
│   └── security-audit-post-v4.md
├── phases/
│   ├── phase-0-setup.md          ← Histórico
│   ├── phase-1-mvp.md
│   ├── phase-2-parity.md
│   ├── phase-3-ai.md             ← Mergeado, dormant sin ANTHROPIC_API_KEY
│   └── phase-vps-migration.md    ← Histórico (reemplazado por Railway)
├── api/                          ← Laravel 11 app (sub-repo yadevOs/yadev-cms-api)
├── studio/                       ← SvelteKit app (sub-repo yadevOs/yadev-cms-studio)
├── runner/                       ← Node webhook runner (sub-repo yadevOs/yadev-cms-runner)
├── infra/                        ← Docker Compose + scripts + runbooks (sub-repo yadevOs/yadev-cms-infra)
│   ├── docker-compose.yml
│   ├── MONITORING.md             ← Sentry setup
│   ├── README.md
│   ├── cron-backup/              ← Imagen para servicio Railway cms-backups
│   └── scripts/
│       ├── setup-backups-railway.md
│       ├── restore-prod.md
│       └── …
├── database/
├── agents-orchestration.md
├── multiservicios-migration-plan.md
└── risks-and-tradeoffs.md
```

---

## Reglas críticas para este subproyecto

### 1. Seguridad multi-tenant ABSOLUTA
- Cada endpoint API debe validar `tenant_id` DEL TOKEN, no del payload.
- Prohibido: `Model::find($id)` sin scope de tenant. Siempre usar `TenantModel::find($id)` que filtra por conexión de DB.
- Test obligatorio: "usuario del tenant A intenta leer recurso del tenant B" → debe devolver 404, NO 403 (no filtrar existencia).

### 2. No romper los sitios en producción
- ECOMAG y Multiservicios están live. El CMS NO se conecta a ellos hasta que un tenant esté 100% migrado y Angel apruebe el cutover.
- Migración = dual-write por 1 semana (contenido hardcodeado + JSON del API). Luego se remueve el hardcode.

### 3. Schema-first
- Todos los bloques (Hero, Services, etc.) se definen con un schema JSON (Zod en el panel, validación Laravel en el API).
- Si agregas un bloque nuevo, DEBES:
  1. Definir schema en `api/app/Blocks/{Name}/schema.php`.
  2. Renderer en `admin/src/lib/blocks/{Name}.svelte`.
  3. Mapper a Astro en `runner/transformers/{name}.mjs`.
  4. Test de contrato.

### 4. Respetar el look YaDev
- Dark theme (`#0a0a0b` base), glassmorphism sutil, Space Grotesk para headings, Inter para body.
- Indigo/purple para acciones primarias, no azul genérico de Material.
- shadcn-svelte como base, pero customizar tokens antes de usar cualquier componente.
- Zero emojis en UI (al estilo Linear).

### 5. Colombiano first
- UI en español colombiano: "Publicar cambios" > "Guardar". "Cotizar" > "Solicitar presupuesto".
- Moneda COP por defecto en cualquier módulo de facturación futuro.
- WhatsApp como canal de notificación prioritario (vía API Cloud de Meta) cuando Angel necesite alertas.

---

## Convenciones de código

**Laravel:**
- PSR-12, strict types on.
- Form Requests para toda validación.
- Service classes para lógica compleja (no Fat Controller, no Fat Model).
- Enums PHP 8.3 para estados (PageStatus, BlockType, etc.).
- Route model binding con constraint: `Route::get('/pages/{page:slug}')`.

**SvelteKit:**
- Svelte 5 runes (`$state`, `$derived`, `$effect`). Nunca `let` reactivo legacy.
- TypeScript estricto.
- SvelteKit `load` functions para data fetching, nunca `onMount + fetch`.
- Stores con `$state` en vez de `writable()` salvo que el estado sea compartido cross-route.

**API REST:**
- `/api/v1/...` siempre versionado.
- Nombres plurales para recursos (`/pages`, `/blocks`).
- JSON:API-ish: `{ data: {...}, meta: {...}, links: {...} }`.
- HTTP status correctos: 201 create, 204 delete, 422 validation, 404 not found.
- Rate limiting: 60 req/min authenticated, 20 req/min anon.

---

## Agentes y skills disponibles

Mismos que el CLAUDE.md raíz:
- **Agentes:** project-orchestrator (este), code-reviewer, content-marketer, devops-engineer, frontend-developer, security-auditor, seo-specialist, Explore, Plan, general-purpose.
- **Skills:** simplify, review, security-review, ui-ux-pro-max, nano-banana-2, claude-api, init, loop, schedule.

Ver `agents-orchestration.md` para mapeo específico de qué agente/skill usar en cada tarea del CMS.

---

## Comandos recurrentes (Fase 1+)

```bash
# Backend
cd api && composer install
php artisan tenants:create multiservicios --domain=multiserviciospj.com
php artisan migrate --tenants
php artisan queue:work --queue=publish,default

# Panel
cd admin && pnpm install && pnpm dev

# Runner
cd runner && pnpm install && pm2 start ecosystem.config.cjs

# Tests
cd api && php artisan test --parallel
cd admin && pnpm test
```

---

## Qué NO hacer en este subproyecto

- NO usar Filament para el panel admin (se decidió SvelteKit custom).
- NO usar Blade templates (API es headless).
- NO usar SMTP desde el VPS para mail transaccional — usar Resend o Amazon SES (el VPS Hostinger tiene IPs rate-limitadas).
- NO guardar media binaria en la DB. Siempre en filesystem o S3-compatible.
- NO hacer `DB::statement(raw SQL)` sin sanitizar. Eloquent + Query Builder siempre.
- NO commitear `.env`. Sí commitear `.env.example`.
- NO crear un tenant nuevo sin probar el flujo completo (create → seed → login → edit → publish) en staging primero.

---

## Contacto de YaDev (referencia)
- WhatsApp principal: +57 300 477 3174
- WhatsApp secundario: +57 300 752 8265
- Email: yadevsistem@gmail.com
- NUNCA inventar números ni emails en seeds/demos.
