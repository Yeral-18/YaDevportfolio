# PROMPT REUTILIZABLE: Sitio Web Corporativo Premium (Astro + Svelte + Tailwind)

---

## =============================================
## SECCION 1: VARIABLES DEL PROYECTO (EDITAR AQUI)
## =============================================

### 1.1 DATOS DE LA EMPRESA

```yaml
nombre_empresa: "ECOMAG S.A.S"
slogan: "Soluciones integrales en obra civil y gestion ambiental"
industria: "Ingenieria civil y gestion ambiental"
descripcion_seo: "ECOMAG S.A.S - Soluciones integrales en obra civil y gestion ambiental en Barrancabermeja, Santander. Certificados ISO 9001, ISO 14001 e ISO 45001."
idioma: "es"
locale: "es_CO"
url_sitio: "https://ecomagsas.com"
ano_copyright: 2026
```

### 1.2 CONTACTO

```yaml
telefono: "+57 XXX XXX XXXX"
telefono_link: "+57XXXXXXXXXX"
email: "info@ecomagsas.com"
whatsapp: "57XXXXXXXXXX"
direccion: "Calle 72 # 19 - 42, Barrancabermeja, Santander"
horario: "Lun-Vie 8:00 AM - 6:00 PM"
horario_schema: "Mo-Fr 08:00-18:00"
coordenadas: { lat: 7.0653, lng: -73.8547 }
```

### 1.3 REDES SOCIALES

```yaml
facebook: "https://www.facebook.com/ecomagsas"
instagram: "https://www.instagram.com/ecomagsas"
linkedin: "https://www.linkedin.com/company/ecomagsas"
```

### 1.4 PALETA DE COLORES

```yaml
# --- COLORES PRINCIPALES (cambiar estos para rebranding) ---
primary:     "#1B5E20"   # Verde oscuro — Color corporativo principal
secondary:   "#0277A8"   # Azul — Acentos secundarios
accent:      "#7CB342"   # Verde lima — Elementos decorativos
cta:         "#E65100"   # Naranja — Botones de accion (call-to-action)
dark:        "#1a1a2e"   # Casi negro — Textos y fondos oscuros (footer)
light:       "#F5F7F2"   # Gris claro — Fondo general del body
surface:     "#FFFFFF"   # Blanco — Tarjetas y superficies

# --- FONDOS POR SECCION (alternados para romper monotonia) ---
fondo_about:      "#FFFFFF"     # About Us — limpio
fondo_valores:    "#DCE8D4"     # Subseccion Valores — verde sabila suave
fondo_services:   "#E0EBD8"     # Servicios — verde claro
fondo_projects:   "#EDE5D8"     # Proyectos — beige/arena
fondo_contact:    "#D8E6D0, #CDDCC4, #D8E6D0"  # Contacto — gradiente verde

# --- PALETA EXTENDIDA (generada a partir del primary) ---
# Cada color principal genera 10 tonos (50-900)
# Ejemplo para primary #1B5E20:
primary_50:  "#e8f5e9"
primary_100: "#c8e6c9"
primary_200: "#a5d6a7"
primary_300: "#81c784"
primary_400: "#66bb6a"
primary_500: "#1B5E20"  # = primary
primary_600: "#165a1c"
primary_700: "#114d16"
primary_800: "#0d3f11"
primary_900: "#08310c"  # Topbar background
```

### 1.5 TIPOGRAFIA

```yaml
font_display: "Plus Jakarta Sans"   # Titulos — moderna y amigable
font_display_weights: [500, 600, 700, 800]
font_body: "Inter"                  # Cuerpo — legible y profesional
font_body_weights: [400, 500, 600]
fuente_url: "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap"
```

### 1.6 SECCIONES DE NAVEGACION

```yaml
nav_links:
  - { label: "Inicio",         href: "#inicio" }
  - { label: "Sobre Nosotros", href: "#sobre-nosotros" }
  - { label: "Servicios",      href: "#servicios" }
  - { label: "Proyectos",      href: "#proyectos" }
  - { label: "Contacto",       href: "#contacto" }
nav_cta: "Cotizar"  # Boton CTA en navbar
```

