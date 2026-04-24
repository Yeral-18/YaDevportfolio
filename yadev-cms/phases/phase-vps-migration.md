# Phase VPS-migration — De local-first a producción real

> Fase intermedia opcional entre Fase 2 y el go-live real con clientes.
> Se ejecuta **solo cuando el MVP funciona end-to-end en local** (docker compose + `.yadev.local` + primer tenant completo) y Yeral contrata el VPS.
> Duración estimada: **2 días** una vez VPS + dominio adquiridos.

---

## Cuándo se ejecuta esta fase

No tiene fecha fija en el timeline del BLUEPRINT. Se ejecuta cuando se cumplen estos 3 criterios:

1. **Fase 1 cerrada** — Multiservicios editable end-to-end desde el panel local (`multiservicios.yadev.local` responde, publicación genera dist/ local, rsync diferido).
2. **Fase 2 al menos al 60%** — bloques avanzados, forms, SEO básico, mediateca estable.
3. **Yeral confirma** que el producto está listo para poner en vivo frente a Multiservicios (primer cliente beta).

Antes de eso: **no migrar**. El costo de mantener local + iterar es cero; el costo de mantener un VPS que se itera es tiempo de ops que se resta de features.

---

## Pre-requisitos

- [ ] **Dominio `yadev.co`** comprado y con DNS bajo control. Opciones:
  - **Hostinger** — conveniente si ya se tiene cuenta (~$10/año para `.co`).
  - **Namecheap** — más barato, DNS API disponible.
  - **Cloudflare registrar** — CDN incluida, renovación at-cost.
  - **Recomendación:** Hostinger (todo bajo un login).
- [ ] **VPS Hostinger KVM 2** contratado.
  - 2 vCPU, 8 GB RAM, 100 GB NVMe, 8 TB transfer.
  - Ubuntu 24.04 LTS (no 22.04).
  - IP pública fija.
  - URL compra: `https://www.hostinger.com/vps-hosting` (plan KVM 2).
  - Costo: ~$8 USD/mes anual.
- [ ] **Cuenta BackBlaze B2** creada + API key generada. Bucket `yadev-backups` creado (privado).
- [ ] **Acceso SSH** al VPS verificado con llave pública (no password).

---

## Día 1 — Setup VPS + migración infra

### 1.1. Provisionar el VPS (1h)

```bash
# Al crear, Hostinger manda root + password por email
ssh root@<ip_vps>

# Crear usuario no-root
adduser yadev
usermod -aG sudo yadev
mkdir -p /home/yadev/.ssh
echo "<pubkey_yeral>" > /home/yadev/.ssh/authorized_keys
chown -R yadev:yadev /home/yadev/.ssh
chmod 700 /home/yadev/.ssh && chmod 600 /home/yadev/.ssh/authorized_keys

# Deshabilitar login root + password-auth
sudo vim /etc/ssh/sshd_config
# PermitRootLogin no
# PasswordAuthentication no
sudo systemctl restart ssh
```

### 1.2. Hardening (30min)

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y ufw fail2ban unattended-upgrades
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 22/tcp 80/tcp 443/tcp
sudo ufw enable
sudo systemctl enable fail2ban
sudo dpkg-reconfigure --priority=low unattended-upgrades
```

### 1.3. Stack base (1h)

Usar el mismo enfoque que local-first pero en el VPS: **el stack externo corre en Docker también**. Copiar `infra/docker-compose.yml` al VPS y adaptar:

- Passwords de producción (no los `_dev_secret`).
- Puertos bind a `127.0.0.1:` (no expuestos al internet).
- MinIO opcional — si migramos a B2 desde día 1, MinIO solo queda como cache local, no como storage primario.

```bash
# En el VPS
git clone git@github.com:yadevOs/yadev-cms-infra.git /srv/yadev-cms/infra
cd /srv/yadev-cms/infra
cp .env.production.example .env                  # passwords de producción generados con openssl rand
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

Laravel y SvelteKit en el VPS sí corren nativos (no Docker) para aprovechar FPM + PM2:

```bash
sudo apt install -y php8.3 php8.3-fpm php8.3-cli php8.3-mysql php8.3-redis \
  php8.3-mbstring php8.3-xml php8.3-curl php8.3-zip php8.3-gd php8.3-intl \
  php8.3-bcmath php8.3-imagick composer
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo bash -
sudo apt install -y nodejs nginx
sudo npm install -g pnpm pm2
```

