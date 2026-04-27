# Phase 0 — Setup local-first

> Objetivo: dejar el entorno de desarrollo local de Angel listo para arrancar Fase 1 (scaffolding Laravel + SvelteKit) sin depender todavía de un VPS, sin tocar DNS públicos, sin gastar en infra.
> Duración estimada: 1 semana (5 días hábiles, ~2-3h/día).
> Resultado: `docker compose up` levanta todo el stack, `api.yadev.local:8000` y `studio.yadev.local:5173` responden, primer tenant creado vía CLI.

---

## Por qué local-first

El VPS Hostinger KVM2 y el dominio `yadev.co` **se contratan después** de que el MVP funcione end-to-end en local. Razones:

1. **Costo cero** mientras Fase 1 itera fuerte (scaffolding cambia mucho los primeros días).
2. **Iteración más rápida** sin esperar deploys, renovar certs, o propagar DNS cada cambio.
3. **Multi-tenancy testeable** con subdominios fake `{slug}.yadev.local` vía `/etc/hosts` — reproduce el comportamiento de producción sin infra real.
4. **Cuando el MVP arranca**, seguir la guía `phases/phase-vps-migration.md` para pasar a producción (estimado: 2 días una vez contratado el VPS).

---

## Requisitos previos

- [ ] **Docker Desktop** instalado y corriendo (Windows 11 con WSL2 backend).
- [ ] **Node 20+** instalado local (`node -v` → v20.x).
- [ ] **PHP 8.3** instalado local (para correr `composer` y `artisan` fuera del container cuando convenga).
- [ ] **Composer 2** (`composer -V` → 2.x).
- [ ] **pnpm 9+** (`pnpm -v` → 9.x). Si no: `npm install -g pnpm`.
- [ ] **gh CLI** (`gh --version`) autenticado (`gh auth status`).
- [ ] **Git** configurado con usuario y email.
- [ ] Los 3 repos clonados localmente en `yadev-cms/api/`, `yadev-cms/studio/`, `yadev-cms/infra/` (ya hecho).
- [ ] Acceso admin a la máquina (necesario para editar `hosts` en Windows).
- [ ] 10 GB libres en disco para volúmenes de Docker (mysql, minio, builds).

---

## Día 1 — Prerequisitos locales

### Verificar Docker Desktop

```bash
docker --version            # Docker version 27.x o superior
docker compose version      # Docker Compose version v2.29.x o superior
docker run --rm hello-world # smoke test
```

Si Docker Desktop no está instalado: https://www.docker.com/products/docker-desktop/. En Windows 11, elegir backend WSL2 (no Hyper-V legacy) al instalar.

### Verificar Node + pnpm

```bash
node -v     # v20.x
pnpm -v     # 9.x
```

Si Node no está: https://nodejs.org/ (descarga LTS 20.x).

### Verificar PHP 8.3 + Composer

```bash
php -v        # PHP 8.3.x
composer -V   # Composer 2.x
```

En Windows, la forma limpia es instalar PHP 8.3 vía https://windows.php.net/download/ (thread-safe VS16 x64) y agregar al PATH, o vía [Laragon](https://laragon.org/) que trae todo junto. Extensiones obligatorias: `mbstring`, `openssl`, `curl`, `pdo_mysql`, `zip`, `gd`, `intl`, `bcmath`, `xml`, `fileinfo`. Verificar con:

```bash
php -m | grep -E "mbstring|openssl|curl|pdo_mysql|zip|gd|intl|bcmath|xml|fileinfo"
```

Composer: `https://getcomposer.org/Composer-Setup.exe` (instalador Windows) detecta PHP del PATH automáticamente.

### Verificar gh CLI

```bash
gh --version
gh auth status    # debe decir "Logged in to github.com as <usuario>"
```

Si no está autenticado: `gh auth login --web`. Scope mínimo: `repo`, `read:org`.

### Verificar acceso a los 3 repos de la org `yadevOs`

