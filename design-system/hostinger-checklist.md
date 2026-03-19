# Hostinger Deployment Checklist

Use this checklist for every client project deployed to Hostinger shared hosting.
Tick each item before considering the deployment complete.

---

## Pre-Build (Local)

- [ ] `astro.config.mjs` has `build.assets = 'assets'` (NOT the default `_astro`)
- [ ] `astro.config.mjs` uses `fileURLToPath()` for `tailwind configFile` path
- [ ] `public/.htaccess` is present and does NOT include a Content-Security-Policy header
- [ ] `public/.htaccess` includes `AddType text/css .css` and `AddType application/javascript .js`
- [ ] `public/.htaccess` includes `AddType image/svg+xml .svg`
- [ ] `public/contact.php` uses `mail()` — NOT PHPMailer with SMTP
- [ ] `public/contact.php` PLACEHOLDER values are replaced (domain, email, company name, color, services)
- [ ] Logo file used in OG image is PNG format (not SVG — WhatsApp cannot render SVG in previews)
- [ ] OG image (`og-image.png`) is exactly 1200x630 pixels with logo centered
- [ ] OG image background uses a solid brand color (avoid transparent or gradient — WhatsApp clips)
- [ ] Favicon is included as `public/favicon.ico` or `public/favicon.svg`
- [ ] `<meta property="og:image">` points to absolute URL (with `https://domain.com/og-image.png`)
- [ ] `<meta property="og:image:width">` = 1200 and `<meta property="og:image:height">` = 630

---

## Build

- [ ] Run `npm run build` and confirm `dist/` folder is generated
- [ ] Confirm `dist/assets/` folder exists (NOT `dist/_astro/`)
- [ ] Confirm `dist/.htaccess` is present in the output
- [ ] Confirm `dist/contact.php` is present in the output
- [ ] Check `dist/sitemap-index.xml` and `dist/sitemap-0.xml` were generated
- [ ] Verify no console errors during build (TypeScript errors, missing modules)

---

## SSL Certificate

- [ ] SSL certificate is active in Hostinger hPanel > SSL
- [ ] Certificate covers the bare domain (`domain.com`)
- [ ] Certificate covers the `www` subdomain (`www.domain.com`)
- [ ] Both `https://domain.com` and `https://www.domain.com` load without SSL warnings
- [ ] If using custom SSL (not Auto SSL), verify expiry date is at least 90 days away

---

## DNS Records

- [ ] A record points to the Hostinger server IP
- [ ] CNAME `www` points to the bare domain
- [ ] SPF record is set for the domain email (prevents contact.php emails from landing in spam)
  - Example: `v=spf1 include:hostinger.com ~all`
- [ ] DKIM record is configured (generate in Hostinger hPanel > Email > DNS)
- [ ] DMARC record is set
  - Example: `v=DMARC1; p=none; rua=mailto:admin@domain.com`

---

## Upload to Hostinger

- [ ] Upload ALL contents of `dist/` to `public_html/` (not the `dist/` folder itself)
- [ ] Verify file structure: `public_html/index.html`, `public_html/assets/`, `public_html/.htaccess`, `public_html/contact.php`
- [ ] If replacing an existing site, delete old `_astro/` folder if it exists
- [ ] Confirm `.htaccess` file is present (Hostinger FTP/File Manager may hide dot-files)
  - In Hostinger File Manager: enable "Show Hidden Files"
- [ ] Confirm `contact.php` has correct permissions: 644 (readable by server, not executable by others)

---

## Post-Upload Verification

- [ ] Purge Hostinger cache: hPanel > Hosting > Manage > Cache > Purge All
- [ ] Open site in incognito window (Chrome/Firefox — avoids your local browser cache)
- [ ] Site loads with HTTPS (padlock icon visible)
- [ ] Bare domain (`https://domain.com`) redirects to HTTPS
- [ ] Fonts load correctly (Plus Jakarta Sans / Inter visible, not falling back to system fonts)
- [ ] CSS is loading correctly (page is not unstyled)
- [ ] JavaScript is loading correctly (interactive elements like nav, contact form work)
- [ ] Images load correctly (no broken image icons)

