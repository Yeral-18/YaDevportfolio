# API Contract — YaDev CMS

> **Base URL:** `https://api.yadev.co/v1/`
> REST versionado bajo `/v1/`. Autenticación: Sanctum token en header `Authorization: Bearer {token}`.
> Content-Type: `application/json`. Respuestas: JSON envuelto en `{ data, meta, links }`.

---

## Estilos de URL soportados

El API acepta dos formas equivalentes para identificar el tenant en cada request:

### A) Implícito por token (default — usado por el panel `studio.yadev.co`)
```
GET https://api.yadev.co/v1/pages
Authorization: Bearer {token}
```
El tenant sale del token Sanctum. Rutas cortas, UX del panel limpia.

### B) Explícito en la URL (usado por el runner/build y calls administrativas)
```
GET https://api.yadev.co/v1/tenants/{tenant_id}/pages
Authorization: Bearer {token}   (o HMAC interno)
```
El tenant sale del path. Si también hay token, **debe coincidir** con el del path (mismatch → 403).

Todos los recursos documentados abajo (`/pages`, `/blocks`, `/media`, `/forms`, `/publish`, etc.) están disponibles en ambas formas. La forma explícita `/tenants/{tenant_id}/...` es obligatoria para:
- Endpoints llamados por el runner Node (que no tiene token de usuario, solo HMAC).
- Endpoints administrativos ejecutados por super-admin impersonando.
- Cualquier integración externa que quiera ser explícita.

El `tenant_id` aceptado puede ser el slug (`multiservicios`) o el ID numérico (`42`) — se acepta cualquiera, el API resuelve.

---

## Convenciones globales

### Formato de respuesta exitosa
```json
{
  "data": { ... },
  "meta": {
    "tenant": "multiservicios",
    "requested_at": "2026-04-22T15:30:00Z"
  }
}
```

### Formato de respuesta con colección
```json
{
  "data": [ { ... }, { ... } ],
  "meta": {
    "total": 42,
    "per_page": 20,
    "current_page": 1,
    "tenant": "multiservicios"
  },
  "links": {
    "next": "/api/v1/pages?page=2",
    "prev": null
  }
}
```

### Formato de error
```json
{
  "error": {
    "code": "VALIDATION_FAILED",
    "message": "El campo título es requerido.",
    "fields": {
      "title": ["El campo título es requerido."]
    }
  },
  "meta": { "request_id": "req_abc123" }
}
```

### HTTP status codes
| Code | Uso |
|------|-----|
| 200 | OK - lectura exitosa |
| 201 | Created - recurso creado |
| 204 | No Content - delete exitoso |
| 400 | Bad Request - JSON malformado |
| 401 | Unauthorized - token faltante/inválido |
| 403 | Forbidden - token válido pero sin permisos |
| 404 | Not Found - recurso no existe O no es del tenant (no filtrar) |
| 422 | Unprocessable Entity - validación falló |
| 429 | Too Many Requests - rate limit |
| 500 | Internal Server Error - bug server |

### Rate limiting
- Authenticated: 60 requests/min por token.
- Unauthenticated: 20 requests/min por IP.
- Header `X-RateLimit-Remaining` presente en toda respuesta.

---

## Endpoints

### Authentication

#### POST /v1/auth/login
(full URL: `https://api.yadev.co/v1/auth/login`)
Body:
```json
{
  "email": "gerencia@multiserviciospj.com",
  "password": "••••••••",
  "tenant_domain": "multiserviciospj.com"
}
```
(`tenant_domain` opcional si el email está en `users_index` central.)

Respuesta 200:
```json
{
  "data": {
    "token": "1|eyJhbGci...",
    "expires_at": "2026-04-29T15:30:00Z",
    "user": { "id": 1, "name": "Yamileth Pérez", "email": "...", "role": "admin" },
    "tenant": { "slug": "multiservicios", "name": "Multiservicios P&J", "domain": "multiserviciospj.com" }
  }
}
```

#### POST /api/v1/auth/logout
Invalida el token actual. Respuesta 204.

#### POST /api/v1/auth/password/forgot
Envía link de reset. Respuesta 204 (no revela si el email existe).

#### POST /api/v1/auth/password/reset
Body: `{ token, email, password, password_confirmation }`. Respuesta 200.

#### GET /api/v1/auth/me
Devuelve usuario actual + tenant. Usado por el panel al iniciar sesión.

---

### Pages

#### GET /api/v1/pages
Lista páginas del tenant.
Query params: `?status=published|draft`, `?search=inicio`, `?page=1&per_page=20`.

