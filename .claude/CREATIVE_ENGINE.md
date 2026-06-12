# YADEV CREATIVE ENGINE — Motor de Dirección Creativa

> **Propósito:** Garantizar que cada proyecto tenga un ADN visual irrepetible.
> Este archivo NO es un menú de opciones. Es un *generador de combinaciones*
> con memoria. Antes de escribir UNA sola línea de componente, Claude debe
> completar el RITUAL (Sección 4) y registrar el resultado en `PROJECT_DNA_LOG.md`.
>
> **Regla de oro:** Si una combinación de ejes ya existe en el log → está PROHIBIDA.
> No se reutiliza. Se genera otra.

---

## 0. POR QUÉ ESTE MOTOR EXISTE

El prompt `PROMPT_ECOMAG_WEBSITE.md` es un excelente **spec técnico** pero un
**molde visual**: navbar sticky + hero (badge + H1 + 2 CTA) + grid 3-col +
footer 4-columnas. Cualquier cliente que pase por ese molde sale siendo un
ECOMAG con otros colores. Eso viola la Regla Crítica #1 del sistema.

La solución NO es tener 10 heroes predefinidos (eso es otro molde, más largo).
La solución es **descomponer el diseño en ejes independientes** y obligar a
elegir una combinación nueva cada vez, registrándola para que nunca se repita.

Con 5 ejes de ~7 opciones cada uno hay **>16.000 combinaciones base**, antes
de contar las variaciones internas. La repetición deja de ser un riesgo.

---

## 1. SEPARACIÓN FUNDAMENTAL: SISTEMA vs DISEÑO

Todo lo que Claude produce cae en UNA de dos categorías. Nunca se mezclan.

| | SISTEMA (idéntico siempre) | DISEÑO (único siempre) |
|---|---|---|
| **Qué es** | Infraestructura invisible | Decisiones creativas visibles |
| **Ejemplos** | SEO, Schema.org, accesibilidad WCAG AA, fixes Hostinger, PHP mail(), DNS, performance, tokens sincronizados, panel YaDev | Hero, composición, grids, navegación, movimiento, transiciones, cursor, personalidad tipográfica |
| **Regla** | Copiar tal cual del boilerplate. NO innovar. | Generar combinación nueva. PROHIBIDO copiar. |
| **Dónde vive** | `/design-system/` + reglas Hostinger | Este motor + `PROJECT_DNA_LOG.md` |

> Si dudas si algo es Sistema o Diseño: ¿el usuario final lo *ve* como estética?
> → Diseño. ¿Es plomería técnica que debe funcionar igual siempre? → Sistema.

---

## 2. LOS 5 EJES CREATIVOS

Cada proyecto elige UN valor por eje. La combinación de los 5 = el ADN del sitio.

### EJE 1 — DIRECTOR CREATIVO (la filosofía de marca)
Define la *actitud* general. No se copia el sitio de la referencia, se adopta su **principio**.

| Director | Principio rector | Se nota en |
|---|---|---|
| **Apple** | Reducción extrema, el producto es el héroe, aire infinito | Whitespace masivo, 1 idea por pantalla, tipografía grande |
| **Stripe** | Precisión técnica con calidez, gradientes sutiles, detalle obsesivo | Microcopys, degradados suaves, código como decoración |
| **Linear** | Velocidad, oscuridad premium, foco monocromático | Dark base, 1 acento, transiciones instantáneas |
| **Patagonia** | Honestidad, naturaleza, textura humana | Fotografía real grande, tonos tierra, editorial honesto |
| **Mailchimp** | Personalidad lúdica, ilustración, anti-corporativo | Ilustración custom, color audaz, formas imperfectas |
| **Aesop** | Lujo silencioso, editorial, restricción cromática | Beige/crema, serif fina, márgenes de revista |
| **Brutalist** | Crudeza intencional, sistema visible, anti-pulido | Bordes duros, mono, sin sombras, grid expuesto |
| **Editorial/Kinfolk** | Diseño de revista, jerarquía tipográfica dramática | Columnas, drop caps, fotografía a sangre |

