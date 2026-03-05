# Sistema de Generacion de PDF con Node.js + Puppeteer

Guia completa para implementar generacion de PDFs en proyectos Node.js/Express con React frontend.

---

## Arquitectura

```
FRONTEND (React/Vue/Angular)
    │
    │  fetch() con Authorization header
    │  Content-Type: application/pdf
    ▼
BACKEND (Express)
    │
    ├── Middleware especial (excluye express.json para PDFs)
    ├── Autenticacion para binarios (respuestas texto, no JSON)
    │
    ▼
PDF CONTROLLER
    │
    ├── 1. Consulta datos de BD
    ├── 2. Carga imagenes → Base64
    ├── 3. Genera HTML con CSS embebido
    ├── 4. Puppeteer: HTML → PDF Buffer
    └── 5. Envia Buffer con headers correctos
```

---

## Estructura de Archivos

```
backend/
├── assets/
│   ├── logo.png
│   └── fondo.png (opcional)
├── controllers/
│   └── pdfController.js
├── middleware/
│   └── auth.js
├── routes/
│   └── pdf.js
└── index.js

frontend/src/
└── components/
    └── PDFDownloadButton.jsx
```

---

## Dependencias

```bash
npm install puppeteer express jsonwebtoken
```

---

## Backend

### 1. Configuracion Express (index.js)

```javascript
const express = require('express');
const cors = require('cors');
const app = express();

// CRITICO: Excluir rutas PDF de express.json()
// Si no se hace, el buffer PDF se convierte en JSON corrupto
app.use((req, res, next) => {
  if (req.path.includes('/api/pdf/')) {
    return next();
  }
  express.json({ limit: '10mb' })(req, res, next);
});

app.use((req, res, next) => {
  if (req.path.includes('/api/pdf/')) {
    return next();
  }
  express.urlencoded({ extended: true })(req, res, next);
});

// CORS especial para PDFs
app.use((req, res, next) => {
  if (req.path.includes('/api/pdf/')) {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept, Authorization');
    if (req.method === 'OPTIONS') return res.sendStatus(200);
    return next();
  }
  cors()(req, res, next);
});

// Si usas rate limiting, excluir PDFs
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 200,
  skip: (req) => req.path.includes('/api/pdf/')
});
app.use('/api/', limiter);

// Rutas
app.use('/api/pdf', require('./routes/pdf'));

app.listen(3000);
```

### 2. Middleware Autenticacion Binarios (middleware/auth.js)

```javascript
const jwt = require('jsonwebtoken');

// Para respuestas binarias: errores en texto plano, NO JSON
const authenticateForBinary = async (req, res, next) => {
  try {
    const authHeader = req.headers.authorization;

    if (!authHeader || !authHeader.startsWith('Bearer ')) {
      return res.status(401).send('Token requerido');
    }

    const token = authHeader.replace('Bearer ', '');
    const decoded = jwt.verify(token, process.env.JWT_SECRET);

    // Buscar usuario (ajustar segun tu ORM)
    const user = await User.findById(decoded.userId);
    if (!user) {
      return res.status(401).send('Usuario no encontrado');
    }

    req.user = user;
    next();

  } catch (error) {
    if (error.name === 'JsonWebTokenError') {
      return res.status(401).send('Token invalido');
    }
    if (error.name === 'TokenExpiredError') {
      return res.status(401).send('Token expirado');
    }
    return res.status(500).send('Error del servidor');
  }
};

module.exports = { authenticateForBinary };
```

### 3. Rutas PDF (routes/pdf.js)

```javascript
const express = require('express');
const router = express.Router();
const { generatePDF } = require('../controllers/pdfController');
const { authenticateForBinary } = require('../middleware/auth');

router.get('/documento/:id', authenticateForBinary, generatePDF);

module.exports = router;
```

### 4. Controlador PDF (controllers/pdfController.js)

