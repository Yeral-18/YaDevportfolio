# READY FOR REVIEW v3 — YaDev CMS Blueprint (local-first pivot)

> Continuación del v2 tras la sesión 2026-04-22 donde Angel confirmó que arrancar local-first (sin VPS) y que la org GitHub ya existe como `yadevOs/` (no `yadev/`).
> Documenta la reescritura estructural que convierte Fase 0 en "setup del entorno local" en vez de "provisioning de VPS".
> Fecha: 2026-04-24.

---

## 1. Qué cambió vs v2

v2 dejó 5 preguntas abiertas (Q1-Q5) que bloqueaban el arranque. En esta sesión Angel respondió las 5, y las respuestas implicaron un **pivot estructural**: en lugar de contratar VPS + dominio + registrar org en Fase 0, arrancamos local-first. Esto significó:

- Reescribir completamente `phases/phase-0-setup.md` (~520 líneas → ~330 líneas, estructura distinta).
- Crear `phases/phase-vps-migration.md` como nueva fase intermedia opcional.
- Actualizar todas las referencias `yadev/` → `yadevOs/` en el blueprint.
- Mencionar arquitectura dual (local-first vs producción) en BLUEPRINT, CLAUDE, system-diagram, security-model.
- Crear infraestructura real ejecutable: `infra/docker-compose.yml`, `infra/.env.example`, `infra/scripts/hosts-setup.md`.
- Reescribir los 3 READMEs default de los repos clonados con contenido real.

---

## 2. Decisiones Q1-Q5 — todas RESUELTAS

### Q1 — Registro del dominio `yadev.co`
**Respuesta:** NO registrado todavía. Arrancar local-first con `.yadev.local` via `/etc/hosts`. Se compra en Fase VPS-migration.

**Traducción técnica:**
- `BLUEPRINT.md` §2: callout agregado "Fase 0-2 local-first con `.yadev.local`, producción post Fase VPS-migration con `.yadev.co`".
- `CLAUDE.md` sección "Arquitectura de dominios" ahora tiene dos bloques explícitos (local-first vs prod).
- `phases/phase-0-setup.md` reescrito: día 4 dedicado a `/etc/hosts` + estrategia de subdominios (Opción A puertos distintos, Opción B nginx proxy).
- `infra/scripts/hosts-setup.md` creado con 3 métodos para Windows 11 (Notepad admin, PowerShell script, VSCode admin).
- `architecture/security-model.md` §7 CORS: agrega bloque permitiendo `http://*.yadev.local:*` en `APP_ENV=local`.
- `architecture/system-diagram.md`: nueva sección "Variante local-first" con diagrama ASCII.

### Q2 — VPS Hostinger KVM 2
**Respuesta:** NO contratado. Se contrata en Fase VPS-migration después del MVP local funcional.

**Traducción técnica:**
- Sección "Fase 0 — Setup infraestructura" en `BLUEPRINT.md` §4 renombrada a "Fase 0 — Setup local-first" con nuevo bullet list.
- Nueva sección "Fase VPS-migration" agregada entre Fase 2 y Fase 3 con estimación 2 días.
- `phases/phase-vps-migration.md` creado: contratación VPS, hardening, Docker prod, Nginx real, certbot, migración MinIO→B2, activación de pipelines de deploy.
- `phases/phase-0-setup.md`: eliminadas las secciones "Contratar VPS", "Acceso SSH inicial", "Hardening básico", "Certbot", "UFW" (movidas a phase-vps-migration).

### Q3 — Org GitHub
**Respuesta:** YA CREADA como `yadevOs/` (capitalización exacta). Los 3 repos YA EXISTEN y están clonados en `yadev-cms/{api,studio,infra}/`.

**Traducción técnica:**
- Find + replace `yadev/yadev-cms-*` → `yadevOs/yadev-cms-*` en:
  - `BLUEPRINT.md` §2.2 (tabla de repos) y §7 (supuestos).
  - `CLAUDE.md` subproyecto sección "Repositorios GitHub".
  - `phases/phase-1-mvp.md` día 1-2 (ahora apunta a repos ya clonados, no dice "crear repo").
  - `architecture/multi-tenancy-strategy.md` línea 123 (clone del site-multiservicios).
- No se tocó `READY-FOR-REVIEW-v2.md` ni `READY-FOR-REVIEW.md` (histórico preservado).
- Los 3 READMEs de `api/`, `studio/`, `infra/` reescritos desde cero con descripción + stack + setup + links al blueprint.

