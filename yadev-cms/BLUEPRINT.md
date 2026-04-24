# YADEV CMS — Blueprint Maestro

> Sistema de gestión de contenidos multi-tenant para clientes de YA Dev.
> Reemplaza el flujo actual de "edición = commit + rebuild manual" por una experiencia de editor self-service estilo Damos.co, alimentando los sitios Astro existentes vía API.

---

## 1. Visión

**Problema actual:** Los sitios de YaDev (ECOMAG, Multiservicios P&J, etc.) tienen todo el contenido hardcodeado en componentes `.astro`. Cuando un cliente quiere cambiar el texto del hero, añadir un servicio, subir una foto nueva o editar horarios, el flujo es:

```
Cliente → WhatsApp a Angel → Angel edita código → commit → rebuild → rsync a Hostinger → cliente revisa
```

Tiempo promedio por cambio trivial: 30-90 min. No escala a 10+ clientes.

**Solución:** YaDev CMS — panel web multi-tenant donde cada cliente accede con su usuario, edita bloques predefinidos (hero, servicios, proyectos, textos, imágenes), presiona "Publicar" y el sitio se rebuilda + deploya automáticamente en <2 minutos.

**Valor para YaDev:**
- Cerrar ciclo de ventas con "panel de administración incluido" como diferencial frente a competencia que entrega solo HTML estático.
- Cobrar **mantenimiento mensual** recurrente (pricing TBD post-MVP, se definirá con data real de costos de operación).
- Escalar a 15-20 clientes sin saturar a Angel.

**Valor para el cliente:**
- Autonomía total sobre su contenido sin conocimiento técnico.
- Experiencia de edición tipo Notion/Webflow.
- Preview antes de publicar.
- Historial de cambios y rollback de un clic.

---

## 2. Arquitectura (decidida: Opción B)

> **Callout — Fases local-first vs producción:** Fase 0-2 del proyecto se desarrolla 100% en la máquina local de Angel usando Docker Compose + subdominios fake `.yadev.local` vía `/etc/hosts`. El VPS Hostinger KVM2 + dominio `yadev.co` real se contratan cuando el MVP funcione end-to-end (ver `phases/phase-vps-migration.md`). Toda la arquitectura descrita abajo aplica igual en ambos entornos — lo único que cambia es dónde corren los containers y qué DNS resuelve los subdominios.


