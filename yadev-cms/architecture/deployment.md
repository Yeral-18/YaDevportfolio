# Deployment — YaDev CMS

> Estado actual de producción. Tres servicios + cron + DB + Redis en Railway,
> tres sitios cliente en Hostinger shared, observabilidad en Sentry, backups
> en BackBlaze B2. Doc viva: cuando cambie el setup, actualizar acá primero.

## Servicios Railway

Proyecto Railway: **`yadev-cms`** (un único proyecto contiene los seis
servicios, lo que permite usar reference variables `${{Service.VAR}}`).

| Servicio | Tipo | Repo / fuente | Build | Healthcheck |
|----------|------|---------------|-------|-------------|
| `yadev-cms-api` | Web | `yadevOs/yadev-cms-api` | Dockerfile (php-fpm + nginx) | `GET /health` → 200 |
| `yadev-cms-studio` | Web | `yadevOs/yadev-cms-studio` | `pnpm build` → static SPA | `GET /` → 200 |
| `yadev-cms-runner` | Worker (web) | `yadevOs/yadev-cms-runner` | Dockerfile (Node 22) | `GET /health` → 200 |
| `MySQL` | Plugin | Railway managed | — | Railway internal |
| `Redis` | Plugin | Railway managed | — | Railway internal |
| `cms-backups` | Cron | `yadevOs/yadev-cms-infra` (root `cron-backup/`) | Dockerfile | Schedule `0 8 * * *` (UTC) |

### Domain mapping

| Dominio | Apunta a | Notas |
|---------|----------|-------|
| `yadev.co` | `yadev-cms-studio` | Landing + studio (mismo SPA) |
| `studio.yadev.co` | `yadev-cms-studio` | Alias canónico para el panel |
| `api.yadev.co` | `yadev-cms-api` | API REST `/v1/*` y `/health` |
| `luqraingenieria.com` | Hostinger shared | Sitio cliente, no Railway |
| `ecomagsas.com` | Hostinger shared | Sitio cliente |
| `multiserviciospj.com` | Hostinger shared | Sitio cliente legacy |

CORS en el API permite explícitamente `https://studio.yadev.co` y
`https://yadev.co`. Para preview/staging adicional, agregar dominios al
allowlist en `api/config/cors.php` (no usar comodín).

### DNS cliente (template Hostinger + M365)

Cuando un cliente usa Microsoft 365 para correo + Hostinger para web:

```
# Web
ALIAS  @     → dominio.com.cdn.hstgr.net
CNAME  www   → www.dominio.com.cdn.hstgr.net

# Correo (Microsoft 365)
MX     @     → dominio-com.mail.protection.outlook.com (prio 10)
TXT    @     → MS=msXXXXXXXX                                 (verificación)
TXT    @     → v=spf1 include:spf.protection.outlook.com ~all
CNAME  selector1._domainkey → selector1-…q-v1.dkim.mail.microsoft
CNAME  selector2._domainkey → selector2-…q-v1.dkim.mail.microsoft
TXT    _dmarc → v=DMARC1; p=none; rua=mailto:admin@dominio.com
```

Detalle por cliente y troubleshooting de DKIM:
[`reference_multiservicios_dns.md`](../../.claude/projects/C--Users-ASUS-APP-YaDevportfolio/memory/reference_multiservicios_dns.md)
en la memoria del proyecto.

## Variables de entorno por servicio

> Sólo lo crítico. Lista completa en `.env.example` de cada repo.

### `yadev-cms-api`

```
APP_ENV=production
APP_KEY=base64:…                        # php artisan key:generate, una vez
APP_URL=https://api.yadev.co

DB_CONNECTION=mysql
DB_HOST=${{MySQL.MYSQLHOST}}
DB_PORT=${{MySQL.MYSQLPORT}}
DB_DATABASE=${{MySQL.MYSQLDATABASE}}    # central DB; tenants se crean dinámicos
DB_USERNAME=${{MySQL.MYSQLUSER}}
DB_PASSWORD=${{MySQL.MYSQLPASSWORD}}

REDIS_HOST=${{Redis.REDISHOST}}
REDIS_PORT=${{Redis.REDISPORT}}
REDIS_PASSWORD=${{Redis.REDISPASSWORD}}

SANCTUM_STATEFUL_DOMAINS=studio.yadev.co,yadev.co
SESSION_DOMAIN=.yadev.co

# Runner contract
RUNNER_WEBHOOK_URL=http://runner.railway.internal:8080/webhook/build
RUNNER_WEBHOOK_SECRET=…                 # 32+ random bytes
RUNNER_CALLBACK_SECRET=…                # 32+ random bytes (split en prod)

# Mail (M365 outbound)
MAIL_MAILER=smtp
MAIL_HOST=smtp.office365.com
MAIL_PORT=587
MAIL_USERNAME=no-reply@yadev.co
MAIL_PASSWORD=…
MAIL_ENCRYPTION=tls
MAIL_FROM_ADDRESS=no-reply@yadev.co

# Sentry (opcional, no-op si vacío)
SENTRY_LARAVEL_DSN=https://…@o…ingest.sentry.io/…
SENTRY_TRACES_SAMPLE_RATE=0.1
SENTRY_PROFILES_SAMPLE_RATE=0.1
SENTRY_ENVIRONMENT=production

# Phase 3 AI (deshabilitado mientras esté vacío)
ANTHROPIC_API_KEY=
```