### 1.7 CONTENIDO DEL HERO

```yaml
hero_badge: "Ingenieria & Gestion Ambiental"
hero_titulo: "Construimos el futuro con responsabilidad ambiental"
hero_subtitulo: "Mas de X anos transformando el territorio con soluciones de ingenieria civil, gestion ambiental y mantenimiento industrial."
hero_cta_primary: "Solicitar Cotizacion"
hero_cta_secondary: "Conocer Mas"
hero_imagen: "/hero-bg.jpg"
```

### 1.8 SERVICIOS (6 items)

```yaml
servicios:
  - titulo: "Obra Civil"
    descripcion: "Construccion de infraestructura vial, edificaciones..."
    imagen: "/images/services/obra-civil.jpg"
  - titulo: "Gestion Ambiental"
    descripcion: "Planes de manejo ambiental, remediacion de suelos..."
    imagen: "/images/services/gestion-ambiental.jpg"
  - titulo: "Mantenimiento Industrial"
    descripcion: "Mantenimiento preventivo y correctivo..."
    imagen: "/images/services/mantenimiento.jpg"
  - titulo: "Consultoria e Interventoria"
    descripcion: "Supervision tecnica de proyectos..."
    imagen: "/images/services/consultoria.jpg"
  - titulo: "Transporte Especializado"
    descripcion: "Transporte de materiales y equipos..."
    imagen: "/images/services/transporte.jpg"
  - titulo: "Suministro de Personal"
    descripcion: "Personal calificado y certificado..."
    imagen: "/images/services/personal.jpg"
```

### 1.9 PROYECTOS (4 items)

```yaml
proyectos:
  - titulo: "Construccion Via Terciaria"
    subtitulo: "Municipio de San Vicente"
    categoria: "Obra Civil"
    descripcion: "Construccion de 12 km de via terciaria..."
    imagen: "/images/projects/via-terciaria.jpg"
    large: true
  # ... (4 proyectos con categorias variadas)
```

### 1.10 ABOUT US

```yaml
about_titulo: "Experiencia que genera confianza"
about_descripcion: "Descripcion de la empresa..."
mision: "Texto de mision..."
vision: "Texto de vision..."
valores: ["Integridad", "Innovacion", "Sostenibilidad", "Seguridad", "Compromiso"]
about_imagen: "/images/about-placeholder.jpg"
```

### 1.11 FOOTER

```yaml
footer_descripcion: "Soluciones integrales en obra civil y gestion ambiental."
certificaciones_imagen: "/images/bureau-veritas-iso.png"
certificaciones_alt: "Certificaciones Bureau Veritas — ISO 9001:2015, ISO 14001:2015, ISO 45001:2018"
credito_dev: "YaDev"
credito_url: "https://yeral-18.github.io/YaDevportfolio/index.html"
```

---

## =============================================
## SECCION 2: STACK TECNOLOGICO
## =============================================

```
Astro 5.x          — Framework SSG con islands architecture
Svelte 5.x         — Componentes interactivos (sintaxis legacy)
Tailwind CSS 3.4    — Estilos utilitarios
Motion.js 12.x      — Animaciones de entrada del hero
@astrojs/sitemap    — Generacion automatica de sitemap.xml
@astrojs/tailwind   — Integracion Tailwind
@astrojs/svelte     — Integracion Svelte
@tailwindcss/typography — Plugin tipografia
```

---

## =============================================
## SECCION 3: ARQUITECTURA Y ORDEN DE COMPONENTES
## =============================================

