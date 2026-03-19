# YaDev Design System — Boilerplate

Centralized starting point for all client projects. Every file here is a production-ready template built from real-world experience with ECOMAG S.A.S and Multiservicios P&J S.A.S, both deployed on Hostinger shared hosting.

---

## Stack

- **Framework:** Astro (static output)
- **UI Components:** Svelte (client:load / client:visible)
- **Styling:** Tailwind CSS + custom CSS variables
- **Fonts:** Plus Jakarta Sans (display) + Inter (body)
- **Deployment target:** Hostinger shared hosting (Apache)
- **Contact:** PHP mail() — NOT SMTP (blocked on Hostinger)

---

## How to Start a New Project

### Step 1 — Copy the templates

```bash
# From the boilerplate directory
cp design-system/tokens-template.ts       my-project/src/design-system/tokens.ts
cp design-system/global-template.css      my-project/src/styles/global.css
cp design-system/astro-config-template.mjs  my-project/astro.config.mjs
cp design-system/tailwind-config-template.mjs my-project/tailwind.config.mjs
cp design-system/htaccess-template        my-project/public/.htaccess
cp design-system/contact-php-template.php my-project/public/contact.php
```

### Step 2 — Replace all PLACEHOLDER values

Search for `PLACEHOLDER` in all copied files and replace:

| Placeholder | What to put |
|---|---|
| `SITE_DOMAIN` | `https://myclient.com` |
| `SITE_URL_BASE` | Same as above, no trailing slash |
| `CLIENT_NAME` | `My Client S.A.S` |
| `DESTINATION_EMAIL` | `info@myclient.com` |
| `SERVICE_LIST` | Array of the client's service names |
| `PRIMARY_COLOR` | Client's main brand color (hex) |
| `SECONDARY_COLOR` | Supporting brand color |
| `ACCENT_COLOR` | Highlight / tag color |
| `CTA_COLOR` | Call-to-action button color (can differ from primary) |
| `DARK_COLOR` | Dark text / footer background |
| `LIGHT_COLOR` | Page background (near-white) |

### Step 3 — Customize the color personality

Do NOT just swap hex values. Think about the industry:

- Construccion / Ingenieria: azules institucionales, grises acero, acentos naranjas
- Ambiental / Forestal: verdes oscuros, azules agua, acentos lima
- Tecnologia / SaaS: negro/gris oscuro, morados o azules neón, acentos cyan
- Salud / Bienestar: blancos, verdes suaves, azules claros
- Restaurante / Food: cafes cálidos, rojos, amarillos terracota
- Logistica / Transporte: azules profundos, grises, naranja CTA agresivo
- Legal / Consultoria: azul marino oscuro, dorados, tipografia serif

### Step 4 — Verify visual uniqueness

Before writing a single component, answer:
- What hero pattern am I using? (NOT the same as the last project)
- What grid layout for services? (zigzag / bento / masonry / carousel)
- What typographic personality? (font pairing, size scale, weight distribution)
- What interaction patterns? (hover effects, scroll reveals)

Reference the file `CLAUDE.md` section "REGLA CRITICA: Diseno Unico por Proyecto".

---

## Component List

All components use CSS variables from the design system. No hardcoded colors.

### Layout
- `.section-container` — max-w-7xl with responsive horizontal padding
- `.section-padding` — py-16 md:py-24 standard vertical rhythm

### Typography
- `.heading-primary` — clamp(1.75rem, 4vw, 3rem), display font, tight tracking
- `.heading-secondary` — clamp(1.25rem, 2.5vw, 1.75rem), display font
- `.text-body` — clamp(0.9375rem, 1.5vw, 1.0625rem), body font, gray-600
- `.text-small` — text-sm, gray-500
- `.section-label` — uppercase, tracking-widest, primary color tag

### Buttons
- `.btn-primary` — filled CTA button, spring hover lift, colored shadow
- `.btn-secondary` — outlined button, fills on hover with primary color

### Cards
- `.card` — white bg, rounded-xl, shadow-sm, lift on hover
- `.card-accent` — adds top border that reveals primary color on hover

### Forms
- `.input-field` — consistent border, focus ring using primary-50, error state

### Badges
- `.badge` + `.badge-primary` / `.badge-accent` — pill label components

### Icon Containers
- `.icon-box` + `.icon-box-sm/md/lg` — square icon wrappers with brand bg

### Animations
- `.reveal` + `.revealed` — scroll-triggered fade-up (add class via IntersectionObserver)
- `.reveal-delay-1/2/3/4` — staggered delays: 100ms / 200ms / 300ms / 400ms
- `.image-zoom` — subtle scale(1.03) on hover
- `.link-underline` — animated underline from left

### Scrollbar
- `.scrollbar-hide` — hides scrollbar, allows scroll
- `.scrollbar-thin` — thin branded scrollbar

### GPU
- `.gpu` — translate3d(0,0,0) will-change:transform for animated elements

---

## Tokens Reference

Design tokens live in `tokens.ts` and are exported as both TypeScript constants and as a function `generateCSSVars()` that creates a `<style>` tag injectable into the Astro Layout.

Alternatively, the tokens are duplicated as CSS custom properties in `:root` inside `global.css`. Both approaches are kept in sync manually.

---

## Hostinger Deployment Checklist

See `hostinger-checklist.md` for the full step-by-step.

Critical non-obvious rules:
1. `build.assets = 'assets'` in astro.config.mjs — Hostinger cannot serve `_astro/` folders
2. NO Content-Security-Policy header in .htaccess — it blocks Google Fonts and inline scripts
3. `AddType text/css .css` MUST be in .htaccess — Hostinger sometimes serves CSS as text/plain
4. Use PHP `mail()`, never SMTP — port 587/465 is blocked on shared hosting
5. Logo must be PNG not SVG — WhatsApp OG preview does not render SVG logos
6. SSL must cover both `domain.com` AND `www.domain.com`
7. Always purge Hostinger cache from hPanel after every upload
8. Test in incognito after deploy — browser cache will lie to you

---

## Project History

| Client | Domain | Stack Notes |
|---|---|---|
| ECOMAG S.A.S | ecomagsas.com | Astro + Svelte + Tailwind, green/blue palette |
| Multiservicios P&J S.A.S | multiserviciospj.com | Same stack, fileURLToPath configFile fix applied |

The `fileURLToPath` fix in `astro.config.mjs` exists because the project path contains special characters (`P&J`). Without it, Vite cannot resolve the Tailwind config file on Windows. Always use this pattern.
