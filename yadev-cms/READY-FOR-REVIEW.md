# READY FOR REVIEW — YaDev CMS Blueprint

> Documento final del Blueprint. Pendiente aprobación de Angel antes de pasar a Fase 1.
> Fecha: 2026-04-22.

---

## 1. Resumen ejecutivo (30 segundos)

Se entregó el Blueprint completo del proyecto **YaDev CMS** — un gestor de contenidos multi-tenant headless que permitirá a los clientes de YA Dev editar sus sitios Astro+Svelte existentes desde un panel web, sin commits ni rebuilds manuales.

- **Arquitectura:** Laravel 11 headless API + SvelteKit panel + Node webhook-runner en VPS Hostinger $8/mes. Sitios estáticos siguen en Hostinger shared.
- **Multi-tenant:** `stancl/tenancy` con DB separada por cliente para aislamiento real.
- **Panel admin:** custom con estética YaDev (dark glassmorphism, Space Grotesk, indigo). NO Filament.
- **Roadmap:** Fase 0 (1 sem setup) → Fase 1 (4 sem MVP con Multiservicios) → Fase 2 (6 sem paridad Damos + ECOMAG) → Fase 3 (4 sem IA + PORON/COICEM). Total 15 semanas.

---

## 2. Decisiones clave tomadas durante el blueprint

Ninguna de las decisiones arquitectónicas principales fue cuestionada (respetadas las que Angel impuso). Estas son las decisiones técnicas nuevas que se tomaron para completar el plan:

| # | Decisión | Justificación |
|---|----------|---------------|
| D1 | Auth: Sanctum token en cookie HttpOnly (panel) y Bearer (API directo) | Balance seguridad/simplicidad. No JWT. |
| D2 | Emails transaccionales: **Resend** (no SMTP del VPS) | Hostinger VPS tiene IPs rate-limitadas. Resend free tier = 3000 emails/mes. |
| D3 | WhatsApp notificaciones: **Meta Cloud API** | Alternativa pagada ~$0.007/msg; alternativa libre Twilio. Elegir en Fase 2. |
| D4 | Backups: **BackBlaze B2** cifrado con openssl, retention 30 días | Costo ~$0.50/mes para proyecto pequeño. S3-compatible. |
| D5 | Monitoring: **UptimeRobot free** + Horizon dashboard + prometheus-node-exporter | Gratis hasta 50 monitors. |
| D6 | Rate limit IA: quota mensual por plan, auto-disable si excedido | Prevenir gasto descontrolado con Anthropic. |
| D7 | Central schema tiene tabla `users_index` (email → tenant_id) | Mejora UX login: el cliente solo pasa email, no tiene que recordar su dominio. |
| D8 | Block schemas en PHP (server) + Zod (client) | Validación doble consistente. |
| D9 | Runner en Node + Fastify + PM2 (no en Laravel) | El build Astro requiere Node; tiene sentido que el runner también sea Node. |
| D10 | Editor WYSIWYG: TipTap + sanitización HTMLPurifier server-side | Mejor UX que Markdown para clientes colombianos no-técnicos. |
| D11 | i18n solo en Fase 3 | Los clientes actuales son 100% español. No urgente. |

---

## 3. Preguntas abiertas para Angel (DEBES responder antes de Fase 1)

### 3.1. Dominio del CMS
**Pregunta:** ¿El subdominio del panel será `admin.yadev.co`, `panel.yadev.co`, `cms.yadev.co`, o `app.yadev.co`?
**Relevancia:** Define DNS, SSL, CORS, branding en emails.
**Sugerencia:** `admin.yadev.co` para el panel y `api.yadev.co` para la API. Usado en toda la doc.

### 3.2. Plan de precios
**Pregunta:** ¿Cuánto cobrarás por el mantenimiento mensual y qué features incluye cada plan?
**Relevancia:** Afecta rate limits IA (Fase 3), features bloqueadas, sales script.
**Propuesta inicial:**
- **Starter:** $80 USD/mes — 1 sitio, 2 users, 100 IA requests, 3 GB media, backups 7 días.
- **Standard:** $150 USD/mes — 1 sitio, 5 users, 500 IA requests, 10 GB media, backups 30 días, 2FA, formularios ilimitados.
- **Pro:** $300 USD/mes — 2 sitios, users ilimitados, 2000 IA, 50 GB media, backups 90 días, multi-idioma, API access.

