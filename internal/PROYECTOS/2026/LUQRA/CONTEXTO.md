# CONTEXTO — LUQRA Ingeniería y Soluciones S.A.S

> Documento de contexto definitivo del proyecto web.
> Generado: 2026-06-12 · Estado: **🟡 BUILD LISTO — bloqueado por 5 P0** · Ruta: `internal/PROYECTOS/2026/LUQRA`

---

## 1. RESUMEN EJECUTIVO

Sitio web corporativo premium (Astro 5 + Svelte 5 + Tailwind 3) que es el **rebrand y ampliación de scope de Multiservicios P&J S.A.S**. Misma infraestructura operativa y clientes, pero nueva marca (azul/naranja 80/20) y **5 áreas operativas integradas**. El build está generado y desplegado en staging (Railway), pero **bloqueado para producción** por datos placeholder del cliente y un problema de deploy (PHP no corre en Railway → necesita Hostinger).

Documentos hermanos: `AUDIT-REPORT.md` (auditoría completa) · `brand/tokens.md` (marca) · `luqra-entra/README-premium.md` (login Entra ID) · predecesor `../MULTISERVICIOS P&J/CONTEXTO.md`.

---

## 2. DATOS CORPORATIVOS

| Campo | Valor | Estado |
|-------|-------|--------|
| **Razón social** | Luqra Ingeniería y Soluciones S.A.S | ✅ |
| **Predecesor** | Multiservicios P&J S.A.S (rebrand 2026-05-03) | ✅ |
| **Sector** | Ingeniería integral: transporte, construcción, energías renovables, ambiental, comercio | ✅ |
| **Dominio** | luqra.co (en `astro.config`) | ✅ |
| **Ubicación** | Corregimiento El Llanito, Barrancabermeja, Santander | ✅ |
| **Coordenadas** | 7.0653, -73.8547 | ✅ |
| **Teléfono / WhatsApp** | +57 320 4464553 · wa.me/573204464553 | ✅ |
| **Email corporativo** | gerencia@luqra.co | ⚠️ inconsistente (ver B5) |
| **Horario** | Lunes a viernes, 7:00 am – 5:00 pm | ✅ |
| **NIT** | — | ❌ pendiente |
| **N° empleados** | rango 10-50 (placeholder) | ❌ pendiente |

### Certificaciones ISO (heredadas, Bureau Veritas)
ISO 9001:2015 · ISO 14001:2015 · ISO 45001:2018

### 5 áreas operativas (servicios)
1. **Transporte y Logística Integral** *(featured)*
2. **Construcción Civil y Arquitectónica** *(featured)*
3. Energías Renovables
4. Gestión Ambiental
5. Comercio Internacional

### Proyectos reales (content-fallback.ts)
| ID | Cliente | Área | Año |
|----|---------|------|-----|
| P001 | Impulsa Social S.A.S | Transporte y Logística | 2024 |
| P002 | UTCMM2 | Izaje y Transporte | 2024 |
| P003 | Ecomag S.A.S | Gestión Ambiental | 2024 |
| P004 | Construagro Colombia S.A.S | Alquiler de Maquinaria | 2024 |
| P005 | — pendiente | — | — |

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
| Backend form | PHP `mail()` (contact.php) | requiere Hostinger |
| Hosting actual | **Railway** (Node — PHP NO ejecuta) | staging |
| Hosting destino | **Hostinger** (Apache + PHP) | pendiente |
| CI | GitHub Actions + Lighthouse (`lighthouse.yml`) | — |
| Package manager | pnpm | — |

**Scripts npm:** `dev` · `build` · `preview` · `start` (`serve dist`, compat Railway) · `astro`

### astro.config.mjs
- `site: 'https://luqra.co'`, `base: '/'`
- Integrations: svelte, tailwind, sitemap
- `build.assets: 'assets'` ✅ (fix Hostinger)
- `vite.build.cssMinify: true`
- `vite.define`: expone `CMS_API_URL`, `CMS_TENANT_ID`, `CMS_BUILD_TOKEN` (CMS-ready, Node-side)
- `vite.preview.allowedHosts: true` (Railway + custom domains)

