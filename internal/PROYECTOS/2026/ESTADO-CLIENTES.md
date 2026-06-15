# ESTADO DE CLIENTES — YaDev 2026

> Índice maestro de los proyectos de cliente en `internal/PROYECTOS/2026/`.
> Última actualización: 2026-06-14. Estado y datos tomados de cada `CONTEXTO.md` / `BRIEF.md`.
> "Logos" = nº de archivos en `brand/logos-envato/` del proyecto.

| Cliente | Dominio | Sector | Estado | Logos | Notas |
|---------|---------|--------|--------|-------|-------|
| **ECOMAG S.A.S** | ecomagsas.com | Ingeniería civil + ambiental | ✅ Completo | 0 | Producción. Carpeta activa `ECOMAG02/`. Verde `#1B5E20` + azul `#0277A8`, hero con hojas SVG flotantes, cursor hoja. |
| **Multiservicios P&J S.A.S** | multiserviciospj.com | Ingeniería e industria de servicios integrales | ⚰️ Retirado | 0 | **Reemplazado por LUQRA** (rebrand 2026-05). Conservado como referencia histórica; su ADN visual queda bloqueado (no reutilizar split-screen / cursor engranaje / zigzag). |
| **LUQRA Ingeniería y Soluciones S.A.S** | luqra.co | Ingeniería integral: transporte, construcción, energías renovables, ambiental, comercio | 🟡 En desarrollo | 11 | Rebrand de Multiservicios. Build listo en staging (Railway), **bloqueado por 5 P0** (datos placeholder + form PHP necesita Hostinger). Paleta azul/naranja 80/20. `luqra-01..11`. |
| **COICEM S.A.S** | coicem.com | Operación, mantenimiento, construcción, energía e infraestructura industrial | 🟡 En desarrollo | 13 | Sitio brutalist (navbar horizontal) en Railway; logo vectorizado. Pendiente: logo vectorial original + datos del cliente. `coicem-01..09` + 4 SVG sueltos (Envato/emblema). `coisem.com` fue typo en desuso. |
| **PORON S.A.S** | poronsas.com | Ingeniería integral / O&M industrial / petrolero / eléctrico / ambiental / construcción / maquinaria | 🔴 Por arrancar | 6 | Solo logo + alcance. Correr `/nuevo-cliente PORON`. `poron-01..06`. Debe diferenciarse de COICEM/LUQRA (mismo sector): Sticky nav prohibida, variar narrativa de datos. Datos duros pendientes. |

---

## Leyenda de estado
- ✅ **Completo** — en producción, entregado.
- 🟡 **En desarrollo** — build existe, pendiente de bloqueadores / datos / deploy final.
- 🔴 **Por arrancar** — solo material de marca (logo + alcance); sin web aún.
- ⚰️ **Retirado** — descontinuado o reemplazado.

## Notas
- Todos comparten el **stack estándar** (Astro 5 + Svelte 5 + Tailwind 3 + PHP `mail()` en Hostinger).
- **Sector saturado:** ECOMAG, LUQRA, COICEM y PORON son del mismo rubro (ingeniería/O&M industrial).
  Por la Regla #1 (diseño único), cada uno debe verse de otra agencia — el motor creativo
  (`.claude/CREATIVE_ENGINE.md` + `PROJECT_DNA_LOG.md`) evita colisiones de ADN visual.
- **Datos duros** (NIT, cifras, contacto, certificaciones) nunca se inventan: van a `pending` y
  bloquean producción hasta que el cliente los confirme.
- Documentación por cliente: `ECOMAG02/` (PROMPT) · `MULTISERVICIOS P&J/CONTEXTO.md` ·
  `LUQRA/CONTEXTO.md` · `COISEM/BRIEF.md` · `PORON/BRIEF.md` + `PORON/CONTEXTO.md`.
