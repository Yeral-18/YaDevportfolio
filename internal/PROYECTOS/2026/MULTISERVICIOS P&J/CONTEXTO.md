# CONTEXTO — MULTISERVICIOS P&J S.A.S

> Documento de contexto definitivo del proyecto web.
> Generado: 2026-06-12 · Estado: **⚰️ RETIRADO — reemplazado por LUQRA (rebrand)** · Ruta: `internal/PROYECTOS/2026/MULTISERVICIOS P&J`
>
> ⚠️ Este sitio se retira. El cliente continúa como **Luqra Ingeniería y Soluciones S.A.S** (`luqra.co`).
> Documento conservado como referencia histórica. Su ADN visual sigue registrado en
> `.claude/PROJECT_DNA_LOG.md` (no reutilizar cursor engranaje / split-screen / zigzag en nuevos clientes).

---

## 1. RESUMEN EJECUTIVO

Sitio web corporativo **en producción** para una empresa de ingeniería y servicios integrales del Magdalena Medio. Stack Astro 5 + Svelte 5 + Tailwind 3, desplegado en **Hostinger** bajo `multiserviciospj.com`. Incluye los 8 entregables estándar YaDev (web, brandbook, firma, membrete, tarjetas, manual de identidad, certificados ISO, OG dinámica).

**Nota estratégica:** Este proyecto es el **predecesor de LUQRA** (rebrand 2026). Comparte infraestructura operativa, datos de contacto y clientes. Ver `../LUQRA/CONTEXTO.md`.

---

## 2. DATOS CORPORATIVOS (reales — desde JSON-LD)

| Campo | Valor |
|-------|-------|
| **Razón social** | MULTISERVICIOS P&J S.A.S |
| **Sector** | Ingeniería e industria de servicios integrales |
| **Dominio** | https://multiserviciospj.com |
| **Dirección** | Corregimiento El Llanito, Barrancabermeja, Santander, Colombia |
| **Código postal** | 687001 |
| **Coordenadas** | 7.0653, -73.8547 |
| **Radio de servicio** | 200 km (GeoCircle) |
| **Teléfono / WhatsApp** | +57 320 4464553 · wa.me/573204464553 |
| **Email contacto** | multiserviciospjsas@gmail.com |
| **Email gerencial** | gerencia@multiserviciospj.com |
| **Email noreply (form)** | noreply@multiserviciospj.com |
| **Horario** | Lunes a Viernes, 07:00 – 17:00 |
| **Área servida** | Santander (CO-SAN), Magdalena Medio |

### Certificaciones ISO (Bureau Veritas)
- **ISO 9001:2015** — Gestión de Calidad
- **ISO 14001:2015** — Gestión Ambiental
- **ISO 45001:2018** — Seguridad y Salud en el Trabajo

### Servicios (6)
1. Transporte de Carga por Carretera
2. Obras Civiles y Mantenimiento Locativo
3. Movimiento de Carga – Izaje
4. Remediación Ambiental
5. Transición Energética (paneles solares)
6. Alquiler de Maquinaria

### Clientes mostrados (5)
Impulsa Social S.A.S · UTCMM2 · Ecomag S.A.S · Construagro Colombia S.A.S · Construcciones, Consultoría y Montajes J.R.S S.A.S

---

## 3. STACK TÉCNICO

| Capa | Tecnología | Versión |
|------|-----------|---------|
| Framework SSG | Astro | ^5.18.0 |
| UI interactiva | Svelte | ^5.53.7 (runes) |
| Estilos | TailwindCSS | ^3.4.0 |
| Animación | Motion | ^12.35.1 |
| Sitemap | @astrojs/sitemap | ^3.7.0 |
| OG dinámica | Satori + @resvg/resvg-js | ^0.26.0 + ^2.6.2 |
| Typography plugin | @tailwindcss/typography | ^0.5.0 |
| Backend form | PHP `mail()` nativo | Hostinger |
| Hosting | Hostinger (Apache + HTTPS) | — |

**Scripts npm:** `dev` · `build` · `preview` · `astro`

### astro.config.mjs
- `site: 'https://multiserviciospj.com'`, `base: '/'`
- Integrations: svelte, tailwind, sitemap
- `build.assets: 'assets'` ✅ (fix Hostinger, evita `_astro/`)
- `vite.build.cssMinify: true`

### tsconfig.json — aliases
`@/` → src/ · `@components/` · `@layouts/` · `@assets/`

---

## 4. IDENTIDAD VISUAL

