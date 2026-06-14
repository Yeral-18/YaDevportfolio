# YADEV CONTENT ENGINE — Motor de Contenido por Cliente

> **Propósito:** Garantizar que cada sitio tenga TODO el contenido que una web
> corporativa industrial debe tener — usando los datos reales del cliente cuando
> existen, y generándolos a partir de su material cuando no.
>
> **Hermano de** `CREATIVE_ENGINE.md` (que define el DISEÑO). Este define el
> CONTENIDO. Ambos corren dentro del comando `/nuevo-cliente`.
>
> **Regla de oro:** ninguna sección obligatoria queda vacía. Si el cliente no
> dio el dato → se genera provisional a partir de su material → se marca como
> PROVISIONAL → se reemplaza cuando el cliente confirme.

---

## 0. EL PRINCIPIO

Hay dos tipos de empresa que llegan a YA Dev:
- **Las que traen material** (brochure, perfil, fotos, lista de servicios).
- **Las que casi no traen nada** (un logo, un par de frases por WhatsApp).

Ambas necesitan el mismo sitio completo. La diferencia es cuánto hay que
**generar** vs cuánto se **transcribe**. Este motor define:
1. Qué secciones SIEMPRE van (el esqueleto obligatorio).
2. Cómo Claude Code investiga el sector del cliente para no inventar a ciegas.
3. Cómo clasifica lo aportado y genera lo faltante.
4. Cómo marca lo provisional para reemplazo futuro.

---

## 1. REVISIÓN DEL MATERIAL DEL CLIENTE (fuente #1, va primero)

ANTES de investigar el sector, Claude Code revisa EXHAUSTIVAMENTE todo lo que el
cliente envió. El material del cliente es la fuente primaria; la investigación de
sector (Sección 2) solo complementa lo que falte.

### Qué revisar — TODO lo que llegue
El cliente suele enviar material disperso del que sale el contexto real:
- **Alcance / objeto social** — qué hace y hasta dónde llega (clave: define los
  servicios reales y los límites).
- **Perfil corporativo / brochure / portafolio** — historia, servicios, sectores.
- **Certificaciones** (ISO, HSEQ, RUC, registros) — definen capacidades reales y
  qué se puede afirmar con verdad.
- **Experiencia / hoja de vida de la empresa** — años, tipos de proyecto, clientes
  (solo usar como dato si está documentado).
- **Fotos de operación** — qué equipos/trabajos hacen realmente.
- **Mensajes sueltos de WhatsApp/correo** — a veces ahí está el dato que falta.

### Cómo procesarlo
1. Leer cada archivo (PDF, DOCX, imágenes, texto). Si hay PDFs/DOCX, extraer
   su contenido, no asumir.
2. Construir un **mapa de capacidades reales**: qué servicios presta, en qué
   sectores, con qué certificaciones/experiencia documentada.
3. Anotar qué está **documentado y confirmable** (se puede afirmar) vs qué es
   **mención suelta sin respaldo** (va a pendientes para confirmar).
4. Ese mapa es la base de TODO el contenido. La investigación de sector se usa
   solo para completar huecos y validar que no falte ninguna sección típica.

> El alcance del cliente manda. Si el alcance dice que hace 4 cosas, el sitio
> habla de esas 4 — no se le agregan servicios del sector que el cliente no
> presta solo porque los competidores los tienen.

---

## 2. INVESTIGACIÓN DE SECTOR (complementa al material del cliente)

ANTES de generar contenido faltante, Claude Code investiga el sector real del
cliente — para completar lo que el material del cliente no cubra y validar que el
sitio no omita ninguna sección típica del rubro.

### Pasos
1. Tomar la **actividad económica real** del cliente (del material revisado en
   Sección 1, o de su código CIIU si está).
2. **Buscar en internet 3-5 empresas reales del MISMO sector** (preferir
   colombianas, mejor aún de la misma región — Santander/Magdalena Medio).
   Usar el web_search del entorno.
3. **Extraer de esos sitios qué secciones/ítems usan** y el LÉXICO del rubro:
   cómo estructuran servicios, qué muestran en "nosotros", qué certificaciones
   exhiben, qué prueba social usan, qué CTAs, qué términos técnicos emplean.
4. **Anotar hallazgos** en un bloque `INVESTIGACIÓN DE SECTOR` que se muestra al
   usuario y se guarda en el CONTEXTO.md del cliente. Incluir las URLs revisadas.

