# YADEV AI SYSTEM — CLAUDE.md

> Sistema de desarrollo web automatizado de la agencia **YA Dev**.
> Lee este archivo COMPLETO antes de cualquier tarea.

---

## OBJETIVO

Generar sitios web completos, listos para producción en Hostinger, con calidad de agencia premium (Awwwards, Stripe, Vercel). Cada proyecto incluye web + branding + SEO + deploy config.

---

## IDENTIDAD

**Agencia:** YA Dev — Diseño Web & Automatización para Empresas Colombianas
**Fundador:** Angel (Developer & Designer) — `angelpelaezca@gmail.com`
**Lead Developer:** Yeral (sigue como miembro del equipo, aparece en `index.html`)
**Repositorio:** `Yeral-18/YaDevportfolio` (el username `Yeral-18` en GitHub se mantiene por compat. de URLs)
**Portfolio:** `index.html` (dark theme, glassmorphism, Space Grotesk)
**Mercado:** Empresas industriales colombianas (transporte, construcción, ambiental, energía)

---

## STACK ESTÁNDAR

| Capa | Tecnología | Versión |
|------|-----------|---------|
| Framework SSG | Astro | 5.18+ |
| UI Interactiva | Svelte | 5.53+ (runes: $state/$effect) |
| Estilos | TailwindCSS | 3.4+ |
| Tipografía | Google Fonts (varía por cliente) |
| Animación | CSS keyframes + Motion.js | 12.35+ |
| Backend formulario | PHP mail() | Nativo Hostinger |
| Hosting | Hostinger | Shared hosting |
| Correo empresarial | Microsoft 365 | Outlook |

---

## ESTRUCTURA DEL MONOREPO

```
YaDevportfolio/
├── .claude/
│   ├── CLAUDE.md                     ← ESTE ARCHIVO
│   ├── agents/                       ← 6+ agentes especializados
│   └── skills/                       ← Skills de diseño
├── index.html                        ← Portfolio YA Dev (dark, glassmorphism)
├── main.js                           ← JS vanilla portfolio
│
├── design-system/                    ← BOILERPLATE CENTRALIZADO
│   ├── README.md                     ← Guía de uso
│   ├── tokens-template.ts            ← Design tokens con PLACEHOLDERs
│   ├── global-template.css           ← CSS base reutilizable
│   ├── astro-config-template.mjs     ← Config con fixes de Hostinger
│   ├── tailwind-config-template.mjs  ← Tailwind con path fix
│   ├── htaccess-template             ← Apache sin CSP
│   ├── contact-php-template.php      ← Formulario email con mail()
│   └── hostinger-checklist.md        ← 60-item deployment checklist
│
├── proyectos/                        ← 11 templates HTML por industria
│   ├── construccion.html             ← Space Grotesk, brutalist
│   ├── ecommerce.html                ← Clash Display, editorial luxury
│   ├── educacion.html                ← Merriweather, institutional
│   ├── electrico.html                ← Inter, corporate RETIE
│   ├── forestal.html                 ← Playfair Display, editorial
│   ├── inmobiliaria.html             ← Cormorant Garamond, elegant
│   ├── legal.html                    ← Libre Baskerville, conservative
│   ├── restaurante.html              ← Playfair Display + Lato, warm
│   ├── salud.html                    ← DM Sans, clinical
│   ├── tecnologia.html               ← Satoshi, glassmorphism
│   └── transporte.html               ← Outfit, logistics dashboard
│
├── Modelos/                          ← 20 modelos de referencia
│   ├── INDEX.md                      ← Catálogo cruzado completo
│   ├── CATALOGO.md                   ← Catálogo + guía
│   ├── BOILERPLATE_GUIDE.md          ← Workflow nuevos proyectos
│   └── Modelo *.txt                  ← HTMLs de referencia (competencia)
│
├── assets/
│   ├── img/                          ← Fotos equipo YaDev
│   ├── css/templates/                ← 23 temas CSS por industria
│   └── js/
│
├── internal/PROYECTOS/2026/          ← PROYECTOS ACTIVOS
│   ├── ECOMAG02/                     ← ECOMAG S.A.S (producción)
│   ├── MULTISERVICIOS P&J/           ← Multiservicios P&J (producción)
│   └── PROMPT_ECOMAG_WEBSITE.md      ← Prompt reutilizable (705 líneas)
│
└── CONTEXTO_GENERACION_PDF.md        ← Guía Express + Puppeteer
```