### Paleta (Tailwind)
| Rol | Color | Hex DEFAULT | Escala |
|-----|-------|-------------|--------|
| **Primary** (Azul institucional) | Azul | `#0089D0` | 50:#e6f4fb · 200:#8AD7F8 · 700:#006BA3 · 950:#002D4D |
| **Secondary** (Verde ambiental) | Verde | `#005B32` | 200:#80b89b · 400:#007A45 · 900:#001F11 |
| **Accent** (Lima energía) | Lima | `#8CC63F` | 300:#A8D86A · 900:#3F6A1A |
| Dark | — | `#1a1a2e` | — |
| Light | — | `#F5F7FA` | — |
| Surface | — | `#FFFFFF` | — |
| CTA | Azul | `#0089D0` (hover `#006BA3`) | — |

### Tipografía
- **Display:** Plus Jakarta Sans (500/600/700/800)
- **Body:** Inter (400/500/600)

### Sombras de marca
- `primary`: `0 8px 24px -4px rgb(0 137 208 / 0.25)`
- `accent`: `0 8px 24px -4px rgb(140 198 63 / 0.25)`

### Animaciones (keyframes)
`waveMove` (10s) · `pulseRing` (2.5s) · `float` (4s) · `fadeIn` (0.5s)
Timing: `spring` cubic-bezier(0.34,1.3,0.64,1) · `smooth` cubic-bezier(0.25,0.46,0.45,0.94)

### Firma visual del proyecto (vs LUQRA / ECOMAG)
- **Hero:** Split-screen (55% texto / 45% visual), gradient azul, iconos flotantes, herramientas cruzadas
- **Servicios:** **Zigzag** alternado L-R (6 filas)
- **Clientes:** Carousel infinito CSS (25s), fade edges
- **Cursor:** Engranaje mecánico (`GearCursor.svelte`)
- **Transiciones:** Wave SVG (`WaveTransition.astro`)
- **Footer:** CTA banner + 4 columnas + sello Bureau Veritas

---

## 5. DESIGN SYSTEM (`src/design-system/tokens.ts`)

Tokens completos exportados como variables CSS en `src/styles/global.css`:
- **Colors:** primary/secondary/accent/cta/dark/light/surface + gray (9 tonos)
- **Spacing:** escala px → 24
- **Radius:** sm 0.375rem · md 0.5rem · lg 0.75rem · xl 1rem · 2xl 1.25rem
- **Typography:** sizes xs→6xl · weights 400-800 · letter-spacing tighter→widest
- **Motion:** durations instant(50ms)→slower(600ms) · easings default/easeOut/spring/smooth
- **Hover:** scale (1.01-1.03) · lift (-2 a -6px) · overlay (0.05-0.15)
- **Z-index:** behind(-1) → max(9999)
- **Breakpoints:** sm 640 · md 768 · lg 1024 · xl 1280 · 2xl 1536

**Componentes CSS:** `.btn-primary` · `.btn-secondary` · `.card` · `.card-accent` · `.reveal` · `.image-zoom` · `.input-field` · `.badge-*` · `.icon-box`
**A11y:** scroll-behavior smooth, antialiasing, `prefers-reduced-motion`, scrollbar custom

---

## 6. ARQUITECTURA DE LA PÁGINA (`index.astro`)

Orden de secciones (14 bloques):

| # | Sección | Componente | Detalle |
|---|---------|-----------|---------|
| 1 | ProgressBar | `ProgressBar.svelte` `client:load` | Barra progreso scroll |
| 2 | Skip link | inline | A11y `#main-content` |
| 3 | Navbar | `Navbar.astro` | Sticky, links internos |
| 4 | **Hero** | `Hero.svelte` `client:load` | Split 55/45, tag + heading + 2 CTA + 3 stats (6 serv, 3 certs, 4+ clientes) |
| 5 | **AboutUs** | `AboutUs.astro` | Stats bar azul (counter) + intro + 3 cards (Misión/Visión/Valores) |
| 6 | **Services** | `Services.astro` | Zigzag 6 filas, número 01-06, icon pills, hover zoom 1.02 |
| 7 | **Benefits** | `Benefits.astro` | 3 cards (solución integral / ISO / transición energética), lift -4px |
| 8 | **Clients** | `Clients.astro` | Carousel infinito CSS 25s, 5 clientes + duplicados |
| 9 | **Contact** | `Contact.svelte` `client:visible` | 3 info cards + form (email + WhatsApp) |
| 10 | **Footer** | `Footer.astro` | CTA banner + grid 4 cols + Bureau Veritas + copyright |
| 11 | ScrollToTop | `ScrollToTop.svelte` `client:idle` | — |
| 12 | WhatsAppButton | `WhatsAppButton.svelte` `client:idle` | Flotante |
| 13 | GearCursor | `GearCursor.svelte` `client:idle` | Cursor engranaje |
| 14 | **Panel YaDev** | inline | Sidebar oculto → brandbook + firma (`internal/`) |

**Componentes Astro (10):** Navbar, Topbar, AboutUs, Services, Benefits, Clients, Footer, WaveTransition, Picture, Projects
**Componentes Svelte (5):** Hero, Contact, ProgressBar, ScrollToTop, WhatsAppButton, GearCursor

