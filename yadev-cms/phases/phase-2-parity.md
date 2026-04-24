# Phase 2 — Paridad Damos + Onboarding ECOMAG

> Duración: **6 semanas** (30 días hábiles).
> Objetivo: CMS con todas las features que un editor profesional necesita. Onboardear ECOMAG como segundo tenant para validar la escalabilidad.
> Entra con Fase 1 estable (Multiservicios publicando sin intervención humana por 2 semanas).

---

## Semana 5 — Bloques avanzados

### Objetivo: cubrir todos los bloques usados en Multiservicios + ECOMAG

Agregar block types faltantes a la librería:
- [ ] `stats_bar` (counters animados).
- [ ] `benefits_grid` (3 cards horizontales con icono).
- [ ] `bento_projects` (featured + 3 smaller).
- [ ] `clients_carousel` (auto-scrolling logo carousel).
- [ ] `cta_banner` (gradient banner con CTA).
- [ ] `footer_mega` (4 columnas + certifications + copyright).
- [ ] `image_gallery` (grid | masonry | carousel).
- [ ] `faq` (accordion).
- [ ] `timeline` (historia de la empresa).
- [ ] `team_grid` (fotos + nombres + roles).
- [ ] `testimonials_slider`.
- [ ] `pricing_table` (planes).

Por cada bloque:
- Schema Laravel + Form Request validator.
- Editor Svelte en `admin/src/lib/blocks/{type}/`.
- Transformer en `runner/transformers/{type}.mjs` que convierte el JSON del API al shape que Astro espera.
- 1+ test feature.

### Sistema de íconos reutilizable
- [ ] Catálogo de iconos: lucide-svelte (1000+ iconos).
- [ ] Campo `icon` en bloques = string name de lucide.
- [ ] En Astro, render con `<Icon name={block.data.icon} />` component custom.

### Día a día semana 5
| Día | Tarea |
|-----|-------|
| 21 | `stats_bar` + `benefits_grid` + tests |
| 22 | `bento_projects` + `clients_carousel` + tests |
| 23 | `cta_banner` + `footer_mega` + tests |
| 24 | `image_gallery` + `faq` + `timeline` + tests |
| 25 | `team_grid` + `testimonials_slider` + `pricing_table` + QA |

---

## Semana 6 — Forms avanzados + notificaciones

### Form builder
- [ ] UI en `/settings/forms` para crear formularios visualmente:
  - Drag-drop de campos (text, email, tel, select, textarea, checkbox, radio, file, date).
  - Propiedades por campo: label, placeholder, required, validación regex, options para selects.
  - Configurar notificaciones: emails, WhatsApp.
  - Thank-you message o redirect URL.
  - reCAPTCHA on/off.

### Submissions dashboard
- [ ] `/forms/{id}/submissions` — tabla paginada con filtros.
- [ ] Click en fila → detalle con todos los campos + metadata (IP, user agent, UTM).
- [ ] Bulk actions: marcar leído, archivar, spam, eliminar.
- [ ] Export CSV / XLSX.
- [ ] Search full-text.

### Notifications workers
- [ ] Job `SendFormNotification($submission)`:
  - Email via **Resend** (no SMTP VPS). API key en `/etc/yadev/secrets.env`.
  - WhatsApp vía Meta Cloud API (token verificado).
  - Webhook saliente si el tenant configuró URL.
- [ ] Plantillas editables de email (Blade + merge tags `{{ nombre }}`).

### Anti-spam
- [ ] Honeypot field oculto.
- [ ] Rate limiting 3/10min por IP.
- [ ] Score reCAPTCHA v3 < 0.5 → marca como spam, no notifica.
- [ ] Blacklist de keywords configurable por tenant.

---

## Semana 7 — SEO + Menús + Popups

### SEO editor por página
- [ ] Tab "SEO" en editor de página con:
  - Meta title (con preview Google SERP).
  - Meta description.
  - OG image picker.
  - Canonical URL.
  - Robots (`index, follow` vs `noindex`).
  - Schema.org JSON-LD con editor visual (presets: LocalBusiness, Organization, FAQPage, BreadcrumbList).
- [ ] SEO score básico: longitud title, length description, missing alt texts, h1 presence.