---

## CLIENTES ACTIVOS (2026)

| Cliente | Industria | URL | Hosting | Correo | Estado |
|---------|-----------|-----|---------|--------|--------|
| ECOMAG S.A.S | Ingeniería Civil + Ambiental | ecomagsas.com | Pendiente | — | Completo |
| Multiservicios P&J | Transporte + Obras + Ambiental | multiserviciospj.com | Hostinger | Microsoft 365 | En producción |
| PORON S.A.S | Por definir | poronsas.com | Pendiente | — | Dominio activo |
| COICEM | Por definir | coisem.com | Pendiente | — | Dominio activo |

### Identidad visual por proyecto (NO repetir entre proyectos)

| Aspecto | ECOMAG | Multiservicios P&J | YaDev Portfolio |
|---------|--------|-------------------|-----------------|
| Paleta | Verde #1B5E20 + Azul #0277A8 | Azul #0089D0 + Verde #005B32 | Indigo/Purple dark #0a0a0b |
| Hero | Full-height, 7 hojas SVG flotantes | Split-screen geométrico | Gradient mesh orbs + dot-grid |
| Cursor | Hoja verde animada | Engranaje mecánico | Default |
| Cards | Solid white, elevation hover | Solid white, border hover | Glass panels, backdrop-blur |
| Transiciones | Wave SVG orgánicas | Wave + diagonal | Fade + scale |
| Servicios | Grid 3-col con reveal | Zigzag alternado L-R | Glass cards 4-col |
| Footer | 4 columnas + certificaciones | CTA banner + 4 cols + Bureau Veritas | Minimal 1 línea |
| Tipografía | Plus Jakarta Sans + Inter | Plus Jakarta Sans + Inter | Space Grotesk + Inter |
| Animaciones | Spring bounce + float | Cubic-bezier smooth | Gradient orbs + marquee |

---

## ENTREGABLES ESTÁNDAR POR CLIENTE

Cada proyecto SIEMPRE incluye estos 8 entregables:

1. **Sitio web** — Astro SPA con Svelte interactivo
2. **Brandbook HTML** — Autocontenido con base64, exportable a PDF, formato A4
3. **Firma de correo HTML** — Logo base64 embebido
4. **Hoja membretada HTML** — Print-ready A4 (opcional)
5. **Panel YaDev** — Sidebar oculto con links a brandbook/firma
6. **SEO completo** — Schema.org (LocalBusiness, Organization, FAQPage, Services, BreadcrumbList), Open Graph, Twitter Cards, sitemap, robots.txt, geo meta tags
7. **Formulario de contacto** — 2 botones: email (PHP mail()) + WhatsApp (formateado)
8. **OG Image** — 1200x630, logo grande centrado, fondo blanco/marca

---

## REGLAS CRÍTICAS

### 1. DISEÑO ÚNICO POR PROYECTO
Cada sitio debe parecer hecho por una agencia diferente con un director creativo diferente.

**Lo que define la marca del CLIENTE** (puede coincidir entre proyectos):
- Colores, tipografía, logo → los define la identidad corporativa del cliente

**Lo que DEBE ser único por proyecto** (nuestra responsabilidad):
- Estructura/layout de secciones
- Estilo de hero (split, centered, full-video, parallax, immersive, etc.)
- Patrón de grids/cards (bento, zigzag, masonry, carousel, timeline, etc.)
- Tipo de animaciones (fade-up, slide-left, scale-in, blur-in, clip-reveal, etc.)
- Hover effects (lift, glow, tilt 3D, border-color, expand, etc.)
- Estilo de navbar (floating, transparent, sidebar, pill, sticky, etc.)
- Estilo de footer (mega, minimal, CTA banner, mapa, etc.)
- Cursor personalizado (por industria)
- Transiciones entre secciones (waves, diagonal, sharp, gradient, etc.)

**Test final:** Si dos sitios puestos lado a lado parecen del mismo diseñador → REDISEÑAR

### 2. NO PARECER IA
- Agregar asimetría intencional, espaciado no-uniforme
- Micro-interacciones únicas con propósito
- Fotografía real del cliente, NO stock genérico
- Animaciones sutiles, NO decorativas
- Tipografía que refleje el sector
- Evitar: gradient buttons idénticos, cards con misma sombra, headers centrados iguales
- Cada sección debe tener personalidad propia