### 3.3. Hosting del VPS
**Pregunta:** ¿Ya tienes cuenta Hostinger con el plan KVM 2, o toca contratarlo?
**Relevancia:** Fase 0 empieza con eso. Confirmar antes de iniciar.

### 3.4. Dominio `yadev.co`
**Pregunta:** ¿Está registrado? Si no, ¿lo registramos o usamos otro (`.co`, `.com.co`, `.dev`)?
**Relevancia:** Todos los subdominios del proyecto dependen de esto.

### 3.5. Repo GitHub
**Pregunta:** ¿Usamos `github.com/Yeral-18/yadev-cms` o creamos una org nueva `github.com/yadev/`?
**Relevancia:** Deploy keys, permissions, branding.
**Sugerencia:** Crear org `yadev` para separar portfolio personal de producto comercial.

### 3.6. Meta Cloud API vs Twilio
**Pregunta:** Para notificaciones WhatsApp, ¿Meta Cloud API (gratis los primeros 1000 msg/mes, luego $0.0055/msg) o Twilio ($0.01/msg, más fácil setup)?
**Relevancia:** Implementación diferente en Fase 2 Semana 6.
**Sugerencia:** Meta Cloud API — más barato y es la fuente.

### 3.7. ¿Cliente necesita acceso sFTP a su storage?
**Pregunta:** Algunos clientes podrían querer subir media directo por FTP (ej: hacer un reel masivo de fotos). ¿Soportamos eso o SOLO via panel?
**Relevancia:** Diseño del filesystem + permisos.
**Sugerencia:** Solo via panel en Fase 1-2. Evaluar demanda en Fase 3.

### 3.8. Formulario contacto de sitios actuales
**Pregunta:** Los sitios actuales (Multiservicios, ECOMAG) usan `contact.php` con `mail()` de Hostinger shared. ¿Migramos ese flujo al API YaDev (sitio envía POST a api.yadev.co/v1/forms/{id}/submit) o mantenemos el PHP local hasta que haya razón para migrar?
**Relevancia:** Arquitectura de formularios.
**Sugerencia:** Fase 1-2 mantenemos ambos en paralelo. El PHP sigue funcionando. El API es adicional, y los formularios nuevos van por API. Migrar contacto de Multiservicios en Fase 2 Semana 6.

### 3.9. Export de tenant
**Pregunta:** Si un cliente cancela, ¿le damos zip con todo (dump + media + código)? ¿O sólo dump + media (y ellos pagan dev para el frontend)?
**Relevancia:** Filosofía de vendor lock-in.
**Sugerencia:** Dump + media + instrucciones. Código del sitio es de YaDev (es IP comercial). Transparente en el contrato.

### 3.10. Facturación cliente
**Pregunta:** ¿Necesitas módulo de facturación COP integrado en el CMS (Fase 2+) o usarás Siigo/Alegra externamente?
**Relevancia:** Si integrado, agrega 1-2 semanas de dev. Si externo, 0.
**Sugerencia:** Externo (Alegra) inicialmente. Integrar si a los 6 meses hay 10+ clientes.

---

## 4. Estimación final en horas

Asumiendo **~30h/semana de Angel + Claude Code como pair programmer**:

| Fase | Semanas | Horas Angel | Horas Claude | Cost AI estimado |
|------|---------|-------------|--------------|------------------|
| Fase 0 — Setup VPS | 1 | 20 | ~5 | $2 |
| Fase 1 — MVP Multiservicios | 4 | 120 | ~40 | $30 |
| Fase 2 — Paridad + ECOMAG | 6 | 180 | ~60 | $50 |
| Fase 3 — IA + PORON/COICEM | 4 | 120 | ~30 | $25 |
| **Total** | **15 sem** | **440h** | **~135h** | **~$110** |

