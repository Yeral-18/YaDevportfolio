# YADEV STANDARD — Lo que TODO sitio YaDev debe tener

> **Propósito:** catálogo COMPLETO y replicable de "lo que SIEMPRE hacemos" en cada
> sitio de cliente. Derivado de auditar Luqra, Multiservicios P&J y ECOMAG (2026-06-13).
>
> **Regla de oro:** el **DISEÑO** es único por proyecto (ver `CREATIVE_ENGINE.md`),
> pero el **SISTEMA** de abajo es idéntico siempre — copiar, no reinventar. Si un sitio
> nuevo NO tiene alguno de estos elementos, está incompleto.
>
> Este doc complementa `CLAUDE.md` (entregables) y se aplica a COICEM y a todo cliente futuro.

---

## 0. STACK ESTÁNDAR
Astro 5.18 + Svelte 5.53 (runes) + Tailwind 3.4 · Motion 12.35 · @astrojs/sitemap · Satori+resvg (OG) · PHP `mail()` (Hostinger) · Railway (staging) → Hostinger (prod).

---

## 1. COMPONENTES OBLIGATORIOS (cada sitio los tiene SIEMPRE)

| Componente | Archivo | Directiva | Función |
|---|---|---|---|
| **ProgressBar** | `ProgressBar.svelte` | `client:load` | Barra fija top 3px, gradiente de marca, % de scroll. `role=progressbar`. |
| **Botón WhatsApp flotante** | `WhatsAppButton.svelte` | `client:idle` | Fijo bottom-right, verde `#25D366`, círculo ~56px, pulse-ring. Aparece tras scroll. |
| **Scroll-to-top (flecha)** | `ScrollToTop.svelte` | `client:idle` | Fijo bottom-right ENCIMA del WhatsApp (~6rem), aparece a scroll >300-600px, smooth scroll. |
| **Cursor personalizado** | `*Cursor.svelte` | `client:idle` | Por industria (engranaje/hoja/triángulo/crosshair). Solo `pointer:fine`, respeta reduced-motion, oculta cursor nativo. |
| **Topbar** | `Topbar.astro` | — | `hidden md:block`. Tel + email (izq) + ubicación (der). Oculto en móvil. |
| **Navbar** | `Navbar.astro` | — | Logo PNG + links + **CTA "Cotizar"/"Solicitar Cotización"**. Sticky con sombra al scroll + scroll-spy. Menú móvil (hamburguesa → overlay/slide). |
| **Contact (formulario)** | `Contact.svelte` | `client:visible` | Ver §3. |
| **Footer** | `Footer.astro` | — | Ver §2. |
| **Panel YaDev oculto** | inline en `index.astro` | — | Ver §4. |

### Detalle WhatsApp button (2 variantes válidas)
- **Simple (Luqra/ECOMAG):** abre `wa.me/<num>?text=<mensaje preformateado>` en nueva pestaña + tooltip al hover.
- **Con mini-formulario (Multiservicios):** card sobre el botón con Nombre + Servicio (select) + Mensaje → arma el texto y abre wa.me. Header verde "Te asesoramos en línea".
- Número desde `site-config`. `aria-label`. **Es SISTEMA: debe estar en CADA página, también en móvil.**

### Detalle Scroll-to-top
- Aparece sobre el WhatsApp (z-index menor). Color de marca con glass/borde. `window.scrollTo({top:0, behavior:'smooth'})`. `aria-label="Volver al inicio"`. reduced-motion → sin animación.

---

## 2. FOOTER (estructura estándar)

Orden de arriba→abajo:
1. **CTA banner** ("¿Listo para su proyecto?" / "Listo para su proyecto") con 2 botones: **"Cotizar ahora"** (color de marca) + **"WhatsApp"**. Fondo gradiente o invertido; transición (wave/diagonal) hacia el footer.
2. **Grid de columnas** (4–5 según proyecto):
   - **Col Brand:** logo wordmark (versión clara) + tagline + **chips ISO** (`ISO 9001` · `ISO 14001` · `ISO 45001` · `BUREAU VERITAS`) + **redes sociales** (Facebook, Instagram, LinkedIn, WhatsApp).
   - **Col Servicios:** links a #servicios / áreas.
   - **Col Empresa:** Sobre nosotros · Servicios · Proyectos · Contacto.
   - **Col CERTIFICACIONES:** imagen **`/images/bureau-veritas-iso.png`** (banner rojo Bureau Veritas con las ISO) — `max-width 180-240px`, `loading=lazy`, alt descriptivo con las normas. **Ver §5.**
   - **Col Contacto:** tel (`tel:`), email (`mailto:`), dirección, web. Iconos.
