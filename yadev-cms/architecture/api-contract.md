# API Contract — YaDev CMS

> Resumen del contrato REST que expone `yadev-cms-api` bajo `/v1/*`. Fuente
> canónica: `api/routes/api.php` + `app/Http/Controllers/Api/V1/*`. Última
> revisión: 2026-05-06 (Phase 3 cierre).
>
> Para regenerar la versión auto desde un entorno con docker arriba:
> `docker compose exec -T api php artisan yadev:docs`. Mientras esa salida
> exista, este archivo se mantiene a mano sincronizado con el router.

## Convenciones

- **Base URL prod:** `https://api.yadev.co`. Healthcheck `/health` no versionado por diseño.
- **Versión:** todo bajo `/v1/`. Cambios incompatibles → `/v2`, no breaking en `/v1`.
- **Auth:**
  - `Public` — sin autenticación.
  - `Public (rate-limited)` — limitador específico (login, forgot-password, search, AI, form-submit).
  - `Bearer (Sanctum)` — header `Authorization: Bearer {token}` emitido por `POST /v1/auth/login`.
  - `Bearer + tenant scope` — Sanctum bearer con ability `tenant:{id}:*` (o `*` super-admin) validada por middleware `tenant.path`.
  - `HMAC X-YaDev-Signature` — handshake Runner → API. SHA-256 del raw body con `RUNNER_CALLBACK_SECRET`. **NO** usa Sanctum.
- **Tenant resolution:** ver [`system-diagram.md`](system-diagram.md) §"Resolución de tenant" y [`security-model.md`](security-model.md) §1.
- **Cross-tenant safety:** un id que no pertenece al tenant activo retorna **404**, jamás 403 (anti-leak de existencia).
- **Response envelope:** `{ "data": …, "meta"?: …, "links"?: … }`. Errores: `{ "message": "…", "errors": { field: [..] }? }` con HTTP semánticos (201 create, 204 delete, 401 sin token, 403 con token sin ability, 404 not found / cross-tenant, 422 validation, 429 throttle).
- **Rate limits globales:** 60 req/min autenticado, 20 req/min anónimo. Buckets específicos detallados abajo.

---

## Health

| Method | Path | Auth |
|--------|------|------|
| GET | `/health` | Public |

Respuesta: `{ "status": "ok", "service": "yadev-cms-api", "time": "ISO8601" }`.

---

## Auth

| Method | Path | Auth | Throttle |
|--------|------|------|----------|
| POST | `/v1/auth/login` | Public | `login` (5/min IP + 3/min email) |
| POST | `/v1/auth/forgot-password` | Public | `forgot-password` |
| POST | `/v1/auth/reset-password` | Public | `forgot-password` |
| POST | `/v1/auth/2fa/challenge` | Public | `login` |
| POST | `/v1/auth/verify-email` | Public | global API |
| POST | `/v1/auth/resend-verification` | Public | `forgot-password` |
| POST | `/v1/auth/logout` | Bearer | — |
| POST | `/v1/auth/logout-all` | Bearer | — |
| GET | `/v1/auth/me` | Bearer | — |
| POST | `/v1/auth/2fa/enable` | Bearer | — |
| POST | `/v1/auth/2fa/verify` | Bearer | — |
| POST | `/v1/auth/2fa/disable` | Bearer + password reconfirm | — |
| POST | `/v1/auth/2fa/regenerate-backup` | Bearer + password reconfirm | — |

### `POST /v1/auth/login`

```
body { email: string<email>, password: string min:8, device_name?: string<=120 }
200  { data: { token, user: {...}, tenants: [{...}] } }
200  { data: { challenge_id } }                      // si 2FA está habilitado
401  credenciales inválidas (genérico, no distingue email vs password)
422  validation
429  throttle
```

### `POST /v1/auth/2fa/challenge`

```
body { challenge_id, code }                          // code = TOTP 6 dígitos | backup code
200  { data: { token, user, tenants } }
422  same shape para "wrong code" y "expired challenge" (anti-enumeration)
```

### `POST /v1/auth/verify-email`

Activa cuenta de un miembro invitado. Body: `{ token }` con HMAC firmado al
crear la invitación. Devuelve 200 + `{ data: { user } }` o 422 si está
expirado/usado.

### `POST /v1/auth/2fa/enable`

```
200  { data: { secret_url, recovery_codes: string[] } }
```

`secret_url` es un `otpauth://` listo para QR. Los `recovery_codes` se
muestran una sola vez. Cliente debe llamar `verify` con el primer TOTP
para activar.

