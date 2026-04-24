# READY FOR REVIEW v2 — YaDev CMS Blueprint

> Continuación del v1 tras la ronda de revisión con Yeral.
> Consolida las 3 decisiones que Yeral tomó, documenta cómo se tradujeron al blueprint, y lista las 5 nuevas preguntas que bloquean el arranque de Fase 0.
> Fecha: 2026-04-22.

---

## 1. Resumen de cambios vs v1

En v1 quedaron 10 preguntas abiertas. Yeral respondió las 3 más estructurales (dominios, pricing, repos). Este v2:

- Marca esas 3 como **RESUELTAS** y documenta su traducción técnica.
- Remueve propuestas de pricing específicas del blueprint (se posponen a post-MVP).
- Agrega 5 preguntas operacionales nuevas que bloquean Fase 0.
- Confirma que **el resto de preguntas abiertas de v1 (3.6 a 3.10) siguen vigentes pero no bloquean Fase 0** — se resuelven en Fase 2.

---

## 2. Decisiones RESUELTAS en esta ronda

### Decisión 1 — Arquitectura de dominios (resuelve v1 §3.1 y v1 §3.4)

**Respuesta de Yeral:**

- Dominio maestro: **`yadev.co`**.
- Dos subdominios en el VPS:
  - `studio.yadev.co` → panel admin custom (SvelteKit + shadcn-svelte). Look YaDev dark glassmorphism. Entran Yeral (super-admin) y los clientes (admin/editor de su propio tenant).
  - `api.yadev.co` → Laravel headless REST. Consumido por el studio y por los builds Astro de cada cliente.
- Los **dominios de cliente** (`ecomagsas.com`, `multiserviciospj.com`, `poronsas.com`, `coisem.com`, etc.) **siguen en Hostinger shared** y no cambian. Un public_html/ por dominio, sitios Astro estáticos.
- **Resolución de tenant en el API** — tres fuentes posibles, validadas en cascada:
  1. `Authorization: Bearer {token}` (token Sanctum embebe `tenant_id`) — caso panel.
  2. `tenant_id` en URL path (`api.yadev.co/v1/tenants/{tenant_id}/...`) — caso runner/build y calls administrativas.
  3. `Origin` header validado contra whitelist `yadev_central.domains` — caso fetch público desde navegador del sitio cliente (raro).

**Traducción técnica (archivos editados):**

- `BLUEPRINT.md` §2.1 — nueva sección "Arquitectura de dominios" con tabla de subdominios y explicación de resolución de tenant.
- `CLAUDE.md` (subproyecto) — nueva sección "Arquitectura de dominios (decidida)" al inicio.
- `architecture/system-diagram.md` — ASCII diagram actualizado con `studio.yadev.co` (no `admin.yadev.co`) y `api.yadev.co`; nueva sección "Resolución de tenant en el API" con tabla.
- `architecture/multi-tenancy-strategy.md` — sección "Resolución de tenant (middleware)" reescrita con las 4 fuentes (token, path, Origin, impersonation).
- `architecture/api-contract.md` — base URL explícita `https://api.yadev.co/v1/`, nueva sección "Estilos de URL soportados" (implícito-por-token vs explícito-por-path), nuevos endpoints runner-facing (`/v1/tenants/{tenant_id}/content-tree`, `/v1/tenants/{tenant_id}/publishes/{publish_id}/complete`).
- `architecture/security-model.md` §7 — CORS reescrito con dos categorías: panel (siempre permitido) y sitios cliente (whitelist dinámica por tenant contra `central.domains`).
- `phases/phase-0-setup.md` — DNS setup usa `api.yadev.co` + `studio.yadev.co`; certbot emite para ambos; nginx vhosts con nombres correctos.
- `phases/phase-1-mvp.md` — `config/tenancy.php central_domains` ahora usa `['api.yadev.co','studio.yadev.co','localhost']`; entregable lista `studio.yadev.co` (no `admin.yadev.co`).

### Decisión 2 — Pricing fuera de scope técnico (resuelve v1 §3.2)

**Respuesta de Yeral:**

