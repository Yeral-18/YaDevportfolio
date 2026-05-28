# YaDev CMS — Qué falta vs Damos + Guía de administración

> Documento operativo. Lee primero §1 (gap vs Damos) y luego §2 (cómo administras una página).
> Fecha de corte: 2026-05-28. Estado del CMS: **Fase 3 cerrada**, stack en producción Railway.
> Sitios live conectables: `luqraingenieria.com`, `ecomagsas.com`, `multiserviciospj.com`.

---

## 1. Comparación real con Damos (lo que tienen ellos, lo que tienes tú)

El análisis exhaustivo feature-by-feature está en [`competitive-analysis-damos.md`](competitive-analysis-damos.md) (63 features, score 48 paridad / 10 YaDev plus / 2 Damos plus). Esta sección destila **solo lo accionable**: qué del PDF de Damos NO tienes hoy en código corriendo, ordenado por impacto comercial.

### 1.1. Lo que YA tienes y Damos también (no toques, está cerrado)

- WYSIWYG con bloques drag-drop (TipTap + 7 bloques schema-validated: Hero, Services, Projects, Stats, Cta, Contact, RichText) — `api/app/Blocks/`.
- **Inserción de scripts HTML/JS** (G7) por tenant + override por página, sanitizada server-side (deny `<form>`/`<base>`/`<object>`/`<embed>`, iframes solo a dominios whitelisted, `<script src>` solo HTTPS). UI en Settings → Scripts y en el editor de página (panel "Scripts de esta página").
- Mediateca con carpetas, tags, variantes automáticas (thumb/webp/og), reemplazo manteniendo URL — `MediaController`, `MediaFolderController`.
- Editor fotográfico inline (Cropper.js + Intervention) — modal en `studio/src/lib/components/media`.
- Versionado por bloque + rollback — `block_versions` + `BlockVersionController`.
- Páginas: crear, duplicar, bulk publish, slug editable, status draft/published, SEO meta + OG — `PageController`.
- Formularios: builder visual, submissions dashboard, CSV export, honeypot + reCAPTCHA, notificación email — `Forms/*Controller`.
- Webhooks salientes (`WebhookController` + deliveries log).
- Activity log con diffs JSON + CSV export — `ActivityLogController`.
- Search global Cmd+K — `SearchController`.
- 2FA TOTP — `AuthController` con `pragmarx/google2fa`.
- Impersonation con banner — `Admin\ImpersonationController`.
- Roles (admin / editor / viewer) — `spatie/laravel-permission`.
- Schema.org + OG + sitemap automático en build — `runner/` pipeline.
- Multi-tenant DB-per-tenant (`stancl/tenancy v3`) — diferenciador estructural, Damos no tiene esto.
- AI Phase 3 endpoints (`AIController`) dormant — encienden cuando agregues `ANTHROPIC_API_KEY`.

### 1.2. Gaps reales del PDF Damos que YaDev NO tiene corriendo hoy

Los marco con prioridad y ubicación donde encajan:

| # | Feature Damos | Estado YaDev | Prioridad | Esfuerzo | Dónde encaja |
|---|---------------|--------------|-----------|----------|--------------|
| G1 | **Analítica server-side sin cookies** (visitas, países, navegadores, palabras clave desde logs) | ✗ no implementado | **ALTA** — Damos lo vende fuerte | 3-5 días | Cron Railway parseando access logs Hostinger via SSH → tabla `tenant_analytics_daily` + dashboard Studio |
| G2 | **Auditor SEO/GEO IA en tiempo real** (panel lateral en editor con score H1/H2/schema/meta + sugerencias) | Endpoint `/ai/audit` existe pero dormant (sin API key) | **ALTA** — diferenciador IA | 1 día (solo activar + UI panel) | `AIController::audit` + nuevo componente `SeoPanel.svelte` en page editor |
| G3 | **Generación de contenido con IA respetando ADN/voz de marca** | Tabla `brand_voice` diseñada, endpoint dormant | **ALTA** — copy ventaja vs Damos | 2 días (activar + UI prompt) | `AIController::generate` + modal en editor |
| G4 | **Traducción multi-idioma con IA** (página completa de un clic preservando estructura de bloques) | Dormant | **MEDIA** — depende si cliente lo pide | 2 días | `AIController::translate` + botón en page header |
| G5 | **Popups programables con triggers** (time/scroll/exit, segmentos, horarios, métricas de clics) | ✗ no implementado | **MEDIA** — pocos clientes lo usan, pero el PDF lo destaca | 4-6 días | Nuevo módulo `Popups` paralelo a `Forms` |
| G6 | **Webmail embebido** (Roundcube SSO) + gestión de cuentas correo desde panel | ✗ no implementado | **BAJA** — tus clientes usan M365, no Hostinger mail | 5-7 días si decides hacerlo | Sub-route `(protected)/tenants/[id]/mail/` con iframe SSO o deep-link |
| G8 | **Capacitación + video tutorial + soporte 1 año** (oferta comercial, no feature técnico) | ✗ — no hay video grabado | **ALTA** comercial | 1 día de grabación con OBS | Pieza de marketing, no de código |
| G9 | **Módulos personalizados** (directorios internos, calculadoras, intranets, reservas) | Diseño del sistema lo permite (block schema-first), pero ningún módulo construido | **BAJA** — bajo demanda | Variable | Caso a caso por cliente |

