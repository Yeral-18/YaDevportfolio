# Multi-Tenancy Strategy — YaDev CMS

## Decisión: database-per-tenant con `stancl/tenancy` v3

### Por qué no single-database multi-tenant
- Aislamiento real: si un cliente hace backup/export, se respalda SU db entera.
- Migraciones por cliente: se puede probar un cambio de schema en un tenant staging sin afectar a producción.
- Performance: tablas más pequeñas = índices más efectivos = queries más rápidas.
- Compliance: un error en una query (olvidar WHERE `tenant_id`) no filtra datos de otro cliente — imposible leer lo que no está en la DB seleccionada.
- Portabilidad: un cliente que se va se le entrega su DB + su código + su media, y listo. No extracción manual.

### Por qué no schema-per-tenant (MySQL no lo soporta nativo)
- MySQL llama "schema" a "database" (sinónimos), por lo tanto schema-per-tenant = database-per-tenant en MySQL.

### Trade-offs aceptados
- Overhead operacional: cada tenant tiene su propia DB → `php artisan migrate --tenants` itera todas.
- Costo de conexión: pool de conexiones por tenant. Se mitiga con `stancl/tenancy` que reutiliza PDO por request.
- Queries cross-tenant imposibles sin switchear conexiones. Para reporting YaDev-wide, se hace agregación desde la DB central o ETL a un warehouse.

---

## Diseño con stancl/tenancy v3

### DB central: `yadev_central`

Tablas clave:
- `tenants` — 1 fila por cliente. id, name, slug, status, plan, settings (JSON), created_at.
- `domains` — mapping dominio → tenant_id. permite múltiples dominios por tenant (ej: `.com` + `.com.co`).
- `users` — usuarios GLOBALES de YaDev (super-admins). Los usuarios del cliente viven en la DB del tenant.
- `subscriptions` — plan y billing del tenant.
- `tenant_activity_log` — registro centralizado de eventos (tenant creado, suspendido, upgrade, etc.).

### DB por tenant: `tenant_{slug}`

Ejemplo: `tenant_multiservicios`.
Tablas:
- `users` — admins/editores DEL CLIENTE. Nunca ven otros tenants.
- `pages` — páginas del sitio.
- `sections` — secciones ordenadas dentro de páginas.
- `blocks` — bloques dentro de secciones con `data` JSON tipado.
- `media` — archivos subidos a la mediateca.
- `forms` + `form_submissions` — formularios y envíos.
- `popups` — popups programables.
- `menus` + `menu_items` — navegación editable.
- `settings` — key-value settings del sitio (SEO global, GA, Meta Pixel, horario, etc.).
- `seo_meta` — meta tags por página.
- `translations` — i18n (Fase 3).
- `activity_log` — log granular de cambios.
- `redirects` — 301/302 redirects.
- `api_tokens` — Sanctum tokens (storage per-tenant).

Ver `database/tenant-schema.sql` para DDL completo.

### Resolución de tenant (middleware)

El API `api.yadev.co` **no resuelve tenant por subdominio del propio API** (siempre es `api.yadev.co`). Resuelve tenant por una de estas fuentes, en orden de prioridad:

**1. Por token Sanctum** (default cuando hay login):
   - Request viene del panel `studio.yadev.co` con `Authorization: Bearer {token}`.
   - Token Sanctum embebe `tenant_id` como ability/claim (`tenant:multiservicios`).
   - Middleware `ResolveTenantFromToken` switchea la conexión MySQL por defecto a `tenant_{slug}`.

**2. Por `tenant_id` en URL path** (runner/build, calls administrativas):
   - Endpoints tipo `GET /v1/tenants/{tenant_id}/content-tree` usados por el runner en build time.
   - Middleware `ResolveTenantFromPath` lee `{tenant_id}` del route param.
   - Si también hay token: validar que `token.tenant_id === path.tenant_id`. Mismatch → 403 + log `cross_tenant_attempt`.
   - Para el runner interno, autenticación es vía HMAC (no token de usuario) + el `tenant_id` en path es la única fuente de verdad.

**3. Por `Origin` header** (sitio cliente haciendo fetch público):
   - Caso raro: endpoint público como form submission desde `multiserviciospj.com`.
   - Middleware `ResolveTenantFromOrigin` busca `Origin` en `yadev_central.domains` → resuelve tenant.
   - Solo aplica a endpoints listados como "públicos" (p.ej. `/v1/public/forms/{slug}/submit`).

**4. Super-admin YaDev (Angel) impersonando:**
   - Angel inicia sesión en `studio.yadev.co` con `super_admin` token.
   - Selecciona un tenant desde el selector del panel → obtiene un token impersonation con `impersonated_tenant_id`.
   - Middleware `ImpersonateTenant` switchea a ese tenant pero registra `impersonator_id` en `tenant_activity_log`.

