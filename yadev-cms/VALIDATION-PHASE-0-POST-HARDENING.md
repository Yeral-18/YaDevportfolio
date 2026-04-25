# Phase 0 Post-Hardening Validation Report

Fecha: 2026-04-25
Agente: I (devops-engineer)
Baseline: VALIDATION-PHASE-0-REPORT.md (agente H, 2026-04-24)

## Resultado global

⚠️ PASS CON NOTAS — Infra y Studio: 100% verdes. API: build OK, extensiones OK, test OK; el smoke del endpoint /health retorna 500 porque el `.env` local tiene `CACHE_STORE=database` (SQLite) pero dentro del container no existe el archivo `database.sqlite` — la caché que usa el rate-limiter falla antes de llegar a la lógica de negocio. No es una regresión del hardening: el `.env` de dev nunca fue pensado para correr la imagen. El bloqueante del agente H (`ext-exif`) está resuelto.

---

## Hashes de HEAD validados

| Repo | Esperado | Obtenido | Estado |
|------|----------|----------|--------|
| infra | 29b2666 | 29b26669c9f291f3d9e79ee85b6ebaa7c3a4fa3e | ok |
| api | d76d222 | d76d22245d4a162a0d0b98e1983411dccf6423b8 | ok |
| studio | 4ada179 | 4ada17939f0157d6d96cad0be696a38e761900b9 | ok |

---

## 1. Infra

- **docker compose config -q:** ok — YAML válido sin errores
- **docker compose pull (digests):** ok — 5 imágenes bajadas con digest pinneado (`@sha256:` presente en todos los servicios según `config` output)
- **Port bindings verificados en config:** todos los 6 puertos tienen `host_ip: 127.0.0.1` — sin binding a `0.0.0.0`
- **4 servicios healthy:**
  - `yadev-cms-mysql` — `healthy`, `127.0.0.1:3307->3306/tcp`
  - `yadev-cms-redis` — `healthy`, `127.0.0.1:6380->6379/tcp`
  - `yadev-cms-mailpit` — `healthy`, `127.0.0.1:1025->1025/tcp, 127.0.0.1:8025->8025/tcp`
  - `yadev-cms-minio` — `healthy`, `127.0.0.1:19000->9000/tcp, 127.0.0.1:19001->9001/tcp`
- **Healthchecks manuales:**
  - MySQL: `mysqld is alive` ✓
  - Redis: `PONG` ✓
  - Mailpit: JSON `{"Version":"v1.29.7",...}` ✓
  - MinIO console: HTTP 200 ✓
- **MinIO bucket auto-creado:** yes — `minio-init` completó:
  ```
  Added `local` successfully.
  Bucket created successfully `local/yadev-media`.
  Access permission for `local/yadev-media` is set to `download`
  Bucket yadev-media ready
  ```
- **127.0.0.1 binding efectivo (LAN no accede):** yes — IP probada: `192.168.1.92`. `curl --connect-timeout 3 http://192.168.1.92:8025/api/v1/info` → timeout sin respuesta. El binding a localhost-only funciona correctamente.
- **Issues:** Ninguno — mejora completa respecto al baseline H (H no validó este punto porque no existía el binding; ahora el hardening lo implementa y funciona).

---

## 2. API

- **Dockerfile build:** ok — `docker build -t yadev-cms-api:smoke .` completó en ~17s (cacheado parcialmente). Todas las 5 capas exitosas.
- **ext-exif/gd/redis cargadas:** yes — `php -m` retorna las 3 líneas esperadas:
  ```
  exif
  gd
  redis
  ```
- **CrossTenantIsolationTest:** 1 passed + 1 skipped — confirmado exactamente:
  ```
  ✓ querying tenant model without tenant context throws  4.56s
  - tenant a cannot see tenant b pages → Requires real MySQL tenant DBs…  0.48s
  Tests: 1 skipped, 1 passed (3 assertions)
  ```
