---
name: optimize-images
description: Optimiza imágenes para web producción — logos retina, OG image, compresión, transparencia
---

## Optimiza todas las imágenes del proyecto para producción.

### TAREAS

#### 1. Logos de clientes
- Mínimo 400px wide (2.5x del display size para retina)
- PNG con fondo transparente (NUNCA JPG para logos)
- Usar Lanczos resampling al redimensionar
- Guardar en: `public/images/clients/`

#### 2. Logo de la empresa
- Versión color con transparencia → `public/logo.png`
- Versión blanca con transparencia → `public/logo-white.png`
- NUNCA usar SVG con raster embebido en navbar (usar PNG)
- Verificar que RGBA tiene canal alpha real

#### 3. OG Image (Open Graph)
- Tamaño: 1200x630px
- Solo el logo GRANDE y centrado
- Fondo blanco (#FFFFFF)
- JPEG calidad 95%
- WhatsApp recorta al centro como thumbnail cuadrado → el logo debe estar centrado
- Guardar en: `public/og-default.jpg`

#### 4. Imágenes de servicios
- Máximo 300KB por imagen
- Considerar WebP cuando sea posible
- Lazy loading por defecto
- Hero image con `fetchpriority="high"`

#### 5. Certificaciones (Bureau Veritas, etc.)
- Usar imagen original sin modificar
- NO remover fondos de certificaciones
- Aplicar `border-radius` via CSS, no modificando la imagen

### HERRAMIENTAS
- Python + Pillow para procesamiento
- `image-rendering: -webkit-optimize-contrast` en CSS para logos
- HTML img: `width` y `height` attributes al 2x del display size

### ANTI-PATTERNS
- NO generar logos borrosos redimensionando JPGs
- NO aplicar filter: invert() a logos con fondo → usar versión white PNG
- NO usar SVG de 86KB con raster embebido