---

## 4. IDENTIDAD VISUAL — Esquema 80/20 azul/naranja

### Filosofía
80% azul (seriedad ingeniería) + 20% naranja (impacto, recordación). El naranja **nunca domina**; es el acento que hace memorable la marca. Diferenciación clara del verde de Multiservicios.

### Paleta de marca (tokens.md + tailwind.config)
| Token | Hex | Uso |
|-------|-----|-----|
| `brand-blue-base` | `#0A2A66` | Texto LUQRA, headings, fondos corporativos |
| `brand-blue-mid` | `#123C8C` | Gradientes |
| `brand-blue-light` | `#1F5FBF` | Acentos, hover azul |
| `brand-orange-base` | `#FF6A00` | Letra "Q", CTAs principales |
| `brand-orange-mid` | `#FF8C1A` | Gradientes |
| `brand-orange-light` | `#FFA533` | Brillos, hover |
| Navy oscuro (secciones/Entra) | `#060F24` / `#050B1A` | Fondos dark |
| Surface | `#FFFFFF` · light bg `#F4F6FA` | Fondos light |

**Escalas Tailwind:** `primary` 50:#e8eef8 → 500:#1F5FBF → 900:#0A2A66 · `accent` 50:#fff3e6 → 400:#FFA533 → 600:#FF6A00 → 800:#c25000

### Tipografía
- **Display:** Plus Jakarta Sans (500/600/700/800)
- **Body:** Inter (400/500/600)
- **Mono:** JetBrains Mono (400/500) — IDs de proyectos, datos técnicos

### Animaciones (tailwind.config)
`pulse-ring` (2.5s) · `float` (4s) · `fade-in` (0.5s) · `slide-up` (0.6s sharp) · `grid-glow` (8s, dot-grid breathing 0.03↔0.07)
Timing: `spring` cubic-bezier(0.34,1.3,0.64,1) · `smooth` (0.25,0.46,0.45,0.94) · `sharp` (0.4,0,0.2,1)
Sombras: `primary` navy glow · `accent` orange glow

### Firma visual del proyecto (vs Multiservicios)
- **Hero:** Full-height centrado, **dot-grid bg con parallax**, textura tiremark, **diagonal cut** inferior (no wave)
- **Servicios:** **Bento grid asimétrico** (2 featured 50/50 + 3 regular 33/33/33) sobre navy `#060F24`
- **Proyectos:** **Masonry 2-col**, cards alternados azul/naranja, IDs P001-P005
- **Stats:** Counter-up con IntersectionObserver, diagonal cuts
- **Cursor:** **Triángulo dual** (azul outline + naranja fill) con lerp, hover scale, click squash (`TriangleCursor.svelte`)
- **Footer:** Mega-footer 5-col + CTA banner + diagonal cut

---

## 5. ARQUITECTURA DE LA PÁGINA (`index.astro`)

| # | Sección | Componente | ID | Detalle |
|---|---------|-----------|----|---------|
| 1 | Topbar | `Topbar.astro` | — | Slim (hidden mobile): logo + email + phone |
| 2 | Navbar | `Navbar.astro` | — | Inicio · Nosotros · Servicios · Proyectos · Contacto |
| 3 | **Hero** | `Hero.svelte` `client:load` | `#inicio` | Eyebrow + heading (accent naranja) + 2 CTA + dot-grid parallax + diagonal cut |
| 4 | **AboutUs** | `AboutUs.astro` | `#nosotros` | Stats bar (5 ejes) + texto + MVV tabs + certs ISO |
| 5 | **Benefits** | `Benefits.astro` | — | Pilares (shield, layers, award, check) |
| 6 | **Services** | `Services.astro` | `#servicios` | Bento grid (2 featured + 3 regular), navy bg |
| 7 | **Projects** | `Projects.astro` | `#proyectos` | Masonry 2-col, P001-P005, azul/naranja |
| 8 | **Clients** | `Clients.astro` | — | Logo grid (Construagro, UTCMM2, Ecomag, Impulsa) |
| 9 | **Stats** | `Stats.astro` | `#trayectoria` | 4 counters: 5 ejes, 3 ISO, 4+ clientes, 10+ años |
| 10 | **Contact** | `Contact.svelte` `client:visible` | `#contacto` | Info + horario / form (5 inputs + select + textarea) |
| 11 | **Footer** | `Footer.astro` | — | CTA banner + 5 cols + social + copyright |
| 12 | Floating UI | `ScrollToTop` · `WhatsAppButton` · `TriangleCursor` · `ProgressBar` | — | `client:idle` / `client:load` |
| 13 | Panel YaDev | inline | `#yadev-panel` | Sidebar oculto → brandbook, firma, membrete |