### 1.3. Lo que YaDev tiene y Damos NO (no perder de vista — son tus armas de venta)

1. **Sitios estáticos en hosting del cliente** → si el VPS YaDev cae, los sitios siguen vivos. Damos cae con su VPS.
2. **DB-per-tenant físicamente aislada** → leak cross-tenant imposible por bug de app. Damos: tenant_id en columnas, aislamiento solo lógico.
3. **Panel en subdominio separado** (`studio.yadev.co`) → superficie de ataque cero en el dominio del cliente. Damos pone admin en `cliente.com/admin_NNN/`.
4. **Stack panel moderno** (Svelte 5 + shadcn dark glassmorphism) → es parte del pitch. Damos = Blade + jQuery genérico.
5. **Costo marginal ≈ $0** por cliente nuevo. Damos paga ancho de banda + CPU de cada visita.
6. **Webhooks outbound + activity log con diffs** → integración Zapier/n8n y auditoría con restore.
7. **Tests: ~390 API + 973 vitest + 8 Playwright + 146 Runner** → calidad demostrable.
8. **Prompt caching Anthropic** cuando enciendas IA → 50-70% cheaper que la IA genérica de Damos.

### 1.4. Recomendación de orden si vas a cerrar gaps (próximas 2 semanas)

1. **G2 + G3 + G4** (3 días) — activas IA. Requiere solo `ANTHROPIC_API_KEY` en Railway y UI panel lateral. Ganas 3 features de venta sin tocar arquitectura.
2. **G1** (5 días) — analytics server-side. Es lo único técnicamente nuevo. Damos lo vende fuerte y tú no lo tienes.
3. **G7** — **DONE.** Scripts injection a nivel tenant + override por página, sanitizado server-side.
4. **G8** (1 día) — graba el video tutorial con tu propio CMS administrando una página de Luqra. Sirve para onboarding + marketing.

G5, G6, G9 los dejas en backlog hasta que un cliente concreto los pague.

---

## 2. Cómo se administra una página en YaDev CMS

Esta sección es la guía operativa. La escribo pensando en que el video tutorial (G8) sale de aquí.

### 2.1. Acceder al panel

1. Abre `https://studio.yadev.co` (en local: `http://studio.yadev.local:5173` con Docker Compose levantado).
2. Login con tu email + contraseña. Si tienes 2FA activado, ingresa el código TOTP de Authenticator.
3. Aterrizas en `/tenants` — lista de clientes que administras. Como dueño, ves todos (Luqra, ECOMAG, Multiservicios, PORON cuando se cree).
4. Click en el cliente que vas a editar → vas al dashboard del tenant.

### 2.2. Estructura del panel del tenant

Sidebar izquierdo (orden actual en `studio/src/routes/(protected)/tenants/[tenant_id]/`):
- **Dashboard** — métricas básicas + atajos
- **Pages** — gestión de páginas (donde vives la mayoría del tiempo)
- **Media** — biblioteca de archivos + carpetas
- **Forms** — formularios + submissions
- **Webhooks** — integraciones outbound
- **Activity** — log de cambios + restore
- **Publishes** — historial de despliegues a producción
- **Settings** — dominios, miembros del equipo, integraciones
- **System Health** — solo admin global, monitoreo Sentry/queue/DB