Si Angel trabaja **full-time** (40h/sem), reduce a ~11 semanas calendario.

### Costos mensuales recurrentes post-launch
| Ítem | Costo |
|------|-------|
| VPS Hostinger KVM 2 | $8 |
| Dominio `.co` | $1 (anualizado) |
| Resend free tier | $0 (< 3k emails/mes) |
| BackBlaze B2 | ~$0.50 |
| Anthropic IA (20 tenants con caching) | ~$40 |
| Cloudflare R2 (opcional si >50 GB media) | ~$5 |
| UptimeRobot free | $0 |
| **Total** | **~$55/mes** |

Con 5 clientes pagando $120 USD/mes promedio = **$600 ingresos − $55 costs = $545 margen/mes**. Escala bien.

---

## 5. Recomendación de primer commit de Fase 1

Si Angel aprueba este Blueprint, el **primer commit de Fase 1** recomendado es:

### Commit: `feat: scaffold yadev-cms monorepo with Laravel 11 + stancl/tenancy`

**Archivos creados:**
```
yadev-cms/
├── api/                          ← NEW
│   ├── .env.example
│   ├── composer.json              (laravel/laravel 11, stancl/tenancy 3.9, sanctum, spatie/permission)
│   ├── artisan
│   ├── config/
│   │   ├── tenancy.php           (bootstrappers configurados)
│   │   ├── sanctum.php
│   │   └── permission.php
│   ├── database/
│   │   ├── migrations/           (schema central adaptado)
│   │   └── migrations/tenant/    (schema tenant adaptado)
│   ├── routes/
│   │   ├── api.php               (versionado /api/v1/, endpoint /health)
│   │   └── tenant.php            (futuro uso)
│   ├── app/
│   │   └── Models/
│   │       ├── Tenant.php         (extends Stancl\Tenancy\Tenant)
│   │       ├── Domain.php
│   │       └── User.php           (central super-admin)
│   └── tests/
│       └── TenancyTestCase.php    (base class)
├── admin/                        (vacío, Semana 3)
├── runner/                       (vacío, Semana 4)
├── infrastructure/
│   ├── nginx/
│   │   ├── api.yadev.co.conf
│   │   └── admin.yadev.co.conf
│   └── deploy/
│       └── github-actions.yml
├── .gitignore
└── README.md                     (summary + quick start)
```

**Comando sugerido para Angel:**
```bash
cd C:/Users/ASUS/APP/YaDevportfolio/yadev-cms/
# Pedirle a Claude Code:
# "Iniciemos Fase 1. Crea el scaffolding del commit descrito en READY-FOR-REVIEW.md
#  punto 5. Usa Laravel 11 y stancl/tenancy 3.9. No corras composer install ni
#  migraciones — sólo crea archivos. Documenta en README.md los pasos para correr local."
```

Después de ese commit, los siguientes commits son:
1. `feat(api): central migrations + tenant migrations ready`
2. `feat(api): sanctum auth endpoints (login, logout, me)`
3. `feat(api): pages + sections + blocks CRUD`
4. `feat(api): block types (hero_split, services_zigzag, about_three_cards, contact_form, rich_text)`
5. `test(api): CrossTenantIsolationTest passing`
6. `feat(admin): SvelteKit scaffold + shadcn-svelte + YaDev theme`
7. `feat(admin): login + dashboard + sidebar`
8. `feat(admin): editor bloques (5 types)`
9. `feat(admin): mediateca UI`
10. `feat(runner): Fastify webhook + HMAC + rsync logic`
11. `feat: integración Laravel → runner con Reverb broadcast`
12. `refactor(multiservicios): branch cms-compatible con site.json consumer`
13. `chore(deploy): Multiservicios tenant en producción + cutover`

---

## 6. Cómo rechazar/modificar este Blueprint

Si Angel discrepa en algún punto, opciones:
- **Cambios menores** (ej: nombre subdominio, plan de precios): editar los archivos .md directamente y commitear.
- **Cambios mayores** (ej: "quiero Filament en vez de SvelteKit"): escribir un decisión-record en `architecture/adr-001-panel-technology.md` y volver a correr este agent con esa restricción.
- **Rechazar todo**: pedir un blueprint alternativo con arquitectura A (monolito Laravel+Blade).