Fuera del scope técnico por ahora. Pricing se define **post-MVP** con data real de costos (VPS, storage, ancho de banda, tiempo de soporte). Mientras tanto: remover propuestas específicas de $80/$150/$300 del blueprint. Dejar únicamente la nota **"pricing TBD post-MVP, se definirá con data real de costos"**.

**Traducción técnica (archivos editados):**

- `BLUEPRINT.md` §1 — línea de "Valor para YaDev" cambiada: ya no dice "$80-150 USD/cliente", dice "pricing TBD post-MVP".
- `BLUEPRINT.md` §7 — lista de supuestos ya no afirma que "clientes aceptarán cargo mensual de $80-150 USD".
- `phases/phase-3-ai.md` línea 14 — rate limit de IA ya no menciona "plan `standard` = 100 requests/mes, `pro` = 1000"; ahora dice "configurables por tenant (pricing y tiers: TBD post-MVP)".
- `risks-and-tradeoffs.md` R9 — monthly quota de IA ya no dice "standard=$3/mes, pro=$15/mes"; ahora dice "valores concretos: TBD post-MVP cuando haya data real".
- `risks-and-tradeoffs.md` R12 mitigación 4 — frase reescrita para no prometer tiers específicos.
- **No se tocó** `database/central-schema.sql` porque el ENUM `plan ('starter','standard','pro','enterprise')` es estructura neutra, no compromete pricing.

### Decisión 3 — Repositorios GitHub multi-repo (resuelve v1 §3.5)

**Respuesta de Yeral:**

Crear organización `yadev/` en GitHub. Tres repos del CMS:

| Repo | Contenido |
|------|-----------|
| `yadev/yadev-cms-api` | Backend Laravel 11 (DB-per-tenant con stancl/tenancy v3) |
| `yadev/yadev-cms-studio` | Panel admin SvelteKit + shadcn-svelte (look YaDev) |
| `yadev/yadev-cms-infra` | Docker configs, setup scripts VPS, nginx vhosts, deploy scripts, runbooks |

Adicionales: repos por sitio cliente (`yadev/site-multiservicios`, `yadev/site-ecomag`, etc.) — sin cambios, siguen separados.

**Traducción técnica (archivos editados):**

- `BLUEPRINT.md` §2.2 — nueva sección "Repositorios GitHub" con tabla + justificación de multi-repo vs monorepo.
- `CLAUDE.md` (subproyecto) — nueva sección "Repositorios GitHub (decididos)" al inicio.
- `phases/phase-0-setup.md` — requisitos previos pide que la org `yadev/` ya esté creada con los 3 repos; sección "CI/CD skeleton" reescrita con 3 workflows separados (uno por repo en vez de uno monorepo); checklist final agrega validación de org GitHub creada.
- Se eliminó la suposición del monorepo `yadev/yadev-cms` que aparecía en v1 §5.

---

## 3. Nuevas preguntas pendientes (bloquean Fase 0)

Estas 5 preguntas **deben resolverse antes de que Yeral ejecute el primer comando** de `phases/phase-0-setup.md`. Sin ellas, el setup no puede avanzar.

### Q1. Registro del dominio `yadev.co`
**Pregunta:** ¿`yadev.co` ya está registrado? Si no, ¿dónde lo compra?
**Opciones:**
- **Hostinger** — conveniente (un solo proveedor con el VPS + DNS unificado). ~$10 USD/año para `.co`.
- **Namecheap** — más barato, DNS manageable vía API, pero DNS queda separado del VPS.
- **GoDaddy** — caro, evitar salvo preferencia personal.
**Recomendación:** Hostinger. Un solo login para VPS + DNS + correos futuros.
**Bloqueo:** sin este dominio, no se pueden crear `api.yadev.co` ni `studio.yadev.co`, no corre certbot, no arranca nada de Fase 0.

### Q2. VPS Hostinger KVM 2 contratado
**Pregunta:** ¿VPS ya contratado?
**Specs obligatorias:**
- 2 vCPU
- 8 GB RAM
- 100 GB NVMe
- 8 TB transfer
- Ubuntu 24.04 LTS
- IP pública fija
**URL de compra:** https://www.hostinger.com/vps-hosting (plan KVM 2, ~$8 USD/mes anual)
**Bloqueo:** Fase 0 Día 1 empieza con `ssh root@<ip_vps>`.

