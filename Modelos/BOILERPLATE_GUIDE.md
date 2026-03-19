# Guia Boilerplate - Nuevos Proyectos YaDev

> Ultima actualizacion: 2026-03-18
> Basado en proyectos: ECOMAG02, MULTISERVICIOS P&J

---

## 1. Estructura Estandar de Proyecto

Cada proyecto de cliente sigue esta estructura dentro de `internal/PROYECTOS/{AÑO}/{NOMBRE_CLIENTE}/`:

```
{NOMBRE_CLIENTE}/
├── brand/                          # Identidad visual
│   ├── brandbook.html              # Manual de marca (HTML autocontenido)
│   ├── firma-correo.html           # Firma de correo electronico (HTML inline)
│   ├── hoja-membretada.html        # Hoja membretada (HTML para imprimir)
│   ├── tarjeta-presentacion.png    # Tarjeta de presentacion
│   ├── tarjetas-corporativas.png   # Variantes de tarjeta
│   ├── logo-oficial.png            # Logo principal PNG
│   ├── isotipo.png                 # Isotipo/icono
│   ├── logo_b64.txt                # Logo en Base64 (para firma correo)
│   ├── logo_main_b64.txt           # Logo principal en Base64
│   ├── logo_small_b64.txt          # Logo pequeño en Base64
│   └── *_b64.txt                   # Otros assets en Base64
│
├── {nombre}-web/                   # Proyecto web (Astro)
│   ├── .astro/
│   ├── .env.example
│   ├── astro.config.mjs
│   ├── tailwind.config.mjs
│   ├── package.json
│   ├── tsconfig.json
│   ├── public/
│   │   ├── favicon.png
│   │   ├── og-image.png            # 1200x630px para WhatsApp/redes
│   │   ├── robots.txt
│   │   └── images/
│   └── src/
│       ├── pages/
│       │   └── index.astro
│       ├── components/
│       ├── layouts/
│       └── styles/
│
├── RECURSOS/                       # Material del cliente (PDFs, fotos, docs)
│   └── (brochures, fotos, textos del cliente)
│
└── *.png, *.svg, *.pdf             # Assets sueltos del proyecto
```

---

## 2. Proceso Paso a Paso para Nuevo Proyecto

### Fase 1: Recopilacion de Informacion
1. Recibir brief del cliente (que hace la empresa, servicios, contacto)
2. Recopilar assets: logo (preferiblemente PNG alta resolucion), fotos, textos
3. Definir estructura del sitio (secciones, paginas)
4. Revisar competencia (archivos en Modelos/ por industria)

### Fase 2: Identidad Visual (brand/)
1. **Brandbook** - Crear manual de marca HTML con:
   - Paleta de colores (primarios, secundarios, neutros)
   - Tipografia (familias, pesos, tamaños)
   - Uso del logo (versiones, espaciado, prohibiciones)
   - Tono de comunicacion
2. **Firma de correo** - HTML inline con logo en Base64
   - Convertir logo a Base64: guardar en `logo_b64.txt`
   - Usar tamaños: 60px, 100px, 200px segun necesidad
   - Toda imagen embebida como data URI (no URLs externas)
3. **Hoja membretada** - HTML con header/footer corporativo
4. **Tarjetas de presentacion** - Diseño front/back

### Fase 3: Seleccion de Template
1. Consultar CATALOGO.md para ver templates y CSS themes existentes
2. Elegir template base segun industria del cliente
3. Seleccionar CSS theme que mejor encaje con la personalidad de marca
4. **REGLA CRITICA:** Verificar que el diseno sea visualmente unico vs otros proyectos del portafolio

### Fase 4: Desarrollo Web
1. Crear proyecto Astro:
   ```bash
   npm create astro@latest {nombre}-web
   ```
2. Instalar dependencias:
   ```bash
   npm install @astrojs/svelte @astrojs/tailwind svelte tailwindcss
   ```
3. Configurar `astro.config.mjs` con fixes criticos (ver seccion 4)
4. Desarrollar paginas basandose en el template elegido
5. Adaptar contenido, colores, imagenes al cliente

### Fase 5: Testing y QA
1. Probar en: Chrome, Firefox, Safari, mobile
2. Verificar: responsive, velocidad de carga, SEO basico
3. Probar formulario de contacto
4. Verificar OG Image en WhatsApp (compartir URL y ver preview)
5. Validar Schema.org con Google Rich Results Test