> Objetivo: que el contenido generado sea **realista y específico del sector**,
> con el vocabulario real del rubro — no genérico. La investigación da el léxico
> y la estructura; el material del cliente (Sección 1) da los datos y el alcance.

### Qué NO hacer con la investigación
- NO copiar textos de los competidores (plagio). Se extraen ESTRUCTURA, ÍTEMS y
  LÉXICO, no prosa.
- NO agregar servicios/certificaciones/clientes que el cliente no tenga. La
  investigación informa la ESTRUCTURA y el VOCABULARIO; los DATOS y el ALCANCE
  son solo del cliente (Sección 1 manda).

---

## 3. ESQUELETO OBLIGATORIO — lo que SIEMPRE va

Toda web corporativa industrial de YA Dev tiene estas secciones. Si el cliente
no aporta el contenido, se genera provisional (ver Secciones 5–6). El ORDEN y el
DISEÑO de estas secciones lo decide el CREATIVE_ENGINE; aquí solo se define que
el CONTENIDO debe existir.

### Núcleo (nunca falta)
| Ítem | Qué contiene | Si falta dato del cliente |
|---|---|---|
| **Hero / propuesta de valor** | Qué hace la empresa + para quién + CTA | Generar de 1 frase del cliente + sector |
| **Nosotros / Quiénes somos** | Historia, qué hacen, dónde operan | Generar de material; si no hay historia, redactar neutra con datos verificables |
| **Misión** | Propósito de la empresa | Generar plantilla del sector, marcar PROVISIONAL |
| **Visión** | A dónde apunta | Generar plantilla del sector, marcar PROVISIONAL |
| **Valores** | 4-6 principios | Generar set estándar del sector (seguridad, calidad, compromiso…) |
| **Servicios / Portafolio** | Lista detallada de lo que ofrecen | EJE CRÍTICO — ver Sección 4 |
| **Contacto** | Teléfono, email, WhatsApp, ubicación, horario, formulario | Datos reales obligatorios; nunca inventar contacto |
| **Footer** | Resumen, links, datos legales, ISO, copyright | Compuesto de lo anterior |

### Confianza / Prueba social (van si aplican al sector)
| Ítem | Cuándo incluirlo | Si falta |
|---|---|---|
| **Certificaciones ISO / HSEQ** | Sector industrial/petrolero casi siempre | Si el cliente las tiene, mostrarlas; si no, NO inventar — omitir o "en proceso" solo si el cliente lo confirma |
| **Clientes / Aliados** | Si el cliente da nombres/logos | Placeholder de estructura, oculto hasta tener datos reales |
| **Proyectos / Experiencia** | Si hay casos reales | Igual: estructura lista, oculta sin datos |
| **Estadísticas / Cifras** | Años, proyectos, cobertura | NUNCA inventar números → `pending` en site-config + gate de producción |
| **Política HSEQ / Calidad** | Sector petrolero/industrial lo espera | Generar plantilla del sector, marcar PROVISIONAL |
| **Sectores atendidos / Cobertura** | Común en el rubro | Generar de la región del cliente |

### Legales / Operativos (SISTEMA — siempre)
| Ítem | Nota |
|---|---|
| **Datos de empresa** (razón social, NIT) | NIT a `pending` si no se tiene |
| **Política de tratamiento de datos** | Obligatoria en Colombia (Ley 1581/2012) si hay formulario — generar plantilla |
| **Aviso de cookies** | Si se usan analytics |
| **WhatsApp + tel: + ubicación** | Conversión móvil, intocable |

---

## 4. SERVICIOS — el eje más importante

Es la sección que más varía por empresa y la que el cliente más necesita bien
hecha. Reglas:

1. **Si el cliente da la lista de servicios** → transcribir, ordenar, y para cada
   uno redactar una descripción de 2-3 frases (el cliente rara vez las da; se
   generan a partir del nombre del servicio + lo que hacen empresas del sector).
2. **Si el cliente da solo nombres sueltos** → agrupar en categorías lógicas del
   sector (la investigación de Sección 2 dice cómo se agrupan normalmente).
3. **Si el cliente casi no especifica** → proponer el portafolio típico del
   sector (de la investigación) y marcar TODO como PROVISIONAL para que el
   cliente confirme/recorte.
4. Cada servicio: nombre + descripción corta + (opcional) ícono + (opcional)
   detalle. Marcar `featured` los 2-3 principales (eso lo usa el diseño).

