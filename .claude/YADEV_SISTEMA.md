# YADEV SISTEMA — Guía maestra (empieza aquí)

> **Qué es:** el índice único del sistema de generación de sitios de YA Dev. Une los
> 4 motores, los 2 scripts, el estándar y la memoria en un solo flujo: el comando
> `/nuevo-cliente`. Si vas a arrancar un cliente o entender cómo encaja todo, lee
> esto primero y salta al archivo detallado que necesites.
>
> **Regla raíz:** **SISTEMA** (infraestructura) se copia idéntico siempre; **DISEÑO +
> CONTENIDO + LOGO** se generan únicos por cliente con los motores. Nunca se inventan
> datos del cliente.

---

## 1. MAPA DEL SISTEMA — qué archivo hace qué

| Pieza | Archivo | Rol |
|---|---|---|
| 🎨 **Motor de diseño** | `.claude/CREATIVE_ENGINE.md` | ADN visual único: 5 ejes (Director, Composición, Movimiento, Navegación, Narrativa) + idea de autor. Realidad móvil. |
| ✍️ **Motor de contenido** | `.claude/CONTENT_ENGINE.md` | Material del cliente (fuente #1) → investigación de sector → esqueleto completo → `CONTENIDO-PARA-REVISAR.md`. |
| 🏷️ **Motor de logo** | `.claude/LOGO_ENGINE.md` | Reconstruye el logo (A fiel / B mejorada) en vector + paquete de marca (9 variantes + manual). |
| 📐 **Estándar** | `.claude/YADEV_STANDARD.md` | Componentes y entregables OBLIGATORIOS (WhatsApp flotante, scroll-top, panel YaDev, footer + certificaciones Bureau Veritas, SEO, los 8 entregables…). |
| 🧬 **Memoria anti-colisión** | `.claude/PROJECT_DNA_LOG.md` | ADN de cada proyecto. Prohíbe repetir la tripleta Director+Composición+Movimiento y ejes saturados. |
| 🤖 **Comando orquestador** | `.claude/commands/nuevo-cliente.md` | `/nuevo-cliente NOMBRE` — corre los 4 motores en orden + valida. |
| 🔧 **Validador de colisión** | `scripts/check-dna.mjs` | Verifica por máquina que el ADN no choque con el log (exit 0/1/2). |
| 🔧 **Validador Hostinger** | `<proyecto>/scripts/check-hostinger.mjs` | Gate pre-deploy: CSP/SMTP reales, reCAPTCHA test key, placeholders TODO, etc. |
| 📋 **Reglas base** | `.claude/CLAUDE.md` | Identidad, stack, reglas críticas, clientes activos, contacto YaDev. |

> Detalle por cliente: cada proyecto vive en `internal/PROYECTOS/2026/<CLIENTE>/`
> con su `CONTEXTO.md`, `BRIEF.md`, material, `<cliente>-web/` y `brand/`.

---

## 2. EL FLUJO: `/nuevo-cliente NOMBRE`

Un solo comando corre todo, en 5 fases / 13 pasos. **No se escribe código ni contenido
hasta la aprobación (Paso 10).**

```
FASE A · CONTEXTO
  1. Leer carpeta del cliente (todo el material)
  2. Leer los 4 motores + el log

FASE B · CONTENIDO  (CONTENT_ENGINE)
  3. Revisar TODO el material del cliente   ← fuente #1, manda
  4. Investigar el sector (WebSearch, 3-5 empresas reales) ← complemento
  5. Mapear contenido + preparar CONTENIDO-PARA-REVISAR.md

FASE C · DISEÑO  (LOGO_ENGINE + CREATIVE_ENGINE)
  6. Logo: extraer paleta (hex reales) + reconstruir A/B + paquete de marca
  7. Dirección creativa (5 ejes + idea de autor)
  8. check-dna.mjs  → OK / COLISIÓN / SATURADO

FASE D · APROBACIÓN
  9. Mostrar bloques: CONTENIDO (§8) + LOGO (A/B, §5) + DIRECCIÓN CREATIVA (§4)
 10. ESPERAR aprobación explícita  🛑

FASE E · CONSTRUCCIÓN  (solo tras aprobar)
 11. Registrar ADN en PROJECT_DNA_LOG.md
 12. Setup: site-config.ts (+pending+gate), tokens.ts (hex reales),
     paquete de marca en brand/, CONTENIDO-PARA-REVISAR.md
 13. Construir componentes (YADEV_STANDARD) → build → QA → deploy
```

---

## 3. CÓMO ENCAJAN LOS MOTORES

- **CONTENT_ENGINE** decide QUÉ dice el sitio (secciones, textos, servicios) — desde el
  material del cliente + léxico del sector. Honesto: datos duros sin confirmar van a
  `pending` u ocultos.
- **LOGO_ENGINE** convierte el logo crudo (JPEG/IA) en vector profesional → alimenta el
  despiece (si el diseño lo usa) y el paquete de marca/brandbook.
- **CREATIVE_ENGINE** decide CÓMO se ve y se siente — único, sin colisionar (lo valida
  `check-dna`).
- **YADEV_STANDARD** garantiza que NO falte ninguna pieza de sistema (WhatsApp,
  scroll-top, panel YaDev, certificaciones, SEO, los 8 entregables).
- **PROJECT_DNA_LOG** es la memoria que mantiene a los 6 sitios diferentes entre sí.

> Línea que nunca se cruza: los **textos** se crean (borrador del sector, el cliente
> aprueba o cambia). Los **datos duros** (cifras, NIT, certificaciones, clientes) nunca
> se inventan — se piden o se ocultan, y el gate de producción bloquea si faltan.

---

## 4. LOS SCRIPTS

```bash
# Antes de codear — el ADN no debe colisionar:
node scripts/check-dna.mjs --director "X" --composicion "Y" --movimiento "Z" \
  --navegacion "W" --easing "curva" --body-font "Fuente"
#   exit 0 OK · 1 COLISIÓN (cambia un eje principal) · 2 SATURADO (cambia ese eje)

# Antes de deploy — reglas Hostinger:
node <proyecto>/scripts/check-hostinger.mjs       # 0 errores obligatorio
npx pa11y http://localhost:4321 --standard WCAG2AA  # accesibilidad limpia
npx @lhci/cli autorun ...                            # Lighthouse ≥95

# Build de producción (bloquea si quedan pendientes):
DEPLOY_TARGET=production npm run build
```

---

## 5. REGLAS TRANSVERSALES (valen para todo cliente)
- **SISTEMA vs DISEÑO:** SISTEMA (SEO, Hostinger, a11y, PHP mail, site-config, panel
  YaDev) = copiar del boilerplate. DISEÑO/CONTENIDO/LOGO = generado, único.
- **Nunca inventar datos del cliente** → `site-config.pending` + `assertProductionReady()`.
- **Hostinger:** `build.assets:'assets'` (no `_astro/`), sin CSP en `.htaccess`, MIME
  types, logo PNG (no SVG) para OG, `mail()` (no SMTP).
- **Móvil intocable:** WhatsApp button + CTA + `tel:` + carga rápida.
- **Commit por fase**, no al final. Deploy de visual a Railway (proyecto "CMS").

---

## 6. ESTADO ACTUAL (2026-06)

| Cliente | Dominio | Estado | Motores aplicados |
|---|---|---|---|
| ECOMAG | ecomagsas.com | 🟢 Completo | (pre-sistema) |
| Multiservicios P&J | multiserviciospj.com | ⚰️ Retirado → LUQRA | (pre-sistema) |
| LUQRA | luqra.co | 🟡 Build listo (P0) | CREATIVE + STANDARD + site-config |
| **COICEM** | coicem.com | 🟡 En Railway | CREATIVE + CONTENT + STANDARD · LOGO pendiente |
| PORON | poronsas.com | 🔴 Por arrancar | correr `/nuevo-cliente PORON` |

> ⚠️ Restricciones vigentes en el log para el próximo cliente: Navegación **Sticky
> prohibida** (3×), Narrativa **Datos/autoridad saturada** (3×), variar easing/tipografía.
> Tripletas usadas (prohibidas): ver `PROJECT_DNA_LOG.md`.

---

## 7. CHEAT SHEET
- **Cliente nuevo** → `/nuevo-cliente NOMBRE` (lo hace todo).
- **¿Choca el diseño?** → `check-dna.mjs`.
- **¿Listo para Hostinger?** → `check-hostinger.mjs` + Pa11y + Lighthouse.
- **¿Qué no puede faltar?** → `YADEV_STANDARD.md` §10 (checklist).
- **¿Qué le muestro al cliente?** → `CONTENIDO-PARA-REVISAR.md` en su carpeta.
- **¿El logo es un JPEG malo?** → `LOGO_ENGINE.md` (reconstrucción A/B).
