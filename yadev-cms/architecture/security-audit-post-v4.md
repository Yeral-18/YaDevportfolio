# Security Audit — YaDev CMS post-v4

> Auditoría ejecutada por el sub-agente `security-auditor` el 2026-04-24 tras el pivot **local-first** del Blueprint (v4).
> Fuentes revisadas: `CLAUDE.md`, `BLUEPRINT.md`, `architecture/*`, `phases/*`, `READY-FOR-REVIEW-v3.md`, `infra/docker-compose.yml`, `infra/.env.example`, `risks-and-tradeoffs.md`.
> **No se modificó ningún archivo** — este documento es el entregable.

---

## 1. Resumen ejecutivo

El threat model original (`security-model.md`) fue diseñado asumiendo producción-first con VPS, HTTPS, nginx y certbot. Tras el pivot a **local-first para Fase 0-2**, la superficie de ataque se reduce drásticamente (todo vive en `127.0.0.1`), pero varios controles del doc quedaron **descriptivos y no ejecutables** (headers Nginx, HSTS, nginx location blocks para media, fail2ban). El gap crítico no es la debilidad local sino la **ausencia de un plan de transición** que fuerce, antes de código productivo, el scaffold de las primitivas de isolation (`TenantModel` base, HTMLPurifier, validación MIME) que sí aplican en ambos entornos.

---

## 2. Threats revisitados tras el pivot local-first

Revisión de los 10 threats de `security-model.md` §1.2:

- **T1 Cross-tenant leak** — Sigue siendo CRÍTICO en ambos entornos. El pivot no cambia nada: el bug de un query mal scopado rompe isolation igual en local que en prod. Control (`TenantModel` global scope) aplica desde día 1 de Fase 1.
- **T2 Privilege escalation** — Aplicable igual. spatie/permission debe sembrarse desde Fase 1 semana 1.
- **T3 Token leak** — Superficie reducida en local (localhost), pero el patrón de cookie HttpOnly + Secure no aplica sin HTTPS. **Nuevo riesgo:** en dev, `Secure=true` en cookie impide login desde `http://studio.yadev.local`. `security-model.md` §3 no distingue esto.
- **T4 SQL injection** — Sin cambios. Eloquent mitiga nativo.
- **T5 XSS en WYSIWYG** — Sin cambios. TipTap + HTMLPurifier es el control, independiente del entorno.
- **T6 File upload abuse** — Sin cambios; el nginx location block de `security-model.md` §6.3 NO existe en local (no hay nginx). Laravel sirve media directo via `php artisan serve` → **nueva superficie:** archivos `.php` subidos pueden ejecutarse si Laravel los sirve como alias estático. Control nuevo: rechazar extensiones peligrosas a nivel de Laravel storage disk, no depender de nginx.
- **T7 Form spam** — Reducido en local (no hay public endpoint accesible desde internet). Control diferible.
- **T8 Brute force login** — Reducido en local. Rate limit igual debe programarse desde Fase 1 para que el test exista.
- **T9 MITM** — **No aplicable en local** (localhost no se intercepta). Pero cuidado: si Angel prueba desde móvil en LAN apuntando a su laptop por IP, el tráfico va plain HTTP — el doc no advierte esto.
- **T10 Backup leak** — Cambió sustancialmente. `security-model.md` §12 dice "dumps cifrados con openssl antes de subir a B2". En local-first, los backups van a `infra/backups/YYYY-MM-DD/dbs.sql.gz` **sin cifrado**. `phase-0-setup.md` día 5 confirma esto. Dado que las DBs tenant contendrán seeds reales de Multiservicios/ECOMAG (emails, teléfonos, nombres de gerentes) y la laptop puede extraviarse/ser comprometida, es un gap real.

---

## 3. Findings clasificados por severidad

### CRITICAL

- **[Multi-tenancy] `TenantModel` base no existe como código**
  `security-model.md` §4 lo describe, pero no está scaffolded. `phases/phase-1-mvp.md` día 6-7 lo menciona como bullet sin ejemplo ejecutable.
  **Recomendación:** generar el abstract class + test `CrossTenantIsolationTest` como **día 1** de Fase 1, bloqueante, no como entregable de semana 1.