### 2.3. Editar una página existente (caso 90% del tiempo)

**Ejemplo:** cambiar el hero de la home de Luqra.

1. Sidebar → **Pages** → ves lista con columnas: título, slug, status (draft/published), última actualización, autor.
2. Click en la página "Inicio" (slug `/`) → entras al editor.
3. El editor tiene 3 zonas:
   - **Columna izquierda:** lista de bloques de la página (Hero, Services, Stats, Projects, Contact). Arrastra para reordenar. Click para editar.
   - **Centro:** preview live del bloque seleccionado.
   - **Columna derecha:** propiedades del bloque (campos validados contra el schema en `api/app/Blocks/{Name}/schema.php`).
4. Editas el bloque Hero: cambias el headline, subes una imagen nueva al campo `background` (esto abre el picker de la mediateca: puedes seleccionar existente o subir nueva con drag-drop). El preview se actualiza con autosave debounce 2s.
5. Cada save crea una **versión** del bloque en `block_versions`. Puedes hacer rollback desde el botón "Historial" del bloque.
6. Cuando termines, arriba a la derecha:
   - **Vista previa** → abre `https://preview.yadev.co/?token=...` con la página renderizada con los cambios sin publicar.
   - **Publicar** → confirma + dispara el flujo: API marca page.status=published → encola job → Runner hace `pnpm build` del sitio Astro → rsync a Hostinger del cliente → invalida caché Cloudflare si está configurado. Toma ~90-120s.
   - **Programar publicación** → date picker para publicar en X hora/día.

### 2.4. Crear una página nueva

1. Sidebar → **Pages** → botón "**+ Nueva página**".
2. Modal pide: título, slug (auto-generado, editable), template inicial.
3. **Templates** disponibles (Phase 3): "En blanco", "Servicio", "Caso de estudio", "Landing producto". Cada template precarga 3-6 bloques.
4. Click "Crear" → entras al editor en modo draft.
5. Click "**+ Agregar bloque**" entre dos bloques → menú con los 7 tipos: Hero / Services / Projects / Stats / Cta / Contact / RichText.
6. Configuras → preview → publicas. Mismo flujo que §2.3.

### 2.5. Duplicar una página (útil para landings de campaña)

1. En la lista de Pages → kebab menu (⋯) en la fila → "**Duplicar**".
2. Modal pide nuevo título + slug (sufijo `-copia` por defecto).
3. Copia todos los bloques con sus contents (no las versiones históricas) + queda en draft.
4. Editas lo que cambia (típicamente headline + CTA + UTM en links).
5. Publicas.

### 2.6. Bulk publish (cuando cambias varias páginas a la vez)

1. En la lista → checkbox al inicio de cada fila.
2. Selecciona N páginas → barra de acción aparece arriba con contadores.
3. Click "**Publicar seleccionadas**" → confirmación → dispara un único job que despliega todas en el mismo build (eficiente).
4. Aparece en **Publishes** como un job agrupado con `page_ids[]`.

### 2.7. SEO de una página

Dentro del editor de página, tab "**SEO**" en columna derecha (o panel inferior):
- **Meta title** (recomendado 50-60 chars, indicador rojo/amarillo/verde).
- **Meta description** (150-160 chars).
- **OG image** — selecciona de mediateca o auto-generada por Runner (1200×630, logo + título de página).
- **Schema.org** — JSON-LD editable como bloque dedicado o auto-derivado del template (LocalBusiness, Service, FAQ).
- **Canonical URL** — auto-generado, override manual si necesitas.
- **Robots** — `index,follow` por defecto. `noindex` para landings de pago.

Cuando enciendas IA (G2): aparece **panel lateral "Auditoría SEO"** con score 0-100 + lista accionable: "H1 muy largo", "falta H2 después de H1", "schema FAQ no detectado", etc. Click en sugerencia → la aplica.

### 2.8. Mediateca (uso operativo)