```
┌─────────────────────────────────────────────────────────────────┐
│  VPS Hostinger ($8/mes)                                         │
│  ┌─────────────────────┐     ┌──────────────────────────────┐   │
│  │ Laravel 11 API      │◄───►│ MySQL (central + N tenants) │   │
│  │ (headless, Sanctum) │     └──────────────────────────────┘   │
│  │ + Horizon queue     │     ┌──────────────────────────────┐   │
│  │ + stancl/tenancy    │◄───►│ Redis (cache, sesiones)      │   │
│  └─────────────────────┘     └──────────────────────────────┘   │
│          ▲                                                      │
│          │ HTTPS                                                │
│  ┌───────┴───────────────┐   ┌──────────────────────────────┐   │
│  │ SvelteKit Admin Panel │   │ Node webhook-runner (PM2)    │   │
│  │ studio.yadev.co       │   │ escucha "publish"            │   │
│  └───────────────────────┘   │ → npm run build              │   │
│                              │ → rsync → Hostinger shared   │   │
│                              └──────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                                          │
                                          ▼ rsync sobre SSH
┌─────────────────────────────────────────────────────────────────┐
│  Hostinger Shared Hosting (existente)                           │
│  multiserviciospj.com  → dist/ (Astro estático)                 │
│  ecomagsas.com         → dist/ (Astro estático)                 │
│  clienteN.com          → dist/                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Flujo de publicación:**
1. Cliente edita bloque "Hero" en panel → `POST /api/v1/blocks/{id}` vía SvelteKit → Laravel valida + guarda en DB tenant.
2. Cliente presiona "Publicar cambios" → Laravel encola job `PublishSite($tenant)` en Redis.
3. Horizon procesa job: llama `POST /webhook/rebuild` al runner Node con HMAC.
4. Runner: `git pull` del repo del cliente en `/srv/builds/{tenant}/`, inyecta JSON del API en `src/content/`, corre `npm run build`, hace `rsync -az dist/ user@hostinger:/public_html/`.
5. Runner responde al API con `status: success, duration: 94s, commit_sha: xxx`.
6. Panel muestra toast "Publicado en 1m 34s ✓" con link al sitio live.

**Por qué no monolito Laravel+Blade:**
- Los sitios ya están hechos en Astro+Svelte, funcionan perfecto, son rápidos (100/100 Lighthouse) y están indexados. Tirarlos a la basura = perder SEO + retrabajo 4x.
- Astro estático en Hostinger shared = $0 de hosting adicional por cliente.
- Blade rendering = VPS debe aguantar todo el tráfico público = requiere upgrade de VPS si llegan 5k visitas/día.

**Por qué VPS + DB separada por tenant:**
- Aislamiento real: migraciones por cliente, backup granular, portabilidad (si un cliente se va, exportas SU db y adiós).
- Compliance: datos del cliente A nunca pueden leerse en una query mal formada del cliente B.
- Performance: tablas más pequeñas = queries más rápidas.
- Trade-off: más complejidad de operación. Se mitiga con automatización en Fase 0.

---

## 2.1. Arquitectura de dominios (decidido)

**Dominio maestro YaDev:** `yadev.co`

**Subdominios del VPS (únicos puntos de entrada al stack YaDev):**

| Subdominio | Rol | Quién entra |
|------------|-----|-------------|
| `studio.yadev.co` | Panel admin custom (SvelteKit + shadcn-svelte, look YaDev dark glassmorphism) | Angel (super-admin) + clientes (admin/editor de su propio tenant) |
| `api.yadev.co` | Laravel 11 headless REST | Consumido por `studio.yadev.co` y por los builds Astro de cada cliente |

**Dominios de cliente (cada empresa conserva el suyo):**
- `ecomagsas.com` → ECOMAG S.A.S
- `multiserviciospj.com` → Multiservicios P&J
- `poronsas.com` → PORON S.A.S
- `coisem.com` → COICEM
- `cliente-N.com` → siguientes tenants

Cada sitio cliente vive en **Hostinger shared** (uno por cliente, un public_html/ por dominio), sirve HTML estático generado por Astro, y:
1. En build time, el runner hace fetch a `https://api.yadev.co/v1/tenants/{tenant_id}/content-tree` para inyectar el contenido.
2. El sitio cliente **nunca** consume el API en runtime — es 100% estático, indexable, y no depende del VPS para estar online.
3. Cuando el cliente guarda cambios en `studio.yadev.co`, el API encola un job que dispara el rebuild + rsync al Hostinger shared correspondiente.

**Resolución de tenant:**
- En `studio.yadev.co` — se resuelve por el tenant activo del usuario logueado (Sanctum token contiene `tenant_id`). Angel como super-admin puede impersonar cualquier tenant.
- En `api.yadev.co` — se resuelve por:
  1. `Authorization: Bearer {token}` (token embebe tenant) — caso panel.
  2. `tenant_id` en la URL path (`api.yadev.co/v1/tenants/{tenant_id}/...`) — caso build/runner.
  3. `Origin` header validado contra whitelist `domains` por tenant — para cualquier fetch desde un sitio cliente en runtime (poco común pero posible).

---

## 2.2. Repositorios GitHub

Organización: **`yadevOs/`** (creada en GitHub, con esa capitalización exacta). Tres repos ya existentes, clonados localmente en `yadev-cms/{api,studio,infra}/`:

| Repo | Contenido | Stack |
|------|-----------|-------|
| `yadevOs/yadev-cms-api` | Backend headless REST | Laravel 11 + PHP 8.3 + stancl/tenancy v3 + MySQL 8 |
| `yadevOs/yadev-cms-studio` | Panel admin del cliente + super-admin | SvelteKit + Tailwind + shadcn-svelte (tema YaDev dark) |
| `yadevOs/yadev-cms-infra` | Infra como código | Docker Compose (local-first), nginx vhosts, scripts setup, deploy pipelines (activados en Fase VPS-migration) |