### 1.4. DNS (esperar propagación 15min-2h)

En el panel DNS del registrador de `yadev.co`:

```
A     yadev.co            → <ip_vps>
A     api.yadev.co        → <ip_vps>
A     studio.yadev.co     → <ip_vps>
```

TTL 300 durante migración, subir a 3600 después. **No tocar el DNS de los dominios cliente** (`ecomagsas.com`, `multiserviciospj.com`, etc.) — ya están en Hostinger shared, ahí siguen.

Verificar:

```bash
dig +short A api.yadev.co        # debe devolver <ip_vps>
dig +short A studio.yadev.co     # idem
```

### 1.5. Nginx + Let's Encrypt (30min)

Ver `yadev-cms-infra/nginx/vhosts/` para los archivos de configuración completos. Resumen:

```bash
sudo apt install -y certbot python3-certbot-nginx
# Copiar vhosts de api.yadev.co y studio.yadev.co
sudo cp /srv/yadev-cms/infra/nginx/vhosts/*.conf /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/api.yadev.co.conf /etc/nginx/sites-enabled/
sudo ln -s /etc/nginx/sites-available/studio.yadev.co.conf /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx

# Emitir certs
sudo certbot --nginx -d api.yadev.co -d studio.yadev.co \
  --email yadevsistem@gmail.com --agree-tos --redirect --non-interactive

sudo certbot renew --dry-run
```

### 1.6. Clonar repos + deploy inicial

```bash
# API
cd /srv/yadev-cms
git clone git@github.com:yadevOs/yadev-cms-api.git api
cd api && composer install --no-dev --optimize-autoloader
cp .env.example .env && vim .env                   # apuntar a containers locales
php artisan key:generate
php artisan migrate --force

# Studio
cd /srv/yadev-cms
git clone git@github.com:yadevOs/yadev-cms-studio.git studio
cd studio && pnpm install --frozen-lockfile && pnpm build
```

---

## Día 2 — Migrar storage y backups a B2

### 2.1. Migrar MinIO local → BackBlaze B2

Todo el contenido que subieron a MinIO en dev local **no** migra a producción (son datos de prueba). En producción arrancamos con bucket B2 limpio y los clientes re-suben su media real.

Configurar Laravel para usar B2 directamente (B2 es S3-compatible):

```php
// config/filesystems.php
'disks' => [
    'media' => [
        'driver' => 's3',
        'key' => env('B2_KEY_ID'),
        'secret' => env('B2_APP_KEY'),
        'region' => env('B2_REGION'),           // us-west-002
        'bucket' => env('B2_BUCKET'),           // yadev-media-prod
        'endpoint' => env('B2_ENDPOINT'),       // https://s3.us-west-002.backblazeb2.com
        'use_path_style_endpoint' => true,
    ],
],
```

Si hay media de dev que sí hay que migrar (caso edge — demo con Multiservicios ya poblada):

```bash
# En local
docker compose exec minio mc alias set b2-prod https://s3.us-west-002.backblazeb2.com $B2_KEY_ID $B2_APP_KEY
docker compose exec minio mc mirror local/yadev-media b2-prod/yadev-media-prod
```

### 2.2. Migrar backups locales → B2 con retención 30 días

Script `infra/scripts/backup-b2.sh` reemplaza a `backup-local.sh` en el VPS:

```bash
#!/usr/bin/env bash
set -euo pipefail
source /etc/yadev/secrets.env
DATE=$(date +%Y-%m-%d)
TMPOUT=/tmp/yadev-backup-$DATE
mkdir -p "$TMPOUT"

# 1. Dump DBs (central + cada tenant)
docker compose exec -T mysql sh -c 'for db in $(mysql -N -e "SHOW DATABASES" | grep -E "^(yadev_central|tenant_)"); do
  mysqldump --single-transaction --routines "$db"
done' > "$TMPOUT/dbs.sql"
gzip "$TMPOUT/dbs.sql"

# 2. Cifrar antes de subir
tar czf - -C /tmp yadev-backup-$DATE | \
  openssl enc -aes-256-cbc -pbkdf2 -salt -out "$TMPOUT.tar.gz.enc" \
  -pass file:/etc/yadev/backup-enc-key

# 3. Subir a B2
b2 authorize-account "$B2_KEY_ID" "$B2_APP_KEY"
b2 upload-file "$B2_BUCKET" "$TMPOUT.tar.gz.enc" "backups/daily/$DATE.tar.gz.enc"

# 4. Primer del mes → guardar también en backups/monthly/ (retención 12 meses)
if [ "$(date +%d)" = "01" ]; then
  b2 copy-file-by-id "$B2_BUCKET" "backups/daily/$DATE.tar.gz.enc" "backups/monthly/$DATE.tar.gz.enc"
fi

# 5. Rotar: borrar daily > 30 días y monthly > 12 meses (via B2 lifecycle rules, no en el script)
rm -rf "$TMPOUT" "$TMPOUT.tar.gz.enc"
echo "Backup $DATE subido a B2"
```