### Q4 — Backups
**Respuesta:** DBs + mediateca. En local-first: disco `infra/backups/`, retención 7 días. En producción: BackBlaze B2, retención 30 días daily + 12 meses monthly.

**Traducción técnica:**
- `phases/phase-0-setup.md` día 5: script `infra/scripts/backup-local.sh` (pseudo-código) + Windows Task Scheduler para 3am diario.
- `phases/phase-vps-migration.md` día 2: script `infra/scripts/backup-b2.sh` con cifrado openssl + subida a B2 + lifecycle rules.
- `infra/README.md` sección Backups explica ambos modos.
- Costo estimado B2: ~$1-2/mes para 20 tenants (vs $5/mes S3).

### Q5 — Flujo de publicación
**Respuesta:** Sitios cliente viven en su propio Hostinger shared con su propio dominio. CMS → webhook → Node runner hace build Astro local (clone del repo `yadevOs/site-{cliente}`) → rsync/FTP al `public_html/` del cliente. El cliente nunca pierde su dominio/SEO/hosting.

**Traducción técnica:**
- Confirmado en `BLUEPRINT.md` §2 (ya estaba pero ahora explícito en callout local-first).
- `architecture/system-diagram.md`: variante local menciona que rsync se hace diferido desde laptop en Fase 0-1, movido al VPS en Fase VPS-migration.
- `api/README.md` y `infra/README.md` mencionan el flujo webhook → runner → rsync como responsabilidad shared entre api + infra.

---

## 3. Archivos creados y editados en esta ronda

### Creados (7)

```
yadev-cms/
├── READY-FOR-REVIEW-v3.md                 ← este archivo
├── phases/
│   └── phase-vps-migration.md             ← nueva fase intermedia post-MVP
└── infra/
    ├── docker-compose.yml                 ← stack local funcional (mysql, redis, mailpit, minio)
    ├── .env.example                       ← variables para infra + plantillas para api/studio
    └── scripts/
        └── hosts-setup.md                 ← guía Windows 11 para /etc/hosts

(READMEs reescritos desde cero — contaban como "default de GitHub", ahora son reales)
yadev-cms/api/README.md                    ← sobreescrito (era 1 línea)
yadev-cms/studio/README.md                 ← sobreescrito
yadev-cms/infra/README.md                  ← sobreescrito
```

### Editados (6)

```
yadev-cms/
├── BLUEPRINT.md                           ← §2 callout local-first, §2.2 tabla yadevOs/, §4 Fase 0 reescrita + Fase VPS-migration agregada, §7 supuestos
├── CLAUDE.md                              ← sección "Arquitectura de dominios" expandida con 2 bloques (local vs prod), "Repositorios GitHub" con yadevOs/, "Stack técnico" con MinIO + Mailpit
├── architecture/
│   ├── system-diagram.md                  ← nueva sección "Variante local-first" con diagrama ASCII + separador hacia variante producción
│   └── security-model.md                  ← §7 CORS con bloque dev permitiendo *.yadev.local
├── phases/
│   ├── phase-0-setup.md                   ← reescritura completa (20 items checklist final, no más VPS)
│   └── phase-1-mvp.md                     ← día 1-2 ahora apunta a repos clonados (yadevOs/), central_domains incluye .yadev.local
└── (multi-tenancy-strategy.md)            ← referencia `yadev/site-multiservicios` → `yadevOs/site-multiservicios`
```

**Total: 13 archivos tocados.** 7 nuevos, 6 editados. Ningún código de aplicación escrito (sigue siendo blueprint/infra, no hay Laravel ni SvelteKit todavía). Ningún proyecto de producción modificado (`internal/`, `index.html`, `proyectos/`, `Modelos/`, `design-system/`, `assets/` intactos).

---

## 4. Asunciones hechas durante la reescritura

Angel dio instrucciones claras en las 5 Q. Las siguientes asunciones se tomaron para rellenar detalles no explícitos:

### A1. Puertos en Fase 0-1
Asumí **Opción A** (`api:8000`, `studio:5173` en puertos distintos) como default para Fase 0-1 porque elimina el container `nginx-proxy` y acelera la iteración. Opción B (nginx con vhosts locales para reproducir CORS/SSL real) queda documentada como opcional para Fase 2+ si Angel quiere probar el comportamiento de producción antes de migrar al VPS. **Revisar:** ¿ok con Opción A para Fase 0-1?