3. **Barra copyright:** `© 2026 <RAZÓN SOCIAL>. Todos los derechos reservados.` + **"Desarrollado por YaDev"** (link). Contraste WCAG AA (no usar opacidad <0.55 en texto).

---

## 3. FORMULARIO DE CONTACTO (estándar)
- Layout side-by-side (info izq / form der) en desktop, apilado en móvil. `client:visible`, reveal con IntersectionObserver.
- Campos: Nombre, Email, Teléfono, **Servicio (select, whitelist)**, Mensaje (opcional, min 10).
- Validación cliente (regex email, requeridos).
- **2 botones:** "Enviar por correo" (→ `mailto:` o POST `/contact.php`) + "Enviar por WhatsApp" (→ `wa.me` con texto formateado en negritas).
- **reCAPTCHA v3** invisible, key vía `PUBLIC_RECAPTCHA_SITE_KEY` (.env), badge oculto por CSS.
- Estados success/error con auto-reset 5s.
- Backend: **`public/contact.php`** con `mail()` nativo (NO SMTP), rate-limit 60s, sanitización CRLF, whitelist servicios, destinatario desde site-config.

---

## 4. PANEL YADEV OCULTO (en CADA sitio)
Inline en `index.astro` (HTML + vanilla JS). Tab fijo a la **izquierda, centrado vertical** (~28×72px, opacidad 0.35→1 hover), abre menú con links a los entregables internos:
- `internal/brandbook.html`
- `internal/firma-generador.html` (o `firma-correo.html`)
- `internal/hoja-membretada-generador.html`

`aria-expanded`. Bloqueado en `robots.txt` (`Disallow: /internal/`).

---

## 5. CERTIFICACIONES (Bureau Veritas) — ESTÁNDAR

**Patrón:** la mayoría de los clientes industriales tienen certificaciones ISO emitidas por **Bureau Veritas (BVQI Colombia)**. Se muestran de DOS formas (ambas):
1. **Imagen banner** `public/images/bureau-veritas-iso.png` (banner rojo: las ISO + sello "BUREAU VERITAS 1828") en la **columna Certificaciones del footer** (y a veces en AboutUs).
2. **Chips de texto** (`ISO 9001`, `ISO 14001`, `ISO 45001`, `BUREAU VERITAS`) en la columna Brand del footer.

**De dónde salen:** los PDFs de certificado del cliente (en su carpeta del proyecto). Convención de nombres: `*_9k.pdf`=ISO 9001, `*_14k.pdf`=ISO 14001, `*_45k.pdf`=ISO 45001, `*_norsok.pdf`=NORSOK. El certificador es **BVQI Colombia Ltda. (Bureau Veritas)**.

**Assets reutilizables** (el sello BV es neutro del certificador):
- `MULTISERVICIOS P&J/brand/cert_BUREAU.png` (banner 3 ISO)
- `ECOMAG02/RECURSOS/bureau-veritas-iso.png`
- `LUQRA/luqra-web/public/images/bureau-veritas-iso.png`

> ⚠️ Cada cliente puede tener un set DISTINTO de certificaciones (p. ej. COICEM tiene ISO 9001:2015 + 14001:2015 + 45001:2018 **+ NORSOK 006:2020**). Si las normas difieren del banner reutilizado, generar el banner correcto o renderizar chips nativos con las normas reales. Nunca afirmar una certificación que el cliente no tenga (verificar en sus PDFs).

### Cómo AMPLIAR el banner BV (añadir una certificación) — lección COICEM 2026-06
Cuando el cliente tiene una norma extra (NORSOK, otra ISO) y la quiere DENTRO del
banner rojo (no como chip suelto), reconstruir el banner con PIL — NO insertar una
franja parcial (deja un escalón en el borde rojo). Receta (`brand/rebuild-bv-banner.py`):
1. Recortar el **sello/óvalo BV** del banner original (detectar gris en la mitad derecha).
2. **Cuadro rojo UNIFORME** = rectángulo sólido completo (`Image.new(RED)`), color real `#D2213C` (210,33,60). Nunca un rojo parcial.
3. **Escalar el óvalo para que quede CONTENIDO** dentro del alto del rojo (no debe sobresalir arriba/abajo) y pegarlo a la derecha centrado.
4. Texto Arial Bold blanco, **grande** (las normas a ~64px, "BUREAU VERITAS" ~82px) — el cliente nota si queda pequeño.
5. Quitar el chip de texto redundante del footer si la norma ya está en el banner.
> Errores que el cliente reportó y hay que evitar: "escalón en el rojo" (franja parcial), "óvalo sobresale" (no contenido), "texto muy pequeño" (mucho padding).