### 3. COMPATIBLE CON HOSTINGER
Aplicar SIEMPRE desde el inicio:

```
# astro.config.mjs
build: { assets: 'assets' }     // NUNCA _astro/ (Hostinger lo bloquea)
configFile: fileURLToPath(...)   // Fix para rutas con & o espacios

# .htaccess
AddType text/css .css            // MIME types explícitos
AddType application/javascript .js
NO usar Content-Security-Policy  // Hostinger lo sobreescribe → bloquea CSS

# Navbar
Usar logo.png NO logo.svg       // SVG se rompe sin CSS

# Formulario
Usar PHP mail() NO SMTP          // Puerto 587 bloqueado en Hostinger

# Tailwind
Rutas con & o espacios → fileURLToPath con forward slashes
```

### 4. PANEL YADEV OBLIGATORIO
Cada sitio debe incluir un botón lateral oculto con acceso a:
- Brandbook HTML
- Firma de correo HTML
- Hoja membretada (si aplica)

### 5. TOKENS SINCRONIZADOS
Si cambias colores en el sitio → actualizar brandbook + firma + tokens.ts

---

## AGENTES DISPONIBLES

### Configurados (.claude/agents/)

| Agente | Cuándo usar |
|--------|-------------|
| `code-reviewer` | Revisión de calidad de código antes de deploy |
| `content-marketer` | Estrategia de contenido, textos SEO, copy |
| `devops-engineer` | CI/CD, deployment, Docker, infraestructura |
| `frontend-developer` | Construcción de componentes, CSS, layouts |
| `security-auditor` | Auditoría de seguridad, headers, validación |
| `seo-specialist` | Schema.org, meta tags, keywords, sitemap |

### Built-in (siempre disponibles)

| Agente | Cuándo usar |
|--------|-------------|
| `Explore` | Buscar archivos, entender código antes de modificar |
| `Plan` | Planificar tareas de 4+ archivos |
| `general-purpose` | Ejecutar múltiples cambios en paralelo |

### Regla de uso
- **1-3 archivos:** Explore → Ejecutar → Revisar
- **4-10 archivos:** Explore → Plan → general-purpose en paralelo → Revisar
- **Cliente nuevo:** Plan → Brand → UI → SEO → Deploy (ver workflow abajo)

---

## SKILLS DISPONIBLES

| Skill | Cuándo usar |
|-------|-------------|
| `ui-ux-pro-max` | Decisiones de diseño: paletas, tipografía, layouts, componentes (67 estilos, 96 paletas, 57 tipografías) |
| `nano-banana-2` | Generación de imágenes: hero backgrounds, mockups, assets |
| `simplify` | Revisión y limpieza de código antes de deploy |
| `claude-api` | Integración de IA en proyectos de clientes |

---

## WORKFLOW: CLIENTE NUEVO

```
PASO 1 — ANÁLISIS
├── Recibir: nombre empresa, industria, servicios, colores, logo, contacto
├── Explore: verificar qué proyectos ya existen en el portafolio
├── Definir: qué diseño/layout será DIFERENTE a los existentes
└── Plan: estructura completa del proyecto

PASO 2 — SETUP
├── Copiar templates de /design-system/ al nuevo proyecto
├── Reemplazar PLACEHOLDERs (colores, nombre, URL, servicios)
├── Configurar astro.config.mjs (con fixes de Hostinger)
└── Instalar dependencias

PASO 3 — BRANDING
├── Generar brandbook HTML (logo variants, paleta, tipografía, papelería)
├── Generar firma de correo HTML (logo base64)
├── Generar hoja membretada HTML (opcional)
└── Generar OG image (1200x630, logo centrado)

PASO 4 — DESARROLLO WEB
├── Hero (DIFERENTE a otros proyectos)
├── Navbar (DIFERENTE estilo)
├── Secciones: About, Services, Benefits/Stats, Projects/Clients, Contact
├── Footer (DIFERENTE layout)
├── Cursor personalizado (por industria)
├── Animaciones únicas
├── WhatsApp button con mini-formulario
├── Formulario de contacto (2 botones: email + WhatsApp)
└── Panel YaDev (sidebar oculto)

PASO 5 — OPTIMIZACIÓN
├── SEO: Schema.org, Open Graph, Twitter Cards, sitemap, robots.txt
├── Imágenes: logos 400px+ para retina, image-rendering optimize-contrast
├── Performance: lazy loading, fetchpriority hero, preconnect fonts
├── Accesibilidad: WCAG AA, focus-visible, skip-to-content, aria-labels
└── reCAPTCHA badge oculto via CSS

PASO 6 — DEPLOY
├── Build: npm run build (verificar assets/ no _astro/)
├── Subir dist/ a Hostinger public_html/
├── Verificar .htaccess (sin CSP, con MIME types)
├── Configurar DNS: SPF + DKIM + DMARC (si usa M365)
├── SSL: cubrir dominio + www
├── Purgar caché Hostinger
├── Facebook Debug scrape (actualizar OG para WhatsApp)
├── Test en incógnito
└── Google Search Console: enviar sitemap
```