**Lib clave:** `cms.ts` + `cms-types.ts` (fetch CMS con fallback) · `content-fallback.ts` (~350 líneas, contenido hardcoded) · `brand.ts` (`brandify()` para highlight naranja) · `blocks/` (hero, services, stats, richtext, cta)

---

## 6. SEO & METADATOS

- **Lang:** `es-CO`
- **Title:** `Luqra Ingenieria y Soluciones S.A.S | Ingenieria Integral en Colombia — Transporte, Construccion, Energias Renovables`
- **Meta geo:** CO-SAN · 7.0653;-73.8547 · ICBM
- **JSON-LD (6):** LocalBusiness · Organization (foundingDate 2026) · WebPage · FAQPage (5) · Service (×5) · BreadcrumbList
- **OG/Twitter:** completo, 1200×630, locale `es_CO`, `og:image https://luqra.co/og-image.jpg`
- **Sitemap:** `/sitemap-index.xml` · **robots.txt** (bloquea `/internal/`)

---

## 7. MICROSOFT ENTRA ID (`luqra-entra/`)

Branding premium de la pantalla de login corporativo (calidad Apple/Stripe). Ver `README-premium.md`.

**Assets:** `background-1920x1080.jpg` (navy + tire-track, sin texto) · `square-240-light/dark` (240×240) · `banner-245x36.png` · `favicon-32.png` (Q) · `LUQRA.css`
**Config recomendada:** fondo `#050B1A` · botón primario gradient navy→#1E5BBA · inputs focus navy halo · links naranja `#FF6A00` · padding form 56px · sugerencia usuario `nombre@luqra.co`
**Texto login (Opción A formal):** acceso autorizado solo colaboradores, soporte `gerencia@luqra.co`, actividad monitoreada.

---

## 8. ENTREGABLES

### `brand/`
brandbook.html · firma-correo.html · firma-generador.html · hoja-membretada.html (+ generador) · tarjeta-presentacion.html · og-image.jpg (1200×630) · logo.png/.jpeg · logo_b64.txt · scripts Python de generación

### `luqra-elements/` (8 elementos de marca despiezados)
01 wordmark-full · 02 wordmark-only · 03 tagline · 04 q-mark · 05 orange-triangle (cursor) · 06 horizon-glow · 07 tire-floor (hero) · 08 background-atmospheric

### `luqra-logos/`
favicon.ico · logo 240×240 · 245×36 · 32×32

---

## 9. ESTRUCTURA DE CARPETAS

```
LUQRA/
├── CONTEXTO.md                  ← este documento
├── AUDIT-REPORT.md              ← auditoría completa (5 P0 + hallazgos)
├── brand/                       brandbook, firmas, membrete, tarjeta, logos, og
├── luqra-elements/              8 elementos de marca despiezados
├── luqra-entra/                 login Entra ID (README-premium.md, CSS, assets)
├── luqra-logos/                 variaciones de logo
├── luqra-web/                   ← Astro app
│   ├── src/
│   │   ├── components/          Astro (Topbar, Navbar, AboutUs, Services, Projects, Stats, Clients, Benefits, Footer) + Svelte (Hero, Contact, ScrollToTop, WhatsAppButton, ProgressBar, TriangleCursor)
│   │   ├── layouts/             Layout.astro (~330 líneas) + BlogLayout.astro
│   │   ├── pages/               index.astro (~135) · blog/
│   │   ├── lib/                 cms.ts · content-fallback.ts · brand.ts · blocks/
│   │   ├── styles/              global.css
│   │   └── design-system/       (vacío por ahora)
│   ├── dist/                    build output (~104 KB HTML) — incluye contact.php
│   ├── public/                  favicons, logos, hero-tracks, og-image
│   ├── .github/workflows/       lighthouse.yml
│   ├── astro.config.mjs · tailwind.config.mjs · tsconfig.json
│   ├── lighthouserc.json · .env.example
│   └── luqra-hostinger.zip      pre-build para Hostinger
└── [scripts Python]             decompose_logo · extract_wordmark · generate_entra_assets
```

