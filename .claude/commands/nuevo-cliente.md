---
description: Inicia un cliente nuevo con RITUAL de diseño + contenido obligatorio. Uso - /nuevo-cliente NOMBRE_CLIENTE
allowed-tools: Read, Glob, Grep, WebSearch, Bash(node:*)
---

# NUEVO CLIENTE — RITUAL OBLIGATORIO (Diseño + Contenido)

Cliente a iniciar: **$ARGUMENTS**

Ejecuta estos pasos EN ORDEN. PROHIBIDO escribir, crear o editar cualquier
componente (.astro, .svelte, .css, .ts de UI) o contenido antes de completar
el paso 10 (aprobación del usuario).

---

## FASE A — CONTEXTO

### Paso 1 — Leer contexto del cliente
Lee TODO el contenido de `internal/PROYECTOS/2026/$ARGUMENTS/` (CONTEXTO.md,
material, logo, colores, servicios, brochure, fotos). Si la carpeta no existe
o está casi vacía, DETENTE y pide los datos mínimos: actividad económica,
servicios, colores/logo, contacto, ciudad.

### Paso 2 — Leer los motores
Lee completos:
- `.claude/CREATIVE_ENGINE.md` (5 ejes de diseño, mapa industria, regla móvil)
- `.claude/CONTENT_ENGINE.md` (esqueleto de contenido, investigación de sector)
- `.claude/LOGO_ENGINE.md` (reconstrucción de logo + paquete de marca)
- `.claude/PROJECT_DNA_LOG.md` (ADN de proyectos previos + saturación)

---

## FASE B — CONTENIDO (CONTENT_ENGINE)

### Paso 3 — Revisar TODO el material del cliente (fuente #1)
Lee exhaustivamente todo lo que el cliente envió: alcance/objeto social, perfil,
brochure, certificaciones, experiencia, fotos, mensajes. Extrae contenido de
PDFs/DOCX (no asumir). Construye el mapa de capacidades REALES: qué hace, hasta
dónde llega, qué está documentado vs qué es mención sin respaldo. El alcance del
cliente manda sobre la investigación.

### Paso 4 — Investigación de sector (complemento)
Identifica la actividad económica. Con WebSearch, busca 3-5 empresas reales del
MISMO sector (preferir colombianas, Santander/Magdalena Medio). Extrae SECCIONES,
ÍTEMS y LÉXICO del rubro (no copiar prosa). Anota las URLs. Sirve para completar
huecos y dar vocabulario real, no para agregar servicios que el cliente no presta.

### Paso 5 — Mapeo de contenido + entregable
Clasifica según CONTENT_ENGINE:
- Secciones desde el material del cliente (alta confianza).
- Borrador específico del sector (misión/visión/valores/desc. servicios) — con
  léxico real del rubro, NO genérico, anclado al alcance del cliente.
- Datos a confirmar (NIT, cifras, certs, clientes) → NO inventar, van a `pending`
  u ocultos.
Prepara el contenido de `CONTENIDO-PARA-REVISAR.md` (el listado dejar/cambiar que
el fundador le pasa al cliente).

---

## FASE C — DISEÑO (CREATIVE_ENGINE)

### Paso 6 — Logo + paleta (LOGO_ENGINE)
Lee `.claude/LOGO_ENGINE.md`. Abre el logo real del cliente en su carpeta:
- Extrae los colores (hex) del archivo, no de memoria.
- Si es un JPEG/foto de baja calidad o hecho con IA, inventaría las piezas,
  detecta defectos, y prepara DOS reconstrucciones vectoriales: A (fiel) y B
  (mejorada). Se muestran al cliente para que elija (default B si no responde).
- La versión elegida es el logo oficial y alimenta el paquete de marca completo
  (variantes + manual) y, si el diseño lo usa, el despiece.
- Marca en `CONTENIDO-PARA-REVISAR.md`: pedir archivo original (.ai/.svg/.pdf),
  fuente del wordmark, y elección A/B.

### Paso 7 — Generar dirección creativa
Elige UN valor por eje (Director, Composición, Movimiento, Navegación,
Narrativa) + idea de autor ligada a la marca. Usa el mapa industria como
punto de partida.

### Paso 8 — Verificación programática de colisión
Ejecuta:
```bash
node scripts/check-dna.mjs --director "X" --composicion "Y" --movimiento "Z" --navegacion "W" --easing "curva" --body-font "Fuente"
```
- COLISIÓN → vuelve al Paso 7 con otra combinación.
- SATURADO → cambia ese eje (Sticky está saturado; varía easing/tipografía).
- Solo continúa con OK.

---

## FASE D — APROBACIÓN

### Paso 9 — Mostrar AMBOS bloques al usuario
Presenta junto:
1. El bloque CONTENIDO (investigación de sector + mapeo + pendientes) —
   formato CONTENT_ENGINE Sección 8. Incluir además el bloque LOGO (A/B) —
   formato LOGO_ENGINE Sección 5.
2. El bloque DIRECCIÓN CREATIVA (5 ejes + hero + idea de autor + anti-patrón +
   resultado de check-dna) — formato CREATIVE_ENGINE Sección 4.
Incluye la paleta extraída del logo.

### Paso 10 — ESPERAR APROBACIÓN
DETENTE. No continúes hasta aprobación explícita del usuario. Si pide cambios
de diseño → vuelve al Paso 7. Si pide cambios de contenido → vuelve al Paso 5.

---

## FASE E — CONSTRUCCIÓN (solo tras aprobación)

### Paso 11 — Registrar ADN
Añade la fila del cliente a la TABLA MAESTRA de `.claude/PROJECT_DNA_LOG.md` +
ficha detallada (con la paleta REAL extraída) + actualiza RESERVA DE EJES.

### Paso 12 — Setup técnico
- Copia templates de `/design-system/`, reemplaza PLACEHOLDERs.
- Crea `src/lib/site-config.ts` con datos reales del cliente (punto único de
  verdad de contacto — nunca hardcodear email/teléfono en componentes) y los
  faltantes en `pending`. Engancha `assertProductionReady()` al build de
  producción.
- Genera el **paquete de marca** (LOGO_ENGINE Sección 3) en `brand/`: variantes
  del logo (full/horizontal/isotipo/wordmark/mono/favicon/OG) + manual de marca.
  Correr SVGO en los SVG. El logo elegido alimenta brandbook, firma, membrete.
- Crea `tokens.ts` desde los hex reales del logo (comentar si son provisionales).
- Crea `CONTENIDO-PARA-REVISAR.md` en la carpeta del cliente (listado dejar/cambiar para el cliente).

### Paso 13 — Construir
Componentes siguiendo el plan móvil del CREATIVE_ENGINE y el contenido del
CONTENT_ENGINE. Contenido generado marcado como PROVISIONAL. Secciones sin
datos (proyectos/clientes/cifras) ocultas, no con placeholders visibles.

---

## Recordatorios permanentes
- SISTEMA (SEO, Hostinger, a11y, PHP mail) = copiar del boilerplate, no innovar.
- DISEÑO = CREATIVE_ENGINE, único por proyecto. CONTENIDO = CONTENT_ENGINE,
  completo y honesto.
- Nunca inventar datos del cliente (cifras, certificaciones, clientes). Lo
  generado es estructura y copy genérico verdadero, marcado PROVISIONAL.
- Móvil: WhatsApp button + CTA + tel: intocables.
- Antes de deploy: `node scripts/check-hostinger.mjs` + Pa11y + Lighthouse ≥95.
- Producción: `DEPLOY_TARGET=production npm run build` (falla si quedan pendientes).
