# System Diagram — YaDev CMS

> Dos variantes:
> - **Local-first (Fase 0-2):** todo corre en la máquina de Yeral con Docker Compose + subdominios fake `.yadev.local`. Ver sección "Variante local-first" abajo.
> - **Producción (post Fase VPS-migration):** VPS Hostinger + dominio real `yadev.co`. Ver sección "Variante producción".

## Variante local-first (Fase 0-2)

```
                        LAPTOP DE YERAL (Windows 11)
                                   │
                                   ▼
               ┌──────────────────────────────────────┐
               │ C:\Windows\System32\drivers\etc\hosts│
               │  127.0.0.1  api.yadev.local          │
               │  127.0.0.1  studio.yadev.local       │
               │  127.0.0.1  multiservicios.yadev.local│
               │  127.0.0.1  ecomag.yadev.local       │
               └──────────────────────────────────────┘
                                   │
                  ┌────────────────┼────────────────────┐
                  ▼                ▼                    ▼
        ┌─────────────┐   ┌──────────────┐   ┌─────────────────────┐
        │ Laravel API │   │ SvelteKit    │   │ Docker Compose      │
        │ php artisan │   │ Studio       │   │ (infra/)            │
        │ serve       │   │ pnpm dev     │   │                     │
        │ :8000       │   │ :5173        │   │ mysql:8.0 :3306     │
        │             │   │              │   │ redis:7 :6379       │
        │  Conecta a: │   │  Conecta a:  │   │ mailpit :1025/:8025 │
        │  - mysql    │◄──┼──────────────┼──►│ minio :9000/:9001   │
        │  - redis    │   │  http://api. │   │                     │
        │  - mailpit  │   │  yadev.local │   │ volumes:            │
        │  - minio    │   │  :8000/v1    │   │  mysql-data         │
        │             │   │              │   │  redis-data         │
        └─────────────┘   └──────────────┘   │  minio-data         │
                                             └─────────────────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │ infra/backups/      │
                        │  YYYY-MM-DD/        │
                        │   dbs.sql.gz        │
                        │   mediateca.tar.gz  │
                        │ Retención 7 días    │
                        └─────────────────────┘
```

Sitios cliente en Hostinger shared siguen vivos, pero en Fase 0-2 **no se tocan** — el build Astro se genera local y no se rsync-ea todavía. El dual-write real llega en Fase 1 semana 4 cuando Yeral decida mover el primer cambio a producción, usando rsync desde la laptop (o delegando el webhook al VPS post Fase VPS-migration).

## Variante producción (post Fase VPS-migration)

Idéntico al diagrama de abajo, pero todos los containers (mysql, redis, minio o B2, mailpit reemplazado por Resend/SES) corren en el VPS, Laravel+SvelteKit sirven detrás de Nginx con SSL, y los subdominios resuelven via DNS real.