### Menús editables
- [ ] `/menus` con drag-drop para ordenar items.
- [ ] Múltiples menús por tenant: header, footer, mobile, etc.
- [ ] Link types: page interna (autocompleta), URL externa, anchor `#seccion`, custom.
- [ ] Sub-items (2 niveles de profundidad).

### Popups
- [ ] `/popups` CRUD.
- [ ] Editor visual del contenido (reutiliza block editor).
- [ ] Triggers: time on page (segundos), scroll (%), exit intent, click en selector.
- [ ] Target: pages (array de slugs o ["*"]), devices (all/desktop/mobile).
- [ ] Frequency: always, once_per_session, once_per_user (cookie).
- [ ] Active dates (from/until).
- [ ] Views/clicks counter → analytics básicos.

### Redirects
- [ ] `/redirects` tabla simple.
- [ ] Import CSV bulk (útil en migraciones).

---

## Semana 8 — Mediateca avanzada + Activity log

### Mediateca avanzada
- [ ] Folders jerárquicos (drag-drop para mover).
- [ ] Tags.
- [ ] Search + filtros por mime, size, date.
- [ ] Conversiones automáticas (cola async):
  - thumb 300x300
  - medium 800x600
  - large 1600x1200
  - webp de cada uno
  - og 1200x630 (si se marca como "Use as OG")
- [ ] Replace imagen manteniendo URL (útil cuando el cliente quiere actualizar un logo sin romper referencias).
- [ ] Usage tracker: mostrar en qué bloques está usada cada imagen.

### CDN-ready
- [ ] Opcional por tenant: configurar Cloudflare R2 bucket.
- [ ] Si está configurado, uploads van a R2 + URLs públicas.
- [ ] Fallback a local filesystem si R2 no está configurado.

### Activity log UI
- [ ] `/activity` timeline con filtros (actor, action, date range).
- [ ] Hover en item → ver diff before/after en JSON.
- [ ] Botón "Restaurar esta versión" en cada cambio de bloque.

### Version restore
- [ ] `POST /api/v1/blocks/{id}/restore/{version}` — crea nueva versión con los datos del pasado + log "block.restored".

---

## Semana 9 — Users management + 2FA + Multi-user collaboration

### Users management
- [ ] `/users` → listar users del tenant.
- [ ] Invite by email → envía link con token de registro.
- [ ] Asignar rol: admin / editor / viewer.
- [ ] Deshabilitar (no borrar, para auditoría).
- [ ] Forzar cambio de password.

### 2FA (TOTP)
- [ ] `composer require pragmarx/google2fa-laravel`.
- [ ] `/settings/security` → enrollment con QR code.
- [ ] Backup codes descargables.
- [ ] Login flow: después de password, pide código TOTP si el user lo tiene habilitado.
- [ ] Obligatorio para `tenant_admin`. Forzar en primer login post-upgrade.

### Collaboration
- [ ] Cuando 2 users editan el mismo bloque → mostrar presencia via Reverb (cursor + avatar).
- [ ] Lock optimista: si alguien guardó mientras editabas → mostrar diff y permitir merge/overwrite.

---

## Semana 9.5 — Paridad Damos: estadísticas, webmail, módulos Colombia

Esta sección agrupa capacidades que Damos.co vende como estándar y que debemos cerrar antes de onboardear ECOMAG. No rompe la cadencia semanal: las tareas se distribuyen a lo largo de semanas 6-9 como subtareas transversales, consolidadas aquí para claridad. Contexto competitivo: ver `competitive-analysis-damos.md`.

### Estadísticas sin cookies con GoAccess

**Decisión:** en lugar de reinventar analytics, reutilizar los logs de acceso que Nginx ya genera. GoAccess los parsea y emite JSON/HTML. Cero scripts client-side, cero consentimiento GDPR/ley 1581 (no hay cookies ni fingerprinting), privacy-first by design.

