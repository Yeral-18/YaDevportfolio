# YaDev Portfolio — Master Resource Index

**Last updated:** 2026-03-18
**Purpose:** Catalog of all design reference models, CSS templates, and HTML project demos. Use this document to select the right combination of resources before starting any new client site.

---

## Table of Contents

1. [Design Models (Modelos/)](#1-design-models)
   - [Electrical / RETIE](#11-electrical--retie-certification)
   - [Transport / Logistics](#12-transport--logistics)
   - [Technology](#13-technology--software)
   - [Oil & Gas / Energy Corporate](#14-oil--gas--energy-corporate)
   - [CMS / Admin Tools](#15-cms--admin-tools)
2. [CSS Templates (assets/css/templates/)](#2-css-templates)
   - [Transporte](#21-transporte-3-variants)
   - [Eléctrico](#22-eléctrico-5-variants)
   - [Construcción](#23-construcción-3-variants)
   - [Forestal](#24-forestal-3-variants)
   - [Salud](#25-salud-3-variants)
   - [Tecnología](#26-tecnología-5-variants)
   - [E-commerce](#27-e-commerce-3-variants)
   - [Restaurante](#28-restaurante-1-variant)
   - [Inmobiliaria](#29-inmobiliaria-1-variant)
   - [Educación](#210-educación-1-variant)
   - [Legal](#211-legal-1-variant)
3. [HTML Project Demos (proyectos/)](#3-html-project-demos)
4. [Cross-Reference Matrix](#4-cross-reference-matrix)
5. [How to Use](#5-how-to-use)

---

## 1. Design Models

Design Models are raw HTML source files scraped from real-world websites. They serve as layout and UX reference material — study their structure, navigation patterns, hero sections, and content hierarchy. Do NOT copy their code directly.

### 1.1 Electrical / RETIE Certification

---

**Modelo1.txt**
- **Source site:** ODIR Certificaciones (odircertificaciones.com)
- **Industry:** Electrical / RETIE-RETILAP certification
- **Hero style:** Full-width image hero with top navigation bar
- **Nav style:** Fixed top navbar, horizontal links, CTA button
- **Grid pattern:** Services listed in icon-card columns (3-col grid)
- **Typography:** Standard sans-serif, yellow (#ffcb36) accent color
- **Key design features:**
  - Yellow brand color dominates CTAs and highlights
  - Google Analytics + Tag Manager integration pattern
  - Standard Bootstrap-era layout
  - Prominent phone/WhatsApp CTA in header
  - Trust signals: ONAC accreditation badges
- **Platform:** Custom PHP/Bootstrap

---

**Modelo2.txt**
- **Source site:** Ingenio Electrocivil (ingenioelectrocivil.com)
- **Industry:** Electrical and civil engineering services
- **Hero style:** Full-width hero with overlay text, slider
- **Nav style:** Fixed transparent-to-solid navbar on scroll
- **Grid pattern:** Services grid with icon cards
- **Typography:** Poppins 300/400/500/600/700
- **Key design features:**
  - Dual focus: electrical AND civil works
  - Phase-based service presentation (estudios, diseño, construcción, legalización)
  - Clean professional tone
  - Uses Metronic admin panel internally (see Editor Modelo2.txt)
- **Platform:** Laravel + Metronic theme

---

**Modelo15 ELECTRICO.txt**
- **Source site:** Enel X Colombia (enelx.com/co/es)
- **Industry:** Corporate electrical certification — large enterprise
- **Hero style:** Full-width corporate hero with gradient overlay, centered CTA
- **Nav style:** Horizontal mega-menu with dropdowns, Enel X brand colors
- **Grid pattern:** 3-step process cards (horizontal), then feature blocks
- **Typography:** Custom Enel corporate font + system fallbacks
- **Key design features:**
  - Enterprise-level trust and authority layout
  - RETIE-focused landing page structure
  - Large format headings with benefit-first copy
  - Adobe AEM CMS platform signatures
  - Strong green (#00a651) corporate identity
  - Accreditation and compliance emphasis
- **Platform:** Adobe AEM (Enterprise CMS)
- **Best for:** Reference when client needs to project large-company authority

---

**Modelo16 ELECTRICO.txt**
- **Source site:** RIG Colombia / Retie Ingeniería y Gestión (retieingenieriaygestion.com)
- **Industry:** RETIE/RETILAP inspection and certification
- **Hero style:** Full-width hero with background image, headline + CTA
- **Nav style:** Fixed top navbar, white background, colored logo
- **Grid pattern:** Services as cards with icons, 3-column layout
- **Typography:** Standard web fonts via Google Fonts
- **Key design features:**
  - Focused on "empresa certificadora" keyword positioning
  - Gallery section for completed certification jobs
  - WordPress + Yoast SEO structure
  - W3 Total Cache optimizations visible
  - Trust signals: years of experience counter
  - Blog/news section for content marketing
- **Platform:** WordPress with custom theme + Elementor-adjacent plugins

---

**Modelo17 ELECTRICO.txt**
- **Source site:** Certiretie S.A.S. (certiretie.com)
- **Industry:** RETIE / RETILAP / RITEL inspection organism
- **Hero style:** Split hero — text left, certification badge image right
- **Nav style:** Sticky top navbar, white, logo left, links right
- **Grid pattern:** About page with image + text blocks alternating
- **Typography:** Clean sans-serif, blue corporate color
- **Key design features:**
  - ONAC accreditation highlighted prominently
  - "Nosotros" page reference — shows team/about structure
  - Minimal design, content-first approach
  - Social proof: Facebook community link
  - Breadcrumb navigation for SEO
- **Platform:** WordPress + Yoast SEO

---

**Modelo18 ELECTRICO.txt**
- **Source site:** Wix-built electrical service company (Colombia)
- **Industry:** Electrical services / RETIE certification
- **Hero style:** Full-screen Wix hero with parallax background
- **Nav style:** Wix transparent sticky navbar, pill-style buttons
- **Grid pattern:** Wix strips / horizontal bands per section
- **Typography:** Wix default fonts
- **Key design features:**
  - Wix platform signature patterns (parastorage CDN)
  - Each section is a full-width horizontal strip
  - Simple, non-developer layout
  - WhatsApp contact integration
  - Mobile-first Wix responsive behavior
- **Platform:** Wix Website Builder
- **Best for:** Reference for clients coming FROM Wix who need migration

---

### 1.2 Transport / Logistics

---

**Modelo11 TRANSPORTE.txt**
- **Source site:** Kuehne+Nagel (kuehne-nagel.com)
- **Industry:** International freight forwarding / supply chain — global enterprise
- **Hero style:** Full-width dark video/image hero, headline centered, search bar below
- **Nav style:** Two-tier horizontal navbar — top utility bar + main navigation with mega menus
- **Grid pattern:** Service tiles in 2x2 or 3x3 grid, then horizontal feature strips
- **Typography:** SuisseIntl (custom) — regular + semibold only (minimalist)
- **Key design features:**
  - Global freight company scale — multiple services (sea, air, road, contract logistics)
  - Search functionality integrated in hero
  - Nuxt.js / Vue-based SPA architecture
  - Dark, authoritative color palette
  - Language selector in nav (multilingual)
  - Solutions organized by industry vertical
- **Platform:** Nuxt.js (Vue 3)
- **Best for:** High-end logistics company wanting global enterprise feel

---

**Modelo12 TRANSPORTE.txt**
- **Source site:** Dispetrocom (dispetrocom.com)
- **Industry:** Transport and distribution of petroleum-derived liquid products
- **Hero style:** Full-width hero with background image + centered overlay text + CTA
- **Nav style:** WordPress sticky navbar
- **Grid pattern:** Services in horizontal cards, stats counter section
- **Typography:** Elementor default fonts
- **Key design features:**
  - Petroleum/fuels sector specialist positioning
  - National distribution network emphasis
  - Revolution Slider for hero carousel
  - amCharts.js integration for coverage maps
  - WordPress + Elementor page builder
  - Premium Addons for Elementor (particle effects, etc.)
- **Platform:** WordPress + Elementor + Revolution Slider

---

**Modelo13 TRANSPORTE.txt**
- **Source site:** OPL Carga (oplcarga.com)
- **Industry:** Sustainable road transport / green logistics — Colombia
- **Hero style:** Split-screen or full-width hero with responsive video background
- **Nav style:** HubSpot-generated sticky top navbar
- **Grid pattern:** Services by sector in icon cards, then sustainability stats
- **Typography:** HubSpot theme fonts
- **Key design features:**
  - "Pioneros en transporte sostenible" — green logistics differentiation
  - Sectors served highlighted (construction, mining, food, etc.)
  - HubSpot CMS — contact forms integrate with CRM
  - Responsive Video module prominent in hero area
  - Environmental/sustainability messaging throughout
- **Platform:** HubSpot CMS
- **Best for:** Transport clients wanting to emphasize green credentials

---

**Modelo14 TRANSPORTE.txt**
- **Source site:** Grupo Frimac (grupofrimac.com)
- **Industry:** Logistics and supply chain solutions — Colombia
- **Hero style:** Multi-section header with top info bar + main header + Bootstrap carousel
- **Nav style:** Bootstrap 3 dual-level header — info bar top + branded navbar + secondary nav
- **Grid pattern:** OWL Carousel for featured content, Bootstrap grid for services
- **Typography:** Bootstrap default + Font Awesome icons
- **Key design features:**
  - Bilingual support (ESP/ENG toggle)
  - "Comunidad Frimac" loyalty/community section
  - Fancybox modal for community popup
  - Multiple header zones: contact info bar + brand bar + nav bar
  - Counter/stats section with animation (CounterUp.js)
  - Custom scrollbar (mCustomScrollbar)
  - Animate.css scroll reveal effects
- **Platform:** Custom HTML + Bootstrap 3 + jQuery
- **Best for:** Reference for complex multi-section header patterns

---

**Modelo19 TRANSPORTE.txt**
- **Source site:** Not explicitly identified (custom-built)
- **Industry:** Transport / logistics services
- **Hero style:** Full-width hero with Bootstrap carousel
- **Nav style:** Bootstrap 3 fixed top navbar
- **Grid pattern:** Bootstrap 3 grid, services in columns
- **Typography:** Bootstrap default sans-serif
- **Key design features:**
  - Classic Bootstrap 3 era transport site structure
  - OWL Carousel for testimonials/partners
  - Animate.css entrance animations
  - jQuery Fancybox for gallery/lightbox
  - Counter animations for stats section
  - Contact form section at bottom
- **Platform:** Custom HTML + Bootstrap 3

---

### 1.3 Technology / Software

---

**Modelo 7.txt**
- **Source site:** Neuralink (neuralink.com)
- **Industry:** Deep technology / brain-computer interfaces
- **Hero style:** Full-screen dark immersive hero — single product image, minimal text
- **Nav style:** Transparent overlay navbar, links right-aligned, ultra minimal
- **Grid pattern:** Vertical storytelling — full-screen sections, one idea per screen
- **Typography:** Custom sans-serif; minimal weight variation
- **Key design features:**
  - Dark/black dominant aesthetic (#000000 background)
  - Single focused message per section — no content overload
  - High-impact product photography as visual language
  - Apple-style scroll-based storytelling
  - Minimal navigation — logo left, 3-4 links + CTA
  - React/Vite SPA architecture
  - No footer distractions — CTA focused
- **Platform:** React + Vite (custom build)
- **Best for:** Premium tech company wanting "Apple-like" gravitas

---

**Modelo 8.txt**
- **Source site:** SpaceX (spacex.com)
- **Industry:** Aerospace / advanced technology — iconic brand
- **Hero style:** Full-screen black video/image background, white text centered, NO scrolling content above the fold
- **Nav style:** Transparent fixed navbar, minimal 5 links, all white on black
- **Grid pattern:** Full-width horizontal sections — each section is full-viewport height
- **Typography:** D-DIN custom typeface — geometric, military-grade aesthetic
- **Key design features:**
  - All sections are full-screen (100vh) — maximum visual impact
  - Video backgrounds for each mission/product section
  - Extreme minimalism: black, white, custom font — no color accents
  - Angular app (Angular framework)
  - No sidebar, no complex grids — pure linear vertical scroll
  - Each product gets its own full-screen section
  - CSS custom properties for white opacity variants
- **Platform:** Angular (SPA)
- **Best for:** Reference for maximum visual impact with minimal UI chrome

---

**Modelo10 cmp-carousel__content LIKE.txt**
- **Source site:** Intel Latin America (intel.la)
- **Industry:** Enterprise technology / semiconductors / AI
- **Hero style:** Multi-panel carousel with animated content slides
- **Nav style:** Intel global navigation — horizontal mega-menu, multi-level dropdowns
- **Grid pattern:** "cmp-carousel" component system — content cards in carousels
- **Typography:** Intel Display + Intel Text custom fonts
- **Key design features:**
  - Component-based AEM architecture (cmp- CSS class prefix)
  - Carousel as primary content delivery mechanism
  - AI-focused messaging ("Intel Inside: creado para la IA")
  - Multi-language support (es-XL Latin America)
  - Performance-optimized asset loading (WAP config pattern)
  - Rich structured data (Schema.org WebPage + Organization)
  - Dark background for tech credibility
- **Platform:** Adobe AEM (Enterprise CMS)
- **Best for:** Reference for carousel/slider content architecture and mega-menu patterns

---

**Modelo 9.txt** (Large file — 107k tokens)
- **Source site:** Facebook (facebook.com) — internal login/feed page
- **Industry:** Social media platform
- **Hero style:** N/A (authenticated app interface)
- **Nav style:** Facebook top navbar — fixed, blue, search + icons
- **Grid pattern:** Two-column feed layout
- **Typography:** Optimistic Display (Facebook custom font)
- **Key design features:**
  - Reference for complex JS asset loading architecture
  - Multi-hundred JS bundle splitting pattern
  - React + Relay data fetching architecture signals
  - Highly optimized preload/prefetch strategy
- **Platform:** React + Relay (Meta internal stack)
- **Best for:** Technical reference only — JS bundle splitting and preload patterns

---

### 1.4 Oil & Gas / Energy Corporate

---

**Modelo 5.txt**
- **Source site:** GeoPark (geo-park.com/es)
- **Industry:** Oil and gas exploration / corporate investor relations
- **Hero style:** Full-width editorial hero with anniversary imagery, centered text overlay
- **Nav style:** Hamburger overlay menu on all screen sizes (custom geopark hamburger), plus language switcher
- **Grid pattern:** OWL Carousel for featured content, custom grid for sustainability data
- **Typography:** Manrope 400/500/600 (Google Fonts)
- **Key design features:**
  - Always-hamburger navigation (unusual choice for desktop — creates premium feel)
  - Multilingual: Spanish/English via WPML
  - Sustainability section with data visualization
  - Social share (AddToAny)
  - Intranet access button in nav
  - LinkedIn + YouTube social prominence
  - WordPress custom theme (geopark theme)
  - Cloudflare CDN + Autoptimize
- **Platform:** WordPress + Custom geopark theme + WPML
- **Best for:** Energy/oil company wanting editorial, investor-focused presentation

---

**Modelo 6.txt**
- **Source site:** Unknown electrical/engineering company (Wix-built, Colombia)
- **Industry:** Engineering / electrical services
- **Hero style:** Wix full-screen Wix hero section
- **Nav style:** Wix platform navbar with scroll behavior
- **Grid pattern:** Wix strip-based layout
- **Typography:** Wix default font system
- **Key design features:**
  - Wix platform — same patterns as Modelo18
  - Origin trials script loading (Wix performance feature)
  - Mobile-first Wix breakpoints
  - Simple content for small service company
- **Platform:** Wix Website Builder
- **Note:** Secondary Wix reference, similar to Modelo18

---

### 1.5 CMS / Admin Tools

---

**Editor Modelo1.txt**
- **Source site:** Damos Soluciones CMS editor (internal tool)
- **Industry:** Internal CMS admin panel (not client-facing)
- **Hero style:** N/A — admin dashboard layout
- **Nav style:** Sidebar admin navigation with card-based item menu
- **Grid pattern:** Card grid with icon + label items (item-menu class)
- **Typography:** Open Sans Condensed 700 + Medula One (Google Fonts)
- **Key design features:**
  - Content management module selector
  - Radial shadow card hover effects
  - 180px fixed-width icon menu cards
  - Modal overlays for content editing
  - Fancybox for media library
- **Platform:** Custom PHP CMS (Damos Soluciones internal)
- **Best for:** Reference for CMS admin panel layout and card-selector UI

---

**Editor Modelo2.txt**
- **Source site:** Metronic-based admin panel for Ingenio Electrocivil
- **Industry:** Internal CMS for electrical company website
- **Hero style:** N/A — admin interface
- **Nav style:** Metronic 7.2.1 — aside/sidebar dark + light header
- **Grid pattern:** Metronic DataTables grid layout
- **Typography:** Poppins 300/400/500/600/700
- **Key design features:**
  - Metronic 7.2.1 admin theme (KTMenu, KTDrawer)
  - Dark sidebar + light header combination
  - Slim.js file upload component
  - DataTables integration
  - Laravel CSRF token integration
- **Platform:** Laravel + Metronic 7.2.1 admin theme
- **Best for:** Reference for admin dashboard patterns using Metronic

---

**Modelo 3/** (Directory — PHP site)
- **Source site:** Full PHP website (multi-page structure)
- **Industry:** Professional services / certification (based on file structure)
- **Hero style:** PHP-rendered slider (top/slider.php)
- **Nav style:** PHP-included navbar (design/navbar.php)
- **Grid pattern:** Modular PHP include system
- **Typography:** Loaded via head.php include
- **Key design features:**
  - Full PHP template architecture — head, navbar, footer as includes
  - Bootstrap 3 jQuery counterUp for stats animations
  - Waypoints.js for scroll-triggered animations
  - Modular content: txtindex, service_index, txtcifras, txtclientes
  - Contact form module (txtcontact_ind.php)
  - Bootstrap Select for dropdowns
  - CounterUp.js for animated statistics
- **Platform:** PHP + Bootstrap 3 + jQuery
- **Best for:** Reference for modular PHP site architecture and stats counter pattern

---

**Modelo 5.txt** *(already listed above under Oil & Gas — dual relevance)*

---

## 2. CSS Templates

CSS Templates are plug-in style sheets for the YaDev HTML project system. Apply them by adding the class name to the `<html>` or `<body>` element. Each template is self-contained and overrides the base YaDev styles.

### 2.1 Transporte (3 variants)

| File | Class | Style | Palette | Key Differentiator |
|------|-------|-------|---------|-------------------|
| `transporte-corporate.css` | `template-transporte-corporate` | Corporate dark | Navy #0f172a + Blue #3b82f6 + Cyan #06b6d4 | Dark background, solid blue border-bottom on navbar, uppercase tracking on links |
| `transporte-modern.css` | `template-transporte-modern` | Glassmorphism | Cyan #06b6d4 + Sky #0ea5e9 + Purple #a855f7 | Light base, frosted glass cards, heavily rounded (pill buttons), blur effects |
| `transporte-split.css` | `template-transporte-split` | Minimal serif | Black #000000 + Gray #737373 on white | Extreme whitespace, serif typography, split-layout hero, editorial feel |

---

### 2.2 Eléctrico (5 variants)

| File | Class | Style | Palette | Key Differentiator |
|------|-------|-------|---------|-------------------|
| `electrico-modern.css` | `template-electrico-modern` | ODIR-inspired clean | White base + Yellow #ffcb36 | Dotted yellow bottom-border on navbar (8px repeating gradient), Inter 800 headings |
| `electrico-corporate.css` | `template-electrico-corporate` | Enel X corporate | Corporate green + white | Horizontal layout, 120px section padding, mega spacing, enterprise authority |
| `electrico-dark.css` | `template-electrico-dark` | Dark energy mode | Black #0d0d0d + surface #1a1a1a | Neon energy border effects, "voltage gradient" accents, premium dark mode |
| `electrico-dashboard.css` | `template-electrico-dashboard` | Admin panel / metrics | Dark blue #0f172a + slate #1e293b | Stats cards layout, dashboard grid, data-display focused |
| `electrico-tech.css` | `template-electrico-tech` | Futuristic / neon | Yellow #ffcb36 glow on dark | Dot-grid background, neon glow CSS shadows, asymmetric layout |

---

### 2.3 Construcción (3 variants)

| File | Class | Style | Palette | Key Differentiator |
|------|-------|-------|---------|-------------------|
| `construccion-blueprint.css` | `template-construccion-blueprint` | Blueprint / technical | Navy blue #1e3a5f + white lines + yellow #fbbf24 | Engineering grid background (CSS background-image grid), JetBrains Mono font |
| `construccion-brutalist.css` | `template-construccion-brutalist` | Brutalist raw | Black #000000 + white #ffffff | Thick borders, oversized typography, raw/unpolished aesthetic, high contrast |
| `construccion-industrial.css` | `template-construccion-industrial` | Industrial heavy | Orange #d97706 + dark stone #292524 | Asymmetric layout, bold typography, rough textures, orange accent |

---

### 2.4 Forestal (3 variants)

| File | Class | Style | Palette | Key Differentiator |
|------|-------|-------|---------|-------------------|
| `forestal-organic.css` | `template-forestal-organic` | Artisan / paper | Cream #faf7f2 + forest green #065f46 + brown #92400e | Paper texture via SVG noise filter, Georgia serif font, handcrafted feel |
| `forestal-dark.css` | `template-forestal-dark` | Dark forest / mystical | Deep green #0c1810 + surface #14281e | Firefly/bioluminescent glow effects, atmospheric dark, nature noir |
| `forestal-immersive.css` | `template-forestal-immersive` | Scroll storytelling | Emerald #059669 + bright #10b981 | Full-screen sections, scroll-triggered reveals, visual narrative, parallax |

---

### 2.5 Salud (3 variants)

| File | Class | Style | Palette | Key Differentiator |
|------|-------|-------|---------|-------------------|
| `salud-clean.css` | `template-salud-clean` | Ultra-minimal clinical | White #ffffff + cyan #0891b2 + teal #0d9488 | Floating navbar (rounded, centered, with box-shadow), Inter font, lots of breathing room |
| `salud-glass.css` | `template-salud-glass` | Glassmorphism medical | Cyan #06b6d4 + teal #14b8a6 on gradient bg | Frosted glass cards, backdrop-filter blur, gradient backgrounds |
| `salud-hospital.css` | `template-salud-hospital` | Institutional / clinical | Deep blue #0369a1 + dark blue #0c4a6e | Red cross accent, institutional grid, strong borders, healthcare authority |

---

### 2.6 Tecnología (5 variants)

| File | Class | Style | Palette | Key Differentiator |
|------|-------|-------|---------|-------------------|
| `tecnologia-light.css` | `template-tecnologia-light` | Apple / Stripe minimal | White #ffffff + surface #f8fafc | Generous whitespace, floating cards, subtle gradients, Inter font, clean |
| `tecnologia-neon.css` | `template-tecnologia-neon` | Cyberpunk / neon | Black #0a0a0a + neon green #00ff88 + pink #ff00ff + cyan #00ffff | Neon border glow (box-shadow), green dot-grid background, glitch aesthetics |
| `tecnologia-neumorphic.css` | `template-tecnologia-neumorphic` | Soft UI / 3D | Light gray #e8eef4 + white highlights | Neumorphic inset/outset shadows, soft 3D buttons, no hard borders |
| `tecnologia-dashboard.css` | `template-tecnologia-dashboard` | Data dashboard | Deep navy + grid lines + monospace | Stats cards, dashboard grid, data-display focused, monospace accents |
| `tecnologia-gradient.css` | `template-tecnologia-gradient` | Bold gradient (Linear-inspired) | Purple-to-blue gradients + glassmorphism | Glowing borders, luminous depth, glassmorphism, gradient backgrounds |

---

### 2.7 E-commerce (3 variants)

| File | Class | Style | Palette | Key Differentiator |
|------|-------|-------|---------|-------------------|
| `ecommerce-minimal.css` | `template-ecommerce-minimal` | Editorial minimal | Black #0a0a0a + white on white | Transparent navbar with extra padding (2rem), Inter font, large editorial headings |
| `ecommerce-dark.css` | `template-ecommerce-dark` | Dark premium store | Black #0a0a0a + surface #141414 | Glassmorphism product cards, neon accent on hover, dramatic shadows |
| `ecommerce-magazine.css` | `template-ecommerce-magazine` | Magazine editorial | Near-black #1a1a1a + white | Asymmetric grid, oversized typography, magazine-page column layouts |

---

### 2.8 Restaurante (1 variant)

| File | Class | Style | Palette | Key Differentiator |
|------|-------|-------|---------|-------------------|
| `restaurante-warm.css` | `template-restaurante-warm` | Warm editorial | Terracotta + rich textures | Warm tones, organic layout, terracotta accents, editorial food photography feel |

---

### 2.9 Inmobiliaria (1 variant)

| File | Class | Style | Palette | Key Differentiator |
|------|-------|-------|---------|-------------------|
| `inmobiliaria-elegant.css` | `template-inmobiliaria-elegant` | Navy + gold luxury | Navy blue + gold accents | Premium real estate aesthetic, luxury property presentation, gold accent details |

---

### 2.10 Educación (1 variant)

| File | Class | Style | Palette | Key Differentiator |
|------|-------|-------|---------|-------------------|
| `educacion-academic.css` | `template-educacion-academic` | Institutional academic | Blue + green institutional | Trustworthy, structured, scholarly feel, academic authority |

---

### 2.11 Legal (1 variant)

| File | Class | Style | Palette | Key Differentiator |
|------|-------|-------|---------|-------------------|
| `legal-classic.css` | `template-legal-classic` | Dark slate + burgundy | Dark slate + burgundy conservative | Authoritative, formal, serif-driven, conservative law firm aesthetic |

---

## 3. HTML Project Demos

These are the fully built demonstration projects in `/proyectos/`. Each is production-ready and uses the YaDev UI system (yadev-tokens.css, yadev-animations.css, yadev-topbar.css, yadev-cookies.css).

| File | Brand Name | Industry | Font Stack | Key Sections |
|------|-----------|----------|-----------|-------------|
| `transporte.html` | TransLogix | Transport / logistics | (YaDev default) | Hero + services + tracking + contact; Schema.org LocalBusiness |
| `electrico.html` | CertiPower | Electrical / RETIE-RETILAP-RITEL certification | (YaDev default) | Hero + certification types + process + contact; Schema.org LocalBusiness |
| `construccion.html` | Constructora Edificar | Construction | TailwindCSS inline config | Tailwind-first build; colors: construction amber #f59e0b, brutal-dark #1c1917 |
| `forestal.html` | EcoForest Solutions | Forestry / environment | Inter + Playfair Display | Swiper.js carousel; YaDev industry CSS (forestal.css) |
| `salud.html` | VitalCare Clinica | Health / medical | Inter + DM Sans | Swiper.js; YaDev industry CSS (salud.css) |
| `tecnologia.html` | NexaTech Solutions | Technology / SaaS | (YaDev default) | Schema.org SoftwareApplication; dark theme (#030712) |
| `ecommerce.html` | ShopStyle Store | E-commerce / retail | Inter | Swiper carousel + preloader; YaDev industry CSS (ecommerce.css) |
| `restaurante.html` | Casa Raices | Restaurant / fine dining | Playfair Display + Lato | Warm hero, menu section, reservations, gallery; food photography focus |
| `inmobiliaria.html` | Elite Propiedades | Real estate / properties | Cormorant Garamond + Nunito Sans | Property listings, search/filter, gallery, mortgage calculator |
| `educacion.html` | Universidad Academica Nacional | Education / academia | Merriweather + Open Sans | Programs, campus, admissions, testimonials; institutional authority |
| `legal.html` | Valcarcel & Asociados | Legal / law firm | Libre Baskerville + Source Sans Pro | Practice areas, team, case results, consultation booking; Schema.org |

**Shared infrastructure across all 11 demos:**
- `yadev-tokens.css` — design tokens (colors, spacing, radius, shadows)
- `yadev-animations.css` — scroll-reveal, hover, transition utilities
- `yadev-topbar.css` — fixed top announcement bar
- `yadev-cookies.css` — GDPR cookie consent banner
- `data-yadev-cookies` attribute activates cookie system
- `data-industry` attribute for analytics/targeting
- Swiper.js (CDN v11) for carousels where used

---

## 4. Cross-Reference Matrix

Use this matrix to match a client's industry to available Modelos (inspiration) and CSS Templates (styling).

| Industry | Modelos for Inspiration | CSS Templates Available | HTML Demo |
|----------|------------------------|------------------------|-----------|
| **Transport / Logistics** | Modelo11 (enterprise), Modelo13 (sustainable), Modelo14 (complex header), Modelo19 (classic Bootstrap) | corporate, modern, split | transporte.html |
| **Electrical / RETIE** | Modelo1 (ODIR), Modelo2 (Ingenio), Modelo15 (Enel X), Modelo16 (RIG), Modelo17 (Certiretie), Modelo18 (Wix) | modern, corporate, dark, dashboard, tech | electrico.html |
| **Construction** | Modelo 3 (PHP modular), Modelo14 (header patterns) | blueprint, brutalist, industrial | construccion.html |
| **Technology / SaaS** | Modelo 7 (Neuralink), Modelo 8 (SpaceX), Modelo10 (Intel carousel) | light, neon, neumorphic, dashboard, gradient | tecnologia.html |
| **Forestry / Environment** | Modelo 5 (GeoPark editorial), Modelo13 (OPL green transport) | organic, dark, immersive | forestal.html |
| **Health / Medical** | (no dedicated health models — use tecnologia or construccion for structural reference) | clean, glass, hospital | salud.html |
| **E-commerce** | Modelo 8 (SpaceX product sections as reference), Modelo10 (Intel carousel) | minimal, dark, magazine | ecommerce.html |
| **Restaurant / Gastronomy** | Modelo 5 (GeoPark editorial warmth), forestal-organic (artisan feel) | warm | restaurante.html |
| **Real Estate / Properties** | Modelo11 (enterprise nav), tecnologia-light (clean UI) | elegant | inmobiliaria.html |
| **Education / Academia** | Modelo15 (Enel X institutional), salud-clean (structured clean) | academic | educacion.html |
| **Legal / Law Firm** | Modelo 5 (GeoPark editorial), Modelo17 (Certiretie conservative) | classic | legal.html |
| **Oil & Gas / Corporate** | Modelo 5 (GeoPark), Modelo11 (Kuehne+Nagel global scale) | corporate variants from transporte/electrico | (custom) |

---

## 5. How to Use

### Standard Workflow for a New Client Website

```
Step 1: IDENTIFY INDUSTRY
  → Determine the client's sector from the matrix above

Step 2: STUDY DESIGN MODELS
  → Open the relevant Modelos from this index
  → Analyze: hero structure, nav pattern, content sections, typography weight
  → Note what makes their UX credible for that industry
  → Do NOT copy code — extract layout logic only

Step 3: SELECT CSS TEMPLATE
  → Choose one CSS template that fits the brand personality
  → Personality guide:
      Client is large/corporate  → corporate variants
      Client wants premium/dark  → dark variants
      Client wants modern/fresh  → modern or glassmorphism variants
      Client is artisan/organic  → organic variants
      Client is tech/startup     → light, neon, or neumorphic
      Client is editorial/store  → magazine or minimal

Step 4: CLONE THE HTML DEMO
  → Copy the relevant proyectos/*.html as starting point
  → Update data-industry attribute
  → Replace demo brand name, copy, and images
  → Apply selected CSS template class to <html> or <body>

Step 5: CUSTOMIZE TOKENS
  → Open: assets/css/yadev-tokens.css (or design-system/tokens.ts for Next.js)
  → Override color palette to match client brand
  → Adjust: primary color, secondary, accent, text, background
  → Keep spacing scale and radius — change only color temperature

Step 6: VERIFY UNIQUENESS
  → Compare with other recent sites in this portfolio
  → Confirm: different hero layout, different nav style, different grid pattern
  → Run the uniqueness checklist from CLAUDE.md before finalizing
```

### Quick-Pick Cheat Sheet by Visual Personality

| Client Brand Vibe | Recommended Template | Recommended Model Reference |
|------------------|---------------------|----------------------------|
| Dark & authoritative | `transporte-corporate` | Modelo11 (Kuehne+Nagel) |
| Clean & clinical | `salud-clean` | Modelo17 (Certiretie) |
| Premium & dark | `electrico-dark` or `ecommerce-dark` | Modelo 8 (SpaceX) |
| Futuristic / AI | `tecnologia-neon` or `electrico-tech` | Modelo 7 (Neuralink) |
| Minimal editorial | `transporte-split` or `ecommerce-minimal` | Modelo 8 (SpaceX) |
| Apple-like clean | `tecnologia-light` | Modelo 7 (Neuralink) |
| Technical blueprint | `construccion-blueprint` | Modelo10 (Intel) |
| Bold industrial | `construccion-industrial` | Modelo14 (Frimac) |
| Raw brutalst | `construccion-brutalist` | Modelo 8 (SpaceX) |
| Nature artisan | `forestal-organic` | Modelo 5 (GeoPark) |
| Nature immersive | `forestal-immersive` | Modelo13 (OPL green) |
| Glassmorphism | `transporte-modern` or `salud-glass` | Modelo 6 / Modelo18 |
| Neumorphic soft | `tecnologia-neumorphic` | (no specific model — UI reference) |
| Magazine editorial | `ecommerce-magazine` | Modelo 5 (GeoPark editorial) |
| Corporate enterprise | `electrico-corporate` | Modelo15 (Enel X) |
| Warm & inviting (food) | `restaurante-warm` | Modelo 5 (GeoPark editorial) |
| Luxury real estate | `inmobiliaria-elegant` | Modelo11 (Kuehne+Nagel) |
| Academic institutional | `educacion-academic` | Modelo15 (Enel X institutional) |
| Conservative law firm | `legal-classic` | Modelo17 (Certiretie) |
| Dashboard data-heavy | `tecnologia-dashboard` | Modelo10 (Intel) |
| Bold gradients SaaS | `tecnologia-gradient` | Modelo 7 (Neuralink) |

### Important Rules

1. Each client site must look like it was made by a different design agency — see `CLAUDE.md` section "REGLA CRITICA: Diseno Unico por Proyecto".
2. Modelos are **reference only** — do not reuse their HTML, classes, or assets.
3. CSS templates are **modular** — only one template per project.
4. Always update `data-industry` on the `<html>` tag for analytics consistency.
5. The `yadev-tokens.css` is the single source of truth for color — do not hardcode colors in component CSS.

---

**Current totals (2026-03-18):** 11 HTML demos, 29 CSS theme variants, 11 industry base CSS files, 20 design reference models.

*Index maintained by YaDev — update this file whenever new Modelos, CSS templates, or HTML demos are added.*