#### GET /api/v1/pages/{id}
Detalle de página con sus bloques embebidos.

Respuesta 200:
```json
{
  "data": {
    "id": 1,
    "slug": "inicio",
    "title": "Página de Inicio",
    "status": "published",
    "template": "home",
    "is_home": true,
    "sections": [
      {
        "id": 10,
        "order": 1,
        "type": "hero",
        "blocks": [
          {
            "id": 100,
            "type": "hero_split",
            "data": {
              "eyebrow": "Empresa de Ingeniería en Barrancabermeja",
              "headline": "Transporte de Carga, Obras Civiles y Remediación Ambiental",
              "description": "...",
              "primary_cta": { "label": "Conocer Servicios", "href": "#servicios" },
              "secondary_cta": { "label": "Contactar", "href": "#contacto" },
              "badges": [ { "label": "Transporte", "icon": "building" }, ... ]
            },
            "version": 3,
            "updated_at": "2026-04-22T14:20:00Z"
          }
        ]
      }
    ],
    "seo": {
      "title": "MULTISERVICIOS P&J S.A.S | ...",
      "description": "...",
      "og_image_id": 42
    }
  }
}
```

#### POST /api/v1/pages
Crea página nueva. Body: `{ slug, title, template, status }`.

#### PUT /api/v1/pages/{id}
Actualiza metadata (no bloques). Body: `{ title?, slug?, status?, seo? }`.

#### DELETE /api/v1/pages/{id}
Soft-delete. 204.

#### POST /api/v1/pages/{id}/duplicate
Duplica página con todos los bloques. Respuesta 201 con la nueva página.

---

### Blocks

#### GET /api/v1/blocks/{id}
Lee un bloque específico (útil para edición aislada).

#### POST /api/v1/pages/{pageId}/blocks
Añade bloque a una página en una sección.
Body:
```json
{
  "section_id": 10,
  "type": "services_zigzag",
  "data": { "heading": "...", "items": [...] },
  "order": 2
}
```

#### PUT /api/v1/blocks/{id}
Actualiza `data` del bloque.
Body: `{ data: {...} }`. El schema se valida server-side según `type`.
Respuesta 200 con el bloque actualizado + `version` incrementada.

#### PATCH /api/v1/blocks/{id}/order
Body: `{ order: 3 }`. Para drag-and-drop.

#### DELETE /api/v1/blocks/{id}
Soft-delete.

#### POST /api/v1/blocks/{id}/restore/{version}
Restaura una versión previa desde `activity_log`.

---

### Media (biblioteca)

#### GET /api/v1/media
Lista media. Filtros: `?folder=hero`, `?type=image`, `?search=logo`.

#### POST /api/v1/media
Upload. `multipart/form-data`: `file`, `folder`, `alt`, `title`.
Respuesta 201: `{ id, url, thumb_url, webp_url, mime, size, width, height, alt }`.
Genera automáticamente thumbs + webp via Intervention (cola async).

#### PUT /api/v1/media/{id}
Edita metadata: `alt`, `title`, `folder`.

#### DELETE /api/v1/media/{id}
Borra archivo + registros. Si está en uso (relación con block), advierte antes.

#### GET /api/v1/media/{id}/usages
Lista bloques/páginas que usan esta imagen.

#### POST /api/v1/media/{id}/transform
Editor fotográfico — ver `phases/phase-1-mvp.md` semana 2 día 15 para UX detallada.
Body:
```json
{
  "crop": { "x": 100, "y": 50, "width": 800, "height": 450 },
  "rotate": 90,
  "flip": "horizontal",
  "filters": { "brightness": 10, "contrast": -5, "saturation": 15, "sharpness": 0 },
  "format": "webp",
  "quality": 85,
  "mode": "replace"
}
```
`mode: 'replace'` sobreescribe el original (mantiene URL); `mode: 'copy'` crea un nuevo media row. Respuesta 200 con el media actualizado o creado + thumbnails regeneradas.

---

### Forms

#### GET /api/v1/forms
Lista formularios del sitio.

#### POST /api/v1/forms
Crea formulario.
Body:
```json
{
  "name": "Contacto Principal",
  "slug": "contact-main",
  "fields": [
    { "name": "nombre", "label": "Nombre Completo", "type": "text", "required": true },
    { "name": "email", "label": "Correo", "type": "email", "required": true },
    { "name": "servicio", "label": "Servicio", "type": "select", "options": [...] }
  ],
  "notifications": {
    "email_to": ["gerencia@multiserviciospj.com"],
    "whatsapp_to": "+573204464553"
  },
  "recaptcha": true
}
```