- [ ] Instalar `goaccess` en el VPS (`apt install goaccess`).
- [ ] Configurar `/etc/goaccess/goaccess.conf` con log format de Nginx (combined + request_time + upstream_addr).
- [ ] Cron cada hora: `goaccess /var/log/nginx/{tenant}-access.log -o /srv/analytics/{tenant}/latest.json --output-format=json --date-format=%d/%b/%Y --time-format=%H:%M:%S --log-format=COMBINED`.
- [ ] Endpoint `GET /v1/tenants/{tenant_id}/analytics/snapshot` lee el JSON más reciente, lo cachea 10 min en Redis, responde dashboard-ready.
- [ ] Tabla `analytics_snapshots` en tenant DB (cache diario — ver schema actualizado).
- [ ] UI dashboard en `/studio/{tenant}/analytics`:
  - Visitas únicas / páginas vistas (hoy, 7d, 30d).
  - Top páginas.
  - Top países + mapa ligero (topojson).
  - Top navegadores + sistemas operativos.
  - Top referrers + términos de búsqueda (cuando vienen en el Referer).
  - Horas pico (heatmap hora×día).
  - Status codes (detectar 404 masivos).
- [ ] Export CSV.

**Nginx multi-tenant log split** (pre-requisito):
Cada vhost de sitio cliente escribe a su propio access.log:
```
server_name multiserviciospj.com;
access_log /var/log/nginx/multiservicios-access.log combined;
```
Pero los sitios cliente viven en Hostinger shared, no en el VPS. **Detalle operacional:** Hostinger expone logs raw via API de cPanel — el runner los descarga diariamente a `/srv/logs/{tenant}/` y GoAccess los procesa ahí. Si el cliente prefiere analytics en tiempo real, se ofrece CNAME opcional a VPS + Nginx proxy (addon post-MVP).

### Webmail integrado (Roundcube embebido)

**Decisión arquitectónica:** no construimos cliente webmail custom (esfuerzo desproporcionado vs valor del usuario final). Se embebe **Roundcube** vía iframe con SSO desde el studio.

- [ ] Instalar Roundcube en `/srv/roundcube/` (binding a `/webmail/` de `studio.yadev.co`).
- [ ] Configurar Roundcube multi-host: lee `?tenant=X` → carga config IMAP/SMTP del tenant desde endpoint interno.
- [ ] Tabla `mail_accounts` (en central, no en tenant) con: `tenant_id`, `host_imap`, `port_imap`, `host_smtp`, `port_smtp`, `username`, `password_encrypted` (vault con AES-256-GCM), `provider` (m365|gworkspace|generic_imap|hostinger).
- [ ] UI en panel: sección "Correo" con listado de cuentas + botón "Abrir webmail" → redirect con SSO token de un solo uso.
- [ ] Para tenants con **Microsoft 365** (caso Multiservicios): opción alternativa "Abrir en Outlook Web" con deep-link directo `outlook.office.com/?prompt=login&login_hint={email}`.
- [ ] Para tenants con **Google Workspace**: deep-link a `mail.google.com/a/{domain}`.
- [ ] Para tenants con **servidor propio / Hostinger mail**: usar Roundcube embebido.
- [ ] Gestión de cuentas (solo si es servidor propio o Hostinger): crear/editar/borrar buzones desde el panel (vía API Hostinger cuando exista, sino manual con instrucciones).

**Roundcube NO sustituye al cliente de correo nativo del empresario.** El usuario sigue usando Outlook desktop/móvil para su día a día. El webmail en panel es para acceso de emergencia y para que la empresa vea "todo en una plataforma" (argumento comercial frente a Damos).

### Block type `stats` (gap Odir)

Contador de estadísticas con animación. Diferente de `stats_bar` ya planificado: este permite iconos custom por item y formato flexible.

Schema:
```php
// api/app/Blocks/Stats.php
'heading' => 'nullable|string|max:200',
'items' => 'required|array|min:2|max:8',
'items.*.value' => 'required|numeric',
'items.*.suffix' => 'nullable|string|max:10', // "+", "%", "K"
'items.*.label' => 'required|string|max:100',
'items.*.icon' => 'nullable|string|max:64', // lucide name
'items.*.color_accent' => 'nullable|regex:/^#[0-9a-f]{6}$/i',
'layout' => 'in:horizontal_bar,grid_2x2,grid_4_col,vertical_stack',
'animation' => 'in:counter_up,fade_in,none',
```

Editor + transformer + test igual que otros bloques. Documentado en `api-contract.md`.

### Entidad `sedes` / sucursales (gap Odir)

Empresas colombianas multi-sucursal (Multiservicios, ECOMAG, etc.) requieren gestionar varias oficinas. Hoy se harcodea. Solución: entidad first-class.

