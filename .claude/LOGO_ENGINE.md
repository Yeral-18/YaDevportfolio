# YADEV LOGO ENGINE — Reconstrucción de Logo + Paquete de Marca

> **Propósito:** Convertir el logo que el cliente trae (normalmente hecho con IA,
> JPEG de WhatsApp, baja resolución, con defectos) en un **logo vectorial
> profesional** y un paquete de marca completo — manteniendo el diseño
> reconocible pero a calidad de estudio.
>
> **Hermano de** `CREATIVE_ENGINE.md` (diseño web) y `CONTENT_ENGINE.md`
> (contenido). Corre dentro de `/nuevo-cliente`, en la Fase de diseño, ANTES de
> extraer la paleta y de cualquier despiece.

---

## 0. EL PRINCIPIO — qué significa "reconstruir un logo"

Un logo hecho con IA suele llegar con defectos reales: tipografía deformada,
engranajes de dientes irregulares, simetrías rotas, degradados sucios, bordes
pixelados, fondo quemado por compresión de WhatsApp. **Calcar esos defectos en
vector sería heredar la baja calidad.**

Reconstruir profesionalmente NO es calcar píxel a píxel. Es:
- **Conservar** lo que hace reconocible la marca: los elementos (engranaje, llave,
  destornillador, wordmark…), su disposición, sus colores, su concepto.
- **Corregir** lo que un diseñador corregiría: geometría, alineación, simetría,
  grosores, curvas, kerning del wordmark, limpieza de color.
- **Entregar** vectores limpios (SVG/paths) escalables a cualquier tamaño, aptos
  para web, impresión, bordado, favicon y — si el diseño lo pide — despiece.

> Meta correcta: **"inconfundiblemente el mismo logo, a calidad profesional"** —
> NO "idéntico píxel a píxel con sus defectos".

---

## 1. DOS VERSIONES SIEMPRE (el cliente elige)

Por cada cliente se generan DOS reconstrucciones y se le muestran lado a lado:

### Versión A — Reconstrucción fiel
Mismo diseño, solo limpiado y vectorizado. Se respetan proporciones y formas tal
como están; solo se elimina pixelado, ruido de compresión y se cierran paths.
Para el cliente apegado a "así es mi logo, no lo cambies".

### Versión B — Reconstrucción mejorada
Lo mismo, pero corrigiendo los defectos evidentes de la IA: regularizar el
engranaje (dientes iguales, centrado), alinear elementos, equilibrar el wordmark,
afinar kerning, limpiar degradados, mejorar contraste. El concepto y los
elementos no cambian; la ejecución sube de nivel.

### Cómo se presenta al cliente
- Render PNG de ambas, mismo tamaño, sobre fondo claro y oscuro.
- Una nota breve por versión: qué se respetó / qué se mejoró en la B.
- Pregunta directa: ¿A (fiel) o B (mejorada)? La elegida se vuelve el logo oficial
  y alimenta el resto del paquete.

> Si el cliente no responde, por defecto se construye el sitio con la **B**
> (mejorada) marcada como pendiente de confirmación — nunca se bloquea el avance,
> pero el logo final queda en `pending` hasta que el cliente elija.

---

## 2. PROCESO DE RECONSTRUCCIÓN (lo que hace Claude Code)

1. **Abrir y analizar** el archivo original (view del JPEG/PNG). Identificar:
   elementos, colores (extracción de hex pixel a pixel), tipografía aproximada
   del wordmark, defectos presentes.
2. **Inventariar piezas**: listar cada elemento como objeto independiente
   (ej. engranaje, llave, destornillador, arco/swoosh, wordmark, "S.A.S").
   Esto sirve también para el despiece si el diseño lo usa.
3. **Redibujar en SVG** cada pieza con paths limpios:
   - Formas geométricas (engranajes, círculos) → construir con geometría exacta,
     no trazar a mano. Un engranaje de N dientes se genera regular.
   - Wordmark → si la fuente es identificable, usar la real o la más cercana;
     si no, redibujar las letras como paths. Anotar qué fuente se usó/aproximó.
   - Color → aplicar la paleta extraída (hex reales), planos o degradados limpios.
4. **Generar las dos versiones** (A fiel / B mejorada) del paso anterior.
5. **Validar**: el SVG debe verse nítido a 32px (favicon) y a tamaño grande;
   paths cerrados; sin elementos sueltos; peso optimizado (correr SVGO).

> Honestidad técnica: la reconstrucción de un wordmark con fuente desconocida es
> una APROXIMACIÓN. Anotarlo. Si el cliente tiene la fuente original o el archivo
> vectorial del diseñador, eso siempre gana — pedirlo en el entregable.

---

