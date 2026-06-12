# BRIEF — COICEM S.A.S

> Brief de cliente para el futuro sitio web. Estado: 🔴 sin web (solo logo + propuestas).
> Al arrancar: correr el RITUAL (`.claude/CREATIVE_ENGINE.md`) y registrar ADN en `PROJECT_DNA_LOG.md`.
> ⚠️ Navegación **Sticky PROHIBIDA** (ya usada 3×). Tripletas prohibidas: Patagonia+Centrado+Orgánico · Stripe+Split+Mecánico · Linear+Bento+Físico.

---

## Identidad

| Campo | Valor |
|-------|-------|
| **Nombre** | Coicem S.A.S (Coicem) |
| **Dominio** | **coicem.com** (activo, comprado — el correcto). `coisem.com` fue typo del cliente, en desuso |
| **Sector** | Operación, mantenimiento, construcción, energía e infraestructura industrial |
| **Tagline (logo)** | "Servicio Mantenimiento Especializado" |
| **Logo** | Engranaje + herramientas (llave, destornillador) en círculo |
| **Paleta (aprox, del logo)** | Azul oscuro `#003D82` + Naranja/dorado `#FF9900` |

### Servicios (de las propuestas)
Construcción, montaje, operación y mantenimiento de infraestructura eléctrica, civil y mecánica · Instrumentación industrial · Energías renovables · Mantenimiento especializado sector petrolero/petroquímico/energético · Consultoría técnica · Gestión ambiental y seguridad industrial · Suministro de equipos y personal técnico.

---

## MISIÓN

En Coicem diseñamos y ejecutamos soluciones integrales de operación, mantenimiento, construcción, energía e infraestructura, respaldadas por servicios técnicos avanzados, gestión ambiental responsable y actividades industriales conexas. Nuestro propósito es optimizar la productividad y sostenibilidad de los proyectos del sector industrial, energético y civil.

## VISIÓN

Coicem para el año 2030, sea reconocida como la empresa líder en Colombia en soluciones integrales de ingeniería, energía e infraestructura industrial, destacándonos por nuestra excelencia operativa, innovación constante y compromiso con la sostenibilidad. Aspiramos a ser el aliado estratégico preferido en proyectos de gran impacto, aportando conocimiento técnico de vanguardia y prácticas responsables que impulsen el desarrollo sostenible del país y fortalezcan el crecimiento del sector industrial y energético.

---

## Material disponible en la carpeta
- Logo (PNG) + documento de alcance (JPEG)
- 4 propuestas/presupuestos PDF: `COICEM_9k.pdf`, `COICEM_14k.pdf`, `COICEM_45k.pdf`, `COICEM_norsok.pdf`

## Pendiente del cliente (antes de producción)
1. **🔴 LOGO VECTORIAL ORIGINAL (.ai/.svg/.pdf)** — CRÍTICO. La idea de autor (despiece SVG del
   engranaje+herramientas) NO se puede hacer desde el JPEG de WhatsApp (mapa de bits plano). El
   diseñador del logo debió entregarlo vectorial. Mientras llega, YaDev prototipa con un SVG
   redibujado (reconstrucción aproximada) que el cliente DEBE validar antes de que sea el héroe.
2. Contacto real: tel / email / WhatsApp / dirección / horario.
3. NIT, nº empleados, ¿certificaciones ISO?
4. Telemetría del hero: % continuidad operativa, MW mantenidos, plantas intervenidas (números reales).
5. Proyectos/clientes reales + fotos de planta.

> Todo lo anterior vive en `coicem-web/src/lib/site-config.ts` → `pending`. El build de producción
> (`DEPLOY_TARGET=production`) se bloquea hasta resolverlos. La paleta de `tokens.ts` es **provisional v1**
> (extraída del JPEG); re-extraer cuando llegue el logo original.

> Nota de naming (RESUELTO): la empresa es **COICEM** (el logo dice "COICEM SAS") y el dominio correcto
> comprado es **coicem.com**. `coisem.com` fue un error del cliente y queda en desuso. La carpeta del repo
> aún se llama `COISEM/` — renombrar a `COICEM/` es opcional (cambiaría rutas; dejar por ahora).
> Usar siempre **COICEM** / **coicem.com** en web, SEO, brandbook y site-config.