> Las descripciones generadas describen capacidades GENÉRICAS del servicio, no
> afirman experiencia específica que el cliente no haya confirmado. "Realizamos
> mantenimiento de tanques de almacenamiento" ✓ · "15 años haciendo X" ✗ (dato).

---

## 5. CONTENIDO ESPECÍFICO DEL SECTOR — no genérico

Esta es la diferencia entre relleno y trabajo real. El contenido provisional NO
es una plantilla universal; se construye desde la **actividad económica concreta
del cliente** + lo extraído de los sitios reales del sector (Sección 2).

### Cómo se genera cada pieza (con ejemplo)

**Mal (genérico — PROHIBIDO):**
> "Somos una empresa comprometida con la calidad y la excelencia, ofreciendo
> soluciones integrales para nuestros clientes."
(Sirve para una panadería o un banco — no dice nada del cliente.)

**Bien (específico del sector real):**
> Cliente: mantenimiento industrial petrolero (COICEM).
> Investigación: las empresas del rubro mencionan paradas de planta, integridad
> de equipos, disponibilidad operativa, continuidad de campo.
> Resultado provisional:
> "Ejecutamos mantenimiento predictivo y correctivo de equipos estáticos y
> rotativos en facilidades de producción, minimizando paradas no programadas y
> sosteniendo la continuidad operativa de campos de hidrocarburos."

La segunda versión usa el vocabulario y las preocupaciones reales del sector
(que Claude Code sacó de los sitios investigados), aplicadas a lo que el cliente
declaró hacer. Sigue siendo PROVISIONAL (el cliente confirma la voz final), pero
es **un borrador útil y creíble**, no un placeholder de relleno.

### Reglas de generación
1. **Anclar en la actividad económica declarada** del cliente (su CIIU / lo que
   dijo que hace). El contenido describe ESO, no genericidades.
2. **Usar el léxico del sector** extraído de la investigación (términos,
   preocupaciones, tipos de servicio que aparecen en los referentes).
3. **Describir capacidades, no logros.** "Realizamos X" (capacidad del servicio,
   verdadera para quien lo ofrece) ✓ · "Líderes con 200 proyectos" (logro/cifra
   no confirmada) ✗.
4. **Misión/Visión/Valores**: redactar una versión plausible y específica del
   rubro y la región del cliente — no la plantilla "ser los mejores en…". Marcar
   PROVISIONAL para que el cliente ajuste su voz.

### Regla de oro
- **Verdad sobre relleno.** Nunca atribuir al cliente logros, cifras, clientes o
  certificaciones que no haya confirmado. Tan grave como placeholders en SEO.
- **Provisional ≠ falso ≠ genérico.** El borrador es verdadero en general,
  específico del sector, y pendiente solo de la voz oficial del cliente.
- **Español de Colombia**, tono profesional del sector, sin marketing vacío.
- **Coherente con el diseño.** El tono acompaña al Director creativo (Brutalist =
  copy directo y técnico; Aesop = copy sobrio y editorial).

---

## 6. CÓMO MARCAR LO CREADO (puede quedarse o reemplazarse)

El contenido generado NO es "relleno temporal" por definición. Es un **borrador
profesional específico del sector** que el cliente puede: (a) aprobar tal cual y
quedarse, (b) ajustar, o (c) reemplazar con su versión. El sistema lo trata como
"creado por YaDev, pendiente de revisión del cliente" — no como error a corregir.

Tres mecanismos combinados:

1. **En `site-config.ts`** → datos DUROS faltantes (NIT, cifras, año fundación)
   van en `pending: { ... }` con `null`. Estos SÍ son obligatorios y el gate
   `assertProductionReady()` bloquea producción si quedan. (Una cifra no se
   "inventa bonito" — o existe o se oculta.)
2. **En el contenido** (`content-fallback.ts` o equivalente) → cada bloque
   creado por YaDev lleva un marcador:
   ```ts
   // CREADO POR YADEV — borrador desde [alcance del cliente + sector].
   // Estado: pendiente revisión cliente (puede quedarse si lo aprueba).
   mision: "...",
   ```
3. **El entregable para el cliente** → `CONTENIDO-PARA-REVISAR.md` (ver Sección 7).
   Es la lista que TÚ le pasas al cliente.

> Diferencia clave: las CIFRAS y DATOS duros sin confirmar se ocultan/bloquean
> (no se inventan). Los TEXTOS (misión, descripciones de servicio, nosotros) se
> crean específicos del sector y se ofrecen al cliente para aprobar o cambiar.

---

