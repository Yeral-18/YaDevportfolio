# Phase 0 Validation Report

Fecha: 2026-04-24
Agente: H (devops-engineer)

## Resultado global

⚠️ PASS CON NOTAS — Infra y Studio funcionan correctamente. El Dockerfile de la API tiene un bug bloqueante que impide `docker build` pero NO bloquea el trabajo de Fase 1 (la API corre nativa via `php artisan serve`, no en Docker todavía).

---

## 1. Infra Docker Compose

- **Config válido:** yes — `docker compose config -q` sin errores
- **4 servicios levantados:**
  - `mysql` (yadev-cms-mysql) → OK — puerto `3307:3306`, status `healthy`
  - `redis` (yadev-cms-redis) → OK — puerto `6380:6379`, status `healthy`
  - `mailpit` (yadev-cms-mailpit) → OK — puertos `1025:1025` y `8025:8025`, status `healthy`
  - `minio` (yadev-cms-minio) → OK — puertos `19000:9000` y `19001:9001`, status `healthy`
- **Healthchecks:**
  - MySQL: `mysqladmin ping` → `mysqld is alive` ✓
  - Redis: `redis-cli ping` → `PONG` ✓
  - Mailpit: `curl http://127.0.0.1:8025/api/v1/info` → JSON con versión `v1.29.7` ✓
  - MinIO console: `curl http://127.0.0.1:19001` → HTTP 200 ✓
- **MinIO bucket auto-creado:** yes — `minio-init` corrió exitosamente:
  ```
  Added `local` successfully.
  Bucket created successfully `local/yadev-media`.
  Access permission for `local/yadev-media` is set to `download`
  Bucket yadev-media ready
  ```
- **Network Docker:** `yadev-cms-net` (bridge) — nombre exacto sin prefijo de carpeta porque el compose define `name: yadev-cms-net` explícitamente.
- **Conflictos de puerto:** Ninguno. Los puertos `3307`, `6380`, `1025`, `8025`, `19000`, `19001` estaban libres.
- **Issues encontrados:** Ninguno en infra.

---

## 2. API Laravel

- **vendor/ instalado:** yes — `vendor/autoload.php` existía desde el scaffold de Agente B. No fue necesario reinstalar.
- **APP_KEY generado:** yes — `api/.env` ya tenía `APP_KEY=base64:JmisFyXn1yjvqhDfchZbvAUW2HiagzbgYOu6ydhdiYY=`
- **Dockerfile build:** FAIL

  **Error exacto en línea 9 del Dockerfile:**
  ```
  #9 [4/4] RUN composer install --no-dev --optimize-autoloader --no-interaction --prefer-dist \
               && php artisan config:cache \
               && php artisan route:cache \
               && php artisan event:cache
  #9 0.492 Your lock file does not contain a compatible set of packages. Please run composer update.
  #9 0.492   Problem 1
  #9 0.492     - spatie/image 3.9.4 requires ext-exif * -> it is missing from your system.
  #9 0.492   Problem 2
  #9 0.492     - spatie/laravel-medialibrary 11.21.2 requires ext-exif * -> it is missing from your system.
  ERROR: exit code: 2
  ```

  **Causa:** La imagen base `serversideup/php:8.3-fpm-nginx` no incluye la extensión `ext-exif`. `spatie/laravel-medialibrary` y `spatie/image` la requieren, y Composer en modo `--no-dev` falla con plataforma incompatible.

  **Fix requerido (una línea en `api/Dockerfile`):** Agregar `--ignore-platform-req=ext-exif` al comando `composer install`, O instalar `exif` en la imagen antes del COPY:

  **Opción A — ignorar platform req (rápido, funcional para dev):**
  ```dockerfile
  RUN composer install --no-dev --optimize-autoloader --no-interaction --prefer-dist \
      --ignore-platform-req=ext-exif \
      && php artisan config:cache \
      && php artisan route:cache \
      && php artisan event:cache
  ```

  **Opción B — instalar la extensión (correcto para producción):**
  ```dockerfile
  RUN install-php-extensions exif \
      && composer install --no-dev --optimize-autoloader --no-interaction --prefer-dist \
      && php artisan config:cache \
      && php artisan route:cache \
      && php artisan event:cache
  ```
  La imagen `serversideup/php` incluye el helper `install-php-extensions` (mlocati/docker-php-extension-installer), por lo que la Opción B es limpia. Recomendada para producción.