### Fase 6: Deploy a Hostinger
1. Build: `npm run build`
2. Subir contenido de `dist/` a `public_html/`
3. Configurar .htaccess
4. Probar en produccion
5. Configurar DNS si es dominio nuevo

---

## 3. Checklist de Entregables

### Obligatorios
- [ ] Sitio web funcional y responsive
- [ ] Brandbook HTML
- [ ] Firma de correo HTML (con logo Base64)
- [ ] OG Image para redes sociales (1200x630px)
- [ ] Favicon PNG
- [ ] Schema.org structured data
- [ ] Meta tags SEO completos
- [ ] Formulario de contacto funcional
- [ ] Cookie/privacy banner

### Opcionales (segun paquete)
- [ ] Hoja membretada HTML
- [ ] Tarjetas de presentacion
- [ ] Brochure digital (PDF)
- [ ] Cotizador/herramienta interactiva
- [ ] Multi-idioma (ES/EN)
- [ ] Blog/noticias
- [ ] Google Analytics integrado

---

## 4. Problemas Conocidos y Soluciones (Pitfalls)

### 4.1 Hostinger bloquea carpeta `_astro/`
**Problema:** Directorios con underscore son restringidos en Hostinger shared hosting.
**Solucion:** En `astro.config.mjs` agregar:
```js
export default defineConfig({
  build: {
    assets: 'assets'  // NUNCA usar '_astro/' (default)
  }
});
```
**Cuando aplicar:** SIEMPRE, desde el primer `astro.config.mjs`

### 4.2 Tailwind no genera clases con `&` en la ruta
**Problema:** El caracter `&` en nombres de carpeta (ej: `MULTISERVICIOS P&J`) rompe el content scanning de Tailwind.
**Solucion:** En `tailwind.config.mjs` usar rutas absolutas con forward slashes:
```js
import { fileURLToPath } from 'url';
const __dirname = fileURLToPath(new URL('.', import.meta.url)).replace(/\\/g, '/');

export default {
  content: [
    __dirname + 'src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'
  ]
};
```
En `astro.config.mjs`:
```js
import { fileURLToPath } from 'url';
// ...
integrations: [
  tailwind({
    configFile: fileURLToPath(new URL('./tailwind.config.mjs', import.meta.url))
  })
]
```
**Cuando aplicar:** Siempre que el nombre de carpeta del proyecto contenga caracteres especiales (&, espacios, acentos)

### 4.3 CSP bloquea CSS en Hostinger
**Problema:** `Content-Security-Policy` en .htaccess es sobreescrito por Hostinger y puede bloquear CSS.
**Solucion:** NO poner CSP en .htaccess. En su lugar agregar:
```apache
AddType text/css .css
AddType application/javascript .js
```
**Cuando aplicar:** En TODOS los archivos .htaccess

### 4.4 Logo SVG aparece gigante sin CSS
**Problema:** SVGs con viewBox propio ignoran width/height HTML.
**Solucion:** Usar PNG en vez de SVG para el logo del navbar. Reservar SVG solo para iconos inline.
**Cuando aplicar:** Siempre en el logo principal del navbar

### 4.5 SMTP bloqueado en Hostinger
**Problema:** Puerto 587 saliente bloqueado en hosting compartido (Office 365 SMTP no funciona).
**Solucion:** Usar `mail()` nativo de PHP:
```php
mail($to, $subject, $message, $headers);
```
**Cuando aplicar:** Todos los formularios de contacto en Hostinger

### 4.6 Logos de clientes borrosos en retina
**Problema:** Imagenes de 200px se ven pixeladas en pantallas retina.
**Solucion:** Escalar a 400px wide (2.5x el tamaño display). Agregar CSS:
```css
img { image-rendering: -webkit-optimize-contrast; }
```
**Cuando aplicar:** Todos los logos de clientes, certificaciones, partners

### 4.7 OG Image para WhatsApp
**Problema:** WhatsApp recorta la preview cuadrada desde el centro.
**Solucion:** Disenar OG Image 1200x630px con logo GRANDE centrado sobre fondo blanco/solido. No poner info en los bordes.
**Cuando aplicar:** Todos los proyectos