## 7. EL ENTREGABLE: `CONTENIDO-PARA-REVISAR.md`

Este es el archivo que pediste — el que le pasas al cliente. Se crea en la
carpeta del cliente. Formato: para cada pieza creada, muestra QUÉ se creó, DE
DÓNDE salió, y la pregunta directa al cliente (¿lo dejamos o lo cambias?).

```markdown
# CONTENIDO DE [CLIENTE] — para tu revisión

Creamos el contenido del sitio a partir de tu alcance, tu material y las
prácticas de tu sector. Revisa cada punto: si te gusta, lo dejamos tal cual;
si quieres ajustarlo o tienes tu propia versión, lo reemplazamos.

## ✅ Creado a partir de TU material (alta confianza)
| Sección | Qué pusimos | Basado en | ¿Lo dejas o lo cambias? |
|---|---|---|---|
| Servicios | [lista real] | tu alcance / brochure | ☐ dejar ☐ cambiar |
| Nosotros | [resumen] | tu perfil corporativo | ☐ dejar ☐ cambiar |

## 📝 Creado como borrador del sector (revisa la voz)
| Sección | Qué pusimos | Basado en | ¿Lo dejas o lo cambias? |
|---|---|---|---|
| Misión | "[texto]" | tu actividad + sector | ☐ dejar ☐ cambiar |
| Visión | "[texto]" | tu actividad + sector | ☐ dejar ☐ cambiar |
| Valores | [lista] | estándar del sector | ☐ dejar ☐ cambiar |

## ❓ Necesitamos que CONFIRMES (datos que no inventamos)
Estos NO los pusimos porque son datos tuyos que no podemos suponer. El sitio
no sale a producción sin ellos (o los ocultamos si prefieres):
- [ ] NIT
- [ ] Años de experiencia / año de fundación
- [ ] Cifras: nº de proyectos, plantas, cobertura, etc.
- [ ] Certificaciones ISO/HSEQ vigentes (¿cuáles y números?)
- [ ] Clientes/proyectos que podamos mostrar (con permiso)
- [ ] Logo en vector (.ai/.svg) si el diseño lo necesita

## 🔒 Lo que ya estaba confirmado por ti
- Contacto, ubicación, horario, WhatsApp: [valores reales]
```

### Reglas del entregable
- **3 categorías claras:** lo creado desde su material (alta confianza), lo
  creado como borrador de sector (revisar voz), y lo que DEBE confirmar (datos
  duros que no se inventan).
- **Lenguaje de cliente, no técnico.** Nada de "site-config.pending" ni "tokens".
- **Cada texto creado se muestra completo** en el .md para que el cliente lo lea
  y decida — no "generamos una misión", sino la misión textual.
- **Marcar con casillas** para que el cliente responda fácil (dejar/cambiar).
- Cuando el cliente responde: reemplazar lo que pidió cambiar, quitar el marcador
  de lo que aprobó (pasa a confirmado), y llenar los datos duros en site-config.

---

## 8. SALIDA DEL MOTOR DE CONTENIDO (lo que se muestra al usuario)

Dentro del ritual de `/nuevo-cliente`, tras revisar material e investigar, mostrar:

```
═══════════════════════════════════════════════
  CONTENIDO — [CLIENTE]
═══════════════════════════════════════════════
  MATERIAL DEL CLIENTE (fuente #1)
   Recibido:      [qué archivos/datos envió]
   Alcance real:  [qué hace y hasta dónde, según su material]
   Confirmable:   [servicios/certs/experiencia documentados]
───────────────────────────────────────────────
  INVESTIGACIÓN DE SECTOR (complemento)
   Sector:        [actividad económica]
   Referentes:    [3-5 URLs revisadas]
   Léxico/ítems:  [vocabulario y secciones típicas del rubro]
───────────────────────────────────────────────
  MAPEO DE CONTENIDO
   Desde su material:  [secciones con alta confianza]
   Borrador de sector: [misión/visión/valores/desc. servicios]
   A confirmar (datos):[NIT, cifras, certs, clientes → no inventados]
   Oculto sin datos:   [proyectos/clientes/cifras]
───────────────────────────────────────────────
  ENTREGABLE → CONTENIDO-PARA-REVISAR.md
   [el listado que el fundador le pasa al cliente:
    qué se creó, de dónde, y dejar/cambiar por cada ítem]
═══════════════════════════════════════════════
```

Esperar aprobación del usuario antes de escribir el contenido en el proyecto.