- **[Backups] Dumps locales contienen PII sin cifrado en disco de dev**
  `phases/phase-0-setup.md` día 5 guarda `dbs.sql.gz` plano. Laptop puede extraviarse.
  **Recomendación:** agregar `openssl enc -aes-256-cbc -pbkdf2` al script local desde el inicio, con passphrase en `%APPDATA%\yadev\backup.key` (fuera del repo). Aplica el mismo control de §12 aunque el destino sea disco local.

### HIGH

- **[Auth/CORS] Mismatch cookie `Secure` vs HTTP plano en local**
  `security-model.md` §3 exige cookie HttpOnly + Secure + SameSite=Lax. En `http://studio.yadev.local:5173` el navegador descarta cookies Secure. No hay decisión documentada: ¿localStorage en local (peor postura) o bajar `Secure` bajo flag `APP_ENV=local`?
  **Recomendación:** documentar explícitamente en `security-model.md` §3 — `Secure=(APP_ENV !== 'local')` y aceptar el trade-off de XSS en dev.

- **[Supply chain] Imágenes Docker con tag `:latest`**
  `docker-compose.yml` usa `mysql:8.0` (ok), `redis:7-alpine` (ok), pero `mailpit:latest`, `minio:latest`, `minio/mc:latest`. Ya reconocido en I16 del v3, pero sin ticket ni owner.
  **Recomendación:** pinnear a digests SHA256 antes de Fase 1 para builds reproducibles.

- **[Media upload] No hay defensa en profundidad sin nginx**
  `security-model.md` §6 depende 100% de nginx location block. En local, Laravel sirve storage.
  **Recomendación:** en Fase 1 semana 2 (día 10 upload endpoint), agregar (a) validación magic-bytes con `finfo`, (b) rename obligatorio a hash content-addressed, (c) storage fuera de `public_path`, (d) rechazo explícito de `.php/.phtml/.phar/.htaccess/.svg-con-script`. SVG especialmente peligroso — `security-model.md` menciona DOMPurify pero DOMPurify es JS. Elegir `enshrined/svg-sanitize` en PHP.

- **[CORS] Regex `^http://[a-z0-9-]+\.yadev\.local(:\d+)?$` muy laxa**
  `security-model.md` §7 permite cualquier subdominio `.yadev.local`. Un atacante que convenza a Angel de agregar `evil.yadev.local` al hosts (social engineering) gana acceso CORS.
  **Recomendación:** whitelist explícita de los 6 subdominios del hosts (`studio`, `api`, `multiservicios`, `ecomag`, `poron`, `coisem`) en vez de regex wildcard.

### MEDIUM

- **[Secret management] Passwords literales en `.env.example` sin plan de rotación documentado**
  A3 del v3 acepta `yadev_dev_secret`. No hay doc de qué pasa si esos `.env.example` accidentalmente quedan en los repos públicos y un futuro prod-`.env` hereda el valor.
  **Recomendación:** documentar en `phase-vps-migration.md` paso explícito "regenerar TODOS los secretos con `openssl rand -base64 32`" antes de `docker compose up` en VPS, y agregar un git pre-commit hook que rechace push si `.env` real aparece.

- **[SQL / ORM] Prohibición de `Model::find()` sin scope no está enforced**
  `CLAUDE.md` §1 dice "Prohibido: `Model::find($id)` sin scope". Convención humana, no técnica.
  **Recomendación:** configurar Larastan/PHPStan custom rule que marque error en PR si un modelo que extiende `TenantModel` se usa con `Model::` (static) fuera de contexto de tenant.

- **[CSRF/Sanctum] SPA mode con dominios distintos requiere configuración específica no documentada**
  `security-model.md` §3 dice "Sanctum token-based" pero `.env.example` incluye `SANCTUM_STATEFUL_DOMAINS=studio.yadev.local:5173,api.yadev.local:8000` (modo cookie SPA, CSRF activo) y `SESSION_DOMAIN=.yadev.local`. Incoherencia: ¿es token bearer puro o SPA con cookies?
  **Recomendación:** elegir uno. Si es SPA, falta `POST /sanctum/csrf-cookie` en flujo de login descrito en `multi-tenancy-strategy.md`.

- **[Headers] HSTS listado en §10 se rompe en local**
  `Strict-Transport-Security` sin HTTPS sobre dominio `.yadev.local` rompería acceso si se entrega por error (browser pin).
  **Recomendación:** condicionar header a `APP_ENV=production` explícitamente.