### `yadev-cms-studio`

```
PUBLIC_API_URL=https://api.yadev.co
PUBLIC_SENTRY_DSN=https://…@o…ingest.sentry.io/…
PUBLIC_SENTRY_ENV=production
SENTRY_DSN=https://…@o…ingest.sentry.io/…   # SSR/preview
SENTRY_ENV=production
```

### `yadev-cms-runner`

```
NODE_ENV=production
PORT=8080

# API contract
API_BASE_URL=https://api.yadev.co
RUNNER_WEBHOOK_SECRET=…                 # debe matchear con yadev-cms-api
RUNNER_CALLBACK_SECRET=…                # idem

# Redis (BullMQ)
REDIS_URL=redis://default:${{Redis.REDISPASSWORD}}@${{Redis.REDISHOST}}:${{Redis.REDISPORT}}

# Hostinger SSH deploy
HOSTINGER_SSH_HOST=…
HOSTINGER_SSH_USER=…
HOSTINGER_SSH_PRIVATE_KEY=…             # Railway "secret file" recomendado
HOSTINGER_SITES_ROOT=/home/uXXXXX/domains

# Railway redeploy (futuro)
RAILWAY_API_TOKEN=                      # pendiente (manual Angel)

# Sentry
SENTRY_DSN=https://…@o…ingest.sentry.io/…
SENTRY_ENV=production
```

### `cms-backups` (cron)

```
MYSQL_HOST=${{MySQL.MYSQLHOST}}
MYSQL_PORT=${{MySQL.MYSQLPORT}}
MYSQL_USER=${{MySQL.MYSQLUSER}}
MYSQL_PASSWORD=${{MySQL.MYSQLPASSWORD}}

S3_BUCKET=yadev-cms-backups
S3_ENDPOINT=https://s3.us-east-005.backblazeb2.com
S3_ACCESS_KEY=…                         # B2 keyID
S3_SECRET_KEY=…                         # B2 applicationKey (single-bucket)
S3_REGION=us-east-1                     # placeholder, B2 ignora
RETENTION_DAYS=30
```

Setup paso a paso (B2 + Railway): [`../infra/scripts/setup-backups-railway.md`](../infra/scripts/setup-backups-railway.md).

## Sentry — observabilidad

Tres proyectos en la org `yadev`:

| Proyecto | Plataforma | Filtros (`before_send`) |
|----------|-----------|------------------------|
| `yadev-cms-api` | Laravel | drop 401/403/404/422 |
| `yadev-cms-studio` | SvelteKit | drop 401/403/404/422 |
| `yadev-cms-runner` | Node | drop 401/403/404/422 |

Alertas configuradas:
- High error rate (>5/min) → email `sistemasodir@gmail.com`.
- New issue → email + (opcional) WhatsApp via webhook.
- Regression → email.

Detalle completo de creación de DSNs, sample rates y reglas de alerta:
[`../infra/MONITORING.md`](../infra/MONITORING.md).

## Smoke tests post-deploy

Correr después de cada deploy a producción (manual o vía script CI):

```bash
# 1. API alive
curl -fsSL https://api.yadev.co/health
# → {"status":"ok","service":"yadev-cms-api","time":"…"}

# 2. Security headers correctos
curl -sI https://api.yadev.co/health \
  | grep -iE 'x-content-type-options|x-frame-options|referrer-policy|permissions-policy|strict-transport-security'
# Deben aparecer los 5

# 3. Studio sirve HTML
curl -fsSL https://studio.yadev.co | grep -q '<title>'

# 4. Runner alive (sólo desde la red interna Railway,
#    o vía `railway run curl http://runner.railway.internal:8080/health`)
railway run --service yadev-cms-runner curl -fsSL http://localhost:8080/health
# → {"status":"ok"}