**Por qué tres repos separados (y no monorepo):**
- Deploy pipelines independientes (cambios en studio no despliegan el API).
- Permisos granulares: un futuro dev frontend solo recibe acceso a `yadev-cms-studio`.
- Release cadence distinto: el API se mueve lento (stable contract), el studio se itera más rápido.
- Secrets por repo (no se filtran credenciales del VPS por accidente al frontend).

Adicionalmente, los repos de sitios cliente (`yadevOs/site-multiservicios`, `yadevOs/site-ecomag`, etc.) siguen existiendo como repos separados — uno por cliente.

---

## 3. Stack técnico

| Capa | Tecnología | Por qué |
|------|-----------|---------|
| Backend API | Laravel 11 + PHP 8.3 | Ecosistema maduro, Horizon, Sanctum, Tenancy battle-tested |
| DB | MySQL 8 | Default Hostinger VPS, sin costo adicional |
| Multi-tenant | stancl/tenancy v3 | Standard de-facto, database-per-tenant nativo |
| Auth | Laravel Sanctum (token) | Ligero, perfecto para SPA consumiendo API |
| RBAC | spatie/laravel-permission | Roles + permisos granulares |
| Mediateca | spatie/medialibrary + Intervention | Conversiones automáticas (thumb, webp, og) |
| Queue | Redis + Laravel Horizon | Dashboard visual, reintentos, monitoreo |
| Panel Admin | SvelteKit + Tailwind + shadcn-svelte | Stack que Angel ya domina, misma estética del portfolio |
| Editor WYSIWYG | TipTap | Extensible, headless, limpio HTML |
| Frontend cliente | Astro 5.18 + Svelte 5.53 | Ya existe, se refactoriza para consumir API |
| Build runner | Node + PM2 | Ejecuta `npm run build` + rsync por tenant |
| Reverse proxy | Nginx | HTTPS terminación, static caching |
| SSL | Let's Encrypt (certbot) | Gratis, auto-renovación |
| IA (Fase 3) | Anthropic SDK (Claude Haiku 4.5 + Sonnet 4.6) | Prompt caching para bajar costos |

---

## 4. Fases y timeline

### Fase 0 — Setup local-first (1 semana)
- Docker Desktop + Node 20 + PHP 8.3 + Composer + pnpm + gh CLI instalados local.
- Trabajar con los 3 repos clonados en `yadev-cms/{api,studio,infra}/` (org `yadevOs/`).
- `infra/docker-compose.yml` con MySQL 8, Redis 7, MinIO (S3-compatible), Mailpit (SMTP testing).
- `/etc/hosts` de Windows con entries `api.yadev.local`, `studio.yadev.local`, `{tenant}.yadev.local`.
- Backups locales diarios a `infra/backups/` (retención 7 días).
- CI/CD skeleton con GitHub Actions (tests + lint, NO deploy aún — el deploy llega en Fase VPS-migration).
- VPS Hostinger KVM2 y dominio `yadev.co` **NO se contratan** en esta fase.

### Fase 1 — MVP Multiservicios PoC (4 semanas)
**Objetivo:** Multiservicios P&J 100% editable desde el panel. Multi-tenant ya establecido aunque solo haya 1 cliente.

- Semana 1: Scaffolding Laravel + stancl/tenancy + auth + seed central (YaDev super-admin).
- Semana 2: Schema tenant (pages/blocks/media) + API CRUD básico + bloques tipo: Hero, Services, RichText, ImageGallery.
- Semana 3: Panel SvelteKit login + dashboard + editor visual bloques + preview.
- Semana 4: Webhook rebuild + rsync a Hostinger + migración real del contenido actual de Multiservicios + QA.

**Criterio de éxito:** el cliente Multiservicios puede entrar al panel, cambiar el título del hero, subir una foto nueva a un servicio, publicar, y en <2 min el cambio está live en multiserviciospj.com sin que Angel toque nada.