- **[File permissions] Scaffold Laravel default trae `storage/` 775**
  No auditado aún porque Fase 1 no ejecutada, pero en Windows+Docker los permisos UNIX no aplican. En VPS sí.
  **Recomendación:** agregar paso en `phase-vps-migration.md` día 1 para `chown -R www-data:www-data storage bootstrap/cache && chmod -R 770`.

### LOW

- **[Runner] HMAC secret único por tenant no definido aún**
  §9 lo menciona, pero `phase-1-mvp.md` día 18 usa `config('yadev.runner_secret')` global.
  **Recomendación:** cambiar a secret per-tenant desde el scaffold inicial del runner (coste marginal, evita refactor futuro).

- **[Logging] No hay sanitización explícita de logs**
  §11 dice "NO loggear passwords, tokens". Laravel logs por default no filtran `password` ni `password_confirmation` si vienen en request body.
  **Recomendación:** configurar `config/logging.php` con `LogSanitizer` middleware desde Fase 1.

### INFO

- **[Puertos expuestos local] `docker-compose.yml` bindea a `0.0.0.0` por default**
  En una laptop conectada a WiFi pública (café, coworking), MySQL en `3307` queda accesible a la LAN.
  **Recomendación:** prefijar puertos con `127.0.0.1:` en el compose local (ej. `127.0.0.1:3307:3306`).

- **[Disclosure] `security@yadev.co` mailbox no existe**
  `security-model.md` §13 promete el canal. Aceptable diferir a post VPS-migration pero agregar TODO.

---

## 4. Gaps críticos antes de Fase 1

1. **Decidir y documentar el modo Sanctum (token bearer vs SPA con cookies).** Hoy coexisten las dos asunciones en docs distintos. Elegir uno cambia `studio/.env`, CORS config y flujo de login.
2. **Scaffold de `TenantModel` abstract + `CrossTenantIsolationTest` como commit 1 de `yadev-cms-api`.** Sin esto, cualquier endpoint de Fase 1 puede leakear. Debe existir antes del primer `php artisan make:model`.
3. **Definir librería PHP para sanitizar SVG.** DOMPurify es JS. Candidatos: `enshrined/svg-sanitize` (estándar de facto). Decidir, pinnear versión.
4. **Cifrar backups locales desde día 1.** PII de Multiservicios aparecerá en seeds reales en Fase 1 semana 4 (cutover). Activar el cifrado antes.
5. **Pinnear digests SHA256 de imágenes Docker.** Build reproducible + supply-chain defense. Trivial de hacer hoy (hash con `docker inspect`).
6. **Acordar formato de secret rotation plan.** Documento corto `infra/SECRETS.md` con tabla "secret, owner, rotation cadence, storage location".
7. **Configurar Larastan con rule que prohíbe `ModelX::query()` sin tenant context** en `yadev-cms-api`. Guardrail técnico > convención.

---

## 5. Controles que se pueden diferir

1. **Nginx hardening + HSTS/CSP production headers.** No aplican en local. Activar en `phase-vps-migration.md` día 1.5 (ya está).
2. **fail2ban + UFW.** No aplicable en laptop. Diferir a VPS.
3. **2FA (TOTP).** `T7` de `risks-and-tradeoffs.md` lo difiere a Fase 2 con mitigación aceptable.
4. **WAF / Cloudflare delante del VPS.** No aplica hasta VPS-migration. Valorar en Fase 3.
5. **Penetration testing externo.** Overkill pre-MVP. Contratar post-VPS cuando haya 3+ tenants reales.

---

## 6. Nuevas preguntas bloqueantes para Angel

1. **¿Algún cliente futuro manejará datos de salud, financieros, o niños?** Si sí, Habeas Data Ley 1581 Colombia + posiblemente HIPAA-equivalente cambian: encryption-at-rest obligatorio, DPA firmado, retención limitada. Cambia backups y logs.
2. **¿La laptop de Fase 0-2 es de uso exclusivo (FDE BitLocker activo) o compartida?** Determina si dumps locales plain son aceptables o si el finding CRITICAL de backups sube a blocker.
3. **¿Sanctum en modo token bearer (simple, localStorage) o SPA con cookies (más seguro vs XSS pero requiere CSRF + same-site cookie setup)?** Decidir HOY; impacta login flow, CORS config, studio fetch wrapper y todos los tests de auth.
