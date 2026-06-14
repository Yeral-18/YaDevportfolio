# PROJECT DNA LOG — Registro de ADN Visual

> **Función:** Memoria de combinaciones creativas usadas. El motor
> (`CREATIVE_ENGINE.md`) consulta este archivo ANTES de cada proyecto y PROHÍBE
> repetir la tripleta `Director + Composición + Movimiento`.
>
> **Mantenimiento:** Claude añade una fila ANTES de codear cada cliente nuevo.
> Nunca se borra una fila. Si un proyecto se rediseña, se añade versión nueva.
>
> **Datos:** extraídos de los CONTEXTO.md reales de cada proyecto (no suposiciones).

---

## ⚠️ CASO ESPECIAL: MISMA EMPRESA, REBRAND

**Luqra ES el rebrand de Multiservicios P&J** (misma operación, mismos clientes,
mismo contacto). Aun así, **decisión del fundador: Luqra DEBE diferenciarse
fuerte de Multiservicios.** Por eso ambos ocupan filas separadas en la tabla de
colisión y NO pueden compartir la tripleta Director+Composición+Movimiento.

Riesgo a vigilar: como Luqra heredó archivos de Multiservicios, tiende a
arrastrar firma visual y datos. Dos defensas:
1. El log de abajo marca lo que YA comparten para forzar separación futura.
2. El \`site-config.ts\` (archivo hermano) mata el bug de contacto heredado (B5).

---

## TABLA MAESTRA DE COLISIÓN

Ninguna fila puede repetir la combinación de las 3 primeras columnas.

| Cliente | Director | Composición | Movimiento | Navegación | Narrativa | Idea de autor |
|---|---|---|---|---|---|---|
| **ECOMAG S.A.S** | Patagonia | Centrado clásico | Orgánico | Sticky | Datos/autoridad | 7 hojas SVG flotantes + cursor hoja |
| **Multiservicios P&J** | Stripe | Split-screen 55/45 | Mecánico/preciso | Sticky | Showcase/portafolio | Cursor engranaje + zigzag L-R + wave SVG |
| **Luqra S.A.S** | Linear | Bento asimétrico | Físico (lerp) | Sticky | Datos/autoridad | Cursor triángulo dual + dot-grid parallax + diagonal cut |
| **COICEM S.A.S** | Brutalist | Editorial/columnas | Tipográfico | Sidebar vertical | Datos/autoridad | Despiece explotado del logo (engranaje+llave+destornillador) que se re-ensambla al scroll + cursor crosshair/calibre |

### Lectura de colisiones actuales
- Tripletas únicas ✓ — ninguna se repite. El sistema está sano en el eje creativo.
- **Pero hay 3 ejes secundarios saturados** que delatan "mismo diseñador":
  - **Navegación: Sticky ×3** → el PRÓXIMO proyecto DEBE usar otra (floating
    pill, sidebar, overlay, dock). Es la señal #1 que rompe la Regla #1.
  - **Tipografía: Plus Jakarta + Inter ×3** → es defendible si es decisión de
    marca del cliente, pero para el 4º proyecto conviene cambiar al menos el body.
  - **Easing spring \`cubic-bezier(0.34,1.3,0.64,1)\` ×3** → mismo "feel" de
    rebote en los tres. Variar la curva en el próximo.
- **Luqra vs Multiservicios (el par crítico):** diferenciación REAL lograda en
  hero (centrado vs split), servicios (bento vs zigzag), cursor (triángulo vs
  engranaje), transición (diagonal vs wave), color (azul/naranja vs azul/verde).
  ✓ Cumple el mandato "diferenciarse fuerte". Solo comparten navbar y tipografía.

---

## FICHAS DETALLADAS

### ECOMAG S.A.S — \`ecomagsas.com\` · 🟢 Completo
- **Industria:** Ingeniería civil + gestión ambiental
- **Paleta:** Verde #1B5E20 + Azul #0277A8 + lima #7CB342 · CTA naranja #E65100
- **Tipografía:** Plus Jakarta Sans + Inter
- **Hero:** Full-height, gradiente sobre imagen, 7 hojas SVG con keyframes únicos
- **Servicios:** Grid 3-col con reveal escalonado
- **Cards:** Sólidas blancas, elevación en hover
- **Transición:** Wave SVG orgánica
- **Footer:** 4 columnas + certificaciones Bureau Veritas
- **Cursor:** Hoja verde animada
- **Movimiento:** Spring bounce + float loops

### Multiservicios P&J S.A.S — \`multiserviciospj.com\` · 🟢 En producción
- **Industria:** Ingeniería e industria de servicios integrales (Magdalena Medio)
- **Paleta:** Azul #0089D0 + Verde ambiental #005B32 + lima #8CC63F
- **Tipografía:** Plus Jakarta Sans + Inter
- **Hero:** Split-screen 55% texto / 45% visual, gradient azul, iconos flotantes, herramientas cruzadas
- **Servicios:** Zigzag alternado L-R, 6 filas, número 01-06
- **Clientes:** Carousel infinito CSS 25s, fade edges
- **Transición:** Wave SVG (\`WaveTransition.astro\`)
- **Footer:** CTA banner + 4 columnas + sello Bureau Veritas
- **Cursor:** Engranaje mecánico (\`GearCursor.svelte\`)
- **Movimiento:** spring 0.34,1.3 / smooth — preciso, técnico
- **6 servicios:** Transporte carga · Obras civiles · Izaje · Remediación ambiental · Transición energética (solar) · Alquiler maquinaria
- **Predecesor de:** Luqra

### Luqra Ingeniería y Soluciones S.A.S — \`luqra.co\` · 🟡 Build listo (5 P0)
- **Industria:** Ingeniería integral (transporte, construcción, energías renovables, ambiental, comercio)
- **Esquema cromático:** 80/20 azul/naranja — el naranja nunca domina, es el acento memorable
- **Paleta:** brand-blue #0A2A66/#123C8C/#1F5FBF + brand-orange #FF6A00/#FF8C1A/#FFA533 · navy dark #060F24/#050B1A
- **Tipografía:** Plus Jakarta Sans + Inter + JetBrains Mono (IDs/datos técnicos)
- **Hero:** Full-height centrado, dot-grid bg con parallax, textura tiremark, diagonal cut inferior (NO wave)
- **Servicios:** Bento grid asimétrico (2 featured 50/50 + 3 regular 33/33/33) sobre navy #060F24
- **Proyectos:** Masonry 2-col, cards alternados azul/naranja, IDs P001-P005
- **Stats:** Counter-up con IntersectionObserver, diagonal cuts
- **Cursor:** Triángulo dual (azul outline + naranja fill) con lerp, hover scale, click squash (\`TriangleCursor.svelte\`)
- **Footer:** Mega-footer 5-col + CTA banner + diagonal cut
- **Movimiento:** spring 0.34,1.3 / smooth / sharp + lerp físico en cursor
- **5 áreas:** Transporte y Logística (featured) · Construcción Civil (featured) · Energías Renovables · Gestión Ambiental · Comercio Internacional
- **Login corporativo:** Microsoft Entra ID branded (navy + tire-track, calidad Apple/Stripe)
- **Rebrand de:** Multiservicios P&J

### COICEM S.A.S — \`coicem.com\` · 🟡 En Railway (staging)
> Marca = **COICEM** (el logo dice "COICEM SAS"). Dominio correcto comprado: **coicem.com**
> (`coisem.com` fue un typo del cliente, queda en desuso). La carpeta del repo aún se
> llama `COISEM/` — renombrar a `COICEM/` pendiente (opcional).
- **Industria:** Mantenimiento industrial especializado · energía · petróleo/petroquímico · construcción · infraestructura
- **Paleta (EXTRAÍDA del logo real con PIL, no supuesta):**
  - Azul primario \`#025199\` · azul medio \`#023F7E\` · azul oscuro \`#002657\` · tint \`#8EB9DC\`
  - Naranja primario \`#F79204\` · naranja claro \`#FFA222\` · ámbar/arco \`#E38325\`
  - Metal/grafito (engranaje) \`#313F50\` / \`#4B6881\` · fondo casi-negro \`#000E27\` · highlight \`#F6FCFD\`
- **Esquema:** base oscura grafito/negro (del fondo del logo) · azul \`#025199\` estructural (80%) · naranja \`#F79204\` hi-vis de seguridad (~10%)
- **Tipografía:** Display Archivo Expanded · Body IBM Plex Sans + IBM Plex Mono (specs/part-numbers) — NO Inter
- **Hero:** "title block" brutalista full-screen, rejilla con reglas visibles + tira de telemetría mono (datos desde \`site-config.ts\`, cero inventados)
- **Composición:** Editorial/columnas (rejilla técnica visible, estética hoja de datos/plano)
- **Movimiento:** Tipográfico, reveals por bloque · easing easeInOutQuint \`cubic-bezier(0.83,0,0.17,1)\` — sin rebote (NO spring 0.34,1.3)
- **Navegación:** Sidebar vertical, riel-índice numerado (01–05 áreas) con scroll-spy (NO Sticky)
- **Cursor:** crosshair/calibre (⛔ NO engranaje — prohibido, es de Multi, aunque el logo de COICEM tenga gear)
- **Idea de autor:** despiece explotado del logo (engranaje+llave+destornillador) con leader lines + part-numbers; al scroll se re-ensambla → "desarmar, calibrar, armar"
- **check-dna:** ✅ OK (exit 0) — tripleta única · Sidebar 0 usos previos · easing ✓ · body ≠ Inter

---

## PROYECTOS PENDIENTES (sin ADN asignado aún)

| Cliente | Dominio | Industria | Acción |
|---|---|---|---|
| PORON S.A.S | poronsas.com | Por definir | Correr RITUAL al arrancar |

> ⚠️ Para PORON — restricciones derivadas del estado actual del log:
> - **Navegación:** PROHIBIDO Sticky (3×). Sidebar ya lo usa COICEM → preferible
>   floating pill / fullscreen overlay / dock / scroll-spy.
> - **Tripletas usadas (prohibidas):** Patagonia+Centrado+Orgánico ·
>   Stripe+Split+Mecánico · Linear+Bento+Físico · **Brutalist+Editorial/columnas+Tipográfico (COICEM)**.
> - **Narrativa:** Datos/autoridad ya 3× → PORON debe variar (Problema→Solución,
>   Storytelling, Conversacional, Inmersivo).
> - **Sugerencias sin colisión:**
>   - Mailchimp + Diagonal + Fluido + Floating pill + Conversacional
>   - Aesop + Overlap/capas + Mínimo + Dock + Problema→Solución
>   - Apple + Asimétrico + Cinemático + Fullscreen overlay + Inmersivo

---

## RESERVA DE EJES POR AGOTAMIENTO

**Directores usados:** Patagonia (1) · Stripe (1) · Linear (1) · Brutalist (1)
**Composiciones usadas:** Centrado (1) · Split-screen (1) · Bento (1) · Editorial/columnas (1)
**Movimientos usados:** Orgánico (1) · Mecánico (1) · Físico (1) · Tipográfico (1)
**Navegaciones usadas:** Sticky (3) ← 🔴 SATURADO — prohibida · Sidebar vertical (1)
**Narrativas usadas:** Datos/autoridad (3) ← 🔴 SATURADO — PORON debe variar · Showcase (1)
**Tipografía body:** Inter (3) · IBM Plex Sans (1) ← COICEM rompió la racha
**Easing principal:** spring 0.34,1.3 (3) · easeInOutQuint 0.83,0,0.17,1 (1) ← COICEM varió