**En `site-config.ts`:**
```ts
certifications: [
  { iso: 'ISO 9001:2015',  scope: 'Gestión de Calidad', certifier: 'Bureau Veritas (BVQI Colombia)' },
  { iso: 'ISO 14001:2015', scope: 'Gestión Ambiental', ... },
  { iso: 'ISO 45001:2018', scope: 'Seguridad y Salud en el Trabajo', ... },
  // + NORSOK u otras según el cliente
]
```

---

## 6. SEO / LAYOUT (estándar en CADA página)
- `lang="es-CO"`, `<title>` con keyword+ubicación, `<meta description>` 150-160, canonical.
- **Geo:** `geo.region CO-SAN`, `geo.position`, `ICBM`.
- **JSON-LD:** LocalBusiness/EngineeringFirm · Organization · WebPage · **FAQPage** · Service[] · BreadcrumbList. (Solo datos reales — sin teléfono/email inventado.)
- **Open Graph + Twitter:** completo, imagen 1200×630, `og:locale es_CO`.
- **OG dinámica:** `/og/[slug].png` con Satori+resvg, fallback `/og-image.jpg`.
- **Fonts:** `preconnect` a Google Fonts.
- **Sitemap:** `@astrojs/sitemap` → `/sitemap-index.xml`. **robots.txt:** Disallow `/assets/` + `/internal/` + `/contact.php`.

---

## 7. LOS 8 ENTREGABLES DE MARCA (siempre, por cliente)
Generados por scripts Python en `brand/` (input = logo en base64), autocontenidos, copiados a `web/public/internal/`:

| # | Entregable | Archivo | Script |
|---|---|---|---|
| 1 | **Brandbook** A4 12-14pp (logo variants, paleta, tipografía, papelería) | `brandbook.html` | `generate-brandbook-v2.py` |
| 2 | **Firma de correo** HTML (logo base64, Outlook-compat) | `firma-correo.html` | `generate-deliverables.py` |
| 3 | **Generador de firmas** interactivo (form + preview + descarga .htm) | `firma-generador.html` | `generate-firma-generador.py` |
| 4 | **Hoja membretada** A4 print | `hoja-membretada.html` | `generate-papeleria.py` |
| 5 | **Generador de membrete** (+ export .doc Word) | `hoja-membretada-generador.html` | `generate-membrete-generador.py` |
| 6 | **Tarjeta de presentación** 90×55mm (frente+reverso) | `tarjeta-presentacion.html` | `generate-papeleria.py` |
| 7 | **OG image** 1200×630 (logo centrado) | `og-image.jpg` | `generate-m365-assets.py` (PIL) |
| 8 | **Logos + Favicons** (PNG ≥400px transparente, base64 .txt, .ico) + **Microsoft Entra ID** (background, square-240, banner) | `*-logos/`, `*-entra/` | `generate-m365-assets.py` |

> Logo para firma: usar `logo_firma_b64.txt` (≤56KB) — Outlook/Gmail strippean imágenes embebidas >100KB.

---

## 8. SISTEMA TÉCNICO (idéntico siempre)
- **`src/lib/site-config.ts`** = fuente única de contacto/marca/certs/telemetría. Nunca hardcodear en componentes. Helpers `whatsappUrl()`, `mailtoUrl()`, `addressLine`.
- **`assertProductionReady()`** en `astro.config` con `DEPLOY_TARGET=production` → bloquea build con placeholders (NIT, contacto, telemetría, logo vectorial, etc.). Staging buildea libre.
- **Hostinger:** `build.assets:'assets'` (no `_astro/`), `fileURLToPath` en tailwind/astro config (rutas con `&`/espacios), `.htaccess` SIN CSP + MIME types, logo PNG (no SVG).
- **`scripts/check-hostinger.mjs`** (gate pre-deploy): detecta CSP real, SMTP real, reCAPTCHA test key, placeholders TODO en MAYÚSCULAS, excluye `internal/`.
- **Client directives:** `client:load` (ProgressBar, Hero) · `client:visible` (Contact) · `client:idle` (ScrollToTop, WhatsApp, Cursor).