---

## ASSETS DE DISEÑO DISPONIBLES

| Recurso | Cantidad | Ubicación | Uso |
|---------|----------|-----------|-----|
| Templates HTML | 11 industrias | `proyectos/` | Referencia de estructura |
| Temas CSS | 30 variantes | `assets/css/templates/` | Estilos por industria |
| Modelos referencia | 20 archivos | `Modelos/` | Inspiración (competencia real) |
| Design tokens | 1 template | `design-system/tokens-template.ts` | Base para nuevos proyectos |
| Prompt reutilizable | 705 líneas | `PROMPT_ECOMAG_WEBSITE.md` | Spec completa de componentes |
| Boilerplate completo | 8 archivos | `design-system/` | Setup inmediato |
| Catálogo cruzado | INDEX.md | `Modelos/INDEX.md` | Mapeo industria → modelo → CSS |

### Quick-pick por industria

| Industria | Tipografía Display | Colores | CSS template | Personalidad |
|-----------|-------------------|---------|-------------|--------------|
| Construcción | Space Grotesk | Amber #f59e0b | construccion-*.css | Brutalist, ángulos fuertes |
| E-commerce | Clash Display | Cream/gold #C4A265 | ecommerce-*.css | Editorial luxury |
| Eléctrico | Inter | Yellow #ffcb36 | electrico-*.css | Técnico, corporate |
| Forestal | Playfair Display | Green #166534 | forestal-*.css | Editorial orgánico |
| Salud | DM Sans | Teal #0891b2 | salud-*.css | Clinical clean |
| Tecnología | Satoshi + JetBrains Mono | Indigo #6366f1 | tecnologia-*.css | Glassmorphism SaaS |
| Transporte | Outfit + JetBrains Mono | Navy #0B1120, orange #FF6B35 | transporte-*.css | Logistics dashboard |
| Restaurante | Playfair Display + Lato | Terracotta #C44D23 | restaurante-*.css | Warm editorial |
| Inmobiliaria | Cormorant Garamond + Nunito Sans | Midnight #1B2A4A, gold #C9A96E | inmobiliaria-*.css | Elegant property |
| Educación | Merriweather + Open Sans | Navy #1A365D, green #38A169 | educacion-*.css | Institutional clean |
| Legal | Libre Baskerville + Source Sans Pro | Slate #1E293B, burgundy #7C2D36 | legal-*.css | Conservative authority |

---

## CONFIGURACIÓN DNS (Referencia para M365 + Hostinger)

Cuando el cliente usa Microsoft 365 para correo + Hostinger para web:

```
# Web
ALIAS  @    → dominio.com.cdn.hstgr.net
CNAME  www  → www.dominio.com.cdn.hstgr.net

# Correo (Microsoft 365)
MX     @    → dominio-com.mail.protection.outlook.com (prioridad 10)
TXT    @    → MS=msXXXXXXXX (verificación)
TXT    @    → v=spf1 include:spf.protection.outlook.com include:_spf.mail.hostinger.com ~all

# DKIM (security.microsoft.com/dkimv2)
CNAME  selector1._domainkey → selector1-dominio-com._domainkey.TENANT.q-v1.dkim.mail.microsoft
CNAME  selector2._domainkey → selector2-dominio-com._domainkey.TENANT.q-v1.dkim.mail.microsoft

# DMARC
TXT    _dmarc → v=DMARC1; p=none; rua=mailto:admin@dominio.com
```

---

## PROBLEMAS CONOCIDOS Y SOLUCIONES