### EJE 2 — SISTEMA DE COMPOSICIÓN (cómo se organiza el espacio)

| Composición | Descripción | Rompe el molde de |
|---|---|---|
| **Centrado clásico** | Todo al centro, simétrico | *(es el molde por defecto — usar solo si ningún otro proyecto lo tiene)* |
| **Split-screen** | Pantalla dividida 50/50 o 60/40 | El hero centrado |
| **Asimétrico** | Pesos visuales desbalanceados a propósito | La simetría predecible |
| **Bento grid** | Mosaico de cajas de distinto tamaño | El grid uniforme 3-col |
| **Editorial/columnas** | Maquetación de revista, ancho de medida | El full-width plano |
| **Diagonal/oblicuo** | Secciones cortadas en ángulo | Las bandas horizontales |
| **Overlap/capas** | Elementos que se montan unos sobre otros | El flujo lineal apilado |
| **Canvas/scroll-horizontal** | Desplazamiento lateral en zonas | El scroll vertical único |

### EJE 3 — SISTEMA DE MOVIMIENTO (cómo se siente la interacción)

| Movimiento | Carácter | Técnica |
|---|---|---|
| **Cinemático** | Lento, dramático, revelaciones | Scroll-driven, parallax, clip-reveal |
| **Fluido** | Suave, líquido, continuo | Smooth scroll (Lenis), easing largos |
| **Mecánico/preciso** | Snappy, instantáneo, técnico | Transiciones cortas, sin bounce |
| **Orgánico** | Natural, respirante, vivo | Float loops, noise, spring bounce |
| **Tipográfico** | El texto es el que se mueve | Split-text, kinetic type, marquee |
| **Mínimo** | Casi nada se mueve, solo lo esencial | Fade simple, sin decoración animada |
| **Físico** | Inercia, peso, magnetismo | Magnetic cursor, drag, momentum |

### EJE 4 — PATRÓN DE NAVEGACIÓN (cómo se recorre)

| Navegación | Descripción |
|---|---|
| **Sticky tradicional** | Barra arriba que se queda *(molde por defecto)* |
| **Floating pill** | Cápsula flotante centrada o abajo |
| **Sidebar vertical** | Navegación lateral fija |
| **Fullscreen overlay** | Menú que cubre toda la pantalla al abrir |
| **Minimal/hamburguesa siempre** | Solo ícono, incluso en desktop |
| **Contextual/scroll-spy** | Indicador lateral de sección activa |
| **Dock** | Barra estilo macOS abajo |

### EJE 5 — NARRATIVA VISUAL (el hilo conductor del recorrido)

| Narrativa | El usuario siente que... |
|---|---|
| **Problema → Solución** | ...se le resuelve un dolor, paso a paso |
| **Storytelling/scroll-journey** | ...avanza por una historia mientras baja |
| **Showcase/portafolio** | ...el trabajo habla por sí solo |
| **Datos/autoridad** | ...está ante expertos (números, certificaciones) |
| **Inmersivo/experiencia** | ...entró a un mundo, no a una web |
| **Conversacional/humano** | ...habla con personas, no con una empresa |

---

## 3. MAPA INDUSTRIA → DIRECTORES SUGERIDOS (no obligatorio)

Punto de partida, NO regla. Si el último cliente de esa industria ya usó el
sugerido, salta al siguiente.