### 4.8 DNS Microsoft 365 + Hostinger
**Configuracion requerida:**
```
SPF:   v=spf1 include:spf.protection.outlook.com include:_spf.mail.hostinger.com ~all
DMARC: v=DMARC1; p=none; rua=mailto:{email}
MX:    {dominio}.mail.protection.outlook.com
DKIM:  Configurar via security.microsoft.com/dkimv2
```
**Cuando aplicar:** Clientes con correo Microsoft 365 en Hostinger

---

## 5. Guia de Seleccion de Template por Industria

### Para industrias existentes:

| Industria del Cliente | Template Base | CSS Theme Recomendado | Tipografia Sugerida |
|---|---|---|---|
| Construccion / Ingenieria Civil | construccion.html | brutalist (premium) o industrial | Space Grotesk |
| Tienda / E-commerce | ecommerce.html | minimal (limpio) o magazine (editorial) | Cambiar a Outfit o Sora |
| Certificaciones Electricas (RETIE) | electrico.html | dashboard (premium) o modern | Inter (mantener) |
| Ambiental / Forestal | forestal.html | organic (artesanal) o immersive (fotos) | Playfair Display |
| Clinica / Salud / Medico | salud.html | glass (premium) o clean | DM Sans |
| Software / SaaS / Tech | tecnologia.html | neon (cyberpunk) o neumorphic (soft) | Satoshi |
| Transporte / Logistica | transporte.html | modern o split | Cambiar a Plus Jakarta Sans |

### Para industrias nuevas (sin template):
1. Elegir el template existente mas cercano en "voz visual"
2. Modificar completamente colores, tipografia y layout
3. Crear 3 CSS themes nuevos para la industria
4. Agregar archivo `assets/css/industries/{industria}.css`

### Mapeo de industria cercana:
| Industria Nueva | Template Base Sugerido | Razon |
|---|---|---|
| Restaurante | forestal.html | Ambos usan calor, fotos grandes, editorial |
| Inmobiliaria | transporte.html | Ambos necesitan busqueda/filtros, info densa |
| Educacion | salud.html | Ambos necesitan calma, confianza, CTAs claros |
| Legal / Abogados | electrico.html | Ambos son corporativos, serios, con acreditaciones |
| Agro / Agricultura | forestal.html | Ambos son naturaleza, tierra, organico |

---

## 6. Stack Tecnico Estandar

```
Framework:    Astro 5
UI:           Svelte 5 (componentes interactivos)
Styling:      TailwindCSS 3
Tipografia:   Google Fonts / Fontshare
Iconos:       SVG inline (Heroicons/custom)
Carousel:     Swiper.js 11
Animaciones:  CSS custom + IntersectionObserver
Hosting:      Hostinger (shared, PHP enabled)
Correo:       Microsoft 365 / Outlook
Formularios:  PHP mail() nativo
Analytics:    Google Analytics 4
SEO:          Schema.org JSON-LD
```

---

## 7. Comandos Rapidos

```bash
# Crear nuevo proyecto Astro
npm create astro@latest {nombre}-web -- --template minimal

# Instalar dependencias comunes
cd {nombre}-web
npm install @astrojs/svelte @astrojs/tailwind svelte tailwindcss

# Build para produccion
npm run build

# Preview local
npm run preview

# Dev server
npm run dev
```

---

## 8. .htaccess Base para Hostinger

```apache
# Redirect HTTP to HTTPS
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]

# MIME Types (critico para Hostinger)
AddType text/css .css
AddType application/javascript .js
AddType image/svg+xml .svg
AddType application/font-woff2 .woff2

# Cache Control
<IfModule mod_expires.c>
    ExpiresActive On
    ExpiresByType text/css "access plus 1 month"
    ExpiresByType application/javascript "access plus 1 month"
    ExpiresByType image/png "access plus 1 year"
    ExpiresByType image/jpeg "access plus 1 year"
    ExpiresByType image/svg+xml "access plus 1 year"
    ExpiresByType font/woff2 "access plus 1 year"
</IfModule>

# Compression
<IfModule mod_deflate.c>
    AddOutputFilterByType DEFLATE text/html text/css application/javascript application/json image/svg+xml
</IfModule>

# Security Headers (sin CSP - Hostinger lo sobreescribe)
Header set X-Content-Type-Options "nosniff"
Header set X-Frame-Options "SAMEORIGIN"
Header set X-XSS-Protection "1; mode=block"
Header set Referrer-Policy "strict-origin-when-cross-origin"

# Custom 404
ErrorDocument 404 /404.html
```