---

## 7. Lista completa de archivos creados por este agent

```
yadev-cms/
├── BLUEPRINT.md
├── CLAUDE.md
├── READY-FOR-REVIEW.md            ← ESTE ARCHIVO
├── agents-orchestration.md
├── multiservicios-migration-plan.md
├── risks-and-tradeoffs.md
├── architecture/
│   ├── system-diagram.md
│   ├── multi-tenancy-strategy.md
│   ├── api-contract.md
│   └── security-model.md
├── database/
│   ├── central-schema.sql
│   ├── tenant-schema.sql
│   └── seed-multiservicios.sql
└── phases/
    ├── phase-0-setup.md
    ├── phase-1-mvp.md
    ├── phase-2-parity.md
    └── phase-3-ai.md
```

**15 archivos, ~4500 líneas de documentación técnica.**

---

## 8. Hallazgos críticos durante el blueprint que pueden cambiar el plan

### H1. El sitio Multiservicios es MUY específico en animaciones/cursor
El `GearCursor.svelte` es un cursor personalizado de engranaje con posición absoluta siguiendo al mouse. Los badges del hero tienen posiciones x%/y% específicas. La dificultad de migrar esto al CMS editable es: **no editable directamente, debe ir como "config del sitio"**, no como bloque.

→ Impacto en plan: confirmar con Angel que está OK que estas cosas NO se editan desde el panel (quedan "hard-coded en el theme del sitio").

### H2. El `Contact.svelte` tiene reCAPTCHA v3 con test key hardcoded
```ts
const RECAPTCHA_SITE_KEY = '6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI'; // TEST KEY
```

→ Impacto: en Fase 1, hay que migrar esto a `settings.recaptcha.site_key` (server-rendered al build-time) para que cada tenant tenga su par de keys.

### H3. El `index.astro` tiene un "YaDev panel" oculto con links a `/internal/brandbook.html` y `/internal/firma-correo.html`.
Eso es útil para YaDev pero NO debe replicarse como feature del CMS para los clientes. Sí debe seguir existiendo como link manual que Angel controla.

→ Impacto: al refactorizar Astro, preservar ese panel oculto (no borrarlo), pero no exponer su edición en el CMS.

### H4. Multiservicios ya tiene Bureau Veritas ISO image hi-res embebida en el footer
Peso: ~800 KB (886x416 px PNG). No es tan pequeño. Recomendación: convertir a WebP al migrar a mediateca (ahorra ~60% size).

### H5. Los logos de clientes del carousel son PNG con transparencia
→ Debe preservarse al migrar (no convertir a JPEG). La mediateca del CMS debe respetar formato original cuando el cliente lo especifique.

### H6. El sitio usa `import.meta.env.BASE_URL` en todas partes
```astro
src={`${import.meta.env.BASE_URL ?? '/multiservicios/'}logo.png`}
```
Eso sugiere que el repo puede haberse usado con base path alternativo en staging. Al migrar al CMS, revisar que el build final respeta el dominio de producción (`/`) y no queda roto con paths absolutos.

---

## 9. Estado del proyecto: LISTO PARA REVIEW

**Lo que SÍ hicimos:**
- Diseño técnico completo de arquitectura, DB, API, security.
- Mapeo 1:1 de Multiservicios al catálogo de bloques.
- Plan de 15 semanas con day-by-day tasks.
- Análisis de riesgos con mitigaciones.
- Orquestación de agentes/skills para cada fase.

**Lo que NO hicimos (por instrucción explícita):**
- NO código Laravel, SvelteKit, ni Node.
- NO modificación a sitios en producción (ECOMAG, Multiservicios).
- NO tocamos `proyectos/`, `Modelos/`, `design-system/`, `assets/`.

**Próximo paso:**
Esperar aprobación de Angel (responder preguntas sección 3) → arrancar Fase 0.

---

_Blueprint entregado por project-orchestrator agent. Fin del documento._
