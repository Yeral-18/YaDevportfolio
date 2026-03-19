---
name: generate-brandbook
description: Genera brandbook HTML completo para un cliente — paleta, tipografía, logo variants, papelería corporativa
---

## Genera un Brandbook HTML autocontenido para el cliente.

### INPUTS REQUERIDOS
- Nombre de empresa
- Industria/sector
- Colores de marca (primary, secondary, accent)
- Logo (PNG con transparencia)
- Servicios principales
- Datos de contacto

### PROCESO
1. Leer el logo del cliente y convertirlo a base64
2. Generar variantes del logo: oficial (fondo blanco), versión para fondo oscuro, isotipo
3. Definir paleta de colores con escalas 50-900
4. Definir tipografía (display + body)
5. Crear secciones del brandbook:
   - Portada con logo y nombre
   - Filosofía de marca (misión, visión, valores)
   - Logo: versiones y variantes
   - Logo: área de respeto y tamaños mínimos
   - Logo: usos incorrectos
   - Paleta de colores (con hex, RGB)
   - Tipografía (familias, pesos, jerarquía)
   - Aplicaciones: tarjetas de presentación
   - Aplicaciones: firma de correo
   - Aplicaciones: hoja membretada
   - Aplicaciones: sitio web corporativo
   - Certificaciones (si aplica: ISO, Bureau Veritas)

### OUTPUT
- HTML autocontenido (todas las imágenes en base64)
- Formato A4 (210mm x 297mm por sección)
- Print-ready (@media print optimizado)
- Guardar en: `{proyecto}/brand/brandbook.html`
- Copiar a: `{proyecto}/web/dist/internal/brandbook.html`

### ESTILO
- Profesional, limpio, moderno
- Usar colores de la marca como acentos
- Fondo blanco con tipografía oscura
- Cada sección ocupa una "página" A4
