---
name: email-signature
description: Genera firma de correo profesional compatible con Outlook — HTML inline, logo base64, responsive
---

## Genera una firma de correo HTML profesional.

### INPUTS REQUERIDOS
- Nombre del firmante
- Cargo
- Empresa
- Teléfono
- Email
- Web
- Logo (PNG → convertir a base64)
- Colores de marca (primary, secondary, accent)
- Dirección física
- Redes sociales (opcional)

### DISEÑO
- HTML con CSS inline (NO <style> tags — Outlook los ignora)
- Usar tablas para layout (Outlook no soporta flexbox/grid)
- Máximo 600px de ancho
- Logo embebido como base64 (data:image/png;base64,...)
- Iconos de contacto como SVG inline o Unicode
- Separador visual entre logo y datos
- Servicios principales en texto pequeño al final
- Certificaciones ISO si aplica

### ESTRUCTURA
```
┌──────────────────────────────────────┐
│  [LOGO]  │  Nombre Completo          │
│          │  Cargo                     │
│          │  EMPRESA S.A.S             │
│          │                            │
│          │  Tel: +57 XXX XXXXXXX      │
│          │  Email: correo@empresa.com │
│          │  Web: www.empresa.com      │
│          │  Dirección                 │
├──────────────────────────────────────┤
│  Servicio 1 • Servicio 2 • Servicio 3│
│  Certificados ISO 9001 | 14001 | ... │
└──────────────────────────────────────┘
```

### COMPATIBILIDAD
- Outlook Desktop (Windows/Mac)
- Outlook Web (OWA)
- Gmail
- Apple Mail
- Thunderbird

### OUTPUT
- HTML autocontenido (sin dependencias externas)
- Guardar en: `{proyecto}/brand/firma-correo.html`
- Copiar a: `{proyecto}/web/dist/internal/firma-correo.html`

### ANTI-PATTERNS
- NO usar CSS external o <style> blocks
- NO usar flexbox/grid (Outlook no lo soporta)
- NO usar imágenes externas (todo base64)
- NO exceder 100KB total