```
src/pages/index.astro          — Pagina principal (ensamblaje)
src/layouts/Layout.astro       — Layout con SEO, meta, Schema.org
src/styles/global.css          — Variables CSS, clases reutilizables
src/components/
  ProgressBar.svelte           — client:load
  Topbar.astro                 — Barra superior con contacto + redes
  Navbar.astro                 — Navegacion sticky con menu movil
  Hero.svelte                  — client:load — Seccion hero con hojas animadas
  WaveTransition.astro         — Separador SVG animado
  AboutUs.astro                — Sobre nosotros + Mision/Vision/Valores
  Services.astro               — Grid de servicios
  Projects.astro               — Grid de proyectos
  Contact.svelte               — client:visible — Formulario con validacion
  Footer.astro                 — Footer con 4 columnas
  ScrollToTop.svelte           — client:load — Boton volver arriba
  WhatsAppButton.svelte        — client:idle — Boton flotante WhatsApp
  LeafCursor.svelte            — client:idle — Cursor personalizado (solo desktop)
```

---

## =============================================
## SECCION 4: SISTEMA DE DISENO
## =============================================

### 4.1 Estilos Globales (global.css)

Variables CSS en `:root` usando los colores de la Seccion 1.4.

Clases reutilizables:
- `.section-container` — `mx-auto max-w-7xl px-4 sm:px-6 lg:px-8`
- `.section-padding` — `py-16 md:py-24`
- `.heading-primary` — `font-display text-3xl font-bold tracking-tight sm:text-4xl lg:text-5xl`
- `.btn-primary` — `bg-cta rounded-lg px-6 py-3 text-white shadow-lg hover:bg-orange-700`
- `.btn-secondary` — `border-2 border-primary rounded-lg px-6 py-3 hover:bg-primary hover:text-white`
- `.card` — `rounded-2xl bg-white p-6 shadow-md hover:-translate-y-1 hover:shadow-xl`

Textos responsive: usar `clamp()` para h1 (`clamp(2rem, 5vw, 3.5rem)`), h2 movil fijo en `1.5rem`.

### 4.2 Easing Universal

CRITICO — Este easing se usa en TODOS los hovers y scroll reveals del sitio:
```
cubic-bezier(0.34, 1.56, 0.64, 1)   /* Spring bounce — hovers y reveals */
cubic-bezier(0.25, 0.46, 0.45, 0.94) /* Smooth — zooms de imagen */
[0.22, 1, 0.36, 1]                   /* Motion.js — entrada hero */
```

### 4.3 Patron de Scroll Reveal

Todos los componentes principales usan IntersectionObserver:
```javascript
// threshold: 0.15 para secciones, 0.2 para about
// Agrega clase 'revealed' — CSS maneja la transicion
// Staggered delays por indice (i * 0.12s a 0.2s)
// observer.unobserve() despues de revelar — solo anima una vez
```

Patron de estado inicial → revelado:
```css
.element { opacity: 0; transform: translate3d(0, 60px, 0); transition: none; }
.element.revealed { opacity: 1; transform: translate3d(0, 0, 0);
  transition: opacity 0.7s ease, transform 0.7s cubic-bezier(0.34, 1.56, 0.64, 1); }
```

### 4.4 GPU Acceleration

En TODOS los elementos animados:
```css
transform: translate3d(0, 0, 0);  /* Fuerza GPU layer */
will-change: transform, opacity;   /* Solo en elementos que animan */
```

### 4.5 Touch Device Handling

Desactivar hover effects en dispositivos tactiles:
```css
@media (hover: none) {
  .card:hover { transform: none !important; box-shadow: initial !important; }
}
```

### 4.6 SSR Guard Pattern (Svelte)

En TODOS los componentes Svelte que usan `window`:
```javascript
onDestroy(() => {
  if (typeof window !== 'undefined') {
    window.removeEventListener('scroll', handler);
  }
});
```

---

## =============================================
## SECCION 5: COMPONENTES DETALLADOS
## =============================================

### 5.1 ProgressBar.svelte
- Fixed top-0 left-0, width 100%, height 3px, z-index 9999
- Gradiente: `linear-gradient(to right, {primary}, {accent}, {secondary})`
- `transform: scaleX(scrollProgress)`, transform-origin left
- Transicion 0.15s ease-out
- Calculo: `scrollTop / (scrollHeight - clientHeight)`