### `POST /v1/auth/2fa/disable` y `regenerate-backup`

```
body { password: string }                            // password reconfirm obligatorio
204  on success
422  password incorrecto / 2FA no habilitado
```

---

## Tenants (super-admin / propietario)

| Method | Path | Auth |
|--------|------|------|
| GET | `/v1/tenants` | Bearer |
| POST | `/v1/tenants` | Bearer (super-admin) |
| GET | `/v1/tenants/{tenant}` | Bearer |
| PUT/PATCH | `/v1/tenants/{tenant}` | Bearer |
| DELETE | `/v1/tenants/{tenant}` | Bearer (super-admin) |

### `POST /v1/tenants`

```
body {
  name: string<=120,
  slug: string<=64 regex:[a-z0-9-]+ (unique),
  domain: string<=255 valid-domain (unique),
  admin_email: string<email>,
  admin_name?: string<=120,
  plan?: enum
}
201 { data: { id, name, slug, plan, status, database, industry, primary_color, logo_path, primary_domain, domains, domain } }
```

Side-effects: crea DB `tenant_{slug}`, ejecuta `migrate --tenants`, registra
domain primario en `central.domains`, envía invitación al `admin_email`.

### Tenant settings (anidados, requieren ability `tenant_admin`)

| Method | Path | Notas |
|--------|------|-------|
| GET | `/v1/tenants/{tenant_id}/domains` | Lista domains del tenant |
| POST | `/v1/tenants/{tenant_id}/domains` | `body { domain }` valida formato + unicidad |
| DELETE | `/v1/tenants/{tenant_id}/domains/{domain}` | `domain` puede contener puntos (regex `.*`) |
| GET | `/v1/tenants/{tenant_id}/members` | Lista miembros + roles |
| POST | `/v1/tenants/{tenant_id}/members` | Invita por email |
| DELETE | `/v1/tenants/{tenant_id}/members/{user_id}` | Revoca acceso al tenant |

---

## Pages

Todas requieren `Bearer + tenant scope`.

| Method | Path |
|--------|------|
| GET | `/v1/tenants/{tenant_id}/pages` |
| POST | `/v1/tenants/{tenant_id}/pages` |
| GET | `/v1/tenants/{tenant_id}/pages/{page}` |
| PUT/PATCH | `/v1/tenants/{tenant_id}/pages/{page}` |
| DELETE | `/v1/tenants/{tenant_id}/pages/{page}` |
| POST | `/v1/tenants/{tenant_id}/pages/{page}/duplicate` |

### Body principal `POST /pages`

```
title: string<=191 required
slug: string<=191 unique tenant-scoped, regex /^[a-z0-9]+(?:-[a-z0-9]+)*$/
status?: enum(draft, published, archived)
template?: string<=64
visibility?: in(public, private, password)
is_home?: boolean
order?: int 0..100000
parent_id?: int (exists)
published_at?: date nullable
```

Response:

```
data: { id, type, attributes, title, slug, status, template, visibility, is_home, order, parent_id, created_by }
```

### `POST /pages/{page}/duplicate`

Crea copia profunda de la página + sections + blocks + block versions
contemporáneos. Slug auto: `{slug}-copy-{n}`. Devuelve la nueva página.

---

## Sections

Idéntico CRUD anidado bajo `/v1/tenants/{tenant_id}/sections/{section}`.

### Body principal `POST /sections`

```
page_id: int required (exists)
order?: int 0..100000
layout?: enum
background?: string<=64 nullable
background_image_id?: int nullable (exists in tenant media)
padding?: in(none, sm, md, lg, xl)
container_width?: in(narrow, default, wide, full)
settings?: array nullable
is_visible?: boolean
```

---

## Blocks

| Method | Path | Notas |
|--------|------|-------|
| GET | `/v1/tenants/{tenant_id}/blocks` | Filtra por `?section_id=` |
| POST | `/v1/tenants/{tenant_id}/blocks` | Schema-validated por `BlockType` |
| GET | `/v1/tenants/{tenant_id}/blocks/{block}` | — |
| PUT/PATCH | `/v1/tenants/{tenant_id}/blocks/{block}` | Crea BlockVersion automático |
| DELETE | `/v1/tenants/{tenant_id}/blocks/{block}` | Soft delete |
| GET | `/v1/tenants/{tenant_id}/blocks/{block}/versions` | Historial (BBC versioning) |
| POST | `/v1/tenants/{tenant_id}/blocks/{block}/versions/{version}/restore` | Restaura snapshot |
| POST | `/v1/tenants/{tenant_id}/blocks/{block}/save-as-template` | Mintea BlockTemplate (DDC) |