- **/health endpoint (smoke):** NO EJECUTADO — el build falló, no se pudo construir la imagen para el smoke test efímero. La ruta existe en `routes/api.php` línea 11 (`Route::get('/health', fn () => ...)`).
- **Issues encontrados:**
  - `ext-exif` faltante en imagen base → Dockerfile build falla (bloqueante para Dockerfile, no bloqueante para Fase 1 que corre `php artisan serve` nativo).
  - El `api/.env` ya existe con valores de `.env.example` correctos (DB_PORT=3307, REDIS_PORT=6380, etc.) — no se necesitó copiar.

---

## 3. Studio SvelteKit

- **pnpm install:** ok — `pnpm v10.32.1`, lockfile ya sincronizado, sin descargas. `node_modules` existía. Completó en 2.1s.
- **pnpm check:** ok — `svelte-check 0 ERRORS 0 WARNINGS 0 FILES_WITH_PROBLEMS` (4527 archivos analizados)
- **pnpm build:** ok — build completó en ~25s. Generó cliente y SSR. Output en `build/` (adapter-static).
  - Client: 4628 módulos transformados
  - SSR: 4641 módulos transformados
  - Warning cosmético de performance: `vite-plugin-sveltekit-guard` consumió 78% del tiempo de build — no es un error, es un plugin de routing guard. No bloquea nada.
- **Issues encontrados:**
  - Warning de `[PLUGIN_TIMINGS]` sobre `vite-plugin-sveltekit-guard` — no es un error, solo información de profiling de Vite. Monitorear si el build se vuelve lento en Fase 1 cuando crezca el código.
  - `.env` no existía, fue creado desde `.env.example`. `VITE_API_URL` apunta a `http://api.yadev.local:8000/v1` — requiere entry en `/etc/hosts` para funcionar en `pnpm dev`.

---

## 4. /etc/hosts entries

- **Existentes:** ninguna — `grep -i "yadev.local"` no encontró resultados.
- **Pendiente manual:** yes

  Angel debe correr el paso manual documentado en `C:/Users/ASUS/APP/YaDevportfolio/yadev-cms/infra/scripts/hosts-setup.md`. Las 6 entries que necesita agregar (requiere abrir Notepad como Administrador y editar `C:\Windows\System32\drivers\etc\hosts`):

  ```
  127.0.0.1   api.yadev.local
  127.0.0.1   studio.yadev.local
  127.0.0.1   multiservicios.yadev.local
  127.0.0.1   ecomag.yadev.local
  127.0.0.1   poron.yadev.local
  127.0.0.1   coisem.yadev.local
  ```

  Después de editar: `ipconfig /flushdns` para aplicar.

---

## 5. Issues que bloquean Fase 1 día 2

### Issue #1 — BLOQUEANTE PARA DOCKERFILE (no para dev nativo)
**Descripción:** `ext-exif` ausente en imagen base `serversideup/php:8.3-fpm-nginx`. `docker build` falla en el paso `composer install`.

**Archivo:** `yadev-cms/api/Dockerfile` línea 9

**Fix sugerido:** Agregar `install-php-extensions exif` antes del `composer install`:
```dockerfile
RUN install-php-extensions exif \
    && composer install --no-dev --optimize-autoloader --no-interaction --prefer-dist \
    && php artisan config:cache \
    && php artisan route:cache \
    && php artisan event:cache
```
**Impacto en Fase 1:** Bajo — en Fase 1 días 1-5 la API corre con `php artisan serve` nativo (si PHP 8.3 está instalado en host) o dentro del container del compose. El Dockerfile solo se necesita en Fase 1 día 2 cuando se integra la API al compose. Hay tiempo para corregirlo.

### Issue #2 — PENDIENTE MANUAL (no bloquea código, bloquea URLs locales)
**Descripción:** No hay entries en `C:\Windows\System32\drivers\etc\hosts` para `*.yadev.local`. Sin ellas, `pnpm dev` carga pero las peticiones al API fallan con DNS error.

**Archivo:** `C:\Windows\System32\drivers\etc\hosts` (requiere admin)

**Fix sugerido:** Correr `infra/scripts/hosts-setup.md` manualmente. No se puede automatizar sin privilegios de administrador.

**Impacto en Fase 1:** Alto para cualquier integración frontend-backend. Sin las entries, `http://api.yadev.local:8000` no resuelve desde el browser ni desde SvelteKit SSR.

### Issue #3 — COSMÉTICO (no bloquea)
**Descripción:** `vite-plugin-sveltekit-guard` consume 78% del tiempo de build del studio.