```
                           INTERNET
                              │
                              ▼
              ┌───────────────────────────────────┐
              │   DNS (Hostinger DNS / Cloudflare)│
              │  yadev.co             → VPS       │  (marketing landing, Fase 2)
              │  api.yadev.co         → VPS       │  (Laravel headless)
              │  studio.yadev.co      → VPS       │  (SvelteKit panel)
              │  multiserviciospj.com → Shared    │
              │  ecomagsas.com        → Shared    │
              │  poronsas.com         → Shared    │
              │  coisem.com           → Shared    │
              └───────────────────────────────────┘
                              │
              ┌───────────────┴────────────────┐
              ▼                                ▼
  ┌──────────────────────┐        ┌─────────────────────────┐
  │  VPS KVM2 (Ubuntu)   │        │ Hostinger SHARED        │
  │  api.yadev.co        │        │ (sitios públicos live)  │
  │  studio.yadev.co     │        │                         │
  │                      │        │ /public_html/           │
  │  Nginx (443 SSL)     │        │  ├─ multiserviciospj/   │
  │   ├─ /api → php-fpm  │        │  │   ├─ assets/         │
  │   └─ /admin → static │        │  │   ├─ index.html      │
  │                      │        │  │   ├─ contact.php     │
  │  PHP 8.3 FPM         │        │  │   └─ .htaccess       │
  │   └─ Laravel 11 API  │        │  └─ ecomagsas/          │
  │                      │        │                         │
  │  MySQL 8             │        │  (no ejecuta PHP        │
  │   ├─ yadev_central   │        │   más allá del          │
  │   │   ├─ tenants     │        │   contact.php)          │
  │   │   ├─ domains     │        └─────────────────────────┘
  │   │   ├─ users       │                    ▲
  │   │   └─ subscriptions                    │
  │   ├─ tenant_multiservicios                │ rsync -az
  │   │   ├─ pages       │                    │ sobre SSH
  │   │   ├─ blocks      │        ┌───────────┴──────────┐
  │   │   ├─ media       │        │ Webhook Runner (Node)│
  │   │   └─ forms       │        │ PM2 daemon           │
  │   ├─ tenant_ecomag   │        │ escucha 8080         │
  │   └─ tenant_poron    │───────►│  /webhook/rebuild    │
  │                      │HMAC    │  → git pull          │
  │  Redis               │        │  → render JSON       │
  │   ├─ sesiones        │        │  → npm run build     │
  │   ├─ cache           │        │  → rsync → shared    │
  │   └─ queue jobs      │        │  → callback al API   │
  │                      │        └──────────────────────┘
  │  Horizon dashboard   │                   │
  │   (admin only)       │                   │
  │                      │        ┌──────────▼──────────┐
  │  certbot / cron      │        │ /srv/builds/        │
  │                      │        │  ├─ multiservicios/ │
  └──────────────────────┘        │  ├─ ecomag/         │
              │                   │  └─ poron/          │
              │                   └─────────────────────┘
              │                              ▲
              ▼                              │
  ┌──────────────────────┐                   │
  │ SvelteKit Panel Admin│                   │
  │ (build estático en   │                   │
  │  Nginx, served desde │                   │
  │  studio.yadev.co)    │                   │
  │                      │                   │
  │  Consume:            │                   │
  │   POST /api/v1/login │                   │
  │   GET  /api/v1/pages │                   │
  │   PUT  /api/v1/blocks│                   │
  │   POST /api/v1/publish──────────────────►│ (encola PublishSite job
  │                      │                      que invoca el runner)
  └──────────────────────┘
```

## Flujo de datos: Editar bloque → Publicar

```
Cliente (Multiservicios)
   │
   │ 1. Login: POST https://api.yadev.co/v1/auth/login
   │    body: { email, password, tenant_domain: "multiserviciospj.com" }
   │    respuesta: { token, user, tenant }
   │    (tenant_domain es opcional si users_index resuelve email → tenant_id)
   │
   ▼
Panel Admin (studio.yadev.co)
   │
   │ 2. GET https://api.yadev.co/v1/tenants/{tenant_id}/pages (header: Bearer $token)
   │    Laravel middleware ResolveTenantFromToken → selecciona DB tenant
   │    (valida que tenant_id del path coincide con el del token)
   │    respuesta: [{ id, title, slug, blocks: [...] }, ...]
   │
   │ 3. Usuario edita bloque "Hero"
   │    PUT /api/v1/blocks/42
   │    body: { data: { title: "Nuevo título", subtitle: "...", image_id: 15 } }
   │    → Laravel valida con BlockSchema\Hero
   │    → guarda en tenant_multiservicios.blocks
   │    → graba ActivityLog
   │
   │ 4. Usuario presiona "Publicar cambios"
   │    POST /api/v1/publish
   │    → Laravel encola job PublishSite($tenant_id)
   │    respuesta: { publish_id, status: "queued" }
   │
   ▼
Redis Queue
   │
   │ 5. Horizon procesa PublishSite job
   │    → Genera JSON content-tree del tenant
   │    → POST http://127.0.0.1:8080/webhook/rebuild
   │       body: { tenant: "multiservicios", content_url: "...", hmac }
   │
   ▼
Webhook Runner (Node, PM2)
   │
   │ 6. Valida HMAC
   │    → cd /srv/builds/multiservicios/
   │    → git pull (por si hay cambios en código)
   │    → descarga content.json del API
   │    → escribe en src/content/site.json
   │    → npm run build (Astro genera dist/)
   │    → rsync -az --delete dist/ user@shared:/public_html/multiserviciospj/
   │    → callback POST /api/v1/publish/{publish_id}/complete
   │       { status: "success", duration_ms: 94210, commit_sha: "abc123" }
   │
   ▼
Laravel API
   │
   │ 7. Marca publish record como completo
   │    → emit evento vía Pusher/Reverb → panel actualiza toast
   │
   ▼
Panel Admin muestra:
   "Publicado exitosamente en 1m 34s ✓
    https://multiserviciospj.com"
```

