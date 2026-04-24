# Migration Plan — Multiservicios P&J → YaDev CMS

> Inventario 1:1 de los componentes actuales del sitio de producción mapeados al catálogo de bloques del CMS.
> Fuente leída (read-only): `internal/PROYECTOS/2026/MULTISERVICIOS P&J/multiservicios-web/src/`

---

## Resumen ejecutivo

- **Componentes actuales:** 15 archivos `.astro` + `.svelte`.
- **Bloques editables en CMS:** 9 (uno por sección real). El resto de componentes (cursor, progress bar, WhatsApp button, scroll-to-top) son utilities globales — se mantienen como código, no se exponen en el panel.
- **Datos a migrar:** ~1200 palabras de copy + 15 imágenes + 5 logos de clientes + 6 iconos de servicios.
- **Tiempo estimado de migración:** 3-4 días (Semana 4 de Fase 1).
- **Estrategia:** refactor en branch `cms-compatible`, nunca tocar `main` hasta cutover verificado.

---

## Inventario de componentes actuales

Ubicación: `internal/PROYECTOS/2026/MULTISERVICIOS P&J/multiservicios-web/src/components/`

| Archivo | Tipo | Función | ¿Editable en CMS? |
|---------|------|---------|-------------------|
| `Topbar.astro` | Astro | Barra superior con teléfono/email/ubicación | ✅ via `settings.business.*` |
| `Navbar.astro` | Astro | Header fijo con logo + menú + CTA | ✅ via menú editable + `settings.brand.logo` |
| `Hero.svelte` | Svelte5 | Split-screen hero con badges flotantes | ✅ bloque `hero_split` |
| `AboutUs.astro` | Astro | Stats bar + intro + 3 cards (mision/vision/valores) | ✅ 2 bloques: `stats_bar` + `about_three_cards` |
| `Services.astro` | Astro | 6 servicios en layout zigzag con imágenes | ✅ bloque `services_zigzag` |
| `Benefits.astro` | Astro | 3 cards horizontales con razones para elegirnos | ✅ bloque `benefits_grid` |
| `Clients.astro` | Astro | Carousel infinito de logos | ✅ bloque `clients_carousel` |
| `Projects.astro` | Astro | Bento grid (featured + 3 smaller) | ✅ bloque `bento_projects` |
| `Contact.svelte` | Svelte5 | Formulario con 2 CTAs (email + whatsapp) + info cards | ✅ bloque `contact_form` + form builder |
| `Footer.astro` | Astro | CTA banner + 4-col footer + certifications + copyright | ✅ 2 bloques: `cta_banner` + `footer_mega` |
| `WhatsAppButton.svelte` | Svelte5 | Botón flotante WhatsApp con mini-form | ⚙️ config global (`settings.business.whatsapp`) |
| `ProgressBar.svelte` | Svelte5 | Barra de progreso scroll top | ⚙️ toggle global (on/off) |
| `ScrollToTop.svelte` | Svelte5 | Botón scroll to top | ⚙️ toggle global |
| `GearCursor.svelte` | Svelte5 | Cursor personalizado (engranaje) | ⚙️ setting `brand.cursor_style` |
| `WaveTransition.astro` | Astro | SVG wave entre secciones | ⚙️ toggle por sección |

---

## Mapeo bloque por bloque

### 1. Topbar (settings global)

**Componente actual:** `Topbar.astro` (hardcoded)
**CMS:** No es un bloque — es `Setting` key-values.

Keys afectados:
- `business.phone` → "+57 320 4464553"
- `business.email_alt` → "multiserviciospjsas@gmail.com"
- `business.address` → "Barrancabermeja, Corregimiento El Llanito"

Componente refactorizado:
```astro
---
import settings from '../content/site.json';
const phone = settings.business.phone;
const email = settings.business.email_alt;
const address = settings.business.address;
---
<div class="topbar">...</div>
```

---

### 2. Navbar (menú + settings)

**Componente actual:** `Navbar.astro`
**CMS:**
- Logo → `settings.brand.logo_path` (media picker).
- Links → `menus` tabla, location=`header`.
- CTA "Solicitar Cotización" → último item del menú, link a `#contacto`.

Datos en seed:
```json
{
  "menus": [
    {
      "location": "header",
      "items": [
        { "label": "Inicio", "href": "#inicio" },
        { "label": "Nosotros", "href": "#nosotros" },
        { "label": "Servicios", "href": "#servicios" },
        { "label": "Proyectos", "href": "#proyectos" },
        { "label": "Contacto", "href": "#contacto" }
      ]
    }
  ]
}
```

---

### 3. Hero → `hero_split`

**Componente actual:** `Hero.svelte`
**Schema del bloque:**
```json
{
  "type": "hero_split",
  "data": {
    "eyebrow": "Empresa de Ingeniería en Barrancabermeja",
    "headline_parts": [
      { "text": "Transporte de Carga,", "style": "default" },
      { "text": "Obras Civiles", "style": "accent" },
      { "text": " y Remediación Ambiental en Barrancabermeja", "style": "default" }
    ],
    "description": "Servicios integrales de transporte de carga...",
    "primary_cta": { "label": "Conocer Servicios", "href": "#servicios" },
    "secondary_cta": { "label": "Contactar", "href": "#contacto" },
    "badges": [
      { "label": "Transporte", "icon": "building" },
      { "label": "Ambiental", "icon": "leaf" },
      { "label": "Energía Solar", "icon": "zap" },
      { "label": "Obras Civiles", "icon": "cog" }
    ],
    "background_style": "gradient_dark_blue"
  }
}
```