#### GET /api/v1/forms/{id}/submissions
Lista envíos. Paginado. Filtros por fecha/estado (leído/no leído).

#### GET /api/v1/forms/{id}/submissions.csv
Export CSV de todos los envíos.

---

### Publish

#### POST /api/v1/publish
Dispara rebuild + deploy del sitio.
Body opcional: `{ note: "Actualización servicios abril" }`.
Respuesta 202 (Accepted):
```json
{
  "data": {
    "publish_id": "pub_xyz789",
    "status": "queued",
    "estimated_duration_ms": 90000
  }
}
```

#### GET /api/v1/publish/{id}
Consulta estado: `queued | building | deploying | success | failed`.

#### GET /api/v1/publish
Historial de publicaciones (últimas 50). Cada una con quién publicó, duración, status.

---

### Settings

#### GET /api/v1/settings
Devuelve todas las settings del tenant (SEO global, GA, Meta Pixel, WhatsApp, horario, dirección, redes sociales).

#### PUT /api/v1/settings
Body: `{ key: value, ... }`. Update parcial.

---

### Menus

#### GET /api/v1/menus
#### POST /api/v1/menus
#### PUT /api/v1/menus/{id}
#### DELETE /api/v1/menus/{id}

Gestión CRUD de menús y sus items.

---

### Popups

#### GET /api/v1/popups
#### POST /api/v1/popups
#### PUT /api/v1/popups/{id}
#### DELETE /api/v1/popups/{id}

Campos clave: `trigger_type` (time, scroll, exit), `trigger_value`, `pages` (where to show), `content` (block data), `active_from`, `active_until`.

---

### Redirects

#### GET /api/v1/redirects
#### POST /api/v1/redirects
Body: `{ from: "/productos", to: "/servicios", status: 301 }`.

#### DELETE /api/v1/redirects/{id}

---

### Sedes / Sucursales [Fase 2 — ver phase-2-parity.md]

Entidad multi-sucursal, consumible por bloques `footer_mega`, `contact_locations_map` y `page_contact`.

#### GET /v1/tenants/{tenant_id}/sedes
Lista sedes ordenadas por `order`, con `is_main` primera.

#### POST /v1/tenants/{tenant_id}/sedes
Body:
```json
{
  "name": "Sede Principal Barrancabermeja",
  "address": "Carrera 20 # 45-30",
  "city": "Barrancabermeja",
  "department": "Santander",
  "country": "CO",
  "phone": "+573204464553",
  "whatsapp": "+573204464553",
  "email": "contacto@multiserviciospj.com",
  "lat": 7.0653,
  "lng": -73.8547,
  "hours": { "mon_fri": "07:00-17:00", "sat": "08:00-12:00", "sun": "closed" },
  "is_main": true,
  "order": 1,
  "icon": "map-pin"
}
```

#### PUT /v1/tenants/{tenant_id}/sedes/{id}
#### DELETE /v1/tenants/{tenant_id}/sedes/{id}

---

### Analytics (sin cookies, vía GoAccess) [Fase 2]

#### GET /v1/tenants/{tenant_id}/analytics/snapshot
Query params: `?range=today|7d|30d|90d`.
Respuesta cacheada 10 min en Redis (procesada por cron GoAccess cada hora).
```json
{
  "range": "7d",
  "generated_at": "2026-04-22T14:00:00Z",
  "visits_unique": 1243,
  "pageviews": 3891,
  "avg_visit_duration_sec": 142,
  "bounce_rate": 0.41,
  "top_pages": [ { "path": "/", "views": 1200 }, ... ],
  "top_countries": [ { "code": "CO", "name": "Colombia", "visits": 980 }, ... ],
  "top_browsers": [ { "name": "Chrome", "share": 0.68 }, ... ],
  "top_referrers": [ { "host": "google.com", "visits": 450 }, ... ],
  "search_keywords": [ { "term": "transporte carga barrancabermeja", "visits": 34 }, ... ],
  "hourly_heatmap": [[...7x24 grid...]],
  "status_codes": { "200": 3800, "404": 45, "500": 2 }
}
```

#### GET /v1/tenants/{tenant_id}/analytics/export.csv
Export raw snapshot para Excel/sheets.

---

### Mail accounts + Webmail SSO [Fase 2]

#### GET /v1/tenants/{tenant_id}/mail-accounts
Lista cuentas de correo configuradas.