## Componentes y puertos

| Componente        | Puerto | Acceso      | Notas                                      |
|-------------------|--------|-------------|--------------------------------------------|
| Nginx             | 80/443 | Público     | Termina SSL, sirve `/api` y `/admin`       |
| PHP-FPM           | 9000   | Solo local  | Laravel API                                |
| MySQL             | 3306   | Solo local  | Nunca exponer al internet                  |
| Redis             | 6379   | Solo local  | Sin password porque sólo local + ufw       |
| Webhook Runner    | 8080   | Solo local  | Laravel API lo llama vía localhost         |
| Horizon dashboard | /horizon (Laravel) | Solo super-admin | Protegido con Gate      |

## Subdominios y rutas

- `api.yadev.co/v1/...` — API REST, JSON only, CORS configurado para `studio.yadev.co` + whitelist `domains` por tenant (para fetchs desde builds).
- `studio.yadev.co` — SPA SvelteKit estática (build generado, sirve index.html con SPA routing).
- `yadev.co` — landing marketing del CMS (opcional, Fase 2).
- `multiserviciospj.com`, `ecomagsas.com`, `poronsas.com`, `coisem.com`, etc. — sitios públicos finales (Hostinger shared, sin conexión directa al VPS salvo el rsync de deploy).

## Resolución de tenant en el API

El middleware de Laravel resuelve el tenant activo según la fuente del request:

| Fuente | Cómo se resuelve | Uso típico |
|--------|------------------|------------|
| `Authorization: Bearer {token}` | El token Sanctum embebe `tenant_id` como ability o claim. Middleware `ResolveTenantFromToken`. | Requests desde el panel `studio.yadev.co` |
| `tenant_id` en URL path (`/v1/tenants/{tenant_id}/...`) | Middleware `ResolveTenantFromPath`. Si hay token, valida que coincide con el del token (anti cross-tenant). | Requests desde el runner/build o calls administrativas |
| `Origin` header | Middleware `ResolveTenantFromOrigin` busca en `central.domains` el tenant al que pertenece ese origin. | Fetchs desde el sitio cliente en runtime (raro, solo endpoints públicos tipo form-submit) |

Si más de una fuente está presente, TODAS deben resolver al mismo tenant. Cualquier inconsistencia → 403 + log `cross_tenant_attempt`.

## Backups y resiliencia

- MySQL dump diario 3am UTC por tenant → BackBlaze B2 (retention 30 días).
- Redis: no se respalda (sólo es queue + cache, datos efímeros).
- `/srv/builds/` está en git + VPS backup semanal Hostinger.
- Sitios públicos: ya viven en Hostinger shared que tiene backup nativo.
- Plan de disaster recovery: restaurar VPS desde snapshot Hostinger + restaurar DBs desde B2 = RTO 2 horas, RPO 24 horas.