## 3. PAQUETE COMPLETO DE MARCA (entregable por cliente)

Una vez el cliente elige A o B, se genera el paquete completo. Estructura en la
carpeta del cliente, `brand/`:

### 3.1 Logo — variantes
| Variante | Uso | Formato |
|---|---|---|
| **Principal full color** | Web, documentos | SVG + PNG (1x/2x/3x) |
| **Horizontal** (isotipo + wordmark lado a lado) | Headers anchos, firmas | SVG + PNG |
| **Vertical/apilado** | Espacios cuadrados | SVG + PNG |
| **Isotipo solo** (símbolo sin texto) | App, favicon, sello | SVG + PNG |
| **Wordmark solo** (texto sin símbolo) | Pie de página, menciones | SVG + PNG |
| **Monocromo negro** | Documentos B/N, fax, sellos | SVG + PNG |
| **Monocromo blanco** (negativo) | Sobre fondos oscuros/foto | SVG + PNG |
| **Favicon** | Navegador | ICO + PNG 32/180/512 |
| **OG/redes** | Compartir en WhatsApp/redes | PNG 1200×630 |

> Recordar regla Hostinger: el logo del navbar para OG de WhatsApp debe ser PNG,
> no SVG (WhatsApp no renderiza SVG en preview).

### 3.2 Manual de uso (mini brandbook)
Un `manual-marca.html` (o PDF) con:
- **Logo y sus variantes** — cuándo usar cada una.
- **Área de protección** — espacio mínimo libre alrededor del logo.
- **Tamaño mínimo** — px mínimos para que sea legible.
- **Paleta** — hex/RGB/CMYK de los colores de marca (extraídos del logo).
- **Tipografía** — display + body del sistema (las del sitio).
- **Usos correctos e incorrectos** — no deformar, no recolorear, no rotar, no
  añadir sombras/efectos, no cambiar proporciones.
- **Versiones sobre fondo** — claro, oscuro, foto.

> Esto es lo que hace que "también les quede a ellos un logo profesional": el
> cliente recibe un sistema de marca usable, no solo un archivo.

### 3.3 Aprovechar lo que ya existe
YA Dev ya produce brandbook/firma/membrete/tarjeta (visto en ECOMAG,
Multiservicios, Luqra). El logo reconstruido ALIMENTA esos entregables — no se
generan aparte. El paquete de marca y el brandbook del sitio son el mismo flujo.

---

## 4. DERECHOS Y EXPECTATIVA (importante decirlo al cliente)

- El logo reconstruido es una **versión vectorial profesional del concepto que el
  cliente aportó**. El cliente es dueño de su marca.
- Si el logo IA original copió o se parece a una marca existente, la
  reconstrucción NO arregla ese problema legal — solo mejora la ejecución.
  Si Claude Code detecta que el logo se parece a una marca conocida, avisar al
  fundador (no es asesoría legal, es una alerta).
- La reconstrucción de tipografía es aproximada salvo que el cliente dé la fuente.
- Siempre pedir el **archivo original del diseñador** (.ai/.svg/.eps/.pdf) en el
  `CONTENIDO-PARA-REVISAR.md`: si existe, es mejor fuente que cualquier
  reconstrucción.

---

## 5. SALIDA DEL MOTOR DE LOGO (lo que se muestra al usuario)

Dentro del ritual de `/nuevo-cliente`, en la fase de diseño:

```
═══════════════════════════════════════════════
  LOGO — [CLIENTE]
═══════════════════════════════════════════════
  Original recibido:  [archivo, formato, calidad detectada]
  Defectos IA:        [lista: dientes irregulares, kerning, etc.]
  Piezas inventariadas: [engranaje, llave, wordmark…]
  Paleta extraída:    [hex reales del logo]
───────────────────────────────────────────────
  RECONSTRUCCIÓN
   Versión A (fiel):     [render] — respeta todo, solo limpia
   Versión B (mejorada): [render] — corrige [defectos]
   → ¿Cuál prefieres, A o B? (default B si no respondes)
───────────────────────────────────────────────
  PAQUETE A GENERAR (tras elegir)
   Variantes: full/horizontal/isotipo/wordmark/mono/favicon/OG
   Manual de marca: área protección, tamaños, paleta, usos
   Alimenta: brandbook, firma, membrete, tarjeta
───────────────────────────────────────────────
  PENDIENTE → CONTENIDO-PARA-REVISAR.md
   - [ ] ¿Tienes el archivo original del logo (.ai/.svg/.pdf)?
   - [ ] ¿Fuente del wordmark? (si la conoces)
   - [ ] Elegir versión A o B
═══════════════════════════════════════════════
```

Esperar elección/aprobación antes de generar el paquete completo.