---

## 9. ACCESIBILIDAD (WCAG AA, siempre)
Skip-link CSS propio · `<main id="main-content">` · `prefers-reduced-motion` en todo · touch targets ≥44px · `aria-label`/`aria-expanded` · contraste AA (texto sobre oscuro ≥4.5:1; no opacidad <0.55 en texto) · `alt` en toda imagen · `focus-visible`.

---

## 10. CHECKLIST "NO PUEDE FALTAR" (gate por sitio)
- [ ] ProgressBar · WhatsApp flotante · Scroll-to-top · Cursor de industria
- [ ] Navbar con CTA Cotizar + scroll-spy + menú móvil · Topbar
- [ ] Formulario contacto dual (email + WhatsApp) + reCAPTCHA + contact.php
- [ ] Footer: CTA banner + columnas + **Certificaciones Bureau Veritas** + redes + "Desarrollado por YaDev"
- [ ] **Panel YaDev oculto** (brandbook + firma + membrete)
- [ ] Los 8 entregables de marca generados
- [ ] SEO completo (JSON-LD, OG, sitemap, robots) · site-config + gate · check-hostinger 0 errores
- [ ] Pa11y limpio + Lighthouse ≥95

---

## 11. ¿SISTEMA o DISEÑO? (no confundir)
- **SISTEMA (idéntico):** todo lo de arriba — copiar del estándar. La PERSONALIDAD móvil del WhatsApp/CTA/tel: es intocable.
- **DISEÑO (único, por el motor):** hero, composición, grids, navegación (patrón), movimiento, transiciones, cursor (estilo), tipografía. Ver `CREATIVE_ENGINE.md` + `PROJECT_DNA_LOG.md`.

> En móvil: la diferenciación de navegación vive en la animación del overlay; el WhatsApp button + CTA + carga rápida son SISTEMA.

---

## 12. ERRORES DE LAYOUT RECURRENTES (checklist anti-bugs — COICEM 2026-06)

Bugs que aparecieron repetidamente. Verificar SIEMPRE antes de dar por listo:

### Navbar/header fijo (`position: fixed`)
- [ ] **`scroll-margin-top` en TODAS las secciones ancla** (`:where([id]){scroll-margin-top: <alto navbar>+16px}`). Sin esto, al navegar por `#ancla` el navbar TAPA el inicio de la sección → "no veo contacto", "cotizar cortado".
- [ ] **`padding-top` en el contenedor de contenido = alto del navbar** (si el navbar cubre el flujo). Sincronizar ambos valores si cambia el alto.
- [ ] **Logo legible**: ≥48px de alto en el navbar (no 40px — "se ve muy pequeño").

### Overflow horizontal en móvil ("contenido cortado a los lados", franja negra a la derecha)
- [ ] **`min-width: 0` en grid/flex items con texto largo.** Un grid item tiene `min-width:auto` por defecto → un titular largo lo expande más allá del viewport → overflow horizontal → todo se ve cortado a la derecha. Causa #1 del bug.
- [ ] **`overflow-wrap: break-word`** en titulares grandes; bajar el mínimo del `clamp()` para móvil.
- [ ] **Verificar con:** `document.documentElement.scrollWidth === clientWidth` en 390px. Si difieren, hay overflow.

### Footer (columnas que se desbordan)
- [ ] **`min-width: 0` + `overflow-wrap: anywhere`** en columnas con palabras largas (MANTENIMIENTO, INFRAESTRUCTURA).
- [ ] **`white-space: nowrap`** en valores cortos que no deben partirse ("PENDIENTE" → no "PENDIEN TE").
- [ ] Sin el sidebar/navbar comiendo ancho, rebalancear el grid de columnas.

### Verificación obligatoria (Playwright MCP)
- [ ] Screenshot en **390px (móvil)** y **1366px (desktop)**: hero, navegación por ancla a #contacto, footer completo (hasta "Desarrollado por YaDev").
- [ ] `scrollWidth === clientWidth` en móvil (sin overflow).
