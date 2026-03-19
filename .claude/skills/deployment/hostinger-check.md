---
name: hostinger-check
description: Validación final completa para deploy en Hostinger — checklist de 30+ items, fixes automáticos
---

## Validación y preparación final para producción en Hostinger.

### PRE-DEPLOY CHECKS

#### Build
- [ ] `npm run build` exitoso sin errores
- [ ] Carpeta de assets es `assets/` (NO `_astro/`)
- [ ] index.html referencia CSS en `/assets/` no `/_astro/`
- [ ] Todas las CSS tienen utility classes de Tailwind (buscar `.flex`, `.grid`)

#### .htaccess
- [ ] NO tiene Content-Security-Policy (Hostinger lo sobreescribe → bloquea CSS)
- [ ] Tiene `AddType text/css .css`
- [ ] Tiene `AddType application/javascript .js`
- [ ] Tiene `AddType image/svg+xml .svg`
- [ ] HTTPS redirect activo
- [ ] Gzip compression habilitado
- [ ] Cache 1 año para assets estáticos
- [ ] Bloqueo de archivos sensibles (.env, .sql, .log)

#### Imágenes
- [ ] Logo navbar es PNG (NO SVG)
- [ ] Logo PNG tiene transparencia (RGBA mode)
- [ ] OG image es 1200x630 con logo centrado
- [ ] Logos de clientes mínimo 400px wide
- [ ] Hero image tiene `fetchpriority="high"`
- [ ] Demás imágenes tienen `loading="lazy"`

#### Formulario
- [ ] contact.php usa `mail()` (NO SMTP — puerto 587 bloqueado)
- [ ] CORS restringido al dominio del sitio
- [ ] Rate limiting activo (1 envío/minuto)
- [ ] Validación de email con FILTER_VALIDATE_EMAIL
- [ ] Whitelist de servicios configurada
- [ ] Reply-To apunta al email del cliente que llena el formulario

#### SEO
- [ ] Title tag con keywords + ubicación
- [ ] Meta description 150-160 caracteres
- [ ] Open Graph tags (og:title, og:description, og:image, og:url)
- [ ] Twitter Card tags
- [ ] Schema.org: LocalBusiness, Organization, FAQPage, Services
- [ ] Canonical URL
- [ ] lang="es-CO"
- [ ] sitemap-index.xml generado
- [ ] robots.txt presente

#### Accesibilidad
- [ ] Skip-to-content link
- [ ] aria-labels en botones icon-only
- [ ] focus-visible outlines
- [ ] reCAPTCHA badge oculto via CSS

#### Panel YaDev
- [ ] Sidebar oculto presente
- [ ] Link a brandbook funciona
- [ ] Link a firma de correo funciona

### POST-DEPLOY CHECKS

#### En Hostinger
- [ ] Subir dist/ completo a public_html/
- [ ] Borrar carpeta _astro/ vieja si existe
- [ ] Purgar caché de Hostinger
- [ ] Verificar SSL cubre dominio + www

#### DNS (si usa Microsoft 365)
- [ ] SPF: include:spf.protection.outlook.com + include:_spf.mail.hostinger.com
- [ ] DKIM: 2 CNAME selectors configurados (security.microsoft.com/dkimv2)
- [ ] DMARC: TXT _dmarc configurado
- [ ] MX apunta a mail.protection.outlook.com

#### Verificación final
- [ ] Abrir en incógnito — CSS carga correctamente
- [ ] Formulario email funciona (probar con curl)
- [ ] Formulario WhatsApp funciona
- [ ] Facebook Debug scrape (developers.facebook.com/tools/debug/)
- [ ] Google Search Console: enviar sitemap
- [ ] Compartir link en WhatsApp — OG image se ve nítida

### PROBLEMAS COMUNES

| Síntoma | Causa | Fix |
|---------|-------|-----|
| CSS no carga | _astro/ bloqueado | build.assets = 'assets' |
| Logo gigante | SVG sin CSS | Usar PNG |
| Email no envía | SMTP bloqueado | Usar mail() |
| "No verificable" | Sin SPF/DKIM | Configurar DNS |
| OG borrosa | Imagen muy compleja | Solo logo centrado |
| reCAPTCHA visible | CSS no cargó | Verificar CSS primero |