- [ ] Tabla `sedes` en tenant schema (ver SQL actualizado).
- [ ] CRUD en `/studio/{tenant}/sedes`.
- [ ] Campos: `name`, `address`, `city`, `department`, `country`, `phone`, `whatsapp`, `email`, `lat`, `lng`, `hours` (JSON), `is_main`, `order`, `icon`.
- [ ] Bloques que consumen la entidad:
  - `footer_mega` → lista sedes en columna "Sedes".
  - `contact_locations_map` (nuevo) → grid con mapa + info por sede.
  - `page_contact` puede referenciar `sede_id` principal para mostrar dirección.
- [ ] Endpoint `GET /v1/tenants/{tenant_id}/sedes`.

### Módulo "Consulta pública" / tracking sin login (gap Odir)

Ejemplo Odir: el visitante ingresa un número de certificado/dictamen y ve su estado. Caso de uso común en Colombia (empresas de certificación, logística, servicios públicos).

- [ ] Plantilla de módulo custom genérica `public_lookup`.
- [ ] Configurable por tenant: definir "colección" (nombre, campos, API source).
- [ ] Frontend: bloque `block_lookup_widget` que renderiza input + botón "Consultar" → fetch a endpoint público del tenant.
- [ ] Backend: endpoint `GET /v1/public/lookup/{tenant}/{collection}/{code}` — rate limited, cacheable, público (sin auth).
- [ ] Fuente de datos: CSV subido por el cliente / Google Sheets webhook / endpoint externo de su ERP.
- [ ] Fase 2 entrega plantilla + ejemplo funcional para ECOMAG (consulta de proyectos en curso). Integraciones custom a ERPs se cotizan como desarrollo a medida.

### Pagos Wompi / Stripe (opcional — posponer si scope aprieta)

Módulo opcional. Se documenta pero se posterga a `phase-future.md` si no hay tenant que lo pida durante Fase 2.

- [ ] `payment_providers` config por tenant: `wompi` (Colombia, tarjetas + PSE + Nequi + Daviplata), `stripe` (internacional).
- [ ] Block type `pricing_table_checkout` con botón "Pagar" que dispara Wompi Widget o Stripe Checkout.
- [ ] Webhook handler `POST /v1/webhooks/wompi` y `POST /v1/webhooks/stripe` → actualiza `payments` table, notifica admin.
- [ ] Decisión de scope: NO en Fase 2 inicial. Documentado para activación bajo demanda.

---

## Semana 10 — Onboarding ECOMAG

### Objetivo
Migrar ECOMAG (segundo cliente) al CMS para validar que el sistema escala a N tenants sin ad-hoc hacks.

### Día a día
- [ ] Día 46: `php artisan tenants:create ecomag --domain=ecomagsas.com ...`.
- [ ] Día 47: Mapear componentes ECOMAG a bloques del CMS. Si aparecen bloques nuevos (ej: el hero con 7 hojas flotantes de ECOMAG), diseñar schema y editor. Si el diseño es muy específico → agregar al catálogo como `hero_leaves_floating` con config editable.
- [ ] Día 48: Seed `seed-ecomag.sql` con datos reales.
- [ ] Día 49: Refactor Astro de ECOMAG en rama `cms-compatible` (similar a Multiservicios semana 4).
- [ ] Día 50: Test publish E2E → cutover.

### Aprendizajes documentados
Al cerrar ECOMAG, documentar en `/docs/onboarding-playbook.md`:
- Tiempo total real.
- Problemas encontrados.
- Bloques nuevos que hubo que crear.
- Ajustes al contrato API.

---

## Entregables Fase 2
- 15+ block types disponibles en el catálogo.
- Form builder completo con submissions management.
- SEO + menús + popups + redirects editables.
- Mediateca con folders/tags/usage tracker.
- 2FA + multi-user collaboration.
- 2 tenants activos en producción (Multiservicios + ECOMAG).
- Playbook de onboarding (<2 días para un sitio similar a los existentes).

## Métricas
- Tiempo onboarding nuevo cliente: <16 horas (desde contrato firmado hasta sitio editable).
- Uptime: 99.5% api + 99.9% sitios estáticos.
- Feedback cualitativo de las dos clientas (NPS >40).

## Preparación Fase 3
- Con 2 tenants y tráfico real, decidir si el plan VPS $8 aguanta o upgradear.
- Tener audit log de publishes que falaron para priorizar bugs de runner.
- Preguntar a Yeral si quiere IA como default o como addon pago.
