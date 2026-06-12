---
description: Inicia un cliente nuevo con el RITUAL de dirección creativa obligatorio. Uso - /nuevo-cliente NOMBRE_CLIENTE
allowed-tools: Read, Glob, Grep, Bash(node:*)
---

# NUEVO CLIENTE — RITUAL OBLIGATORIO

Cliente a iniciar: **$ARGUMENTS**

Ejecuta estos pasos EN ORDEN. PROHIBIDO escribir, crear o editar cualquier
componente (.astro, .svelte, .css, .ts de UI) antes de completar el paso 7.

## Paso 1 — Leer contexto del cliente
Lee TODO el contenido de `internal/PROYECTOS/2026/$ARGUMENTS/` (CONTEXTO.md,
datos, logo, colores, servicios). Si la carpeta no existe o está vacía,
DETENTE y pide al usuario los datos mínimos: industria, servicios, colores/logo,
contacto, ciudad.

## Paso 2 — Leer el motor y el log
Lee completos:
- `.claude/CREATIVE_ENGINE.md` (los 5 ejes, el mapa industria, regla móvil)
- `.claude/PROJECT_DNA_LOG.md` (ADN de TODOS los proyectos previos + saturación)

## Paso 3 — Generar dirección creativa
Elige UN valor por cada eje (Director, Composición, Movimiento, Navegación,
Narrativa) + una idea de autor ligada a la marca del cliente. Usa el mapa
industria→director como punto de partida, no como regla.

## Paso 4 — Verificación programática de colisión
Ejecuta:
```bash
node scripts/check-dna.mjs --director "X" --composicion "Y" --movimiento "Z" --navegacion "W" --easing "curva"
```
- Si sale `COLISIÓN` → vuelve al Paso 3 con otra combinación. NO negocies.
- Si sale `SATURADO` en navegación/easing/tipografía → cambia ese eje.
- Solo continúa con `OK`.

## Paso 5 — Mostrar el bloque de dirección creativa
Presenta al usuario el bloque del RITUAL (formato de CREATIVE_ENGINE.md
Sección 4) incluyendo: los 5 ejes con justificación, hero concept, idea de
autor, anti-patrón (qué NO repites del proyecto anterior), y el resultado
del check-dna.

## Paso 6 — ESPERAR APROBACIÓN
DETENTE. No continúes hasta que el usuario apruebe explícitamente
("aprobado", "dale", "ok", "sí"). Si pide cambios, vuelve al Paso 3.

## Paso 7 — Registrar ADN
Añade la fila del nuevo cliente a la TABLA MAESTRA de
`.claude/PROJECT_DNA_LOG.md` + su ficha detallada + actualiza la sección
RESERVA DE EJES POR AGOTAMIENTO. Recién después de guardar, puedes codear.

## Paso 8 — Setup técnico (SISTEMA)
Copia templates de `/design-system/`, reemplaza PLACEHOLDERs, crea
`src/lib/site-config.ts` con los datos reales del cliente (punto único de
verdad de contacto — nunca hardcodear email/teléfono en componentes).

## Recordatorios permanentes
- SISTEMA (SEO, Hostinger, a11y, PHP mail) = copiar del boilerplate, no innovar.
- DISEÑO = generado por el motor, prohibido copiar de otro proyecto.
- Móvil: la diferenciación de navegación vive en desktop; en móvil garantizar
  WhatsApp button, CTA visible y carga rápida (eso es SISTEMA).
- Antes de deploy: `node scripts/check-hostinger.mjs` + Pa11y + Lighthouse ≥95.