```javascript
const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs').promises;

// =============================================
// CARGAR IMAGENES EN BASE64
// =============================================
const getImageBase64 = async (imageName) => {
  try {
    const imagePath = path.join(__dirname, '../assets', imageName);
    const imageBuffer = await fs.readFile(imagePath);
    const ext = path.extname(imageName).slice(1);
    return `data:image/${ext};base64,${imageBuffer.toString('base64')}`;
  } catch (error) {
    console.log(`Imagen ${imageName} no encontrada`);
    return null;
  }
};

// =============================================
// GENERAR PDF
// =============================================
const generatePDF = async (req, res) => {
  let browser = null;

  try {
    const { id } = req.params;

    // 1. OBTENER DATOS (ajustar a tu BD)
    const data = await TuModelo.findById(id);
    if (!data) {
      return res.status(404).send('No encontrado');
    }

    // 2. CARGAR IMAGENES
    const logoBase64 = await getImageBase64('logo.png');
    const fondoBase64 = await getImageBase64('fondo.png');

    // 3. GENERAR HTML
    const html = generarHTML({ data, logoBase64, fondoBase64 });

    // 4. PUPPETEER → PDF
    browser = await puppeteer.launch({
      headless: 'new',
      args: ['--no-sandbox', '--disable-setuid-sandbox']
    });

    const page = await browser.newPage();
    await page.setContent(html, { waitUntil: 'load', timeout: 30000 });

    const pdfBuffer = await page.pdf({
      format: 'Letter',
      margin: { top: '0.5in', right: '0.5in', bottom: '0.5in', left: '0.5in' },
      printBackground: true
    });

    await browser.close();
    browser = null;

    // 5. ENVIAR PDF
    const fileName = `documento_${id}_${Date.now()}.pdf`;

    res.setHeader('Content-Type', 'application/pdf');
    res.setHeader('Content-Disposition', `attachment; filename="${fileName}"`);
    res.setHeader('Content-Length', pdfBuffer.length);
    res.setHeader('Cache-Control', 'no-cache');

    res.send(Buffer.from(pdfBuffer));

  } catch (error) {
    console.error('Error PDF:', error);
    res.status(500).send('Error generando PDF');
  } finally {
    if (browser) await browser.close();
  }
};

// =============================================
// GENERAR HTML
// =============================================
const generarHTML = ({ data, logoBase64, fondoBase64 }) => {
  return `
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="utf-8">
      <style>
        @page {
          size: Letter;
          margin: 0;
          ${fondoBase64 ? `
            background-image: url('${fondoBase64}');
            background-size: 100% 100%;
          ` : ''}
        }

        body {
          font-family: Arial, sans-serif;
          padding: 0.5in;
          font-size: 12px;
        }

        .logo {
          position: fixed;
          top: 10px;
          right: 10px;
        }

        .logo img { width: 80px; }

        .header {
          background: #333;
          color: white;
          padding: 15px;
          text-align: center;
          font-size: 18px;
          font-weight: bold;
        }

        table {
          width: 100%;
          border-collapse: collapse;
          margin-top: 20px;
        }

        th, td {
          border: 1px solid #ccc;
          padding: 8px;
          text-align: left;
        }

        th { background: #333; color: white; }

        .total { background: #333; color: white; font-weight: bold; }
        .text-right { text-align: right; }

        .footer {
          margin-top: 30px;
          text-align: center;
          font-size: 10px;
          color: #666;
        }
      </style>
    </head>
    <body>
      ${logoBase64 ? `<div class="logo"><img src="${logoBase64}" /></div>` : ''}

      <div class="header">TITULO DEL DOCUMENTO</div>

      <table>
        <thead>
          <tr>
            <th>Descripcion</th>
            <th>Cantidad</th>
            <th>Valor</th>
          </tr>
        </thead>
        <tbody>
          ${data.items?.map(item => `
            <tr>
              <td>${item.descripcion}</td>
              <td class="text-right">${item.cantidad}</td>
              <td class="text-right">$${item.valor?.toLocaleString()}</td>
            </tr>
          `).join('') || ''}

          <tr class="total">
            <td colspan="2" class="text-right">TOTAL</td>
            <td class="text-right">$${data.total?.toLocaleString()}</td>
          </tr>
        </tbody>
      </table>

      <div class="footer">
        Generado: ${new Date().toLocaleDateString()}
      </div>
    </body>
    </html>
  `;
};

module.exports = { generatePDF };
```

---

## Frontend

### Componente de Descarga

```jsx
import { useState } from 'react';

const PDFDownloadButton = ({ documentId, fileName }) => {
  const [loading, setLoading] = useState(false);

  const handleDownload = async () => {
    setLoading(true);

    try {
      // IMPORTANTE: Usar fetch(), NO Axios
      // Axios puede tener interceptores que corrompen binarios
      const token = localStorage.getItem('token');
      const baseURL = import.meta.env.VITE_API_URL || 'http://localhost:3000';

      const response = await fetch(`${baseURL}/api/pdf/documento/${documentId}`, {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Accept': 'application/pdf'
        }
      });

      if (!response.ok) {
        throw new Error(await response.text());
      }

      const blob = await response.blob();

      // Validar que sea PDF
      const buffer = await blob.arrayBuffer();
      const header = new TextDecoder().decode(new Uint8Array(buffer).slice(0, 5));
      if (header !== '%PDF-') {
        throw new Error('Respuesta no es PDF valido');
      }

      // Descargar
      const url = window.URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.download = `${fileName || 'documento'}.pdf`;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      setTimeout(() => window.URL.revokeObjectURL(url), 1000);

    } catch (error) {
      alert('Error: ' + error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <button onClick={handleDownload} disabled={loading}>
      {loading ? 'Generando...' : 'Descargar PDF'}
    </button>
  );
};

export default PDFDownloadButton;
```

---

## Imagenes en Base64

### Por que Base64?

Puppeteer tiene problemas cargando:
- URLs externas (CORS, timeouts)
- Rutas de archivo locales

**Solucion**: Embeber imagenes como Data URI

### Formato

```
data:image/png;base64,iVBORw0KGgoAAAANSUhEUg...
```

### Tipos soportados

| Extension | MIME |
|-----------|------|
| .png | image/png |
| .jpg | image/jpeg |
| .gif | image/gif |
| .svg | image/svg+xml |

### Uso en HTML

```html
<img src="data:image/png;base64,..." />
```

### Uso en CSS (fondo)

```css
@page {
  background-image: url('data:image/png;base64,...');
}
```

---

## Problemas Comunes

| Problema | Causa | Solucion |
|----------|-------|----------|
| PDF corrupto con JSON | express.json() procesa la respuesta | Excluir rutas PDF del middleware |
| Axios corrompe PDF | Interceptores modifican response | Usar fetch() nativo |
| Imagenes no aparecen | Puppeteer no carga URLs | Convertir a Base64 |
| Error auth devuelve JSON | Middleware normal | Usar authenticateForBinary |
| Sin fondos CSS | printBackground deshabilitado | `page.pdf({ printBackground: true })` |

---

## Puppeteer en Produccion

### Docker

```dockerfile
RUN apt-get update && apt-get install -y \
    chromium \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdbus-1-3 \
    libdrm2 \
    libgbm1 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    --no-install-recommends

ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true
ENV PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium
```

### Args produccion

```javascript
puppeteer.launch({
  headless: 'new',
  args: [
    '--no-sandbox',
    '--disable-setuid-sandbox',
    '--disable-dev-shm-usage',
    '--disable-gpu',
    '--no-first-run',
    '--no-zygote'
  ]
});
```

---

## Checklist

- [ ] Instalar puppeteer
- [ ] Crear carpeta assets/ con imagenes
- [ ] Configurar exclusion de middleware para PDFs
- [ ] Crear authenticateForBinary
- [ ] Crear controlador con funciones Base64
- [ ] Crear rutas con middleware especial
- [ ] Implementar componente frontend con fetch()
- [ ] Probar generacion y descarga