### Fase 2 — Paridad Damos + onboarding ECOMAG (6 semanas)
- Bloques avanzados: Bento, Timeline, FAQ, Stats counter, CTA, Form builder.
- Gestor de formularios: submissions en DB + export CSV + notificaciones.
- SEO editor: meta tags, OG image, schema.org por página.
- Menús y navegación editables.
- Pop-ups programables (con triggers: tiempo, scroll, exit-intent).
- Mediateca con folders, tags, CDN-ready (Cloudflare R2 opcional).
- Activity log + restore de versiones anteriores.
- Migración de ECOMAG como segundo tenant.

### Fase VPS-migration — Ir a producción real (2 días, opcional-intermedia)

Ejecutada cuando el MVP (Fases 0-1-2) corre estable en local y Angel decide publicar. Ver `phases/phase-vps-migration.md`. Resumen:

- Contratar VPS Hostinger KVM 2 (~$8 USD/mes) + dominio `yadev.co` (~$10/año).
- Provisionar VPS: hardening, Docker Compose prod, Nginx real, Let's Encrypt auto-renew.
- DNS real: `api.yadev.co` y `studio.yadev.co` → VPS IP.
- Migrar storage MinIO local → BackBlaze B2 (S3-compatible, más barato que S3).
- Migrar backups locales → B2 con retención 30 días diario + 12 meses mensual.
- Activar deploy pipelines en los 3 workflows de GitHub Actions (secrets `SSH_PRIVATE_KEY`, `VPS_HOST`).

No es una fase obligatoria del timeline original — puede ocurrir entre Fase 2 y Fase 3, o incluso después de Fase 3 si Angel quiere seguir iterando local antes de publicar.

### Fase 3 — IA + automatización (4 semanas)
- "Asistente de contenido": generar/mejorar textos con Claude Haiku 4.5.
- Generación de OG image con Nano Banana 2.
- SEO score automático con sugerencias.
- Traducción multi-idioma (ES → EN) con caching.
- Migración de PORON y COICEM.

**Total: 15 semanas (≈4 meses calendario para un dev + Claude).**

---

## 5. Riesgos principales (ver `risks-and-tradeoffs.md` para detalle)

| # | Riesgo | Probabilidad | Impacto | Mitigación |
|---|--------|-------------|---------|------------|
| 1 | Latencia de rebuild > 3 min frustra al cliente | Media | Alto | Build cache en Astro, solo rebuild el HTML afectado (ISR manual) |
| 2 | VPS $8 insuficiente para 20 clientes | Baja | Medio | Horizon monitorea, upgrade a $16 cuando CPU sostenido >60% |
| 3 | Cliente rompe layout con rich text | Alta | Medio | TipTap sanitiza, bloques validados con schema JSON |
| 4 | Pérdida de DB tenant = cliente pierde todo | Baja | Crítico | Backup diario por tenant a S3-compatible (Hostinger cloud storage o BackBlaze B2) |
| 5 | Cliente exporta y se va a competencia | Media | Bajo | No es malo, es ético. Exportar JSON + media zip en 1 clic es un feature. |
| 6 | Colisión de webhook simultáneo | Media | Medio | Queue con `unique lock` por tenant |

---

## 6. Por qué YaDev hace esto (y no usa Webflow/Wordpress)

- **Webflow:** $39/mes/sitio = $780/mes para 20 clientes + dependencia total de un SaaS extranjero. No edita los sitios Astro existentes.
- **Wordpress:** Ecosistema lento, plugins inseguros, cliente rompe todo, no se integra con el stack Astro+Svelte+Tailwind que define la marca de YaDev.
- **Strapi/Directus self-hosted:** Buenos pero su UI no refleja la marca YaDev, curva de personalización alta, y no tienen rebuild-on-publish integrado.

Construir propio = control total, personalización a la medida del cliente colombiano (UX en español, WhatsApp first, etc.), y activo de software propio que se puede licenciar/vender.