### 5.2 Topbar.astro
- Fondo: `{primary_900}`, py-1.5, texto blanco
- Izquierda: telefono + email + horario con iconos SVG
- Derecha: iconos redes sociales con colores de marca
- Touch targets: min-h-[44px], hover color accent-200
- Ocultar elementos secundarios en mobile para no saturar

### 5.3 Navbar.astro
- Sticky top-0, z-40, fondo white/95 con backdrop-blur
- Logo: h-10 (sm: h-12, lg: h-16)
- Links desktop con hover underline animado (scaleX)
- Boton CTA solo en desktop
- Menu movil: w-72, slide desde derecha (300ms ease-in-out), backdrop black/50
- On scroll > 10px: agregar shadow-md + backdrop-blur-md
- Touch targets 44px en hamburger y links movil
- Escape key y backdrop click cierran menu

### 5.4 Hero.svelte (COMPONENTE ESTRELLA)

**Estructura:**
- min-height: 100vh (mobile: 85vh)
- Fondo: gradiente 135deg sobre imagen hero
  - `rgba({primary}, 0.92) 0%, rgba({secondary}, 0.7) 50%, rgba({primary}, 0.4) 100%`

**Contenido:**
- Badge: borde white/35, backdrop blur(4px), bg white/8, border-radius full
- H1: `clamp(2rem, 5vw, 3.5rem)`, fw 800, lh 1.1, blanco
- Subtitulo: `clamp(1rem, 2vw, 1.25rem)`, white/85
- CTAs: Primary (naranja {cta}) + Secondary (borde blanco)
- Botones se apilan verticalmente en < 400px

**7 Hojas SVG Animadas:**
- 7 formas organicas unicas con SVG paths, colores rgba variados del primary/accent
- Cada hoja tiene keyframes UNICOS (no repetir):
  - Diferentes duraciones (5s a 12s)
  - Diferentes delays negativos para desincronizar
  - Combinan translate + rotate + scale
  - Movimientos: arcos, ondulaciones, flutter rapido
- Filter: `drop-shadow(0 2px 8px rgba(0,0,0,0.15))`
- Mobile: ocultar 3 hojas, achicar las restantes
- Position absolute, pointer-events none

**Entrada con Motion.js:**
- Elementos [data-animate]: opacity 0→1, translateY 24px→0
- Duracion 0.7s, easing [0.22, 1, 0.36, 1]
- Delay staggered: 0.15s * indice
- Respetar prefers-reduced-motion

### 5.5 WaveTransition.astro
- Separador SVG animado entre hero y contenido
- Dos ondas SVG superpuestas (viewBox 0 0 1440 150), width 200%
- Onda trasera: opacity 0.45, animation 12s
- Onda frontal: animation 8s
- Keyframes: translateX(0) → translateX(-25%) → translateX(0)
- Altura responsive: 50px (sm: 80px, md: 110px, lg: 140px)
- Margin-top negativo para overlap con hero
- preserveAspectRatio="none"

### 5.6 AboutUs.astro

**Fondo:** `{fondo_about}` con patron de puntos radiales rgba({primary}, 0.04)

**Imagen (lado derecho en desktop):**
- Aspect 4/3, rounded-xl
- Reveal: clip-path `inset(0 100% 0 0)` → `inset(0 0 0 0)`, 0.8s ease-out
- Accent decoration: bloque absolute -bottom-4 -right-4, bg accent-100
- **On HOVER (no constante):** animation `aboutImageFloat` 4s ease-in-out infinite
  - Keyframes: translate(0,0) scale(1.02) → (8px,-5px) scale(1.04) → (-5px,-10px) scale(1.03) → (10px,-3px) scale(1.05)
- Accent tambien flota en direccion opuesta on hover

**Cards Mision/Vision/Valores (3 cards):**
- rounded-2xl, bg-white, p-6, shadow-md, border-top 3px transparent
- Hover con spring bounce 0.4s:
  - translateY(-8px) scale(1.02), shadow intenso
  - Border-top cambia a color tematico (Mision: primary, Vision: secondary, Valores: accent)
  - Gradiente sutil en background
