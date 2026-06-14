# INVESTIGACIÓN DE SECTOR — COICEM S.A.S

> **Qué es:** Paso 2 del CONTENT_ENGINE. Se revisaron empresas reales con el MISMO
> alcance/actividad económica de COICEM (O&M industrial · petrolero/petroquímico ·
> energía · construcción/montaje) para extraer **estructura y léxico del rubro** —
> NO para copiar prosa ni atribuir a COICEM datos/clientes que no tiene.
>
> **Fecha:** 2026-06-14 · **Método:** búsqueda + revisión de sitios en vivo.

---

## 1. REFERENTES REVISADOS (5 empresas reales del sector)

| Empresa | Por qué es referente | Alcance que coincide con COICEM |
|---|---|---|
| **OMIA** (ex-Skanska Colombia) · `omia.com.co` | **El gemelo más cercano.** Ingeniería + Construcción + O&M en hidrocarburos, energía, infraestructura, industrial y minería. ISO 9001/14001/45001 + **NORSOK S-006** + CCS. Clientes: Ecopetrol, Ocensa, Cenit, Hocol, Geopark, Mansarovar. | Casi 1:1. Mismas 3 líneas (O&M / Ing.&Construcción) + mismas certificaciones (ISO + NORSOK). |
| **Tecnioriente** · Barrancabermeja | Mismo territorio (Magdalena Medio). Mantenimiento industrial, fabricación/reparación de líneas de flujo, montajes mecánicos, plataformas. | Mantenimiento + montaje mecánico/electromecánico. |
| **Confipetrol Colombia** | Mantenimiento integral eléctrico + mecánico + instrumentación. Especialistas en **paradas de planta**. | Mantenimiento multidisciplinario + instrumentación. |
| **Magnex Group** | Operación, mantenimiento, proyectos, construcción y **paradas de planta**; piping y equipos rotativos; ingeniería Brownfield en refinerías de Colombia. | Integralidad O&M + paradas + equipos rotativos. |
| **Inemec S.A.S** | Mantenimiento integral de campos de gas (Cusiana/Cupiagua, Ecopetrol): facilidades de producción, sistemas eléctricos, operaciones de superficie. | Operación de campo + facilidades + superficie. |

Referente internacional de apoyo (gestión): **Stork** (capacidades de operaciones).

---

## 2. LÉXICO REAL DEL RUBRO (vocabulario que SÍ usan)

Términos exactos extraídos de los referentes — usar este vocabulario hace que el
copy de COICEM suene del sector y no genérico:

- **Paradas de planta** (shutdowns / turnarounds) — concepto central, lo usan TODOS.
- **Integridad de activos** (asset integrity).
- **Equipos estáticos y rotativos** (recipientes, intercambiadores · bombas, turbinas, compresores).
- **Mantenimiento predictivo con técnicas nombradas:** **termografía, análisis de vibraciones, ultrasonido**. ← COICEM hoy solo dice "predictivo" sin nombrarlas.
- **Facilidades de producción · operaciones de superficie · líneas de flujo / piping.**
- **Disponibilidad · confiabilidad · continuidad operativa** (los 3 KPIs que vende el sector).
- **Modelo de gestión de servicio · indicadores de gestión (KPIs).**
- **Estándares de gestión de activos:** además de ISO + NORSOK → **PASS 55 / ISO 55000** y **ISO 14224** (confiabilidad). COICEM puede mencionar "gestión de activos".
- **Brownfield** (intervención sobre instalación existente en operación).

---

## 3. ESTRUCTURA QUE USA EL SECTOR (secciones de sus webs)