1. Sidebar → **Media** → ves grid con miniaturas, filtros por carpeta/tag/tipo.
2. Subir: drag-drop directo o botón "+". Sube N archivos en paralelo con barra de progreso (RRB chunked upload sigue pendiente en backlog — actualmente single-shot funciona bien hasta ~20 MB).
3. Click en una imagen → modal con:
   - **Editor:** crop, rotate, flip, filtros básicos. Save crea variante nueva.
   - **Variantes:** thumb / webp / og (auto-generadas por sharp en Runner).
   - **Reemplazar:** sube archivo nuevo manteniendo la URL — útil para "cambiar logo" sin tocar todos los bloques que lo usan.
   - **Usage:** muestra en qué páginas y bloques está usada (gap cerrado vs Damos).
   - **Tags + carpeta:** edita.
4. Eliminar: warning si la imagen tiene `usage_count > 0`.

### 2.9. Formularios (caso típico: contacto)

1. Sidebar → **Forms** → "**+ Nuevo formulario**".
2. Builder visual: arrastras campos (text, email, phone, textarea, select, checkbox, file upload, hidden con UTM).
3. Settings del formulario:
   - **Notificaciones:** email destinatarios (admin de tu cliente), template subject + body.
   - **WhatsApp** (cuando G2 IA active el formateo automático): número + plantilla.
   - **Auto-respuesta al lead:** template HTML.
   - **Spam:** honeypot ON, reCAPTCHA v3 opcional.
   - **Redirección post-submit:** URL thank-you.
4. **Embed:** copias snippet `<form data-yadev-form="abc123">` y lo pegas en cualquier bloque RichText o un componente del sitio Astro.
5. **Submissions:** sidebar del form muestra todos los envíos paginados, filtro por fecha/estado leído, export CSV completo o filtrado.

### 2.10. Publicación: qué pasa cuando le das al botón

Flujo end-to-end ([detalle en `architecture/publish-flow.md`](architecture/publish-flow.md)):

```
1. Click "Publicar" en Studio
   ↓
2. API: PageController@publish
   - valida permisos (rol editor+)
   - marca page.status = published
   - graba en activity_log con diff
   - encola job PublishPageJob en queue 'publish' (Redis)
   - responde 202 Accepted con publish_id
   ↓
3. Studio: muestra toast "Publicando..." + polling /publishes/{id}/status
   ↓
4. Worker Horizon ejecuta PublishPageJob:
   - llama Runner via HMAC: POST /jobs/build con tenant_id + page_ids[]
   ↓
5. Runner (Node + BullMQ):
   - clona o pull repo del sitio del cliente (yadevOs/site-luqra)
   - fetch al API: GET /v1/tenants/{id}/pages/published → JSON completo de páginas
   - transformers/ mapean bloques → componentes Astro
   - pnpm build → dist/
   - sharp genera variantes de imágenes nuevas
   - rsync -avz dist/ user@hostinger.com:public_html/
   - opcional: purge Cloudflare cache si el tenant tiene CF habilitado
   - notifica API: POST /v1/publishes/{id}/complete
   ↓
6. Studio: toast cambia a "Publicado" + link al sitio live + entrada en Publishes log.
```

Tiempo típico: 90-120 segundos. Si falla, Sentry lo captura + el job queda en `failed_jobs`, lo reintentas desde el dashboard de Horizon (`api.yadev.co/horizon`).

### 2.11. Rollback (algo se publicó mal)

Dos caminos:

**A) Rollback de un bloque específico** (granular, no requiere publicación nueva del sitio entero):
1. Page editor → bloque → "Historial" → ves versiones con timestamp + autor.
2. Click "Restaurar" en la versión que quieres → activity log graba la restauración.
3. Publicas la página (vuelve al flujo §2.10).

**B) Rollback del sitio entero a un build anterior:**
1. Sidebar → **Publishes** → ves lista de despliegues con timestamp + commit hash + page_ids.
2. Click en el build bueno → "**Restaurar este build**" → Runner hace rsync del snapshot guardado (los últimos 10 builds quedan en `runner/snapshots/{tenant}/{build_id}/`).
3. Toma ~30s (no rebuild, solo rsync).

### 2.12. Webhooks (integrar con Zapier / n8n / CRM)

1. Sidebar → **Webhooks** → "**+ Nuevo**".
2. Configuras: URL destino, secret HMAC, eventos suscritos (`page.published`, `form.submitted`, `media.uploaded`, etc.).
3. Cada vez que el evento dispara, Runner envía POST con payload firmado.
4. **Deliveries** muestra cada intento con request/response/status, reintentos automáticos con backoff exponencial.

### 2.13. Configuración del tenant (Settings)