**Impacto en Fase 1:** Ninguno actualmente. Monitorear si el build supera los 60s en Fase 1 con más rutas.

---

## 6. Cosas que salieron bien (confirmación de funcionalidad base)

- [x] `docker compose config -q` pasa sin errores — YAML válido
- [x] Los 4 servicios de infra levantan correctamente con sus healthchecks en verde
- [x] Puertos `3307`, `6380`, `1025`, `8025`, `19000`, `19001` libres — sin conflictos con `odir_mysql` ni `odir_redis`
- [x] MySQL responde `mysqld is alive` con root password
- [x] Redis responde `PONG`
- [x] Mailpit UI responde JSON válido en `/api/v1/info`
- [x] MinIO console responde HTTP 200 en puerto `19001`
- [x] MinIO bucket `yadev-media` creado automáticamente por `minio-init` con acceso público de descarga
- [x] `vendor/autoload.php` existe en `api/` — composer install ya corrió
- [x] `APP_KEY` ya configurado en `api/.env`
- [x] `api/.env` tiene DB_PORT=3307 y REDIS_PORT=6380 correctos para el stack local
- [x] `pnpm install --frozen-lockfile` completa sin descargas (lockfile sincronizado)
- [x] `pnpm check` → 0 errores, 0 warnings en 4527 archivos TypeScript/Svelte
- [x] `pnpm build` → build de producción limpio en ~25s, output en `build/`
- [x] `docker compose down` limpió todos los containers correctamente (volúmenes preservados)

---

## 7. Comandos útiles para retomar

### Levantar el stack de infra completo

```bash
# Desde Git Bash / PowerShell
cd C:/Users/ASUS/APP/YaDevportfolio/yadev-cms/infra

# Si es primera vez (ya debería existir el .env):
cp .env.example .env

docker compose up -d
docker compose ps   # verificar que los 4 servicios estén "healthy"
```

### Verificar salud de los servicios

```bash
# MySQL
docker compose exec mysql mysqladmin ping -h localhost -u root -pyadev_root_dev_secret

# Redis
docker compose exec redis redis-cli ping

# Mailpit (UI en navegador: http://localhost:8025)
curl http://127.0.0.1:8025/api/v1/info

# MinIO (consola en navegador: http://localhost:19001 — login: yadev / yadev_dev_secret)
curl -o /dev/null -w "%{http_code}" http://127.0.0.1:19001
```

### Correr la API Laravel en modo nativo (Fase 1 — requiere PHP 8.3 en host)

```bash
cd C:/Users/ASUS/APP/YaDevportfolio/yadev-cms/api
php artisan serve --host=0.0.0.0 --port=8000
# → http://127.0.0.1:8000/health debe devolver {"status":"ok",...}
```

### Correr el Studio SvelteKit en modo dev

```bash
cd C:/Users/ASUS/APP/YaDevportfolio/yadev-cms/studio
pnpm dev --host --port 5173
# → http://127.0.0.1:5173  (o http://studio.yadev.local:5173 si hosts está configurado)
```

### Fix del Dockerfile (aplicar antes de Fase 1 día 2)

Editar `C:/Users/ASUS/APP/YaDevportfolio/yadev-cms/api/Dockerfile` y reemplazar el bloque RUN:

```dockerfile
RUN install-php-extensions exif \
    && composer install --no-dev --optimize-autoloader --no-interaction --prefer-dist \
    && php artisan config:cache \
    && php artisan route:cache \
    && php artisan event:cache
```

Luego:

```bash
docker build -t yadev-cms-api:local C:/Users/ASUS/APP/YaDevportfolio/yadev-cms/api/
```

### Detener el stack (preservando datos)

```bash
cd C:/Users/ASUS/APP/YaDevportfolio/yadev-cms/infra
docker compose down    # containers down, volúmenes intactos
# NUNCA: docker compose down -v  (borra DBs y mediateca)
```

### Agregar entries a hosts (requiere admin — paso manual)

Abrir Notepad como Administrador → `C:\Windows\System32\drivers\etc\hosts` → agregar:

```
127.0.0.1   api.yadev.local
127.0.0.1   studio.yadev.local
127.0.0.1   multiservicios.yadev.local
127.0.0.1   ecomag.yadev.local
127.0.0.1   poron.yadev.local
127.0.0.1   coisem.yadev.local
```

Luego en PowerShell: `ipconfig /flushdns`

Ver guía completa en: `C:/Users/ASUS/APP/YaDevportfolio/yadev-cms/infra/scripts/hosts-setup.md`