### Body principal `POST /blocks`

```
section_id: int required (exists in tenant.sections)
type: enum (Hero, Services, ContentRichText, FeatureGrid, Stats, Cta, FAQ, ContactForm, …)
order?: int >=0
is_visible?: boolean
data: array required           // valida contra BlockSchema/{type}.php
```

Response:

```
data: { id, section_id, type, order, version, is_visible, data, created_at, updated_at }
```

---

## Block templates (biblioteca por tenant, DDC)

| Method | Path | Notas |
|--------|------|-------|
| GET | `/v1/tenants/{tenant_id}/block-templates` | Lista templates del tenant |
| PATCH | `/v1/tenants/{tenant_id}/block-templates/{template}` | Solo metadata (`name`, `description`); `data` inmutable |
| DELETE | `/v1/tenants/{tenant_id}/block-templates/{template}` | — |
| POST | `/v1/tenants/{tenant_id}/sections/{section}/blocks/from-template/{template}` | Aplica template como nuevo block en la sección |

No hay `POST` directo: los templates se crean exclusivamente vía
`/blocks/{block}/save-as-template` para que los `data` siempre pasen por
schema validation antes de entrar a la tabla.

---

## Media

Endpoints anidados bajo `/v1/tenants/{tenant_id}/media`. Las rutas
`folders`, `bulk-delete`, `bulk-move` se declaran ANTES del
`apiResource` para que no las consuma el wildcard `{media}`.

| Method | Path | Notas |
|--------|------|-------|
| GET | `/v1/tenants/{tenant_id}/media` | Lista paginada, filtros `?folder=`, `?type=` |
| POST | `/v1/tenants/{tenant_id}/media` | Multipart upload |
| GET | `/v1/tenants/{tenant_id}/media/{media}` | URL firmada |
| PUT/PATCH | `/v1/tenants/{tenant_id}/media/{media}` | Update metadata (`alt_text`, `caption`, `focal_point`, etc.) |
| DELETE | `/v1/tenants/{tenant_id}/media/{media}` | Soft delete + cleanup eventual |
| GET | `/v1/tenants/{tenant_id}/media/folders` | Lista jerarquía de folders |
| POST | `/v1/tenants/{tenant_id}/media/bulk-delete` | `body { ids: int[] }` |
| POST | `/v1/tenants/{tenant_id}/media/bulk-move` | `body { ids: int[], folder_id: int|null }` |

### Body principal `POST /media`

```
file: required, max 50MB, mime image/jpeg|png|webp|gif|svg+xml | application/pdf
alt_text?: string<=255
caption?: string<=1000
title?: string<=255
focal_point?: { x: 0..1, y: 0..1 }
```

Response: `{ data: { id, type, url, url_expires_at, original_filename, file_name, disk, path, mime_type, size_bytes, dimensions, alt_text } }`.

---

## Forms (lead capture)

CRUD studio-facing + endpoint público de submit (sin tenant en URL).

| Method | Path | Auth |
|--------|------|------|
| GET | `/v1/tenants/{tenant_id}/forms` | Bearer + tenant scope |
| POST | `/v1/tenants/{tenant_id}/forms` | Bearer + tenant scope |
| GET | `/v1/tenants/{tenant_id}/forms/{form}` | Bearer + tenant scope |
| PUT/PATCH | `/v1/tenants/{tenant_id}/forms/{form}` | Bearer + tenant scope |
| DELETE | `/v1/tenants/{tenant_id}/forms/{form}` | Bearer + tenant scope |
| GET | `/v1/tenants/{tenant_id}/forms/{form}/submissions` | Bearer + tenant scope |
| PATCH | `/v1/tenants/{tenant_id}/forms/{form}/submissions/{sub}/read` | Bearer + tenant scope |
| POST | `/v1/public/forms/{form_id}/submit` | Public (rate-limited) |

### `POST /v1/public/forms/{form_id}/submit`

- Sin auth. Tenant resuelto desde `Origin` contra `central.domains`.
- Throttle apilado: `form-submissions` (5/min keyed por (IP, form_id))
  y `forms-public-form` (20/hora por form_id).
- Body: schema dinámico definido en el `Form` (`fields[]`).
- Side-effect: registra `FormSubmission`, dispara notificación email
  al owner (M365 SMTP) si `notify_on_submit=true`.