#### POST /v1/tenants/{tenant_id}/mail-accounts
Body: `{ username, host_imap, port_imap, host_smtp, port_smtp, password, provider }`. Password se cifra con vault AES-256-GCM.

#### POST /v1/tenants/{tenant_id}/mail-accounts/{id}/sso-token
Genera token de un solo uso (TTL 60s) para abrir Roundcube pre-autenticado.
Respuesta: `{ sso_url: "https://studio.yadev.co/webmail/?token=..." }`.

---

### Public Lookup / Tracking (sin login) [Fase 2]

Módulo para consultas públicas estilo "consulta de dictamen" de Odir.

#### GET /v1/public/lookup/{tenant_slug}/{collection_slug}/{code}
Público, sin auth, rate-limited 10 req/min por IP.
Respuesta 200: `{ data: { ...campos configurados por el tenant... } }` o 404 si no existe.

---

### Activity Log

#### GET /api/v1/activity-log
Lista últimos 100 eventos del tenant. Filtros: `?actor=user_id`, `?action=update`, `?subject_type=block`.

---

### Runner-facing endpoints (build time)

Estos endpoints son consumidos por el webhook-runner Node cuando ejecuta un rebuild, y por el build de Astro cuando inyecta contenido. Autenticación: HMAC (header `X-YaDev-Signature: sha256=...` sobre el body) + `tenant_id` explícito en path.

#### GET /v1/tenants/{tenant_id}/content-tree
Devuelve el content-tree completo del tenant, listo para inyectar en `src/content/site.json` del Astro. Incluye: pages, sections, blocks, settings, menús, redirects, seo_meta, media URLs resueltas.

Respuesta 200: JSON grande (~50-200 KB típico). Cacheable con `ETag`. El runner verifica `ETag` antes de rebuildar — si no cambió el hash, skip build.

#### POST /v1/tenants/{tenant_id}/publishes/{publish_id}/complete
Callback del runner al terminar el build. Body: `{ status, duration_ms, commit_sha, log_url? }`.

---

### Super-admin only (role: yadev_super_admin)

#### GET /api/v1/admin/tenants
Lista todos los tenants.

#### POST /api/v1/admin/tenants
Provisiona nuevo tenant (ver `multi-tenancy-strategy.md`).

#### PATCH /api/v1/admin/tenants/{slug}/suspend
#### PATCH /api/v1/admin/tenants/{slug}/resume
#### POST /api/v1/admin/tenants/{slug}/impersonate
Devuelve un token limitado para ver el panel del tenant (con banner "estás impersonando a X").

#### GET /api/v1/admin/metrics
Agregados cross-tenant: total tenants, total submissions mes, errores de publish.

---

## Webhooks salientes (tenant settings → notifications)

El cliente puede configurar URLs externas para recibir eventos:

```
POST {url} (por evento)
Headers: X-YaDev-Signature: sha256=hmac(body, secret)
Events:
  - form.submission.created
  - publish.completed
  - publish.failed
  - media.uploaded
```

---

## IA endpoints (Fase 3)

Todos usan Claude Haiku 4.5 con prompt caching activado por defecto. Sonnet 4.6 solo para `audit` cuando el scope es página completa (razonamiento más profundo). Cada llamada inyecta el `brand_voice` del tenant como system prompt cacheable (ver `phases/phase-3-ai.md`).

#### POST /v1/tenants/{tenant_id}/ai/generate
Generación unificada de contenido respetando brand voice. [ver phase-3-ai.md semana 11]
Body:
```json
{
  "type": "blog_post | service_description | meta_description | hero_copy | about_paragraph",
  "context": { "topic": "...", "target_keywords": [...], "outline": "..." },
  "constraints": { "max_words": 800, "tone_override": "cercano" }
}
```
Respuesta: `{ text, tokens_used, model, cache_hit_ratio }`.

#### POST /api/v1/ai/rewrite
Body: `{ text, tone: "professional|friendly|formal", max_words: 120 }`. Devuelve `{ text: "..." }`.

#### POST /v1/tenants/{tenant_id}/ai/translate
Traducción estructura-preserving. [ver phase-3-ai.md semana 13]
Body:
```json
{
  "source_locale": "es-CO",
  "target_locale": "en",
  "blocks": [ { "id": 100, "type": "hero_split", "data": { ... } } ],
  "translate_slugs": false,
  "preserve_fields": ["urls", "emails", "phones", "logos", "schema_jsonld.sameAs"]
}
```
Respuesta: `{ blocks: [...], tokens_used, model }` — blocks con misma forma, strings traducidos.

