# YaDevportfolio — CLAUDE.md

> Contexto central para Claude Code. Lee este archivo antes de cualquier tarea.

---

## ¿Qué es este proyecto?

**YaDevportfolio** es la plataforma interna de **YA Dev** (marca de desarrollo web y automatización).
Centraliza todos los proyectos de clientes activos, templates HTML por industria, modelos de diseño y herramientas internas.

**Repositorio:** `Yeral-18/YaDevportfolio`
**Infraestructura:** Railway (proyecto `vivacious-fulfillment`) + GitHub

---

## Estructura del monorepo

```
YaDevportfolio/
├── CLAUDE.md                         ← Este archivo
├── index.html                        ← Landing de YA Dev
├── main.js
├── proyectos/                        ← Templates HTML por industria
│   ├── construccion.html
│   ├── ecommerce.html
│   ├── electrico.html
│   ├── forestal.html
│   ├── salud.html
│   ├── tecnologia.html
│   └── transporte.html
├── Modelos/                          ← 19+ modelos de diseño web
├── assets/                           ← Recursos visuales globales
├── internal/PROYECTOS/2026/
│   ├── ECOMAG02/                     ← Cliente ECOMAG S.A.S
│   │   ├── ecomag-web/               ← Sitio web (Astro 5 + Svelte 5 + Tailwind)
│   │   └── brand/                    ← Brandbook + Firma de correo
│   └── MULTISERVICIOS P&J/           ← Cliente Multiservicios P&J S.A.S
│       ├── multiservicios-web/       ← Sitio web (Astro 5 + Svelte 5 + Tailwind)
│       ├── brand/                    ← Brandbook + Firma de correo
│       └── RECURSOS/                 ← PDFs corporativos del cliente
└── CONTEXTO_GENERACION_PDF.md        ← Guía técnica para generar PDFs
```

---

## Clientes activos (2026)

| Cliente | Industria | Stack | Deploy | Estado |
|---|---|---|---|---|
| ECOMAG S.A.S | Obra civil + Gestión ambiental | Astro 5 + Svelte 5 + Tailwind | Railway (ECOMAG) | ✅ Desplegado |
| MULTISERVICIOS P&J S.A.S | Transporte + Ingeniería + Ambiental | Astro 5 + Svelte 5 + Tailwind | Railway (multiservicios-web) | ✅ Desplegado |

---

## Entregables estándar por cliente

Cada proyecto de cliente incluye siempre los mismos 4 entregables:

1. **Sitio web** — Landing page profesional: Hero, Sobre Nosotros, Servicios, Proyectos, Contacto
2. **Brandbook HTML** — Manual de identidad corporativa formato A4, exportable a PDF
3. **Firma de correo HTML** — Generador interactivo con logo base64 embebido
4. **Panel YaDev** — Botón lateral en el sitio con acceso rápido al brandbook y firma

---

## 🤖 AGENTES DISPONIBLES — ÚSALOS SIEMPRE

Tienes 3 agentes configurados. **No trabajes sin activar el agente correcto para cada tarea.**

### `Explore`
**Activar cuando:** necesites buscar en el codebase antes de hacer cambios.
```
Úsalo antes de modificar cualquier cosa:
- Encontrar colores hardcodeados en archivos de cliente
- Localizar componentes duplicados entre proyectos
- Verificar qué archivos existen antes de crear nuevos
- Mapear dependencias antes de un refactor
```

### `Plan`
**Activar cuando:** la tarea involucre múltiples archivos o decisiones de arquitectura.
```
Úsalo para:
- Onboarding de cliente nuevo (estructura completa del proyecto)
- Rediseño de secciones existentes
- Migración de colores corporativos en todo un sitio
- Planificar qué archivos tocar antes de ejecutar
```
> ⚠️ Regla: si una tarea toca más de 3 archivos, primero activa Plan, luego ejecuta.

### `general-purpose`
**Activar cuando:** debas modificar múltiples archivos en paralelo.
```
Úsalo para:
- Actualizar colores/tipografías de marca en todo un sitio de cliente
- Cambiar contenido (misión, visión, servicios) en varias secciones simultáneamente
- Crear un cliente nuevo desde un template existente
- Sincronizar brandbook + sitio web + firma con los mismos tokens de diseño
```

---