| Industria | Directores afines | Evitar |
|---|---|---|
| Construcción/Ingeniería | Brutalist, Stripe, Linear | Aesop (demasiado suave) |
| Ambiental/Forestal | Patagonia, Editorial, Aesop | Brutalist (frío) |
| Tecnología/SaaS | Linear, Stripe, Apple | Editorial (lento) |
| Salud | Apple, Aesop, Mailchimp | Brutalist (agresivo) |
| Legal/Consultoría | Aesop, Editorial, Apple | Mailchimp (informal) |
| Transporte/Logística | Linear, Stripe, Brutalist | Aesop |
| Restaurante/Food | Editorial, Mailchimp, Patagonia | Linear (frío) |
| Inmobiliaria | Aesop, Editorial, Apple | Brutalist |
| Eléctrico/RETIE | Stripe, Linear, Apple | Mailchimp |

---

## 4. EL RITUAL (obligatorio antes de codear)

Claude NO escribe ningún componente hasta completar y mostrar esto al usuario:

```
═══════════════════════════════════════════════
  DIRECCIÓN CREATIVA — [NOMBRE CLIENTE]
═══════════════════════════════════════════════
  Industria:        [...]
  Director:         [Eje 1] — porque [razón ligada a la marca]
  Composición:      [Eje 2] — rompe con [proyecto previo]
  Movimiento:       [Eje 3]
  Navegación:       [Eje 4]
  Narrativa:        [Eje 5]
───────────────────────────────────────────────
  Hero concept:     [1 frase describiendo el hero ÚNICO]
  Anti-patrón:      [qué del proyecto anterior NO repito]
───────────────────────────────────────────────
  VERIFICACIÓN DE COLISIÓN (programática)
  $ node scripts/check-dna.mjs --director "..." \
      --composicion "..." --movimiento "..." \
      --navegacion "..." --easing "..."
  Resultado:  [ OK / COLISIÓN → regenerar / SATURADO → cambiar eje ]
───────────────────────────────────────────────
  VERIFICACIÓN DE SATURACIÓN (ejes secundarios)
  Navegación:  ¿ya saturada en el log (🔴)?     [ SÍ → cambiar / NO ]
  Easing:      ¿misma curva que proyectos previos? [ SÍ → variar / NO ]
  Tipografía:  ¿mismo body que todos los previos?  [ SÍ → considerar variar / NO ]
═══════════════════════════════════════════════
```

### Pasos
1. Leer `PROJECT_DNA_LOG.md` completo — incluyendo la sección RESERVA DE EJES
   POR AGOTAMIENTO (los 🔴 son prohibiciones, los 🟡 son advertencias).
2. Elegir los 5 ejes. Consultar el mapa industria (Sección 3) como punto de partida.
3. **Verificar colisión programáticamente:** ejecutar `node scripts/check-dna.mjs`
   con la propuesta. La tripleta `Director + Composición + Movimiento` NO puede
   repetirse, y los ejes marcados 🔴 en el log están prohibidos. Si el script
   devuelve COLISIÓN o SATURADO, regenerar. NO confiar en verificación a ojo.
4. Mostrar el bloque del ritual al usuario y esperar confirmación (o auto-aprobar
   si el usuario pidió flujo autónomo).
5. Registrar en `PROJECT_DNA_LOG.md` ANTES de escribir componentes: fila en la
   TABLA MAESTRA + ficha detallada + actualizar RESERVA DE EJES.
6. Recién entonces, codear — usando el spec técnico de `PROMPT_ECOMAG_WEBSITE.md`
   SOLO para la parte de SISTEMA (SEO, accesibilidad, fixes), nunca para copiar
   su estructura visual.

> **Enforcement:** este ritual está empaquetado como slash command
> `/nuevo-cliente NOMBRE` (`.claude/commands/nuevo-cliente.md`). Usar SIEMPRE
> el comando para iniciar clientes — evita que el ritual se salte en sesiones
> largas o flujos autónomos.

---

## 5. CÓMO USAR EL PROMPT DE ECOMAG A PARTIR DE AHORA

`PROMPT_ECOMAG_WEBSITE.md` se reclasifica. Ya NO es "el prompt de un sitio".
Se parte en dos:

- **Lo que se conserva como SISTEMA (reutilizable tal cual):** Secciones 1.1–1.6
  (datos, contacto, SEO), Sección 4.4 (GPU), 4.5 (touch), 4.6 (SSR guard),
  y todo lo de SEO/Schema/accesibilidad/Hostinger.
- **Lo que se marca como EJEMPLO-NO-MOLDE (solo ECOMAG):** Sección 3 (orden de
  componentes), 5.3–5.x (navbar sticky, hero con hojas, grids, footer 4-col).
  Estas son las decisiones de UN proyecto. Para el próximo cliente, el motor
  genera otras. Nunca se copian salvo que el motor las regenere por azar Y el
  log confirme que no colisionan.

> En la práctica: cuando arranques un cliente nuevo, NO abras el prompt de ECOMAG
> y reemplaces valores. Corre el RITUAL primero, define el ADN, y usa el prompt
> solo como checklist de "qué piezas de SISTEMA no olvidar".

---

## 6. REALIDAD MÓVIL — dónde vive la diferenciación

**El contexto real:** los clientes de YA Dev son empresas industriales
colombianas. La mayoría de sus visitantes llega por **WhatsApp en un celular**,
no por desktop. El motor genera ADN creativo, pero el ADN debe sobrevivir
al móvil sin sacrificar conversión.

### Regla de adaptación por eje

| Eje | En desktop | En móvil (≤768px) |
|---|---|---|
| **Navegación** | Vive la diferenciación completa (pill, sidebar, dock, overlay) | Casi todas colapsan a hamburguesa/overlay — esto es NORMAL y esperado. La personalidad se conserva en la *animación de apertura* y el *estilo del overlay*, no en el patrón |
| **Composición** | Bento, split, diagonal a pleno | Bento → apila inteligente (featured arriba) · Split → apila texto-primero · Diagonal → reduce el ángulo, no lo elimines · Scroll-horizontal → conviértelo en carousel táctil con scroll-snap |
| **Movimiento** | Completo | Reducir intensidad, respetar `prefers-reduced-motion`, NUNCA bloquear el scroll. Cursor personalizado: solo desktop (ya es la práctica: `client:idle` + detección touch) |
| **Tipografía** | Escala completa | `clamp()` siempre; titulares "objeto de diseño" deben seguir legibles a 360px |

### Lo intocable en móvil (es SISTEMA, no diseño)

Independiente del ADN creativo, en móvil SIEMPRE:
- **WhatsApp button** visible y accesible (es el canal #1 de conversión)
- **CTA principal** alcanzable sin scroll excesivo (primer viewport o sticky)
- **Teléfono clickeable** (`href="tel:"`)
- **Carga rápida**: hero sin video pesado en móvil, imágenes responsive
- **Touch targets ≥44px** (ya está en las reglas de código)

> Test de aceptación: el ADN creativo se evalúa en desktop; la conversión se
> evalúa en móvil. Un sitio premiable que no convierte en móvil es un fracaso
> para estos clientes.

---

## 7. NIVEL AWWWARDS — el 10% extra

Para pasar de "agencia premium" a "premiable", añadir AL MENOS UNO de estos por
proyecto (distinto cada vez, registrar cuál):

- **Una idea visual de autor:** un detalle que solo tiene sentido para ESTA marca
  (ECOMAG = hojas; un transporte = trazado de ruta animado; un legal = sello
  lacrado que se imprime al hacer scroll).
- **Un momento de sorpresa:** una transición o revelación que el usuario no espera.
- **Tipografía como protagonista:** un titular tratado como objeto de diseño, no
  como texto.
- **Coherencia obsesiva:** cursor, loader, scrollbar, selección de texto, 404 —
  todos hablan el mismo idioma de marca.

Lo que NUNCA da Awwwards: gradient buttons clonados, cards con la misma sombra,
hero centrado genérico, animaciones decorativas sin propósito. (Ya está en la
Regla #2 "No parecer IA" — esto la operacionaliza.)