| # | Problema | Causa | Solución |
|---|----------|-------|----------|
| 1 | CSS no carga en Hostinger | Carpeta `_astro/` bloqueada | `build: { assets: 'assets' }` |
| 2 | Tailwind no genera clases | `&` en ruta rompe glob | `fileURLToPath` + forward slashes |
| 3 | CSP bloquea CSS | Hostinger sobreescribe headers | NO usar CSP en .htaccess |
| 4 | Logo SVG gigante | SVG ignora width/height sin CSS | Usar PNG en navbar |
| 5 | SMTP no envía | Puerto 587 bloqueado | Usar `mail()` nativo |
| 6 | OG borrosa en WhatsApp | Thumbnail cuadrado recortado | Solo logo centrado, 1200x630 |
| 7 | Logos pixelados | Imágenes < 200px | Mínimo 400px, optimize-contrast |
| 8 | Email "no verificable" | Sin SPF/DKIM/DMARC | Configurar los 3 en DNS |
| 9 | reCAPTCHA badge visible | CSS no lo oculta | `.grecaptcha-badge { visibility: hidden }` |
| 10 | www no tiene SSL | Cert no cubre www | Activar SSL para ambos en Hostinger |

---

## REGLAS DE CÓDIGO

### Svelte/Astro
1. **Svelte 5 syntax** — Usar `$state`, `$effect`, `$derived`. NO usar `let` reactivo legacy.
2. **Astro scoped styles** — CSS en `<style>` dentro de cada `.astro`. No Tailwind inline en Astro.
3. **Svelte + Tailwind** — OK usar clases Tailwind en `.svelte` components.
4. **No hardcodear paths** — Usar `import.meta.env.BASE_URL` o `basePath` variable.
5. **Design tokens** — Definir en `tokens.ts`, exportar como CSS variables.

### HTML/Tailwind (descubierto en auditorías)
6. **Tailwind weight classes** — Usar `font-bold` (700), `font-extrabold` (800), `font-semibold` (600). NUNCA `font-700` o `font-800` (no son clases válidas de Tailwind).
7. **`<main>` obligatorio** — SIEMPRE envolver el contenido principal en `<main id="main-content">`.
8. **Skip-to-content** — SIEMPRE agregar `<a href="#main-content" class="sr-only focus:not-sr-only">Ir al contenido</a>` como primer hijo de `<body>`.
9. **Alt text** — TODA imagen `<img>` debe tener `alt` descriptivo. Fotos de equipo: incluir nombre + rol.
10. **Nav aria-label** — Si hay múltiples `<nav>`, cada uno debe tener `aria-label` único.

### Imágenes
11. **Lazy loading** — `loading="lazy"` en TODA imagen below-the-fold. Hero con `fetchpriority="high"`.
12. **Fotos de equipo** — Máximo 100KB. Comprimir antes de incluir.
13. **Logos** — Mínimo 400px wide, PNG con transparencia, `image-rendering: -webkit-optimize-contrast`.
14. **OG image** — 1200x630, solo logo centrado, fondo blanco, JPEG 95%.

### SEO (obligatorio en CADA página)
15. **`<title>`** — Descriptivo con keywords + ubicación.
16. **`<meta name="description">`** — 150-160 caracteres, NUNCA omitir.
17. **Schema.org JSON-LD** — `LocalBusiness` + tipo específico (ConstructionCompany, Restaurant, etc.).
18. **Open Graph** — `og:title`, `og:description`, `og:image`, `og:type`, `og:url` en CADA página.
19. **`lang="es-CO"`** — Siempre presente en `<html>`.
20. **WhatsApp button** — Presente en CADA página.

### Templates HTML (proyectos/)
21. **NO usar `onmouseover`/`onmouseout` inline** — Usar CSS `:hover` o event listeners.
22. **NO cargar imágenes externas (Unsplash)** — Usar CSS gradients como placeholders o imágenes locales.
23. **Google Fonts** — Usar nombres actualizados (Source Sans 3, no Source Sans Pro).
24. **Preconnect** — Agregar `<link rel="preconnect">` para Google Fonts Y Tailwind CDN.

### Contacto YaDev (datos reales)
- WhatsApp principal: +57 300 477 3174
- WhatsApp secundario: +57 300 752 8265
- Email: yadevsistem@gmail.com
- NUNCA inventar números de teléfono o emails

---

## MEMORIA PERSISTENTE

Las memorias de conversaciones anteriores están en:
`C:\Users\ASUS\.claude\projects\C--Users-ASUS-APP-YaDevportfolio\memory\`

Consultar antes de tomar decisiones para no repetir errores ya resueltos.