```bash
gh repo view yadevOs/yadev-cms-api --json name,visibility,defaultBranchRef
gh repo view yadevOs/yadev-cms-studio --json name,visibility,defaultBranchRef
gh repo view yadevOs/yadev-cms-infra --json name,visibility,defaultBranchRef
```

Los 3 deben responder. Si alguno da 404 → revisar permisos en github.com/yadevOs.

---

## Día 2 — Estructura monorepo local

Los 3 repos ya están clonados como subcarpetas de este subproyecto:

```
yadev-cms/
├── BLUEPRINT.md              ← blueprint maestro
├── CLAUDE.md                 ← reglas del subproyecto
├── architecture/             ← docs de arquitectura
├── database/                 ← schemas SQL de referencia
├── phases/                   ← docs de fases (este archivo)
├── api/                      ← clone de yadevOs/yadev-cms-api (Laravel, Fase 1)
│   ├── .git/
│   └── README.md
├── studio/                   ← clone de yadevOs/yadev-cms-studio (SvelteKit, Fase 1)
│   ├── .git/
│   └── README.md
└── infra/                    ← clone de yadevOs/yadev-cms-infra (Docker, scripts)
    ├── .git/
    └── README.md
```

Cada subcarpeta es un repo git **independiente** con su propio remote a GitHub. Desde `yadev-cms/api/` puedes hacer `git status`, `git pull`, `git push` y solo afecta al repo de API.

### Trabajar con los 3 repos en paralelo

**Opción recomendada — 3 terminales abiertas simultáneamente:**

```
Terminal 1:   cd yadev-cms/api     → trabajo Laravel
Terminal 2:   cd yadev-cms/studio  → trabajo SvelteKit
Terminal 3:   cd yadev-cms/infra   → docker compose, scripts
```

**Orquestación git:** los commits van cada uno a su repo. No hay monorepo — cada PR toca un solo repo. Referencias cruzadas entre repos van por issue o PR link, no por commit compartido.

**Sincronización entre repos:**
- Cuando `yadev-cms-api` cambie un endpoint, actualizar `architecture/api-contract.md` (en `yadev-cms/` raíz, NO en el repo de API) con el nuevo contrato.
- Cuando `yadev-cms-studio` necesite un endpoint nuevo, abrir issue en `yadev-cms-api`.
- Cuando `yadev-cms-infra` cambie el docker-compose, avisar en issue cross-referenciado.

### VSCode multi-root workspace (opcional pero útil)

Crear `yadev-cms/yadev-cms.code-workspace`:

```json
{
  "folders": [
    { "name": "cms-root", "path": "." },
    { "name": "api", "path": "api" },
    { "name": "studio", "path": "studio" },
    { "name": "infra", "path": "infra" }
  ],
  "settings": {
    "files.exclude": {
      "**/.git": true,
      "**/node_modules": true,
      "**/vendor": true
    }
  }
}
```

Abrir con `code yadev-cms.code-workspace` → 4 carpetas en sidebar, buscador global, terminales separadas por folder.

---

## Día 3 — Docker Compose local-first

Todo el stack externo (MySQL, Redis, MinIO, Mailpit) vive en containers. Laravel y SvelteKit corren **fuera de Docker** en Fase 0-1 (dev server más rápido, hot-reload sin volumes).

### Archivo `infra/docker-compose.yml`

Ya escrito (ver `infra/docker-compose.yml`). Servicios incluidos:

| Servicio | Imagen | Puerto host | Propósito |
|----------|--------|-------------|-----------|
| `mysql` | mysql:8.0 | 3306 | DB central + tenant DBs |
| `redis` | redis:7-alpine | 6379 | Queues, cache, sesiones |
| `mailpit` | axllent/mailpit:latest | 1025 (SMTP), 8025 (UI) | Captura emails en dev sin mandarlos |
| `minio` | minio/minio:latest | 9000 (S3), 9001 (console) | Mediateca S3-compatible local |

Networks: `yadev-cms-net` (bridge). Volumes: `mysql-data`, `redis-data`, `minio-data` (persistentes entre `docker compose down`).

### Arrancar el stack