---

## 7. FORMULARIO DE CONTACTO (`public/contact.php`)

- **Método:** POST JSON · CORS origin `https://multiserviciospj.com`
- **Envío:** `mail()` PHP nativo → `noreply@multiserviciospj.com`
- **Asunto:** `Nueva consulta - {servicio} - Multiservicios P&J`
- **Seguridad server-side:**
  - Rate limit: 1 req/min (session)
  - Sanitización CRLF (anti header-injection) + HTML escape ENT_QUOTES UTF-8
  - Validación email (FILTER_VALIDATE_EMAIL)
  - Límites: nombre 200 · email 254 · mensaje 5000 · teléfono 30 chars
  - **Whitelist de servicios** (6)
- **2 caminos:** Enviar por correo (PHP) · Enviar por WhatsApp (wa.me con texto preformateado)
- **reCAPTCHA v3** invisible (badge oculto por CSS)

---

## 8. SEO & PRODUCCIÓN

- **Title:** `MULTISERVICIOS P&J S.A.S | Transporte de Carga, Obras Civiles y Remediación Ambiental en Barrancabermeja, Santander`
- **Meta geo:** CO-SAN · 7.0653;-73.8547 · ICBM
- **JSON-LD:** LocalBusiness · Organization · Service (×6) · FAQPage (6) · BreadcrumbList · WebPage
- **OG/Twitter:** completo, imagen 1200×630, locale `es_CO`
- **OG dinámicas:** `/og/[slug].png` via Satori + resvg (fallback `/og-default.jpg`)
- **Sitemap:** `/sitemap-index.xml` (auto) · **robots.txt** (Disallow `/assets/`)
- **RSS:** `/rss.xml`
- **CSP:** vía `<meta http-equiv>` en Layout.astro (Hostinger sobreescribe headers)

### .htaccess (Hostinger)
Force HTTPS 301 · remove trailing slash · `Options -Indexes` · gzip DEFLATE · cache 1 año assets · bloqueo `.env/.bak/.sql/.log` · HSTS max-age 31536000

---

## 9. ENTREGABLES

### `brand/`
| Entregable | Archivo |
|-----------|---------|
| Brandbook interactivo | `brandbook.html` (~3.9 MB) |
| Firma de correo | `firma-correo.html` |
| Generador de firmas | `firma-generador.html` |
| Hoja membretada | `hoja-membretada.html` + `.png` |
| Logos | logo-oficial, logo-white, logo-industrial, logo-rehab-ambiental, isotipo |
| Tarjetas | tarjeta-presentacion, tarjeta-corp-1/2, tarjetas-corporativas |
| Certificación | cert_BUREAU.png |
| Base64 | logo_main, logo_firma, logo_white, bureau (`.txt`) |

### `RECURSOS/`
- Manual de identidad `PJ-GG-M-02` (PDF + DOCX + 5 PNG)
- Certificados ISO oficiales 9001 / 14001 / 45001 (PDF)
- Brochure (2.2 MB PDF)
- IMAGENES/ (fotos operacionales)

---

## 10. ESTRUCTURA DE CARPETAS

```
MULTISERVICIOS P&J/
├── CONTEXTO.md                  ← este documento
├── multiservicios-web/          ← Astro app (en producción)
│   ├── src/
│   │   ├── components/          (16: Astro + Svelte)
│   │   ├── layouts/             Layout.astro + BlogLayout.astro
│   │   ├── pages/               index.astro · blog/ · og/[slug].png.ts
│   │   ├── design-system/       tokens.ts
│   │   └── styles/              global.css
│   ├── public/                  contact.php · .htaccess · robots.txt · images/ · internal/
│   ├── dist/                    build output
│   ├── astro.config.mjs · tailwind.config.mjs · tsconfig.json
│   └── lighthouserc.json
├── brand/                       entregables de marca
└── RECURSOS/                    manual identidad, certificados ISO, brochure
```

---

## 11. ESTADO Y PENDIENTES

**Estado:** 🟢 En producción en `multiserviciospj.com`.

**Pendientes / mejoras menores:**
- [ ] Reemplazar reCAPTCHA **test key** (`6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI`) por clave real de producción
- [ ] Validar entrega de `noreply@multiserviciospj.com` en Hostinger (SPF/DKIM/DMARC M365)
- [ ] Monitorear Lighthouse en CI
- [ ] Limpiar archivos sueltos "Diseño sin título *.png" en raíz del proyecto

**Referencias cruzadas:**
- Memoria: `…/memory/project_multiservicios.md`
- DNS/correo: `…/memory/reference_multiservicios_dns.md`
- Rebrand: `../LUQRA/CONTEXTO.md`
