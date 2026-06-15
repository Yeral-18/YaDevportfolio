# CONTEXTO — PORON S.A.S

> Documento de contexto del proyecto web. Estado: 🔴 **por arrancar** (correr `/nuevo-cliente PORON`).
> Ruta: `internal/PROYECTOS/2026/PORON`. Hermano: `BRIEF.md`.
> Todo dato duro no confirmado va marcado **❌ pendiente** y al arrancar pasa a `site-config.ts → pending`
> (bloquea producción). **Nunca inventar** NIT, cifras, certificaciones ni contacto.

---

## 1. DATOS CORPORATIVOS

| Campo | Valor | Estado |
|-------|-------|--------|
| **Razón social** | PORON S.A.S | ✅ |
| **Dominio** | poronsas.com | ✅ (definido, deploy pendiente) |
| **Sector** | Ingeniería integral / O&M industrial / petrolero / eléctrico / ambiental / construcción / maquinaria | ✅ |
| **NIT** | — | ❌ pendiente |
| **Teléfono / WhatsApp** | — | ❌ pendiente |
| **Email corporativo** | — | ❌ pendiente |
| **Dirección / ciudad** | — | ❌ pendiente |
| **Horario** | — | ❌ pendiente |
| **Nº empleados / cifras de trayectoria** | — | ❌ pendiente |
| **Certificaciones ISO** | — | ❌ pendiente (confirmar si tiene) |
| **Proyectos / clientes reales + fotos** | — | ❌ pendiente |

---

## 2. ALCANCE (objeto social — transcripción completa del JPEG)

> Prestación integral de servicios de ingeniería, operación, mantenimiento y consultoría, para obras
> civiles, industriales, eléctricas, electromecánicas, metalmecánicas, ambientales, petroleras y de
> infraestructura en general. Incluye servicios de operación y mantenimiento industrial, limpieza
> técnica especializada, control de corrosión, sistemas eléctricos de alta, media y baja tensión y
> protección industrial. Gestión y remediación ambiental, construcción de obras civiles que incluye
> actividades de adecuaciones, mantenimientos locativos y vías, movimiento de tierra; alquiler de
> maquinaria pesada y equipos industriales. Servicios de apoyo logístico empresarial,
> comercialización de productos minerales y agroindustriales, consultoría técnica e interventoría.

Fuente: `alcance de Poron.jpeg`.

---

## 3. MAPA DE SERVICIOS / ÁREAS (derivado del alcance)

Borrador de agrupación para estructurar la web (a validar con el cliente):

1. **Ingeniería, Operación y Mantenimiento (O&M) industrial**
   - O&M de plantas e infraestructura industrial
   - Limpieza técnica especializada
   - Control de corrosión
2. **Sistemas Eléctricos y Electromecánicos**
   - Alta, media y baja tensión
   - Protección industrial
   - Servicios electromecánicos y metalmecánicos
3. **Sector Petrolero / Industrial**
   - Servicios especializados para industria petrolera y de infraestructura
4. **Gestión y Remediación Ambiental**
   - Gestión ambiental, remediación de sitios
5. **Construcción de Obras Civiles**
   - Adecuaciones, mantenimientos locativos, vías
   - Movimiento de tierra
6. **Alquiler de Maquinaria y Equipos**
   - Maquinaria pesada y equipos industriales
7. **Apoyo Logístico y Comercialización**
   - Apoyo logístico empresarial
   - Comercialización de productos minerales y agroindustriales
8. **Consultoría Técnica e Interventoría**

> Estos grupos son un punto de partida; el cliente puede reordenar/renombrar. El alcance es amplio:
> conviene priorizar 4-6 áreas "featured" para no saturar la home.

---

## 4. LOGO

**Descripción.** Wordmark **"PORON SAS"** en negro/grafito bold; la segunda "O" estilizada como
**anillo azul** (acento de marca); "SAS" en gris claro. Sobre el wordmark, un **emblema geométrico
abstracto** de barras/vigas cruzadas en **perspectiva isométrica**, en azul, negro y verde lima,
que evoca **estructura metálica / construcción / montaje industrial**.

**Archivos (`internal/PROYECTOS/2026/PORON/`):**
- `IMG_9656.JPG.jpeg` — logo original (referencia de marca)
- `alcance de Poron.jpeg` — objeto social
- `brand/logos-envato/poron-01.svg`, `poron-02.png`, `poron-03.svg`, `poron-04.svg`, `poron-05.png`, `poron-06.png` — **6 variantes** descargadas (Envato)

> Igual que en otros clientes: **vectorizar el original** (no redibujar a mano) + wordmark tipográfico.
> Re-extraer la paleta del logo original al arrancar el branding.

---

## 5. PALETA (provisional, del logo)

| Rol | Color (aprox) | Nota |
|-----|---------------|------|
| Primario | **Azul** | Anillo de la "O", acentos |
| Texto / base | **Negro / grafito** | Wordmark |
| Acento | **Verde lima** | Barras del emblema |
| Neutro | **Gris** | "SAS", textos secundarios |

Hex exactos: ❌ pendiente (extraer del logo vectorial al arrancar).

---

## 6. RESTRICCIONES DE DISEÑO (diferenciación obligatoria)

PORON pertenece al **mismo sector** que clientes ya entregados/registrados en el portafolio:
**COICEM** (O&M / energía industrial) y **Multiservicios P&J → LUQRA** (ingeniería integral). Por la
Regla #1 del sistema (diseño único por proyecto) PORON **debe verse de otra agencia**.

Restricciones heredadas del sistema (`.claude/PROJECT_DNA_LOG.md` / motor creativo) a respetar al
correr el RITUAL:

- **Navegación Sticky: PROHIBIDA** (ya usada 3× en el portafolio). Elegir otro patrón de navbar.
- Narrativa de **Datos/autoridad saturada** (stats bar + counters everywhere) ya muy usada en el
  sector → variar el enfoque narrativo.
- NO reutilizar de COICEM/Multiservicios/LUQRA: cursor (engranaje / triángulo dual), hero
  split-screen, servicios en zigzag o bento idéntico, footer mega 5-col con certificaciones.
- Verificar **colisión de tripleta** Director+Composición+Movimiento contra el log antes de codear.

**Aprovechar la marca:** el emblema isométrico de vigas y la "O"-anillo dan pie a un lenguaje visual
propio (estructura metálica, líneas isométricas, ensamblaje) que NO comparte con los otros clientes.

> Nota: las reglas detalladas de SISTEMA (SEO, fixes Hostinger, PHP mail, panel YaDev, 8 entregables)
> son idénticas siempre → copiar del boilerplate. Solo el DISEÑO debe ser único.

---

## 7. AL ARRANCAR (`/nuevo-cliente PORON`)

1. Revisar TODO el material del cliente (logo + alcance) como fuente #1.
2. Correr el RITUAL del motor creativo y registrar el ADN en `PROJECT_DNA_LOG.md`.
3. Solicitar/centralizar datos duros pendientes (sección 1) → mientras no lleguen, van a `pending`.
4. Generar contenido borrador por sector → listar en `CONTENIDO-PARA-REVISAR.md`.
5. Construir los 8 entregables estándar YaDev + SEO + deploy config Hostinger.