### Q3. Organización GitHub `yadev/` creada
**Pregunta:** ¿La org ya existe? Si no, ¿quiere que se documente el paso manualmente o él la crea antes de Fase 0?
**Pasos manuales:**
1. github.com/organizations/new → nombre `yadev` → plan Free.
2. Crear 3 repos privados: `yadev-cms-api`, `yadev-cms-studio`, `yadev-cms-infra`.
3. Crear deploy SSH key desde VPS (ver phase-0 Día 2), agregarla como **deploy key global a nivel de org**.
4. Settings → Secrets → Actions → agregar `SSH_PRIVATE_KEY` y `VPS_HOST` a cada repo.
**Recomendación:** Yeral crea manualmente en ~15min antes de Fase 0; este agent no puede crear orgs GitHub.

### Q4. Mapeo de dominios cliente → VPS
**Pregunta:** ¿Cómo se conectan los sitios cliente con el API?
**Opción A (recomendada):**
- Sitios cliente (ecomagsas.com, multiserviciospj.com, etc.) siguen 100% en Hostinger shared, como están hoy.
- Los fetchs al API (`api.yadev.co`) ocurren **solo en build time**, desde el runner Node del VPS (server-to-server).
- **No hay CNAME del cliente hacia el VPS.** El DNS del cliente no se toca.
**Opción B (no recomendada):**
- Cada sitio cliente pone un CNAME `api.cliente.com → api.yadev.co`, expone fetch client-side en runtime. Agrega latencia y complejidad de CORS por tenant.
**Recomendación:** Opción A. Se confirma explícitamente que **no se toca el DNS de ningún cliente** en Fase 0-1.

### Q5. Política de backups
**Pregunta:** ¿Alcance del backup y retención?
**Opciones:**
- **Solo DBs** — dump diario cifrado a BackBlaze B2, retención 30 días. Suficiente para recuperar contenido.
- **DBs + mediateca** — incluye archivos subidos por cada tenant (storage/tenants/). Retención 30 días.
- **DBs + mediateca + builds** — incluye también `/srv/builds/` (los repos clone y dist/). Raramente necesario (builds se regeneran desde el API).
- **Retención:** 30 días granular, ¿o también 12 meses mensual para compliance?
**Recomendación:** **DBs + mediateca**, retención **30 días granular + 12 meses mensual (solo el primero de cada mes)**. Estimación costo: ~$1-2/mes a BackBlaze B2 para 20 tenants.
**Bloqueo:** Fase 0 Día 4 configura el cron de backup. Si no está decidido, hay que volver a ejecutar Día 4.

---

## 4. Preguntas de v1 que NO bloquean Fase 0 (siguen vigentes)

Estas se respondieron o se pospusieron, pero no bloquean el arranque:

| Ref v1 | Tema | Estado |
|--------|------|--------|
| v1 §3.3 | Cuenta Hostinger KVM2 | Se vuelve a preguntar en Q2 arriba |
| v1 §3.6 | Meta Cloud API vs Twilio para WhatsApp | Sigue pendiente, se resuelve en Fase 2 Semana 6 |
| v1 §3.7 | sFTP directo para clientes | Sigue pendiente, evaluar en Fase 3 |
| v1 §3.8 | Formulario contacto PHP vs API YaDev | Sigue pendiente, resuelve en Fase 2 Semana 6 |
| v1 §3.9 | Export completo al cancelar tenant | Sigue pendiente, política de offboarding |
| v1 §3.10 | Facturación integrada (Alegra externo) | Sigue pendiente, evaluar en Fase 3+ |

---

## 5. Archivos editados en esta ronda

Lista completa de archivos tocados para aplicar las 3 decisiones:

```
yadev-cms/
├── BLUEPRINT.md                            ← §1, §2.1 (nueva), §2.2 (nueva), §4 (Fase 0), §7
├── CLAUDE.md                               ← sección "Contexto rápido" ampliada
├── READY-FOR-REVIEW.md                     ← sin cambios (se conserva v1 como histórico)
├── READY-FOR-REVIEW-v2.md                  ← NUEVO (este archivo)
├── architecture/
│   ├── system-diagram.md                   ← ASCII + sección "Resolución de tenant"
│   ├── multi-tenancy-strategy.md           ← sección "Resolución de tenant (middleware)" reescrita + login flow
│   ├── api-contract.md                     ← base URL, "Estilos de URL", endpoints runner
│   └── security-model.md                   ← §7 CORS reescrito, checklist final
├── phases/
│   ├── phase-0-setup.md                    ← requisitos, DNS, nginx vhosts, CI/CD reescrito, checklist
│   ├── phase-1-mvp.md                      ← tenancy central_domains + entregables
│   └── phase-3-ai.md                       ← rate limits sin pricing específico
└── risks-and-tradeoffs.md                  ← R9 mitigación sin $$ específicos, R12 mitigación 4
```

**12 archivos editados.** Ningún código tocado (sigue siendo blueprint/doc, no scaffolding).

---

## 6. Siguiente paso concreto

**Yeral confirma los 5 puntos arriba (Q1-Q5) y arrancamos Fase 0 día 1 ejecutando el script `phases/phase-0-setup.md`.**

Orden de ejecución:
1. Confirmar Q1-Q5 en este archivo (responder inline o en chat).
2. Ejecutar Fase 0 Día 1 — provisionar VPS + configurar SSH + hardening + DNS (`phases/phase-0-setup.md` líneas 19-85).
3. Una vez DNS propaga (ver con `dig api.yadev.co` y `dig studio.yadev.co`), continuar Día 2 (stack base PHP/MySQL/Redis/Node).
4. Día 3: nginx + certbot para ambos subdominios.
5. Día 4: filesystem + secrets + backups a BackBlaze B2 con la política que se definió en Q5.
6. Día 5: CI/CD skeleton con los 3 repos GitHub ya creados (Q3) + monitoring.

Al cerrar el checklist de Fase 0 (final de `phase-0-setup.md`), se abre Fase 1 — scaffold Laravel + stancl/tenancy en `yadev/yadev-cms-api`.

---

## 7. Inconsistencias encontradas durante la edición

Hallazgos del agent revisando los docs cross-linked:

### I1. `api-contract.md` mezclaba `/api/v1/` y `/v1/` como prefijo
En v1 muchas referencias decían `/api/v1/auth/login` y otras `/v1/auth/login`. Con la base URL ahora explícita (`https://api.yadev.co/v1/`), **el prefijo correcto es `/v1/` sin `/api/`** (Laravel puede no usar el prefix `api` cuando el subdominio YA es `api.yadev.co`). Se actualizó el login endpoint como muestra. **Acción pendiente Fase 1:** al scaffold-ear el API, confirmar que `routes/api.php` se monte en `/v1/` (no `/api/v1/`) editando `bootstrap/app.php` con `apiPrefix: ''` o routing equivalente. Esta es una decisión de implementación, no un cambio de contrato hacia afuera.

### I2. `phase-0-setup.md` asumía monorepo con `admin/` como subcarpeta
El workflow de GitHub Actions en v1 hacía `cd admin && pnpm build`. Con la decisión de multi-repo, se reescribió para 3 workflows separados. **Pero:** el nombre del directorio dentro de `yadev-cms-studio` ya no es `admin/` — es la raíz del repo. Los paths de deploy cambiaron de `admin/build/` → `build/` (raíz del repo studio). Se actualizó.

### I3. `CLAUDE.md` subproyecto lista estructura con `api/`, `admin/`, `runner/` como carpetas hermanas
Eso venía del modelo monorepo. Ahora cada uno es un repo separado que se clona en `/srv/yadev-cms/{api,studio,runner}/`. La estructura física en el VPS no cambia (carpetas hermanas en `/srv/yadev-cms/`), pero el repo origen es distinto. **No se editó la sección "Estructura del subproyecto" del CLAUDE.md** porque esa sección describe la estructura dentro de `yadev-cms/` (este repo raíz del portfolio), que es donde vive el blueprint — no la estructura del VPS ni de los repos GitHub. Esa ambigüedad la dejamos porque corregirla requiere reescribir la sección entera y el contenido es correcto para el blueprint actual.