Versión legacy campo único:
`POST /api/v1/ai/translate` — Body: `{ text, target_lang: "en" }`.

#### POST /v1/tenants/{tenant_id}/ai/audit
Auditor SEO + GEO en tiempo real. [ver phase-3-ai.md semana 12]
Body:
```json
{
  "page_id": 1,
  "partial_html": "<section>...</section>",
  "block_id": 100
}
```
`partial_html` y `block_id` son opcionales — si vienen, audita fragmento (síncrono <2s). Si solo `page_id`, audita página completa (async, Horizon queue).

Respuesta (ver shape completa en `phases/phase-3-ai.md`):
```json
{
  "score_seo": 82,
  "score_geo": 67,
  "score_overall": 74,
  "grade": "B",
  "issues": [ { "id", "severity", "category", "message", "field_path", "suggestion" } ],
  "suggestions_inline": { "blocks": { "100": { "headline": "...", "description": "..." } } },
  "audited_at": "...",
  "model": "claude-haiku-4-5",
  "cache_hit_ratio": 0.73
}
```
Categorías de `issues[]`: `seo` (tradicional) | `geo` (Generative Engine Optimization, SGE/AI Overviews). Se guarda en `seo_audits` (tenant schema).

Endpoint legacy: `POST /api/v1/ai/seo-score` — mismo efecto, shape más simple, sigue operativo por retrocompatibilidad.

#### GET /v1/tenants/{tenant_id}/brand-voice
#### PUT /v1/tenants/{tenant_id}/brand-voice
CRUD del ADN comercial del tenant. Body PUT:
```json
{
  "tone": ["profesional", "cercano"],
  "vocabulary_prefer": ["aliado estratégico", "Barrancabermeja"],
  "vocabulary_avoid": ["barato", "low cost"],
  "sample_texts": [
    { "label": "About us real", "text": "..." },
    { "label": "Servicio principal", "text": "..." }
  ],
  "industry_context": "Ingeniería civil y ambiental, sector petrolero Magdalena Medio",
  "target_audience": "Gerentes de proyectos de Ecopetrol, Cenit, Terpel"
}
```

#### POST /api/v1/ai/og-image
Body: `{ page_id, prompt? }`. Genera OG image via Nano Banana 2 + sube a media.

---

## Schemas de bloques (inicio)

Schemas completos viven en `api/app/Blocks/*/schema.php`. Listado resumido:

| Tipo | Campos requeridos | Componente Astro mapeado |
|------|-------------------|--------------------------|
| `hero_split` | eyebrow, headline, desc, cta | Hero.svelte |
| `hero_centered` | headline, desc, cta, bg_image_id | HeroCentered.svelte |
| `services_zigzag` | heading, items[] | Services.astro |
| `services_grid` | heading, items[] | ServicesGrid.astro |
| `stats_bar` | items[{value,label,suffix}] | StatsBar.astro |
| `stats` | heading?, items[{value,suffix,label,icon,color_accent}], layout, animation | Stats.astro |
| `about_three_cards` | intro, mission, vision, values[] | AboutUs.astro |
| `bento_projects` | featured, items[] | Projects.astro |
| `clients_carousel` | items[{name,logo_id,industry}] | Clients.astro |
| `benefits_grid` | heading, items[{title,desc,icon}] | Benefits.astro |
| `contact_form` | form_id, info_cards[] | Contact.svelte |
| `contact_locations_map` | sedes_ids[], default_zoom, show_hours | ContactLocations.astro |
| `footer_mega` | tagline, columns[], certifications[], sedes_ids[]? | Footer.astro |
| `cta_banner` | heading, desc, cta | (parte de Footer.astro) |
| `rich_text` | html (TipTap output) | RichText.astro |
| `image_gallery` | items[{media_id,alt}], layout | Gallery.astro |
| `faq` | items[{question,answer}] | FAQ.astro |
| `timeline` | items[{year,title,desc}] | Timeline.astro |
| `block_lookup_widget` | collection_slug, placeholder, result_template | LookupWidget.svelte |
| `pricing_table_checkout` | plans[{name,price,currency,features,provider}] | PricingCheckout.svelte |

La lista crece en Fase 2.

---

## Versionado del API

- `/api/v1/` es el contract actual. Nunca se rompe sin bump de versión.
- Cambios breaking = `/api/v2/`. Viejo sigue online 6 meses.
- Cambios no-breaking (nuevo endpoint, nuevo campo opcional) se agregan en `v1`.