### A2. Retención de backups locales = 7 días
Angel dijo "retención 30 días rolling" en el contexto de producción con B2. Para local asumí **7 días** porque (a) el disco del dev es limitado, (b) los datos de dev son menos críticos, (c) el backup real de la intención de publicar ya está en el repo GitHub del sitio. **Revisar:** ¿subir local a 14 días? ¿30 días?

### A3. Variables de entorno no sensibles en `.env.example`
Usé passwords literales `yadev_dev_secret`, `yadev_root_dev_secret` en `.env.example` (no en `.env` real). Son strings triviales, pero cualquiera con acceso a leer el archivo sabe cómo entrar al MySQL local. En local-first esto es aceptable (127.0.0.1 bound, no internet). **Revisar:** si Angel prefiere placeholders `CHANGE_ME_*` en el example para forzar edición consciente al copiar a `.env`, reemplazo.

### A4. MinIO se crea bucket `yadev-media` automáticamente
Agregué el servicio `minio-init` (one-shot container `minio/mc`) que bootstrap-ea el bucket `yadev-media` en cada arranque. Alternativa: dejarlo manual y documentar en README el comando. Elegí automático porque reduce fricción en onboarding. **Revisar:** ¿queda así?

### A5. El `docker-compose.yml` expone puertos al host
`3306`, `6379`, `1025`, `8025`, `9000`, `9001` se bindean al host para que Laravel/SvelteKit corriendo nativos puedan conectarse. En producción se cambian a `127.0.0.1:PORT` para que no sean accesibles desde internet — esto va en `docker-compose.prod.yml` (override documentado pero no escrito en esta ronda, llega en Fase VPS-migration).

### A6. No scaffoldee Laravel ni SvelteKit
Angel pidió explícitamente "NO instalar Laravel ni SvelteKit todavía". Los READMEs documentan los pasos de scaffold pero no los ejecuté. Los repos siguen con solo `.git/` + `README.md`.

### A7. No toqué `competitive-analysis-damos.md` ni otros docs estables
Solo toqué archivos que cambian por el pivot local-first o por el rename `yadev/` → `yadevOs/`. `competitive-analysis-damos.md`, `risks-and-tradeoffs.md`, `multiservicios-migration-plan.md`, `database/*.sql`, `architecture/api-contract.md` no se tocaron. Pueden necesitar revisión puntual de referencias futuras pero no bloquean Fase 0.

### A8. Task Scheduler en Windows (vs cron nativo)
Para el backup local diario, recomendé Windows Task Scheduler porque la laptop de Angel es Windows 11. Si corre WSL2 con cron nativo, el backup-local.sh puede instalarse como `crontab -e` dentro de WSL. Documenté ambos enfoques en el README pero el ejemplo principal es Task Scheduler.

---

## 5. Inconsistencias detectadas

### I12. `READY-FOR-REVIEW-v2.md` sigue diciendo `yadev/` (intencional)
v2 se conserva como histórico. Todas las nuevas refs usan `yadevOs/`. Igual patrón que v1 preservó `admin.yadev.co` original.

### I13. `agents-orchestration.md` no se editó
Las referencias a agentes (`project-orchestrator`, `devops-engineer`, etc.) son correctas y no dependen del nombre de la org GitHub. Sin cambios.

### I14. `api-contract.md` tiene ejemplos con `https://api.yadev.co/v1/`
Correcto para producción, pero en Fase 0-2 la base URL local es `http://api.yadev.local:8000/v1/`. No se editó porque el contrato describe **producción**; los wrappers tipados en SvelteKit deben usar `VITE_API_URL` (variable de entorno) — documentado en `studio/README.md`. Detalle de implementación, no cambio de contrato.

### I15. `tenants:create` espera un `--domain` que en local será `.yadev.local`
Ejemplo del README: `php artisan tenants:create multiservicios --domain=multiservicios.yadev.local`. En producción será `multiservicios.yadev.co`. El CLI debe aceptar ambos. Si se usa stancl/tenancy domain resolution, hay que mantener los dos dominios en `yadev_central.domains` para el mismo tenant durante la Fase VPS-migration (dev seguirá usando `.yadev.local` aunque prod ya tenga `.yadev.co`). Detalle menor, resolver en Fase 1.

### I16. `docker-compose.yml` usa imagen `minio/minio:latest`
`latest` tag es anti-pattern para producción. En Fase VPS-migration se pinnea a tag inmutable (ej. `minio/minio:RELEASE.2026-01-15T12-00-00Z`) o a Bitnami. Para dev local no bloquea, pero deja en `docker-compose.prod.yml` override.