- Desactivado en touch: `@media (hover: none)`

**Subseccion Valores:**
- Fondo diferenciado: `{fondo_valores}` con rounded corners
- Mobile: scroll horizontal snap-x snap-mandatory, items min-w-[160px]
- Desktop: grid 5 columnas
- Items hover: translateY(-4px), sombra verde

### 5.7 Services.astro

**Fondo:** `{fondo_services}` con radial gradients decorativos

**Grid:** 3 cols desktop, 2 tablet, 1 mobile

**Cards:**
- Reveal: opacity 0, translate3d(0, 60px, 0) rotate(2deg) → normal
- Delay staggered: i * 0.12s
- Hover: translateY(-12px), shadow intenso, border-left 3px {primary}

**Imagen en cada card:**
- Aspect 16/10 (sm: 4/3)
- **On HOVER (no constante):** animation `serviceImageFloat` 5s infinite
  - Similar a aboutImageFloat pero con diferentes valores
  - + filter brightness(1.08)
- Color overlay verde aparece on hover (opacity 0 → 1)

**Icono overlay:** circulo 40px bg-primary, scale(0) → scale(1) on reveal

### 5.8 Projects.astro

**Fondo:** `{fondo_projects}` con lineas de cuadricula

**Mobile:** Stack vertical, gap-5
- Overlay verde: `from-[{primary_900 oscuro}]/90 via-[{primary}]/30 to-transparent`
- Descripcion visible debajo de cada imagen (NO scroller horizontal)

**Desktop:** Grid 2 columnas
- Reveal: opacity 0, translate3d(±80px, 0, 0) rotate(±3deg) → normal, 0.8s
- **Hover del CARD COMPLETO (no solo imagen):**
  - translateY(-12px) scale(1.03) rotate(-1deg)
  - Shadow: 0 35px 70px -15px rgba(0,0,0,0.3)
  - z-index sube a 10
- Imagen interna: scale(1.08) on hover
- Overlay intensifica con gradiente verde
- Content slides up: translate3d(0, -6px, 0)

**Linea accent inferior (::after) por categoria:**
- height 4px, scaleX(0) → scaleX(1) on hover
- Color varia segun categoria (usar primary, accent, secondary, cta)

### 5.9 Contact.svelte

**Fondo:** gradiente `linear-gradient(180deg, {fondo_contact})`

**Grid:** 1 col mobile, md: 5fr 7fr

**Info (izquierda):**
- Card blanca con 4 items de contacto (icono + titulo + valor)
- Placeholder de mapa (borde dashed, icono centrado)

**Formulario (derecha):**
- Campos: nombre*, empresa, telefono* + email* (2 cols en sm), mensaje*
- Validacion real-time on blur:
  - Telefono: regex colombiano `/^(\+57\s?)?[0-9\s\-()]{7,15}$/`
  - Email: regex estandar
  - Mensaje: min 10 caracteres
- Inputs: min-height 44px mobile, focus ring color primary
- **Honeypot** anti-spam: campo hidden `position: absolute; left: -9999px`
- Submit: btn-primary full width, min-height 48px
- Estados: idle → loading (spinner) → success (checkmark) / error (retry)
- Aria-invalid, aria-describedby para accesibilidad

**Scroll Reveal:**
- Header: fade up
- Info card: slide desde izquierda (translate3d(-40px, 0, 0))
- Form card: slide desde derecha (translate3d(40px, 0, 0))
- Detail items: stagger 100ms cada uno

### 5.10 Footer.astro

**Fondo:** `{dark}`, texto gray-300, COMPACTO: py-4 md:py-6

**Grid 4 columnas (lg):**
1. Logo (brightness-0 invert para hacerlo blanco) + descripcion
2. Enlaces de navegacion con hover accent + underline
3. Contacto con iconos SVG accent
4. Redes sociales + imagen certificaciones

**Social icons hover:** Cambia a color de la red social
```css
.social-icon:hover {
  background-color: var(--brand-color); /* Facebook:#1877F2, Instagram:#E4405F, LinkedIn:#0A66C2 */
  color: white;
  box-shadow: 0 0 20px color-mix(in srgb, var(--brand-color) 50%, transparent);
  transform: translateY(-3px);
}
```