---

## 10. 🚧 BLOQUEADORES P0 (NO PRODUCCIÓN) — ver AUDIT-REPORT.md

| ID | Problema | Fix |
|----|----------|-----|
| **B1** | JSON-LD con placeholders (`+57 TODO`, `TODO@…`, dirección/empleados TODO) → Google indexa spam | Datos reales del cliente |
| **B2** | Disclaimer visible "proyectos son placeholders" (`Projects.astro`) | Proyectos reales u ocultar sección |
| **B3** | Stats muestran "—" + badge "Cifras pendientes TODO" | Números confirmados |
| **B4** | `<h3>TODO: Confirmar nombre del proyecto</h3>` | Títulos reales (P001-P004 ya en fallback) |
| ~~**B5**~~ ✅ | **RESUELTO (2026-06-12).** `site-config.ts` es fuente única. Cableado en cta.ts, Layout JSON-LD, Footer (email viejo eliminado), Contact.svelte, Topbar, contact.php. Todo → `gerencia@luqra.co`. Build limpio. | — |
| **G1** | `contact.php` NO ejecuta en Railway (sin PHP) → form no envía | Migrar a Hostinger o serverless (Web3Forms/Resend/endpoint Astro) |

### P1 (antes de go-live)
- ~~**E1:** preload `/hero-bg.jpg` 404~~ ✅ **RESUELTO** (preload eliminado, hero es CSS).
- **E6:** reCAPTCHA — ✅ **cableado a `PUBLIC_RECAPTCHA_SITE_KEY` (.env)** con fallback a la test key en Layout + Contact. ⏳ **Falta manual:** crear key real en Google para `luqra.co` y ponerla en `.env`.
- ~~**C8:** skip-link frágil (dependía de utilidades Tailwind de otra página)~~ ✅ **RESUELTO** (CSS `.skip-link` scoped en `index.astro`, autocontenido).
- ~~**C9/C10:** contraste WCAG bajo (footer copyright .22, topbar .45)~~ ✅ **RESUELTO** (copyright → .6, topbar → .65).
- ~~**H3:** `contact.php` `$to = 'TODO@…'`~~ ✅ **RESUELTO** (→ `gerencia@luqra.co`, parte de B5).
- **H7:** falta `.htaccess` para Hostinger → incluir al migrar

---

## 11. CHECKLIST PRE-PRODUCCIÓN

- [ ] Reemplazar `TODO` restantes del JSON-LD (headcount, NIT) — email/phone ya vienen de `site-config.ts`
- [ ] Confirmar 5º proyecto (P005) + stats reales
- [x] ~~Unificar email único~~ → hecho vía `site-config.ts` (B5)
- [ ] Resolver formulario: **migrar a Hostinger** (PHP) o serverless
- [ ] Generar reCAPTCHA key real para `luqra.co` y ponerla en `.env` (`PUBLIC_RECAPTCHA_SITE_KEY`)
- [x] ~~Fix preload 404 · contraste WCAG · skip-link CSS~~ → hecho (E1, C9/C10, C8).
- [ ] Incluir `.htaccess` Hostinger · confirmar dominio `luqra.co` vs `.com.co`
- [ ] Facebook Debug scrape (OG WhatsApp) · enviar sitemap a Search Console

**Referencias:** `AUDIT-REPORT.md` · `brand/tokens.md` · `luqra-entra/README-premium.md` · `…/memory/project_luqra.md` · predecesor `../MULTISERVICIOS P&J/CONTEXTO.md`