### I4. Referencia a `admin.yadev.co` sobrevive en `READY-FOR-REVIEW.md` v1
Intencionalmente no se editó — v1 es histórico. Todas las nuevas refs usan `studio.yadev.co`.

### I5. `database/central-schema.sql` tiene ENUM `plan('starter','standard','pro','enterprise')`
No se tocó porque el ENUM es estructura neutra, no compromete pricing. Cuando Yeral defina tiers post-MVP, los valores del ENUM pueden simplemente mapearse a esos tiers sin migración de schema. Si los tiers post-MVP tienen nombres distintos, se hace un `ALTER TABLE` trivial.

### I6. Un tema que quedó sin resolver en docs: nombres de tenant
El CLI de provisioning usa `--slug=multiservicios` (corto), pero los endpoints runner usan `{tenant_id}` que puede ser slug o ID numérico. Convendría estandarizar a solo **slug** en URLs (human-readable) y solo **ID numérico** internamente. No es bloqueante para Fase 0.

---

## 8. Estado: LISTO PARA Fase 0

**Una vez Yeral responda Q1-Q5, el blueprint está 100% listo para ejecutar.**

Blueprint completo: 16 archivos, ~5000 líneas de documentación técnica.

No se escribió código. No se tocaron proyectos en producción. No se modificó nada fuera de `yadev-cms/`.

---

## 9. Actualización v3 — análisis competitivo Damos 2026

Fecha: 2026-04-22. Yeral revisó la spec oficial 2026 actualizada de Damos.co (`https://www.damos.co/servicios/diseno-web/ventajas-de-nuestro-cms-gestor-de-contenidos`) + visitó en vivo un cliente real (`https://www.odircertificaciones.com`, admin en `/admin_245/`). Esta ronda cierra gaps funcionales detectados y formaliza el análisis competitivo.

### 9.1. Archivo nuevo

- **`competitive-analysis-damos.md`** — análisis competitivo formal: resumen ejecutivo, matriz feature-by-feature (63 features comparadas), 5 diferenciadores técnicos YaDev vs Damos, comparativa arquitectura ASCII, estrategia go-to-market, links evidenciales. Documento vivo — revisar trimestralmente.

### 9.2. 6 gaps vs Damos 2026 cerrados

| Gap | Solución YaDev | Archivo(s) actualizado(s) |
|-----|----------------|---------------------------|
| **A. Auditor SEO/GEO con IA tiempo real** | Endpoint `POST /v1/tenants/{t}/ai/audit`. DOM analyzer JS-side → Claude Haiku 4.5 con prompt caching → scores SEO + GEO + issues + suggestions_inline. Tabla `seo_audits`. Panel lateral en editor. | `phases/phase-3-ai.md`, `architecture/api-contract.md`, `database/tenant-schema.sql` |
| **B. Generación IA con ADN de marca** | Tabla `brand_voice` (tone, vocabulary_prefer/avoid, sample_texts, industry_context, target_audience). Inyectada como system prompt cacheable en TODA llamada IA. Endpoint `POST /v1/tenants/{t}/ai/generate` con 5 tipos (blog_post, service_description, meta_description, hero_copy, about_paragraph). | `phases/phase-3-ai.md`, `architecture/api-contract.md`, `database/tenant-schema.sql` |
| **C. Traducción multi-idioma con estructura preservada** | Endpoint `POST /v1/tenants/{t}/ai/translate` recibe `blocks[]` ES y devuelve `blocks[]` EN/PT/etc. Preserva Schema.org, alt text, URLs, enum values. Tabla `translations` reescrita (shape estructurada). Bulk translate via Horizon queue con progreso Reverb. | `phases/phase-3-ai.md`, `architecture/api-contract.md`, `database/tenant-schema.sql` |
| **D. Editor fotográfico integrado** | Adelantado a **Fase 1 semana 2** (no Fase 2). Stack: Cropper.js client + Intervention Image server. Modal con tabs Recortar/Rotar/Filtros/Exportar. Endpoint `POST /v1/media/{id}/transform`. | `phases/phase-1-mvp.md`, `architecture/api-contract.md` |
| **E. Estadísticas sin cookies** | GoAccess parseando logs Nginx (cron cada hora → JSON). Endpoint `GET /v1/tenants/{t}/analytics/snapshot`. Tabla `analytics_snapshots` (cache diario). Dashboard con visitas, países, navegadores, keywords, heatmap. Export CSV. | `phases/phase-2-parity.md` (nueva sección semana 9.5), `architecture/api-contract.md`, `database/tenant-schema.sql` |
| **F. Webmail integrado** | **Decisión arquitectónica: Roundcube embebido** vía iframe en `studio.yadev.co/webmail/?tenant=X`. No se construye cliente propio (esfuerzo desproporcionado). Tabla `mail_accounts` en central (no tenant). SSO token de un solo uso. Deep-link a Outlook Web / Gmail según provider. | `phases/phase-2-parity.md` (semana 9.5), `architecture/api-contract.md` |