**Notas:**
- La posición de los badges (x%, y%) queda hardcoded en el componente Svelte (decisión de diseño, no editable por el cliente).
- Los colores del gradient son parte del "theme" del sitio, no editables por bloque.
- Campo `headline_parts` permite que la clienta elija qué frase va con gradient y cuál en blanco.

---

### 4. AboutUs → 2 bloques

**Componente actual:** `AboutUs.astro` (es realmente 2 secciones visualmente)

#### 4a. `stats_bar`
```json
{
  "type": "stats_bar",
  "data": {
    "items": [
      { "value": 6,  "suffix": "",  "label": "Servicios Integrales" },
      { "value": 3,  "suffix": "",  "label": "Certificaciones ISO" },
      { "value": 4,  "suffix": "+", "label": "Clientes en Santander" },
      { "value": 10, "suffix": "+", "label": "Años de Experiencia" }
    ],
    "background_style": "gradient_blue"
  }
}
```

#### 4b. `about_three_cards`
```json
{
  "type": "about_three_cards",
  "data": {
    "eyebrow": "SOBRE NOSOTROS",
    "headline": "Empresa de Ingeniería y Servicios Integrales...",
    "intro_html": "<p><strong>MULTISERVICIOS P&J S.A.S</strong> es una empresa...</p>",
    "cards": [
      { "kind": "mission", "title": "Misión", "icon": "target", "text": "..." },
      { "kind": "vision",  "title": "Visión", "icon": "eye",    "text": "..." },
      { "kind": "values",  "title": "Valores Corporativos", "icon": "shield_check",
        "values": [
          { "name": "Excelencia y Calidad", "desc": "..." },
          { "name": "Responsabilidad Ambiental", "desc": "..." },
          { "name": "Seguridad y Bienestar", "desc": "..." }
        ]
      }
    ]
  }
}
```

---

### 5. Services → `services_zigzag`

**Componente actual:** `Services.astro`
**Schema:**
```json
{
  "type": "services_zigzag",
  "data": {
    "eyebrow": "NUESTROS SERVICIOS",
    "headline": "Servicios Integrales de Ingeniería en Barrancabermeja y Colombia",
    "description": "Ofrecemos un portafolio completo...",
    "items": [
      { "number": "01", "title": "Transporte de Carga por Carretera", "description": "...", "image_path": "/images/services/transporte.jpg", "icon": "truck" },
      { "number": "02", "title": "Obras Civiles y Mantenimiento Locativo", ... },
      { "number": "03", "title": "Movimiento de Carga - Izaje", ... },
      { "number": "04", "title": "Remediación Ambiental", ... },
      { "number": "05", "title": "Transición Energética", ... },
      { "number": "06", "title": "Alquiler de Maquinaria", ... }
    ],
    "cta_label": "Solicitar cotización",
    "cta_href": "#contacto"
  }
}
```

**Notas:**
- El array `items` es drag-sortable en el CMS. El cliente puede reordenar los servicios.
- `image_path` se reemplaza por `image_id` cuando se sube nueva foto → al hacer publish, el runner resuelve `id → URL`.
- Los iconos se seleccionan desde un catálogo lucide con 20 iconos preseleccionados de "industrial".

---

### 6. Benefits → `benefits_grid`

**Componente actual:** `Benefits.astro`
**Schema:** análogo a `services_zigzag` pero más simple (3 items fijos, layout grid).

---

### 7. Clients → `clients_carousel`

**Componente actual:** `Clients.astro`
**Schema:**
```json
{
  "type": "clients_carousel",
  "data": {
    "eyebrow": "Nuestros Aliados",
    "headline": "Clientes que Confían en Nosotros",
    "description": "Empresas líderes del sector energético...",
    "items": [
      { "name": "Impulsa Social S.A.S",   "industry": "Transporte de carga por carretera",     "logo_path": "/images/clients/impulsa-social.png" },
      { "name": "UTCMM2",                 "industry": "Movimiento de cargas, Izaje, Transporte y Alquiler de Maquinaria", "logo_path": "/images/clients/utcmm2.png" },
      { "name": "Ecomag S.A.S",           "industry": "Reforestación y Remediación Ambiental", "logo_path": "/images/clients/ecomag-logo.png" },
      { "name": "Construagro Colombia",   "industry": "Alquiler de Maquinaria",                 "logo_path": "/images/clients/construagro.png" },
      { "name": "JRS S.A.S",              "industry": "Construcción e Infraestructura",         "logo_path": "/images/clients/construcciones-jrs.png" }
    ]
  }
}
```

---

### 8. Projects → `bento_projects`

**Componente actual:** `Projects.astro`
Ver schema en `database/seed-multiservicios.sql` sección `bento_projects`.