Configurar **lifecycle rules en B2 (vía consola web)**:
- `backups/daily/*` → borrar después de 30 días.
- `backups/monthly/*` → borrar después de 365 días.

Costo estimado: para 20 tenants (~20GB rolling + picos), ~$1-2 USD/mes en B2. Mucho más barato que S3 ($5/mes por TB).

### 2.3. CI/CD deploy activado

Agregar a cada workflow de los 3 repos un job `deploy` que solo corre en `push` a `main` y usa SSH al VPS. Ver ejemplo completo en `yadev-cms-infra/ci-templates/deploy-api.yml`.

Secrets nuevos a agregar en cada repo de la org `yadevOs`:
- `SSH_PRIVATE_KEY` — llave deploy del user `yadev@vps`.
- `VPS_HOST` — `api.yadev.co` (o IP).
- `VPS_USER` — `yadev`.

### 2.4. Health + monitoring

```bash
# UptimeRobot (free tier) monitorea:
#   https://api.yadev.co/v1/health
#   https://studio.yadev.co/
# Alerta email + SMS si 2 fails consecutivos en 5min.

# Horizon dashboard en /horizon (gated por super-admin)
# Laravel Telescope opcional (más pesado, solo en pre-prod)
```

---

## Cambios operacionales post-migración

Una vez cerrada esta fase:

| Cosa | Antes (local) | Después (VPS) |
|------|---------------|---------------|
| Dominios | `.yadev.local` via hosts | `.yadev.co` via DNS |
| SSL | HTTP plano en dev | HTTPS Let's Encrypt auto-renew |
| DB | MySQL container local | MySQL container en VPS (misma imagen) |
| Redis | Container local | Container en VPS |
| Mediateca | MinIO local | BackBlaze B2 directo |
| Email transaccional | Mailpit (captura) | Resend o Amazon SES (production IPs) |
| Backups | Disco local, 7 días | B2 con retención 30 días diario + 12 meses mensual |
| Deploy | `git pull` manual | GitHub Actions auto-deploy on push to main |
| Monitoring | Logs de docker compose | UptimeRobot + Horizon + Nginx access logs |

---

## Checklist final Fase VPS-migration

- [ ] VPS contratado y accesible via SSH con llave (no password).
- [ ] UFW + fail2ban + unattended-upgrades activos.
- [ ] DNS `yadev.co`, `api.yadev.co`, `studio.yadev.co` propagados.
- [ ] Docker compose prod corriendo (mysql + redis + optional minio-cache).
- [ ] Laravel desplegado en `/srv/yadev-cms/api` con `.env` de producción.
- [ ] SvelteKit build desplegado en `/srv/yadev-cms/studio/build`.
- [ ] Nginx vhosts para `api.yadev.co` y `studio.yadev.co` activos.
- [ ] SSL Let's Encrypt emitido, `certbot renew --dry-run` pasa.
- [ ] BackBlaze B2 bucket `yadev-media-prod` + `yadev-backups-prod` creados.
- [ ] Mediateca Laravel apunta a B2 (no MinIO).
- [ ] `backup-b2.sh` ejecutado manualmente al menos una vez, backup visible en B2.
- [ ] Lifecycle rules B2 configuradas (30d daily + 365d monthly).
- [ ] GitHub Actions `deploy` workflows configurados con secrets correctos en los 3 repos.
- [ ] UptimeRobot monitoreando ambos subdominios.
- [ ] `curl https://api.yadev.co/v1/health` devuelve 200 + JSON healthy.
- [ ] Test de restore desde B2: descargar último backup, descifrar, importar a DB staging, verificar datos.

**Al marcar los 15 items: producción lista. Primer tenant real (Multiservicios) se conecta. Cliente ve cambios live en su `multiserviciospj.com` con el nuevo flujo.**