```bash
cd yadev-cms/infra
cp .env.example .env                  # editar si hace falta personalizar passwords
docker compose up -d                  # -d = detached (background)
docker compose ps                     # todos deben estar "healthy" en ~20 seg
docker compose logs -f mysql          # ver logs de un servicio específico
```

### Verificar conectividad

```bash
# MySQL — debe aceptar conexión con user yadev
docker compose exec mysql mysql -u yadev -pyadev_dev_secret -e "SHOW DATABASES"
# esperado: yadev_central, mysql, information_schema, performance_schema

# Redis
docker compose exec redis redis-cli PING
# esperado: PONG

# Mailpit UI
# abrir http://localhost:8025 en el navegador — debe mostrar bandeja vacía

# MinIO console
# abrir http://localhost:9001 — login: yadev / yadev_dev_secret
# crear bucket 'yadev-media' manualmente o con mc:
docker compose exec minio mc alias set local http://localhost:9000 yadev yadev_dev_secret
docker compose exec minio mc mb local/yadev-media
docker compose exec minio mc anonymous set download local/yadev-media  # público solo para download
```

### Detener / limpiar

```bash
docker compose stop                  # stop sin borrar datos
docker compose down                  # borra containers, preserva volumes
docker compose down -v               # ⚠ BORRA TODO incluyendo volumes (DBs limpias)
```

---

## Día 4 — `/etc/hosts` + estrategia de subdominios

Laravel y SvelteKit deben responder a `api.yadev.local` y `studio.yadev.local` para que el código multi-tenant funcione igual que en producción. En Fase 0-1 usamos **Opción A** (puertos diferentes, sin proxy). En Fase 2 se evalúa **Opción B** (nginx container con vhosts) si queremos reproducir CORS/SSL real antes del VPS.

### Opción A (recomendada para Fase 0-1) — puertos distintos

Laravel corre en `:8000` (artisan serve), SvelteKit en `:5173` (vite dev):

```
http://api.yadev.local:8000/health   (operational endpoint, unversioned by design)
http://studio.yadev.local:5173/
http://multiservicios.yadev.local:8000/v1/tenants/multiservicios/pages   (primer tenant)
```

**Ventajas:** cero configuración de proxy, cada app tiene sus logs separados, recarga instantánea.
**Limitaciones:** CORS en dev permite `http://studio.yadev.local:5173` (ver `architecture/security-model.md` §7). No hay SSL local — tokens van en headers sobre HTTP, aceptable en dev.

### Opción B (recomendada para Fase 2+) — nginx container con vhosts

Container `nginx-proxy` escuchando `:80` (y `:443` con mkcert), reverse-proxy a `api:8000` y `studio:5173`. Permite testear multi-tenant con hostnames reales + TLS local. Documentado en `phases/phase-vps-migration.md`.

### Agregar entries al `hosts` de Windows

Instrucciones detalladas (incluyendo cómo abrir `hosts` como admin en Windows 11): `infra/scripts/hosts-setup.md`.

Entries obligatorias para Fase 0-1:

```
127.0.0.1   api.yadev.local
127.0.0.1   studio.yadev.local
127.0.0.1   multiservicios.yadev.local
127.0.0.1   ecomag.yadev.local
127.0.0.1   poron.yadev.local
127.0.0.1   coisem.yadev.local
```

Verificar:

```bash
ping api.yadev.local         # debe responder 127.0.0.1 con "Reply from 127.0.0.1"
ping studio.yadev.local      # idem
```

Si no resuelve: cerrar todos los browsers, `ipconfig /flushdns`, abrir de nuevo.

### Levantar Laravel local (preview — Fase 1 lo scaffoldea real)

En Fase 0 no hay app Laravel todavía. Placeholder para verificar routing local:

```bash
cd yadev-cms/api
# una vez scaffold Fase 1:
php artisan serve --host=0.0.0.0 --port=8000
# luego curl http://api.yadev.local:8000/health → {"status":"ok"}
# (health is unversioned — k8s/docker/AWS healthchecks expect /health, not /v1/...)
```

### Levantar SvelteKit local (preview — Fase 1 lo scaffoldea real)