---

### 9. Contact → `contact_form` + form builder

**Componentes actuales:** `Contact.svelte` + formulario hardcoded
**CMS:**
- Form definition separada (tabla `forms`) con 5 campos.
- Block `contact_form` referencia al `form_id` y define el contenido visual (eyebrow, headline, info cards).

Ver seed SQL para valores exactos.

---

### 10. Footer → 2 bloques: `cta_banner` + `footer_mega`

**Componente actual:** `Footer.astro`
- CTA banner arriba → `cta_banner`.
- Footer principal → `footer_mega` (con social, menú services, contact info, certifications image, copyright).

Ver seed.

---

## Assets a migrar

### Imágenes (subir a mediateca del tenant)
Ubicación actual: `internal/PROYECTOS/2026/MULTISERVICIOS P&J/multiservicios-web/public/images/`

- `/images/services/transporte.jpg` (hero card servicio 1)
- `/images/services/obras-civiles.jpg`
- `/images/services/izaje.jpg`
- `/images/services/remediacion.jpg`
- `/images/services/transicion-energetica.jpg`
- `/images/services/maquinaria.jpg`
- `/images/projects/transporte-proyecto.jpg`
- `/images/projects/ambiental-proyecto.jpg`
- `/images/projects/maquinaria-proyecto.jpg`
- `/images/clients/impulsa-social.png`
- `/images/clients/utcmm2.png`
- `/images/clients/ecomag-logo.png`
- `/images/clients/construagro.png`
- `/images/clients/construcciones-jrs.png`
- `/images/bureau-veritas-iso.png` (certifications)
- `/logo.png` (logo principal)
- `/logo-white.png` (logo blanco para footer)
- `/og-image.jpg` (Open Graph)

**Proceso:** script `php artisan tenants:import-media multiservicios --source=/path/to/public/images/` que:
1. Itera carpeta.
2. Sube cada archivo al storage tenant con path original preservado.
3. Genera conversions (thumb, webp).
4. Inserta fila en `media`.
5. Return mapping `{ "original_path": "media_id" }` para replace en seeds.

---

## Refactor del código Astro (rama `cms-compatible`)

### Cambios por archivo

#### `src/pages/index.astro`
```astro
---
import Layout from '@layouts/Layout.astro';
import siteData from '../content/site.json';  // ← generado por runner
import Navbar from '@components/Navbar.astro';
import Hero from '@components/Hero.svelte';
import AboutUs from '@components/AboutUs.astro';
// ...

const page = siteData.pages.find(p => p.slug === 'inicio');
const getBlock = (type) => page.sections
  .flatMap(s => s.blocks)
  .find(b => b.type === type)?.data;

const heroData = getBlock('hero_split');
const statsData = getBlock('stats_bar');
const aboutData = getBlock('about_three_cards');
// ...
---

<Layout
  title={page.seo.meta_title}
  description={page.seo.meta_description}
>
  <Navbar menu={siteData.menus.header} brand={siteData.settings.brand} />
  <main id="main-content">
    <Hero data={heroData} client:load />
    <StatsBar data={statsData} />
    <AboutUs data={aboutData} />
    <!-- ... -->
  </main>
</Layout>
```

#### `src/components/Hero.svelte`
Cambio mínimo: exponer prop `data`:
```svelte
<script lang="ts">
  let { data } = $props<{ data: HeroSplitData }>();
  // ... resto del componente usa data.headline_parts, data.badges, etc.
</script>
```

#### Componentes `.astro` similares:
Recibir `data` como prop y usar `{data.items.map(...)}` en vez de arrays hardcoded.

---

## Validación pre-cutover (checklist)

- [ ] Build local de `cms-compatible` branch produce `dist/` byte-idéntico (o casi) al deploy actual. Comparación visual con Percy o screenshots.
- [ ] Lighthouse score ≥ 90 en todas las métricas (no debe degradarse).
- [ ] Todos los links funcionan (anchor links, WhatsApp, tel, mailto, certificaciones).
- [ ] Formulario envía correctamente a `gerencia@multiserviciospj.com`.
- [ ] reCAPTCHA sigue activo.
- [ ] Verificar que seed_multiservicios.sql produce exactamente el contenido del sitio live.
- [ ] Clienta verifica 2-3 cambios desde el panel y ve que se reflejan.

## Cutover day (checklist)

1. Tenant `multiservicios` provisionado en producción.
2. Último snapshot del sitio live (backup manual).
3. Deploy inicial via CMS desde panel → verificar que el sitio publicado es igual al actual.
4. Activar formulario en el CMS (desactivar el PHP anterior sólo si el nuevo funciona bien).
5. Enviar credenciales a la clienta.
6. Onboarding call 30 min.
7. Monitoreo intensivo por 7 días.

## Rollback plan

Si después del cutover hay problemas graves:
1. `rsync` del último backup pre-cutover a `/public_html/`.
2. Restaurar contact.php original si cambió.
3. Deshabilitar tenant en el CMS (`php artisan tenant:suspend multiservicios`).
4. Comunicar a la clienta.
5. Debugging offline antes de reintentar.