**Imagen certificaciones:** max-w-[200px] mobile, max-w-[240px] desktop

**Bottom bar:** border-t white/10, copyright + "Desarrollado por {credito_dev}"

### 5.11 ScrollToTop.svelte
- Fixed bottom 6rem right 1.25rem (sm: bottom 8rem right 2rem)
- Alineado encima del boton WhatsApp
- z-index 45, circulo 44px, borde 2px rgba({primary}, 0.35), bg white/95
- Visible cuando scrollY > 400
- Pulse animation: ring de 6px que se desvanece cada 2.5s
- Hover: scale(1.1), shadow verde, animation se pausa
- **SSR guard** en onDestroy

### 5.12 WhatsAppButton.svelte
- Fixed bottom 1.25rem right 1.25rem (sm: 1.5rem)
- z-index 50, aparece con delay 1500ms
- Boton: 60px (sm: 68px), rounded-full, bg #25D366
- **3 pulse rings** concentricos:
  - Border 3px #25D366, animation `pulseWave` 2.4s infinite
  - Delays: 0s, 0.8s, 1.6s
  - scale(1) opacity(0.6) → scale(1.35) opacity(0) (sm: scale hasta 1.5)
- Tooltip "Necesitas ayuda?" solo desktop (oculto max-width 639px)
- Hover: scale(1.12), shadow intenso

### 5.13 LeafCursor.svelte
- Solo activo en desktop (fine pointer) y si no prefers-reduced-motion
- SVG hoja 24px, color {primary}
- Seguimiento suave del mouse con lerp (factor 0.15)
- Rotacion dinamica basada en atan2(dy, dx) + 45 grados
- Oculta cursor nativo del body

---

## =============================================
## SECCION 6: SEO COMPLETO
## =============================================

### 6.1 Layout.astro — Head

```html
<!-- Basicos -->
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{titulo_pagina}</title>
<meta name="description" content="{descripcion_seo}" />
<link rel="canonical" href="{url_canonica}" />

<!-- Google Search Console (descomentar cuando este verificado) -->
<!-- <meta name="google-site-verification" content="CODIGO" /> -->

<!-- Preload LCP image -->
<link rel="preload" as="image" href="/hero-bg.jpg" type="image/jpeg" />

<!-- Favicon -->
<link rel="icon" type="image/svg+xml" href="/favicon.svg" />
<link rel="apple-touch-icon" href="/apple-touch-icon.png" />

<!-- Open Graph -->
<meta property="og:type" content="website" />
<meta property="og:url" content="{url_canonica}" />
<meta property="og:title" content="{titulo_pagina}" />
<meta property="og:description" content="{descripcion_seo}" />
<meta property="og:image" content="{url_sitio}/og-default.jpg" />
<meta property="og:locale" content="{locale}" />
<meta property="og:site_name" content="{nombre_empresa}" />

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{titulo_pagina}" />
<meta name="twitter:description" content="{descripcion_seo}" />
<meta name="twitter:image" content="{url_sitio}/og-default.jpg" />
```