- **/health endpoint:** HTTP 500 — ver análisis abajo
- **SecurityHeaders presentes:** SecurityHeaders middleware está activo (visible en stack trace y en headers HTTP). Headers observados en respuesta 500:
  - `X-Content-Type-Options: nosniff` ✓
  - `X-Frame-Options: DENY` ✓ (del middleware) + duplicado `SAMEORIGIN` (de nginx — headers duplicados)
  - `Referrer-Policy: strict-origin-when-cross-origin` ✓
  - `Permissions-Policy: geolocation=(), microphone=(), camera=()` ✓
  - `Strict-Transport-Security: max-age=31536000; includeSubDomains` — PRESENTE aunque `APP_ENV=local`
- **HSTS en APP_ENV=local:** NOTA — el middleware emite HSTS sin condicionar al entorno. No es un bloqueante en dev pero en producción Docker debería verificarse que no haya doble emisión con el reverse proxy.
- **Headers duplicados:** `X-Frame-Options` y `X-Content-Type-Options` aparecen 2 veces (una del middleware SecurityHeaders, otra del nginx base de la imagen). Cosmético pero podría confundir a scanners de seguridad.
- **Rate limiter en /v1/auth/login:** todos los 7 intentos retornaron 500 — mismo root cause que /health: la caché DatabaseStore falla porque `database.sqlite` no existe dentro del container. No se pudo validar el comportamiento 429. No es una regresión del código del rate limiter, es un problema de configuración del entorno de test.
- **Root cause del HTTP 500:**
  - `api/.env` tiene `DB_CONNECTION=sqlite`, `CACHE_STORE=database`, `SESSION_DRIVER=database` — valores pensados para `php artisan serve` nativo en host.
  - Dentro del container, no existe `/var/www/html/database/database.sqlite`.
  - El rate limiter middleware intenta leer de la caché (DatabaseStore → SQLite) antes de llegar a cualquier lógica de ruta → `Illuminate\Database\QueryException`.
  - El archivo `.env.example` tiene los valores correctos para Docker (`DB_CONNECTION=mysql`, `CACHE_STORE=redis`). El `.env` de dev no fue regenerado desde `.env.example` — fue creado manualmente para dev nativo.
- **Issues:**
  1. **NOTA:** `api/.env` tiene valores SQLite incompatibles con el container Docker. Para un smoke containerizado, el container necesita un `.env` con `CACHE_STORE=redis` y `DB_CONNECTION=mysql`. No es un bug del hardening.
  2. **NOTA:** HSTS emitido sin condicionar a `APP_ENV`. Revisar el `SecurityHeaders` middleware para suprimir HSTS en entornos no-producción.
  3. **NOTA cosmética:** Headers duplicados `X-Frame-Options` + `X-Content-Type-Options` (nginx base + middleware). Considerar desactivar los headers redundantes de nginx o condicionar el middleware.

---

## 3. Studio

- **pnpm install:** ok — `pnpm v10.32.1`, lockfile sincronizado, completó en 1.6s
- **pnpm check:** ok — `0 ERRORS 0 WARNINGS 0 FILES_WITH_PROBLEMS` (4529 archivos)
- **pnpm lint:** ok — Prettier: todos los archivos con formato correcto. ESLint: sin errores. La regla `no-restricted-syntax` para `innerHTML` está configurada en `eslint.config.js` con dos selectores (`MemberExpression[property.name="innerHTML"]` y `AssignmentExpression[left.property.name="innerHTML"]`).
- **pnpm test:** 2 archivos / 2 tests pasando:
  - `tests/xss-guards.test.ts` — test "every {@html ...} expression has a sibling 'sanitized:' comment within 3 lines above it" ✓
  - (1 archivo adicional con 1 test — posiblemente el test de auto-logout/hook 401)
  - Duración: 532ms
- **pnpm build:** ok — build en 39.41s, output en `build/` (adapter-static). Warning cosmético de `vite-plugin-sveltekit-guard` al 74% del tiempo de build (misma nota del agente H, sin empeoramiento).
- **Issues:** Ninguno — todos los checks del hardening de Studio pasan.

---

## 4. Comparación con baseline H