### 9.3. 4 gaps Odir (sitio vieja-generación, útiles para Colombia)

| Gap | Solución YaDev | Archivo(s) |
|-----|----------------|-----------|
| **Block type `stats`** | Contador animado con icono + color accent por item. 4 layouts (horizontal_bar, grid_2x2, grid_4_col, vertical_stack). Animación counter_up al viewport. | `architecture/api-contract.md` (tabla de block types + schema), `phases/phase-2-parity.md` |
| **Entidad `sedes`/sucursales** | Tabla first-class con name, address, city, department, phone, whatsapp, email, lat/lng, hours JSON, is_main, order. CRUD en `/studio/{t}/sedes`. Endpoints REST. Consumida por `footer_mega`, `contact_locations_map` (nuevo bloque), `page_contact`. | `database/tenant-schema.sql`, `architecture/api-contract.md`, `phases/phase-2-parity.md` |
| **Módulo tracking público** | Plantilla `public_lookup` — cliente configura colección (nombre, campos, source). Bloque `block_lookup_widget` renderiza input+botón. Endpoint público `GET /v1/public/lookup/{tenant}/{collection}/{code}` rate-limited 10/min IP, sin auth. Ejemplo Fase 2: ECOMAG consulta de proyectos. | `phases/phase-2-parity.md`, `architecture/api-contract.md` |
| **Integración pagos (Wompi + Stripe)** | Módulo opcional. Documentado como `pricing_table_checkout` block type. Providers configurables por tenant. Webhooks handler. **Pospuesto a `phase-future.md` / scope on-demand** — no entra a Fase 2 inicial salvo que un tenant lo requiera. | `phases/phase-2-parity.md` (mención), `architecture/api-contract.md` (block type) |

### 9.4. Decisión arquitectónica destacable

**Webmail = Roundcube embebido, NO cliente custom.**

Razonamiento: construir un cliente webmail propio requiere 6-8 semanas full-time (IMAP/SMTP, rendering MIME, adjuntos, contactos, filtros antispam, búsqueda). Roundcube es maduro, extensible, con SSO vía plugin, y todos los usuarios pyme colombianos ya han visto interfaces tipo Roundcube (hosting cPanel lo usa por defecto). Embeber en iframe desde `studio.yadev.co/webmail/` da la experiencia "todo en un panel" sin el costo de desarrollo. Cuando el tenant usa M365 o Google Workspace, deep-link directo a Outlook Web / Gmail en su pestaña — mejor UX que forzar Roundcube para clientes enterprise. Esta decisión ahorra ~1.5 meses de Fase 2 y reduce superficie de mantenimiento.

### 9.5. Estado de bloqueadores

**Ningún nuevo bloqueador.** Las 5 preguntas Q1-Q5 de la sección §3 (dominio yadev.co, VPS KVM2, org GitHub, mapeo DNS cliente, política backups) siguen siendo lo único que bloquea el arranque de Fase 0. Yeral sigue pendiente de responderlas.

### 9.6. Archivos editados en v3