---

## Functionality Testing

- [ ] Navbar scroll behavior works (sticky, color change on scroll)
- [ ] Mobile menu opens and closes (hamburger button)
- [ ] All internal anchor links scroll to correct section
- [ ] Contact form submits successfully (test with a real email)
- [ ] Contact form shows success message after submission
- [ ] Contact form shows error message if required fields are empty
- [ ] Contact form rate limit works (submit twice within 60s, second should be blocked)
- [ ] Email is received at DESTINATION_EMAIL from the contact form submission
- [ ] Reply-To header is correct in received email (reply goes to form submitter, not noreply@)
- [ ] WhatsApp button (if present) opens correct phone number
- [ ] Scroll-to-top button (if present) appears after scrolling and works

---

## SEO and Social

- [ ] Page title is descriptive and includes primary keyword
- [ ] Meta description is between 120-160 characters
- [ ] `<html lang="es">` (or appropriate language code)
- [ ] Sitemap is accessible at `https://domain.com/sitemap-index.xml`
- [ ] Sitemap can be submitted to Google Search Console
- [ ] robots.txt allows crawling (or is absent — Astro does not generate one by default)
- [ ] Facebook / WhatsApp OG preview: use Facebook Sharing Debugger
  - URL: https://developers.facebook.com/tools/debug/
  - Enter the site URL and click "Scrape Again"
  - Verify OG image appears correctly (1200x630, logo centered, no clipping)
  - WhatsApp preview uses Facebook's OG metadata — this debugger covers both

---

## Performance

- [ ] Run PageSpeed Insights: https://pagespeed.web.dev/
- [ ] Mobile score >= 70 (target 85+)
- [ ] Desktop score >= 85 (target 95+)
- [ ] Core Web Vitals: LCP < 2.5s, CLS < 0.1, FID/INP < 200ms
- [ ] Images are in WebP or AVIF format (not PNG/JPG for photos)
- [ ] No render-blocking resources (fonts loaded with `display=swap`)

---

## Accessibility

- [ ] Skip-to-content link is present at top of page (hidden, visible on focus)
- [ ] All images have descriptive `alt` attributes
- [ ] Color contrast passes WCAG AA (4.5:1 for normal text, 3:1 for large text)
- [ ] All interactive elements are keyboard accessible (Tab, Enter, Space, Escape)
- [ ] Form inputs have associated `<label>` elements
- [ ] Focus ring is visible on all focusable elements
- [ ] No content relies solely on color to convey meaning

---

## Final Sign-off

- [ ] Client has reviewed and approved the live site
- [ ] Login credentials for Hostinger are stored securely (not in plaintext files)
- [ ] Domain registrar login is documented
- [ ] SSL renewal reminder is set (if not using Auto SSL)
- [ ] Project folder in `internal/PROYECTOS/` is updated with final assets

---

## Common Hostinger Issues and Fixes

| Problem | Cause | Fix |
|---|---|---|
| Site loads unstyled (no CSS) | MIME type issue, CSS served as text/plain | Add `AddType text/css .css` to .htaccess |
| Assets return 404 | Build output in `_astro/` folder | Set `build.assets = 'assets'` in astro.config.mjs |
| Contact form returns 500 | SMTP blocked | Use `mail()` not PHPMailer/SMTP |
| Fonts not loading | CSP header blocking fonts.gstatic.com | Remove Content-Security-Policy from .htaccess |
| WhatsApp shows no OG image | SVG logo in OG image | Convert OG image to PNG (1200x630) |
| HTTPS mixed content warning | Some assets loaded over HTTP | Check all asset URLs use HTTPS or are protocol-relative |
| PHP contact form 403 | .htaccess blocking .php files | Check FilesMatch patterns, add explicit allow for contact.php |
| Tailwind config not found | Special chars in path | Use `fileURLToPath(new URL('./tailwind.config.mjs', import.meta.url))` |
| Site not updating after upload | Hostinger server cache | Purge cache from hPanel after every upload |
| Email in spam folder | Missing SPF/DKIM records | Configure SPF, DKIM, DMARC DNS records |