# 5. Auth end-to-end (genera Sanctum token efímero)
curl -fsSL -X POST https://api.yadev.co/v1/auth/login \
  -H 'Content-Type: application/json' \
  -d '{"email":"…","password":"…","device_name":"smoke"}' \
  | jq -r '.data.token' \
  | tee /tmp/token

# 6. Tenant visible para super-admin
curl -fsSL https://api.yadev.co/v1/tenants \
  -H "Authorization: Bearer $(cat /tmp/token)" \
  | jq '.data | length'   # ≥ 1

# 7. Cleanup
curl -fsSL -X POST https://api.yadev.co/v1/auth/logout \
  -H "Authorization: Bearer $(cat /tmp/token)"
```

Para Hostinger sites:

```bash
for site in luqraingenieria.com ecomagsas.com multiserviciospj.com; do
  curl -fsSL -o /dev/null -w "$site → %{http_code} %{time_total}s\n" "https://$site"
done
```

## Rollback

Railway preserva el historial de deployments por servicio. Para revertir:

1. Railway dashboard → servicio (ej. `yadev-cms-api`) → tab **Deployments**.
2. Localizar el deployment anterior conocido como bueno (verde).
3. Click en el menú `…` → **Redeploy**.
4. Esperar healthcheck verde (~60–90s para api, ~30s para studio).
5. Correr smoke test (sección anterior).

Si el rollback de api requiere también revertir migraciones de DB:

```bash
railway run --service yadev-cms-api php artisan migrate:rollback --step=N
# y para tenants:
railway run --service yadev-cms-api php artisan migrate:rollback --tenants --step=N
```

> **Nota**: rollback de migraciones es destructivo. Confirmar primero que
> el backup más reciente del cron `cms-backups` está sano (paso siguiente).

### Restore desde B2

Procedimiento completo: [`../infra/scripts/restore-prod.md`](../infra/scripts/restore-prod.md).
Resumen:

```bash
# 1. Listar snapshots
mc ls prodbackup/yadev-cms-backups/yadev-cms/backups/

# 2. Descargar snapshot del día
mc cp -r prodbackup/yadev-cms-backups/yadev-cms/backups/2026-05-05/ ./restore/

# 3. Restaurar central + tenants en MySQL Railway
gunzip -c ./restore/yadev_cms_central.sql.gz \
  | railway run --service MySQL mysql -h $MYSQLHOST -u $MYSQLUSER -p$MYSQLPASSWORD yadev_cms_central
# repetir por cada tenant_*.sql.gz
```

RTO esperado ~30 min, RPO 24 h.

## Pendientes manuales (Angel)

Estos pasos requieren credenciales o decisiones de negocio que no son
automatizables desde Claude:

1. Comprar `yadev.co` + (opcional) Hostinger KVM2 VPS si se quiere
   reemplazar Railway.
2. Provisionar `ANTHROPIC_API_KEY` + billing si se activa Phase 3 AI.
3. DNS cutover Multiservicios → Luqra (cambio de ALIAS).
4. `RAILWAY_API_TOKEN` en env del runner para auto-redeploys de sitios
   cliente en cambios de tema (opcional, post-MVP).
5. BackBlaze B2 + Railway cron `cms-backups` (guía paso a paso:
   [`../infra/scripts/setup-backups-railway.md`](../infra/scripts/setup-backups-railway.md)).
6. Sentry org + 3 DSNs (guía: [`../infra/MONITORING.md`](../infra/MONITORING.md)).

## Documentos relacionados

- [`system-diagram.md`](system-diagram.md) — topología y data flow.
- [`api-contract.md`](api-contract.md) — endpoints `/v1/*`.
- [`security-model.md`](security-model.md) — auth, CORS, headers, anti-tenant-leak.
- [`publish-flow.md`](publish-flow.md) — handshake API ↔ Runner.
- [`../infra/README.md`](../infra/README.md) — Docker Compose dev local.
- [`../infra/MONITORING.md`](../infra/MONITORING.md) — Sentry setup.
- [`../infra/scripts/setup-backups-railway.md`](../infra/scripts/setup-backups-railway.md) — B2 + cron.
- [`../infra/scripts/restore-prod.md`](../infra/scripts/restore-prod.md) — restore desde B2.