### I17. Falta bandera para diferenciar dev vs prod en el compose
Cuando se cree `docker-compose.prod.yml` (Fase VPS-migration), hay que bindear puertos a `127.0.0.1` y usar passwords fuertes. El compose actual es 100% dev. Decisión: **no premature**. El prod compose se diseña cuando VPS exista.

---

## 6. "Ready to start Fase 1" checklist — qué debe confirmar Angel

Antes de mover un commit real a Fase 1 (scaffold Laravel + SvelteKit), Angel debe validar:

### Entorno
- [ ] **Docker Desktop instalado** con backend WSL2 activo. `docker --version` responde.
- [ ] **Node 20+** (`node -v`).
- [ ] **pnpm 9+** (`pnpm -v`). Si no: `npm install -g pnpm`.
- [ ] **PHP 8.3** con extensiones requeridas (ver `api/README.md`). Verificar: `php -m | grep -E "mbstring|pdo_mysql|redis|..."`.
- [ ] **Composer 2.x** (`composer -V`).
- [ ] **gh CLI** autenticado a `yadevOs`: `gh auth status`.

### Repos
- [ ] `git remote -v` en `yadev-cms/api/`, `yadev-cms/studio/`, `yadev-cms/infra/` apunta a `github.com:yadevOs/yadev-cms-{api,studio,infra}.git`.
- [ ] Angel puede pushear a cada repo (confirmar con un commit vacío o branch de prueba).

### Stack local funcional
- [ ] Hosts con las 6 entries de `.yadev.local` (ver `infra/scripts/hosts-setup.md`).
- [ ] `cd yadev-cms/infra && cp .env.example .env && docker compose up -d` levanta los 5 servicios healthy en ~30s.
- [ ] `ping api.yadev.local` responde 127.0.0.1.
- [ ] Mailpit UI abre en `http://localhost:8025`.
- [ ] MinIO console abre en `http://localhost:9001` con bucket `yadev-media` ya creado.

### Revisión de documentos
- [ ] Angel leyó y aprobó `phases/phase-0-setup.md` (reescrito).
- [ ] Angel leyó y aprobó `phases/phase-vps-migration.md` (nuevo).
- [ ] Angel confirmó las asunciones A1-A8 de la sección 4 arriba (o pidió cambios).

### Decisiones pendientes para Fase 1 (no bloquean Fase 0)
- [ ] Elegir entre Pest v3 o PHPUnit nativo para tests (recomendación: Pest).
- [ ] Confirmar nombre final del panel: `studio`, `admin`, `dashboard`, `panel`. Actualmente "studio" en todo el blueprint.
- [ ] Tag del commit inicial en cada repo: `v0.0.1-infra` para `yadevOs/yadev-cms-infra` tras mergear este docker-compose.

---

## 7. Siguiente paso concreto

1. **Angel revisa este `READY-FOR-REVIEW-v3.md`** completo.
2. Confirma asunciones A1-A8 o pide cambios.
3. Completa el checklist de sección 6 (install Docker, verificar Node/PHP/pnpm, agregar hosts entries).
4. Ejecuta `phases/phase-0-setup.md` día 3 — `docker compose up -d` y verifica los 4 servicios healthy.
5. Si todo OK: Angel hace los 3 commits iniciales (uno por repo) que yo dejé listos sin committear:
   - `yadevOs/yadev-cms-infra`: agrega `docker-compose.yml`, `.env.example`, `scripts/hosts-setup.md`, `README.md` nuevo.
   - `yadevOs/yadev-cms-api`: agrega `README.md` nuevo.
   - `yadevOs/yadev-cms-studio`: agrega `README.md` nuevo.
6. Una vez cerrados los 20 items del checklist final de `phases/phase-0-setup.md`, se abre **Fase 1 semana 1** — scaffold Laravel real en `yadev-cms/api/` + primer tenant `multiservicios` creado por CLI.

---

## 8. Estado: READY FOR REVIEW

Blueprint local-first consolidado. 13 archivos tocados (7 nuevos + 6 editados). Ningún código de aplicación, ningún commit en los 3 repos, ningún cambio fuera de `yadev-cms/`.

**Angel: revisá las asunciones A1-A8 y el checklist de sección 6. Si todo OK, arrancamos Fase 0 día 3 (levantar el stack).**

_Actualización v3 entregada por project-orchestrator agent. Fin del documento._