---

## Publishes

Pipeline canónico documentado en [`publish-flow.md`](publish-flow.md).

| Method | Path | Auth |
|--------|------|------|
| GET | `/v1/tenants/{tenant_id}/publishes` | Bearer + tenant scope |
| POST | `/v1/tenants/{tenant_id}/publishes` | Bearer + tenant scope |
| GET | `/v1/tenants/{tenant_id}/publishes/{publish}` | Bearer + tenant scope |
| POST | `/v1/tenants/{tenant_id}/publishes/{publish}/complete` | HMAC X-YaDev-Signature |

### `POST /publishes`

```
body {
  page_ids?: int[] max:200,           // opcional → publish parcial
  commit_sha?: string regex:^[0-9a-f]{7,40}$
}
202 { data: { id, status: "pending"|"queued", page_ids, commit_sha, runner_job_id, build_log_url, error_message, requested_by, started_at, completed_at, created_at, updated_at } }
```

Si `page_ids` está ausente o vacío → publica todas las páginas
publicadas del tenant.

### `POST /publishes/{publish}/complete`

```
headers X-YaDev-Signature: sha256=<hex>
body {
  status: enum(success|failed) required,
  build_log_url?: url<=500,
  error_message?: string<=2000,
  commit_sha?: string regex:^[0-9a-f]{7,40}$
}
200 { data: Publish (terminal state) }
401 HMAC missing/invalid
404 publish_id desconocido o tenant mismatch
409 publish ya está en estado terminal (idempotente, devuelve estado actual)
```

---

## Activity log

| Method | Path | Auth |
|--------|------|------|
| GET | `/v1/tenants/{tenant_id}/activity-log` | Bearer + tenant scope |

Filtros query: `?user_id=`, `?entity_type=`, `?action=`, `?since=YYYY-MM-DD`,
`?per_page=` (default 25, max 100). Read-only audit trail.

---

## Search

| Method | Path | Auth | Throttle |
|--------|------|------|----------|
| GET | `/v1/tenants/{tenant_id}/search?q=…` | Bearer + tenant scope | `search` (60/min/tenant) |

Búsqueda global cross-entity (pages, blocks, media). `q` < 2 chars
devuelve `{ data: [] }` sin tocar la DB. `q` ausente o vacío → 422.

Response:

```
data: [
  { entity: "page" | "block" | "media", id, title, snippet, url, score }
]
meta: { total, took_ms }
```

---

## AI (Phase 3 — degrada a 503 si `ANTHROPIC_API_KEY` está vacío)

| Method | Path | Auth | Throttle |
|--------|------|------|----------|
| POST | `/v1/tenants/{tenant_id}/ai/seo-audit` | Bearer + tenant scope | `ai` (10/min/tenant) |
| POST | `/v1/tenants/{tenant_id}/ai/suggest-copy` | Bearer + tenant scope | `ai` |
| POST | `/v1/tenants/{tenant_id}/ai/rewrite-tone` | Bearer + tenant scope | `ai` |

Cuerpos varían por endpoint; ver `app/Http/Controllers/Api/V1/AIController.php`.
Modelo default: `claude-haiku-4-5`, fallback `claude-sonnet-4-6` para
tareas largas. Prompt caching activo.

---

## Limitadores configurados

Definidos en `app/Providers/AppServiceProvider.php`:

| Limiter | Llave | Cap |
|---------|-------|-----|
| `login` | IP + email | 5/min IP, 3/min email |
| `forgot-password` | IP + email | 5/min IP, 3/min email |
| `search` | tenant_id | 60/min |
| `ai` | tenant_id | 10/min |
| `form-submissions` | IP + form_id | 5/min |
| `forms-public-form` | form_id | 20/hora |
| API global | user_id (auth) o IP (anon) | 60/min auth, 20/min anon |

---

## Documentos relacionados

- [`system-diagram.md`](system-diagram.md) — topología prod, data flow.
- [`security-model.md`](security-model.md) — anti-tenant-leak, abilities, headers, CORS.
- [`auth-decision.md`](auth-decision.md) — Sanctum bearer Phase 1 → cookies Phase 2.
- [`publish-flow.md`](publish-flow.md) — handshake API ↔ Runner detallado.
- [`multi-tenancy-strategy.md`](multi-tenancy-strategy.md) — DB-per-tenant + middleware.
- [`deployment.md`](deployment.md) — env vars, smoke tests, rollback.
