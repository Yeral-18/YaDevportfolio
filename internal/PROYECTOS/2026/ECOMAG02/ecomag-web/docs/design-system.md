# ECOMAG S.A.S — Design System

Sistema de diseño inspirado en Apple, Linear, Vercel y Stripe.

---

## Filosofía de Diseño

1. **Minimalismo sofisticado** — Menos es más
2. **Jerarquía visual clara** — El usuario sabe qué es importante
3. **Animaciones sutiles** — Naturales, no intrusivas
4. **Espaciado consistente** — Sistema de 4px base
5. **Accesibilidad AA** — Focus states, contraste, touch targets

---

## Tokens

### Ubicación
```
/src/design-system/tokens.ts
```

### Colores Principales

| Token | Hex | Uso |
|-------|-----|-----|
| `primary.500` | #1B5E20 | Color corporativo, headers, links |
| `secondary.500` | #0277A8 | Acentos secundarios, visión |
| `accent.500` | #7CB342 | Badges, tags, valores |
| `cta` | #E65100 | Botones de acción |
| `dark` | #1A1A2E | Texto, footer |
| `light` | #F5F7F2 | Fondo general |

### Sombras (Estilo Apple)

```css
--shadow-xs:  0 1px 2px 0 rgb(0 0 0 / 0.03);
--shadow-sm:  0 1px 3px 0 rgb(0 0 0 / 0.05);
--shadow-md:  0 4px 6px -1px rgb(0 0 0 / 0.07);
--shadow-lg:  0 10px 25px -3px rgb(0 0 0 / 0.08);
--shadow-xl:  0 20px 40px -5px rgb(0 0 0 / 0.1);
--shadow-primary: 0 8px 24px -4px rgb(27 94 32 / 0.2);
```

### Transiciones

```css
--ease-default: cubic-bezier(0.4, 0, 0.2, 1);    /* Estándar */
--ease-out:     cubic-bezier(0, 0, 0.2, 1);      /* Entrada */
--ease-spring:  cubic-bezier(0.34, 1.3, 0.64, 1); /* Hover sutil */
--ease-smooth:  cubic-bezier(0.25, 0.46, 0.45, 0.94); /* Transforms */

--duration-fast:   150ms;
--duration-normal: 250ms;
--duration-slow:   400ms;
```

---

## Componentes

### Botones

```html
<!-- Primario -->
<button class="btn-primary">Cotizar</button>

<!-- Secundario -->
<button class="btn-secondary">Conocer más</button>
```

**Hover behavior:**
- `translateY(-2px)` — lift sutil
- Sombra con color del botón
- Duración: 250ms

### Cards

```html
<div class="card">Contenido</div>
<div class="card card-accent">Con borde accent</div>
```

**Hover behavior:**
- `translateY(-4px)` — NO scale
- `box-shadow: shadow-lg`
- Duración: 250ms

### Inputs

```html
<input class="input-field" placeholder="Texto" />
<input class="input-field error" /> <!-- Con error -->
```

---

## Animaciones

### Principios

1. **Rápidas** — 150-400ms máximo
2. **Naturales** — Easing suave, no bouncy
3. **Propósito** — Guían la atención del usuario
4. **No intrusivas** — El usuario no debería notarlas conscientemente

### Scroll Reveal

```html
<div class="reveal">Aparece con fade-in</div>
<div class="reveal reveal-delay-2">Con delay</div>
```

Comportamiento:
- Fade in desde abajo (20px)
- Duración: 500ms
- Easing: ease-out

### Hover States

| Elemento | Transform | Duración |
|----------|-----------|----------|
| Botones | `translateY(-2px)` | 250ms |
| Cards | `translateY(-4px)` | 250ms |
| Imágenes | `scale(1.03)` | 400ms |
| Links | underline `scaleX(1)` | 200ms |

**NO usar:**
- `scale > 1.03`
- Rotaciones en hover
- Animaciones infinitas en elementos principales
- Bounces exagerados

---

## Tipografía

### Fuentes

```css
--font-display: 'Plus Jakarta Sans', system-ui;
--font-body: 'Inter', system-ui;
```

### Escala

| Clase | Mobile | Desktop | Uso |
|-------|--------|---------|-----|
| `.heading-primary` | 1.75rem | 3rem | Títulos de sección |
| `.heading-secondary` | 1.25rem | 1.75rem | Subtítulos |
| `.text-body` | 0.9375rem | 1.0625rem | Párrafos |
| `.text-small` | 0.875rem | 0.875rem | Labels, captions |

---

## Espaciado

Base: **4px**

```
4px  (0.25rem) — Spacing mínimo
8px  (0.5rem)  — Entre elementos pequeños
16px (1rem)    — Entre elementos relacionados
24px (1.5rem)  — Entre grupos
32px (2rem)    — Entre secciones pequeñas
64px (4rem)    — Padding de sección (mobile)
96px (6rem)    — Padding de sección (desktop)
```

---

## Responsive

### Breakpoints

```
sm:  640px   — Tablet pequeño
md:  768px   — Tablet
lg:  1024px  — Desktop
xl:  1280px  — Desktop grande
2xl: 1536px  — Pantallas amplias
```

### Touch devices

```css
@media (hover: none) {
  /* Desactivar hover effects */
  .card:hover { transform: none; }
}
```

---

## Accesibilidad

- Touch targets: mínimo 44x44px
- Focus visible: `outline: 2px solid primary`
- Contraste: mínimo 4.5:1 para texto
- Skip links implementados
- Aria labels en iconos

---

## Archivos Clave

```
/src/design-system/tokens.ts   — Tokens centralizados
/src/styles/global.css          — Clases globales
/tailwind.config.mjs            — Configuración Tailwind
```

---

*Desarrollado por YaDev — Marzo 2026*