## 🎨 SKILLS DISPONIBLES — ÚSALOS SIEMPRE

Tienes 4 skills configurados. **Actívalos explícitamente para cada tipo de tarea.**

### `ui-ux-pro-max`
**Activar para:** cualquier tarea visual o de diseño.
```
Úsalo cuando:
- Diseñes o mejores componentes de un sitio de cliente
- Revises la landing page de YA Dev
- Crees un brandbook nuevo
- Evalúes calidad visual de un entregable antes de enviarlo al cliente
- Elijas paletas de color, tipografías o layouts
```
> Este skill tiene 67 estilos, 96 paletas y 57 combinaciones tipográficas.
> Siempre consúltalo antes de tomar decisiones de diseño.

### `nano-banana-2`
**Activar para:** generación de imágenes y assets visuales.
```
Úsalo para:
- Imágenes hero de sitios nuevos de cliente
- Fondos y texturas para secciones
- Assets visuales para brandbooks
- Mockups de proyectos en la sección Portfolio del cliente
```

### `simplify`
**Activar para:** revisión de calidad de código.
```
Úsalo siempre después de:
- Completar la creación de un sitio nuevo
- Hacer cambios grandes (migración de colores, restructuración de componentes)
- Antes del deploy a Railway
- Entregar código al cliente
```

### `claude-api`
**Activar para:** integración de IA en proyectos.
```
Úsalo cuando:
- Algún cliente solicite funcionalidad con IA (chatbot, generador de textos, etc.)
- Necesites automatizar la generación de contenido del brandbook
- Quieras agregar IA al cotizador PDF interno de YA Dev
```

---

## 🔄 Flujo de trabajo estándar por tarea

### Tarea pequeña (1–3 archivos, cambio puntual)
```
1. Explore → verificar qué existe
2. Ejecutar cambio
3. simplify → revisar código resultante
```

### Tarea mediana (4–10 archivos, cambio de sección o componente)
```
1. Explore → mapear archivos afectados
2. Plan → diseñar estrategia
3. general-purpose → ejecutar en paralelo
4. ui-ux-pro-max → validar resultado visual
5. simplify → limpiar código
```

### Cliente nuevo (proyecto completo)
```
1. Plan → definir estructura completa del proyecto
2. ui-ux-pro-max → definir identidad visual (paleta, tipografía, estilo)
3. nano-banana-2 → generar assets visuales (hero, backgrounds)
4. general-purpose → crear todos los archivos en paralelo
   (sitio web + brandbook + firma + panel YaDev)
5. simplify → revisión final de código
6. Deploy a Railway
```

---

## Stack técnico por tipo de entregable

| Entregable | Stack | Notas |
|---|---|---|
| Sitio web cliente | Astro 5 + Svelte 5 + Tailwind CSS | Deploy en Railway vía Docker |
| Brandbook | HTML puro + CSS | Formato A4, exportable a PDF |
| Firma de correo | HTML puro | Logo embebido en base64 |
| Landing YA Dev | HTML + Tailwind CDN + vanilla JS | |
| Templates por industria | HTML puro | En `/proyectos/` |

---

## Reglas críticas del monorepo

1. **Nunca modifiques archivos de un cliente sin antes hacer `Explore`** — los proyectos comparten estructura pero tienen identidades visuales independientes.
2. **Los tokens de color de cada cliente son sagrados.** Verifica siempre el brandbook antes de tocar CSS.
   - ECOMAG: colores propios de obra civil/gestión ambiental
   - Multiservicios P&J: `#0089D0` (azul), `#005B32` (verde), `#8CC63F`, `#737374`
3. **Antes de deploy en Railway**, siempre correr `simplify` y verificar que no haya `base: '/ruta/'` en `astro.config.mjs`.
4. **El Panel YaDev** (botón lateral) debe estar presente en todos los sitios de cliente.
5. **Los brandbooks y firmas deben estar sincronizados** con los colores del sitio web. Si cambias uno, actualiza todos.

---

## Contexto adicional

- Guía técnica para PDFs: ver `CONTEXTO_GENERACION_PDF.md` en la raíz
- Cada cliente tiene su propio `CLAUDE.md` en su carpeta de proyecto con contexto específico
- El repo es público en GitHub: `Yeral-18/YaDevportfolio`