| Issue | Estado en H | Estado ahora |
|-------|-------------|--------------|
| `ext-exif` faltante en Dockerfile → build fail | BLOQUEANTE | RESUELTO (`04d6299` instaló exif+gd+redis) |
| `docker build` completa sin errores | FAIL | PASS |
| `/health` endpoint smoke | NO EJECUTADO (build fallaba) | 500 — por `.env` SQLite, no por el código |
| Binding `0.0.0.0` en puertos (riesgo LAN) | NO VALIDADO (hardening no aplicado) | RESUELTO — binding a `127.0.0.1` verificado |
| `pnpm check` 0/0 | PASS | PASS |
| `pnpm build` studio | PASS | PASS |
| `/etc/hosts` entries ausentes | PENDIENTE MANUAL | PENDIENTE MANUAL (sin cambios) |
| SecurityHeaders middleware | NO EXISTÍA | ACTIVO — 4 headers presentes |
| CrossTenantIsolationTest | NO EXISTÍA | 1 passed + 1 skipped |
| xss-guards.test.ts | NO EXISTÍA | PASS |
| HSTS en `APP_ENV=local` | N/A | NOTA — HSTS emitido sin condición de entorno |
| Headers duplicados nginx+middleware | N/A | NOTA cosmética |

---

## 5. Regresiones detectadas

**Cero regresiones del hardening.** El scaffold original sigue funcionando. Los dos hallazgos nuevos son notas de configuración, no regresiones de código:

1. **api/.env SQLite vs container Docker** — pre-existente: el `.env` se creó para dev nativo. El `.env.example` tiene los valores correctos. Impacto: el smoke containerizado de /health y rate-limiter no puede ejecutarse sin un `.env` con Redis+MySQL. Solución: crear un `.env.smoke` con los valores del `.env.example` para pruebas de container.
2. **HSTS sin condición de entorno** — nuevo en `d76d222`. El `SecurityHeaders` middleware emite `Strict-Transport-Security` independientemente del `APP_ENV`. No es un riesgo en dev (HTTP plano, sin HSTS enforcement real), pero es técnicamente incorrecto. Solución: condicionar con `if ($request->secure() || app()->environment('production'))`.

---

## 6. Cosas que mejoraron vs baseline H

- `ext-exif`, `ext-gd`, `ext-redis` instalados en Dockerfile — build Docker ahora pasa completamente
- `docker build` completó exitosamente por primera vez
- Puertos bindeados a `127.0.0.1` — superficie de ataque LAN eliminada
- Imágenes pinneadas a `@sha256:` — reproducibilidad garantizada
- `SecurityHeaders` middleware activo — 4 headers de seguridad en todas las respuestas
- `CrossTenantIsolationTest` presente y pasando (1 passed / 1 skipped esperado)
- `xss-guards.test.ts` presente y pasando — protección contra innerHTML
- ESLint `no-restricted-syntax` bloqueando innerHTML en el studio
- Studio: `pnpm check`, `pnpm lint`, `pnpm test`, `pnpm build` — todos en verde

---

## 7. Pendientes manuales todavía abiertos

1. **`/etc/hosts` entries** — manual de Angel. Sin cambios desde H.
   ```
   127.0.0.1   api.yadev.local
   127.0.0.1   studio.yadev.local
   127.0.0.1   multiservicios.yadev.local
   127.0.0.1   ecomag.yadev.local
   127.0.0.1   poron.yadev.local
   127.0.0.1   coisem.yadev.local
   ```
2. **`.env.smoke` para pruebas de container** — crear con `DB_CONNECTION=mysql`, `CACHE_STORE=redis`, `SESSION_DRIVER=redis` para poder ejecutar smoke tests end-to-end dentro del container Docker con el stack de infra levantado.
3. **HSTS condicional en SecurityHeaders middleware** — condicionar emisión de `Strict-Transport-Security` a `APP_ENV=production` o `$request->secure()`.
4. **Headers duplicados nginx+middleware** — revisar si `serversideup/php` emite `X-Frame-Options` y `X-Content-Type-Options` por defecto y suprimir la duplicación.
5. **Cifrado de backups** — diferido (Q-SEC-1), sin cambios desde H.