**Regla de oro:** si más de una fuente está presente en el request, TODAS deben resolver al mismo tenant. Cualquier inconsistencia → 403.

### Flujo de login del cliente

```
1. Cliente va a studio.yadev.co
2. Pantalla login pide: email, password, (opcional: "¿tu dominio?" autocompleta)
3. POST https://api.yadev.co/v1/auth/login { email, password }
   → Laravel consulta yadev_central.users_index (email → tenant_id) para resolver el tenant
   → Si el email está asociado a múltiples tenants, pide tenant_domain al usuario
4. Laravel resuelve tenant, switchea conexión, valida credenciales contra tenant.users
5. Genera Sanctum token con abilities según rol: ['tenant:multiservicios', 'edit:pages', 'publish:site']
6. Devuelve { token, user, tenant }
7. Cliente (studio.yadev.co) guarda token en cookie httpOnly con Secure + SameSite=Lax (CORS con credentials).
8. Todos los requests siguientes van desde studio.yadev.co → api.yadev.co con Authorization: Bearer $token.
```

**Recomendación:** introducir una tabla auxiliar `yadev_central.users_index` con `(email, tenant_id)` para que el cliente solo teclee email + password (sin tener que recordar su dominio). Aparece como sugerencia abierta en `READY-FOR-REVIEW.md`.

---

## Provisionar un tenant nuevo (flujo operacional)

```bash
# 1. Super-admin ejecuta desde dashboard o CLI
php artisan tenants:create \
  --name="Multiservicios P&J" \
  --slug=multiservicios \
  --domain=multiserviciospj.com \
  --admin-email=gerencia@multiserviciospj.com \
  --admin-name="Yamileth Pérez" \
  --plan=standard

# Internamente ejecuta:
# a) INSERT en central.tenants + central.domains + central.users_index.
# b) CREATE DATABASE tenant_multiservicios CHARACTER SET utf8mb4.
# c) php artisan tenants:migrate --tenant=multiservicios (corre todas las migraciones del tenant).
# d) php artisan tenants:seed --tenant=multiservicios (seed base: roles, admin user, páginas por defecto).
# e) Envía email a gerencia@... con link de primer-login + set-password.

# 2. (Opcional) cargar contenido inicial
php artisan tenants:import --tenant=multiservicios --file=seed-multiservicios.sql

# 3. Inicializar build dir en runner
ssh vps 'mkdir -p /srv/builds/multiservicios && cd /srv/builds/multiservicios && git clone git@github.com:yadevOs/site-multiservicios.git .'

# 4. Registrar dominio en el runner
curl -X POST http://localhost:8080/admin/register-site \
  -H "X-Admin-Key: $ADMIN_KEY" \
  -d '{"tenant":"multiservicios","deploy_target":"user@shared:/public_html/multiservicios/","build_dir":"/srv/builds/multiservicios"}'

# 5. Primer build manual
php artisan tenant:publish --tenant=multiservicios --force
```

El comando `tenants:create` debe ser idempotente-seguro: si falla a la mitad, dejar el tenant en `status=provisioning` y permitir reintentar.

---

## Apagar / exportar un tenant (offboarding)

1. `php artisan tenant:suspend multiservicios` — marca `status=suspended`. El API devuelve 403 a sus requests. El sitio público sigue online.
2. `php artisan tenant:export multiservicios --format=zip` — genera zip con:
   - dump SQL de la DB tenant
   - zip de `storage/tenants/multiservicios/` (media)
   - zip del repo del runner `/srv/builds/multiservicios/`
   - README.md con instrucciones para auto-hostear.
3. `php artisan tenant:delete multiservicios --confirm` — elimina DB, media, runner dir. Guarda registro en central con `deleted_at` por compliance (no hard-delete la fila del tenant en central durante 90 días).

---

## Testing multi-tenant

- Test base: `TenancyTestCase` que crea un tenant de prueba en `setUp`, ejecuta el test dentro de ese tenant, y borra todo en `tearDown`.
- Test de seguridad obligatorio: `CrossTenantIsolationTest` — crea 2 tenants, intenta acceder a recursos del tenant B con token del tenant A. Debe devolver 404.
- Test de performance: provisionar 20 tenants + correr migraciones en todos < 60 segundos (sanity check).

---

## Limitaciones conocidas

- No hay cross-tenant reporting nativo. Para "cuántos clientes totales usan el CMS", se consulta central. Para "total submissions del mes", se requiere un job nocturno que agregue a central.
- Backups de DB por-tenant son muchos archivos pequeños. A 20+ tenants conviene script que los tarree diariamente antes de mandar a B2.
- `php artisan migrate --tenants` en 20 tenants tarda ~2 minutos. No crítico pero planificar windows de mantenimiento.