De OMIA (la más completa) y los demás:
1. Hero (carousel o claim fuerte).
2. **Líneas de negocio agrupadas:** O&M · Ingeniería & Construcción · **Suministro/Procurement** · HSEQ · Sostenibilidad/RSE.
3. **Marco "Cinco Ceros"** (compromiso HSEQ central y memorable): cero accidentes · cero incidentes ambientales · cero faltas éticas · cero pérdidas · cero defectos. ← patrón distintivo y fuerte del rubro.
4. **Métricas/cifras:** barriles/día operados · personal O&M contratado · años de experiencia · n.º de mantenimientos/paradas ejecutadas · departamentos con presencia.
5. Prueba social: **logos de clientes** (operadoras) + proyectos.
6. Certificaciones (ISO + NORSOK) — a veces como sello, a veces en HSEQ.
7. Contacto + cobertura geográfica (departamentos).
8. Footer.

---

## 4. RECOMENDACIONES ACCIONABLES PARA COICEM

Cada una es una mejora de CONTENIDO (borrador de sector, el cliente aprueba/ajusta).
Ninguna inventa datos duros.

| # | Mejora | Dónde | Tipo |
|---|---|---|---|
| R1 | Nombrar las técnicas predictivas reales: **termografía, vibraciones, ultrasonido** en el área Mantenimiento. | `Areas.astro` (mantenimiento) + `CONTENIDO-PARA-REVISAR.md` | Léxico (borrador sector) |
| R2 | Usar el trío **disponibilidad · confiabilidad · continuidad** como promesa de valor en hero/nosotros. | `Hero.astro` subtítulo · MisionVision | Léxico |
| R3 | Adoptar un **marco de compromiso HSEQ tipo "Cero"** (cero accidentes / cero incidentes ambientales) — encaja con NORSOK y con la estética brutalist de panel/telemetría. Reemplaza o complementa los 6 valores genéricos. | Sección valores/HSEQ + `CONTENIDO-PARA-REVISAR.md` | Borrador sector |
| R4 | Ajustar las **celdas de telemetría del hero** a las que el sector sí exhibe: en vez de "MW mantenidos" (más eléctrico), considerar **años de experiencia · paradas ejecutadas · disponibilidad % · personal técnico**. Siguen siendo `pending` hasta que el cliente dé cifras reales. | `Hero.astro` telemetry + `site-config.telemetry` | Estructura (datos siguen pending) |
| R5 | Mencionar **"gestión de activos" (ISO 55000 / PASS 55)** como marco, si el cliente lo maneja — sube autoridad técnica. Confirmar antes de afirmarlo. | Nosotros/HSEQ | A confirmar con cliente |
| R6 | Añadir línea de **"Suministro de equipos y personal técnico"** como servicio visible (hoy está enterrado dentro de Infraestructura). El sector lo trata como línea propia. | `Areas.astro` infraestructura | Estructura |
| R7 | Definir **público objetivo real**: operadoras tipo Ecopetrol/Cenit/Ocensa. No afirmar como clientes sin permiso, pero orientar el copy a ese comprador. | Tono general | Estrategia |

---

## 5. QUÉ NO HACER (límites del CONTENT_ENGINE)

- ❌ NO copiar prosa de OMIA/Confipetrol/etc. (plagio) — solo estructura y léxico.
- ❌ NO atribuir a COICEM los **clientes** (Ecopetrol, Ocensa…) ni las **cifras**
  (barriles/día, años) de los referentes. Esos son datos duros → `pending`.
- ❌ NO afirmar certificaciones extra (PASS 55, ISO 55000) sin que el cliente las tenga.
- ✅ SÍ usar el vocabulario del rubro y la estructura típica como borrador que el
  cliente aprueba o ajusta (queda en `CONTENIDO-PARA-REVISAR.md`).

---

## 6. FUENTES

- OMIA — https://omia.com.co/ · https://omia.com.co/lineas-de-negocios/servicios/
- Tecnioriente — brochure Campetrol (Barrancabermeja)
- Confipetrol — https://confipetrol.com/Colombia/mantenimiento/
- Magnex Group — https://magnexgroup.com/
- Inemec — contrato O&M Cusiana/Cupiagua (Ecopetrol)
- Stork — https://www.stork.com/es/capacidades/gestion/operaciones
- Contexto Refinería Barrancabermeja — Ecopetrol / Vanguardia (paradas de planta 2025)