```
yadev-cms/
├── BLUEPRINT.md                               ← §6 ampliado con "Diferenciadores vs competencia colombiana directa (Damos.co)"
├── READY-FOR-REVIEW-v2.md                     ← esta sección §9
├── competitive-analysis-damos.md              ← NUEVO
├── architecture/
│   └── api-contract.md                        ← nuevos endpoints: /media/{id}/transform, /ai/audit, /ai/generate, /ai/translate (estructurado), /brand-voice, /sedes, /analytics/snapshot, /mail-accounts, /public/lookup. Block types table ampliada (stats, contact_locations_map, block_lookup_widget, pricing_table_checkout)
├── database/
│   └── tenant-schema.sql                      ← translations reescrita + nuevas tablas: brand_voice, seo_audits, analytics_snapshots, sedes
└── phases/
    ├── phase-1-mvp.md                         ← semana 2 día 15 ampliada con editor fotográfico (Cropper.js + Intervention)
    ├── phase-2-parity.md                      ← nueva sección "Semana 9.5 — Paridad Damos" (estadísticas GoAccess, webmail Roundcube, block stats, sedes, public_lookup, pagos mencionados)
    └── phase-3-ai.md                          ← reescrita: principio 7 brand_voice, UI asistente + brand voice wizard, endpoint /ai/generate unificado, auditor SEO/GEO tiempo real con arquitectura, traducción estructura-preserving
```

**8 archivos editados + 1 archivo nuevo = 9 archivos tocados.** Ningún código escrito, ningún proyecto en producción modificado, nada fuera de `yadev-cms/`.

### 9.7. Inconsistencias detectadas en v3

- **I7. Endpoint `/ai/audit` vs `/ai/seo-score` legacy.** El endpoint antiguo `POST /api/v1/ai/seo-score` (v1-v2 del blueprint) se mantiene documentado por retrocompatibilidad, pero el nuevo `/ai/audit` es el recomendado porque devuelve scores separados (SEO + GEO) y categoriza issues. Recomendación Fase 3: deprecar `/ai/seo-score` cuando se confirme que nadie depende del shape legacy, o hacer que redirija internamente al nuevo servicio.
- **I8. Endpoint `/ai/translate` tiene dos firmas.** La legacy `{ text, target_lang }` (texto único) y la nueva `{ blocks, source_locale, target_locale, preserve_fields }` (estructurada). Ambas coexisten en Fase 3. Acción: el router Laravel debe discriminar por shape del body o exponerlas como rutas distintas (`/ai/translate-text` vs `/ai/translate-blocks`). Decisión de implementación, no bloqueante.
- **I9. Tabla `translations` cambió de shape entre v1 y v3.** En v1-v2 era row-per-field (`translatable_type`, `field`, `value`). En v3 es row-per-page con `translated_blocks` JSON. Si Yeral ya scaffoldeó en la rama de desarrollo las migrations viejas, hay que reescribir ANTES de Fase 3 (no bloquea Fase 1 ni 2). Recomendación: dejar una nota en `CLAUDE.md` del subproyecto para que el primer comando `php artisan make:migration` use el shape nuevo.
- **I10. `analytics_snapshots` en tenant schema asume que Nginx loggea por tenant.** Pero los sitios cliente viven en Hostinger shared, no en el VPS YaDev. Los logs hay que traerlos vía API Hostinger/cPanel cada día. Esa ingest task no está documentada aún — queda pendiente como detalle operacional de Fase 2. No bloqueante (es un cron job nuevo, no cambio de arquitectura).
- **I11. `mail_accounts` decisión de ubicación.** Los dije en central (no tenant) para poder gestionar cuentas desde super-admin, pero contiene passwords cifradas del tenant. Trade-off: si se hackea la DB central, se expone todo el vault de correo. Alternativa: guardar en tenant DB (aislamiento físico) pero complica el SSO a Roundcube. **Pendiente de decisión final en Fase 2 semana 9.5** — si Yeral prefiere aislamiento más estricto, mover a tenant DB con pequeña complejidad adicional en el proxy Roundcube.

---

_Actualización v3 entregada por project-orchestrator agent. Fin del documento._