### Diferenciadores vs competencia colombiana directa (Damos.co)

Damos.co es el competidor directo en Colombia: 15+ años de trayectoria, cientos de clientes PyME, stack Laravel monolito server-rendered con WYSIWYG + mediateca + IA + webmail nativo integrado. Su spec 2026 está documentada en `https://www.damos.co/servicios/diseno-web/ventajas-de-nuestro-cms-gestor-de-contenidos`. Un cliente real en producción: `https://www.odircertificaciones.com` (admin en `/admin_245/`).

Análisis feature-por-feature, matriz comparativa y estrategia de posicionamiento: **ver `competitive-analysis-damos.md`**.

Diferenciadores técnicos clave de YaDev:

1. **Sitios servidos como SSG estático con CDN** (Astro pre-render + Hostinger shared + Cloudflare). Damos renderiza Blade server-side → su tráfico público depende del uptime de su VPS. Un ataque DDoS al VPS de Damos tumba TODOS los sitios de sus clientes. En YaDev, el VPS solo sirve al panel y al API de build time; si el VPS cae, los sitios cliente siguen vivos porque ya están estáticos en Hostinger.
2. **Superficie de ataque cero en producción** — el sitio público del cliente no tiene PHP, no tiene DB, no tiene auth. Damos expone `/admin_245/index.php` en el MISMO dominio del cliente (obfuscation by path). YaDev usa subdominio independiente `studio.yadev.co` — separación real, no cosmética.
3. **DB-per-tenant (stancl/tenancy v3)** — aislamiento físico de datos. Damos, como monolito Laravel con cientos de clientes, probablemente usa DB compartida con `tenant_id` en cada fila (deducción de arquitectura típica de la escala que operan). Un bug en una query mal scopada en Damos = leak cross-tenant. En YaDev, imposible por diseño: conexiones MySQL distintas por tenant.
4. **Stack moderno para el panel** — SvelteKit 5 + shadcn-svelte vs panel Blade+jQuery. DX de edición superior: autosave debounce, presencia multi-user en tiempo real vía Reverb, editor de bloques estilo Notion/Webflow.
5. **Costo operativo menor a escala** — VPS KVM2 $8/mes soporta 20 tenants porque la carga es editar + build, no servir tráfico público. Damos escala verticalmente el VPS para sostener los Blade renders de todos los sitios. A 50 tenants, YaDev sigue en $8/mes + Hostinger shared por cliente (que paga el cliente); Damos requiere upgrade de VPS.

---

## 7. Dependencias y supuestos

- Angel tiene acceso root al VPS Hostinger.
- Dominio `yadev.co` registrado y con DNS bajo control de Angel (para crear `api.yadev.co` y `studio.yadev.co`).
- Organización `yadevOs/` creada en GitHub con los 3 repos del CMS (`yadev-cms-api`, `yadev-cms-studio`, `yadev-cms-infra`) + repos por sitio cliente (`yadevOs/site-multiservicios`, `yadevOs/site-ecomag`, etc.).
- Claude Code disponible para asistir el desarrollo (acelera 3-4x).
- DNS de los dominios de cliente (`ecomagsas.com`, `multiserviciospj.com`, etc.) sigue apuntando a Hostinger shared — **no** se toca esa configuración.
- Pricing del servicio se define post-MVP con data real de costos de operación.

---

## 8. Definition of Done para el Blueprint

- [x] Estructura de carpetas creada en `yadev-cms/`.
- [x] BLUEPRINT.md (este archivo).
- [x] CLAUDE.md específico del subproyecto.
- [x] 4 docs en `architecture/`.
- [x] 3 archivos SQL en `database/`.
- [x] 4 docs de fases en `phases/`.
- [x] `agents-orchestration.md`.
- [x] `multiservicios-migration-plan.md`.
- [x] `risks-and-tradeoffs.md`.
- [x] `READY-FOR-REVIEW.md` con preguntas abiertas y recomendación de primer commit.

No se escribe código Laravel ni SvelteKit en esta fase. Solo planificación.