### 6.2 Schema.org JSON-LD (LocalBusiness)

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "{nombre_empresa}",
  "description": "{descripcion_seo}",
  "url": "{url_sitio}",
  "logo": "{url_sitio}/logo.png",
  "image": "{url_sitio}/og-default.jpg",
  "telephone": "{telefono}",
  "email": "{email}",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Calle 72 # 19 - 42",
    "addressLocality": "Barrancabermeja",
    "addressRegion": "Santander",
    "addressCountry": "CO"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 7.0653,
    "longitude": -73.8547
  },
  "openingHours": "{horario_schema}",
  "sameAs": ["{facebook}", "{instagram}", "{linkedin}"],
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Servicios de {industria}"
  }
}
```

### 6.3 Sitemap

Generado automaticamente por `@astrojs/sitemap` en `astro.config.mjs`:
```javascript
import sitemap from '@astrojs/sitemap';
export default defineConfig({
  site: '{url_sitio}',
  integrations: [sitemap(), svelte(), tailwind()],
});
```

### 6.4 robots.txt (en /public/)

```
User-agent: *
Allow: /
Sitemap: {url_sitio}/sitemap-index.xml
```

### 6.5 Imagenes SEO

- `og-default.jpg` — 1200x630px, imagen de preview para redes sociales
- `apple-touch-icon.png` — 180x180px
- `favicon.svg` — Icono vectorial
- Todas las imagenes con `alt` descriptivo que incluya nombre de empresa
- `loading="lazy"` y `decoding="async"` en todo excepto hero
- Hero image: `<link rel="preload">` como optimizacion LCP

### 6.6 Google Analytics (preparado)

Incluir comentado en el head, descomentar cuando se tenga el ID:
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

---

## =============================================
## SECCION 7: ACCESIBILIDAD
## =============================================

- Skip to main content link (sr-only, focus:not-sr-only)
- Todos los botones/links: min-height 44px (touch target WCAG)
- Aria labels completos en botones de icono
- Focus rings visibles: `focus-visible:outline-2 outline-offset-2`
- Aria-invalid y aria-describedby en campos del formulario
- role="contentinfo" en footer, role="list" en listas nav
- `prefers-reduced-motion`: deshabilitar scroll-behavior smooth
- Contraste suficiente en todos los textos
- Imagenes con alt descriptivos

---

## =============================================
## SECCION 8: RESPONSIVE BREAKPOINTS
## =============================================

```
Default    — Mobile first (< 640px)
sm: 640px  — Tablet pequeno
md: 768px  — Tablet
lg: 1024px — Desktop
xl: 1280px — Desktop grande
2xl: 1536px

Custom:
@media (max-width: 639px) — Mobile-specific
@media (min-width: 380px) — Telefono grande
@media (hover: none) — Touch devices
@media (pointer: fine) — Mouse/trackpad (para LeafCursor)
```

---

## =============================================
## SECCION 9: ESTRUCTURA DE ARCHIVOS
## =============================================

```
proyecto-web/
├── public/
│   ├── logo.png
│   ├── favicon.svg
│   ├── apple-touch-icon.png
│   ├── hero-bg.jpg
│   ├── og-default.jpg              # 1200x630 para redes sociales
│   ├── robots.txt
│   └── images/
│       ├── about-placeholder.jpg
│       ├── bureau-veritas-iso.png   # Certificaciones
│       ├── services/               # 6 imagenes
│       └── projects/               # 4 imagenes
├── src/
│   ├── layouts/Layout.astro
│   ├── pages/index.astro
│   ├── styles/global.css
│   └── components/                 # 13 componentes
├── astro.config.mjs
├── tailwind.config.mjs
├── tsconfig.json
└── package.json
```

---

## =============================================
## SECCION 10: NOTAS PARA QUE NO PAREZCA IA
## =============================================

1. **Animaciones variadas:** Las 7 hojas del hero tienen movimientos UNICOS, no copiar/pegar
2. **Fondos alternados:** Cada seccion tiene su propio fondo (blanco, verde, beige, gradiente)
3. **Hovers creativos:** Card completo rota y escala (no solo color), imagenes flotan organicamente
4. **Micro-interacciones:** Cursor hoja, pulse rings WhatsApp, lineas accent por categoria, progress bar
5. **Spacing intencional:** No usar espaciado uniforme — varia entre secciones
6. **Overlays verdes:** En vez de negro/gris, usar tonos del primary para overlays
7. **Easing natural:** El `cubic-bezier(0.34, 1.56, 0.64, 1)` da un bounce sutil que se siente artesanal
8. **Detalles ocultos:** El LeafCursor solo aparece en desktop, el tooltip WhatsApp solo en hover desktop
9. **Colores de marca en redes:** Cada red social tiene su color real, no un generico
10. **Formulario con estados:** Loading spinner, success checkmark, error con retry — no un simple alert()