```bash
cd yadev-cms/studio
# una vez scaffold Fase 1:
pnpm dev --host --port 5173
# luego abrir http://studio.yadev.local:5173/
```

---

## Día 5 — Backups locales

En producción los backups van a BackBlaze B2 (ver `phases/phase-vps-migration.md`). En Fase 0-1 los backups van al disco local del dev — suficiente para no perder contenido si hay `down -v` accidental.

### Script `infra/scripts/backup-local.sh`

Dump de DBs central + cada tenant, tar+gzip de bucket MinIO, guardado en `infra/backups/YYYY-MM-DD/`. Pseudo-código:

```bash
#!/usr/bin/env bash
set -euo pipefail
DATE=$(date +%Y-%m-%d)
OUT=infra/backups/$DATE
mkdir -p "$OUT"

# 1. Dump DBs
docker compose exec -T mysql sh -c 'for db in $(mysql -N -e "SHOW DATABASES" | grep -E "^(yadev_central|tenant_)"); do
  mysqldump --single-transaction --routines "$db"
done' > "$OUT/dbs.sql"
gzip "$OUT/dbs.sql"

# 2. Tar mediateca MinIO
docker compose exec -T minio mc mirror local/yadev-media /tmp/mediateca
docker compose cp minio:/tmp/mediateca "$OUT/mediateca"
tar czf "$OUT/mediateca.tar.gz" -C "$OUT" mediateca && rm -rf "$OUT/mediateca"

# 3. Rotar: borrar backups > 7 días
find infra/backups -maxdepth 1 -type d -mtime +7 -exec rm -rf {} +

echo "Backup completo: $OUT"
```

### Scheduling

**Windows** — Task Scheduler GUI o PowerShell:

```powershell
$action = New-ScheduledTaskAction -Execute "bash.exe" -Argument "C:\Users\ASUS\APP\YaDevportfolio\yadev-cms\infra\scripts\backup-local.sh"
$trigger = New-ScheduledTaskTrigger -Daily -At 3am
Register-ScheduledTask -TaskName "YadevCmsBackupLocal" -Action $action -Trigger $trigger
```

**Retención:** 7 días en local (disco pequeño, no necesitamos más). Cuando migremos a VPS → retención 30 días en B2 (ver phase-vps-migration.md).

**Restore manual:**

```bash
gunzip -c infra/backups/2026-04-25/dbs.sql.gz | docker compose exec -T mysql mysql -u yadev -pyadev_dev_secret
```

Probar restore al menos una vez en Fase 0 para validar que el flujo funciona antes de Fase 1.

---

## CI/CD skeleton (3 repos, no deploy aún)

La arquitectura de repos es multi-repo (ver `BLUEPRINT.md` §2.2). Cada repo tiene su propio workflow de GitHub Actions. **En Fase 0 los workflows solo corren tests + lint, NO deployan a ningún servidor** — porque no hay servidor. Los pipelines de deploy llegan en `phases/phase-vps-migration.md`.

### `yadevOs/yadev-cms-api` → `.github/workflows/ci.yml`

```yaml
name: CI API
on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]
jobs:
  test:
    runs-on: ubuntu-latest
    services:
      mysql:
        image: mysql:8.0
        env:
          MYSQL_ROOT_PASSWORD: root
          MYSQL_DATABASE: yadev_central
        ports: ['3306:3306']
        options: --health-cmd="mysqladmin ping" --health-interval=10s --health-timeout=5s --health-retries=5
      redis:
        image: redis:7-alpine
        ports: ['6379:6379']
    steps:
      - uses: actions/checkout@v4
      - uses: shivammathur/setup-php@v2
        with:
          php-version: '8.3'
          extensions: mbstring, pdo_mysql, redis, bcmath, intl
      - run: composer install --prefer-dist --no-interaction
      - run: cp .env.example .env && php artisan key:generate
      - run: php artisan test --parallel
      - run: vendor/bin/pint --test
```

### `yadevOs/yadev-cms-studio` → `.github/workflows/ci.yml`