Sidebar → **Settings**:
- **General:** nombre del cliente, logo, paleta de colores (CSS vars del sitio), zona horaria.
- **Dominios:** lista de dominios verificados (luqraingenieria.com, www.luqraingenieria.com). Verificación por TXT record.
- **Miembros:** invitar usuarios con rol admin/editor/viewer. Magic link de invitación.
- **Integraciones:** API keys de servicios externos (Cloudflare, Meta Cloud API WhatsApp cuando exista).
- **Scripts:** Settings → Scripts. Dos textareas (`<head>` global y `<body>` end global) más una lista estructurada de scripts gestionados (label + ubicación + código + toggle activo). Cada página tiene además un panel "Scripts de esta página" con modos `Heredar` / `Sumar` / `Reemplazar`. El sanitizador rechaza `<form>`, `<base>`, `<object>`, `<embed>`, iframes a dominios no listados (whitelist en `config('yadev.scripts.allowed_iframe_domains')`), y `<script src>` por HTTP no-HTTPS. Errores aparecen con código `SCRIPT_FORBIDDEN_PATTERN` en el toast del editor.
- **Backups:** muestra histórico de backups B2 con botón "Restaurar este backup" (admin global only).

### 2.14. Atajos de teclado (cheatsheet — RRA cerrado, ver modal en panel con `?`)

- `Cmd/Ctrl + K` — Search global (páginas, media, formularios, settings).
- `Cmd/Ctrl + S` — Save manual (autosave ya activo, esto fuerza).
- `Cmd/Ctrl + P` — Preview de la página actual.
- `Cmd/Ctrl + Shift + P` — Publicar.
- `Esc` — Cerrar modal / volver atrás.
- `?` — Mostrar este cheatsheet.

### 2.15. Errores comunes y cómo resolverlos

| Síntoma | Causa probable | Solución |
|---------|----------------|----------|
| "Publicación falló" con 502 | Runner no responde | Check Railway dashboard del servicio `yadev-cms-runner`. Reinicia. Reintentar publish. |
| Imagen sube pero queda sin variantes | sharp falló en Runner | Logs Runner. Generalmente formato no soportado (HEIC, AVIF muy nuevo). Reconvertir a JPG/PNG antes. |
| Cambio publicado pero no se ve en el sitio | Caché Cloudflare o navegador | Hard refresh (Cmd+Shift+R). Si persiste, purga caché desde Settings → Integraciones → Cloudflare. |
| "Sesión expirada" mientras editas | Token Sanctum expiró (24h default) | Login de nuevo. Tu draft está autosaved, no pierdes contenido. |
| Bloque que no acepta un valor | Schema rechazó el input | Mensaje rojo abajo del campo. Schema en `api/app/Blocks/{Type}/schema.php` es la fuente de verdad. |
| Sitio live caído | Hostinger del cliente, no tu CMS | Tu CMS sigue funcionando porque los sitios son estáticos. El cliente debe contactar a su Hostinger. |

---

## 3. Resumen ejecutivo

- **Lo que falta de Damos en YaDev (real):** 3 items con código nuevo (analytics G1, popups G5, webmail G6) + 3 items que solo requieren encender la API key de IA (G2, G3, G4) + 1 pieza de marketing (G8 video tutorial). G7 (scripts injection) ya está implementado. Total deuda funcional contra el PDF Damos: **manejable en 2 semanas**.
- **Lo que YA tienes y vale como pitch:** 5 diferenciadores estructurales (sitios estáticos en hosting del cliente, DB-per-tenant, panel en subdominio separado, stack moderno, costo marginal ≈ $0) + 10 features que Damos no tiene (brand voice IA, prompt caching, webhooks, activity log con diffs, etc.).
- **Cómo administras una página hoy:** flujo descrito §2.3 a §2.11. Editor visual + autosave + preview + publish + rollback. Todo funcional en `studio.yadev.co`.
- **Próximo paso accionable:** decidir si invertir 2 semanas en cerrar G1-G4 antes de salir a vender, o si sales ya con lo que tienes y los cierras bajo demanda del primer cliente externo.

---

_Documento generado 2026-05-28. Cualquier feature mencionada en §2 sin link explícito está en `api/app/Http/Controllers/Api/V1/` o `studio/src/routes/(protected)/`._