```yaml
name: CI Studio
on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v3
        with: { version: 9 }
      - uses: actions/setup-node@v4
        with: { node-version: 20, cache: 'pnpm' }
      - run: pnpm install --frozen-lockfile
      - run: pnpm lint
      - run: pnpm check                 # svelte-check
      - run: pnpm test                  # vitest
      - run: pnpm build                 # sanity-check del build
```

### `yadevOs/yadev-cms-infra` → `.github/workflows/ci.yml`

```yaml
name: CI Infra
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Validate docker-compose
        run: docker compose -f docker-compose.yml config > /dev/null
      - name: Lint bash scripts
        run: |
          sudo apt-get install -y shellcheck
          find scripts -name '*.sh' -exec shellcheck {} +
      - name: Smoke test local stack
        run: |
          cp .env.example .env
          docker compose up -d
          sleep 20
          docker compose ps
          docker compose exec -T mysql mysqladmin ping -h localhost -u yadev -pyadev_dev_secret
          docker compose down -v
```

### Secrets en Fase 0

Ninguno por ahora. Cuando lleguemos a Fase VPS migration agregamos `SSH_PRIVATE_KEY`, `VPS_HOST`, `B2_KEY_ID`, etc. — documentado en `phases/phase-vps-migration.md`.

---

## Checklist final Fase 0

### Entorno local
- [ ] Docker Desktop instalado y corriendo (`docker ps` responde).
- [ ] Node 20+ + pnpm 9+ verificados.
- [ ] PHP 8.3 + Composer 2 verificados con extensiones requeridas.
- [ ] gh CLI autenticado con scopes `repo`, `read:org`.

### Repos clonados y operables
- [ ] `yadev-cms/api/` es clone de `yadevOs/yadev-cms-api`, `git remote -v` correcto.
- [ ] `yadev-cms/studio/` es clone de `yadevOs/yadev-cms-studio`, remote correcto.
- [ ] `yadev-cms/infra/` es clone de `yadevOs/yadev-cms-infra`, remote correcto.
- [ ] Los 3 READMEs de cada repo escritos con descripción, stack, setup (ver paso 9 del project-orchestrator).

### Docker stack
- [ ] `infra/docker-compose.yml` pasa `docker compose config` sin errores.
- [ ] `docker compose up -d` levanta los 4 servicios con status `healthy`.
- [ ] MySQL accesible con user `yadev`, DB `yadev_central` existe.
- [ ] Redis responde `PONG`.
- [ ] Mailpit UI abre en `http://localhost:8025`.
- [ ] MinIO console abre en `http://localhost:9001`, bucket `yadev-media` creado.

### Subdominios locales
- [ ] `hosts` de Windows tiene las 6 entries (`api`, `studio`, `multiservicios`, `ecomag`, `poron`, `coisem` en `.yadev.local`).
- [ ] `ping api.yadev.local` responde 127.0.0.1.
- [ ] `ping studio.yadev.local` responde 127.0.0.1.

### Backups
- [ ] Script `infra/scripts/backup-local.sh` ejecuta sin error y genera `infra/backups/YYYY-MM-DD/dbs.sql.gz`.
- [ ] Task Scheduler (o cron equivalente) tiene el job registrado para 3am diario.
- [ ] Test de restore manual ejecutado exitosamente al menos una vez.

### CI/CD skeleton
- [ ] `yadevOs/yadev-cms-api` tiene `.github/workflows/ci.yml` con tests PHP corriendo.
- [ ] `yadevOs/yadev-cms-studio` tiene `.github/workflows/ci.yml` con lint + build corriendo.
- [ ] `yadevOs/yadev-cms-infra` tiene `.github/workflows/ci.yml` con docker-compose validate.
- [ ] Los 3 workflows verde al menos una vez.

### Documentación
- [ ] `READY-FOR-REVIEW-v3.md` creado y revisado por Angel.
- [ ] Inconsistencias documentadas en sección I.

**Al marcar los 20 items, Fase 0 cerrada. Próximo paso: `phases/phase-1-mvp.md` — scaffold real de Laravel + SvelteKit dentro de los repos clonados.**
