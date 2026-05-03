"""Genera hoja-membretada.html + tarjeta-presentacion.html para Luqra.

- A4 print-ready autocontenido con logo b64 embebido.
- Tarjeta 90x55mm estandar Colombia, ambos lados en una pagina.
- Paleta 80/20 azul/naranja segun tokens.md.
- Datos NO inventados: TODOs visibles para que el cliente los confirme.
"""
import os

with open('logo_b64.txt') as f:
    LOGO_B64 = f.read().strip()


# ============================================================
# HOJA MEMBRETADA — A4 vertical, print-ready
# ============================================================
hoja = '''<!DOCTYPE html>
<html lang="es-CO">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Hoja Membretada - Luqra Ingenieria y Soluciones S.A.S</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet" />
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --blue-base: #0A2A66;
      --blue-mid:  #123C8C;
      --blue-light:#1F5FBF;
      --orange-base: #FF6A00;
      --orange-mid:  #FF8C1A;
      --ink:    #1A1A1A;
      --muted:  #6B7280;
      --hair:   #E5E7EB;
    }

    body {
      background: #d0d0d0;
      display: flex;
      justify-content: center;
      align-items: flex-start;
      min-height: 100vh;
      padding: 20px;
      font-family: "Inter", "Plus Jakarta Sans", Arial, sans-serif;
      color: var(--ink);
    }

    .page {
      width: 210mm;
      min-height: 297mm;
      background: #ffffff;
      position: relative;
      overflow: hidden;
      box-shadow: 0 6px 40px rgba(0,0,0,0.22);
      display: flex;
      flex-direction: column;
    }

    /* ===== HEADER — institucional, sobrio ===== */
    .header {
      width: 100%;
      padding: 18mm 20mm 10mm 20mm;
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 18mm;
      flex-shrink: 0;
      position: relative;
    }

    .header-logo img {
      width: 50mm;
      height: auto;
      display: block;
      image-rendering: -webkit-optimize-contrast;
    }

    .header-meta {
      text-align: right;
      font-family: "Plus Jakarta Sans", Arial, sans-serif;
      padding-top: 2mm;
    }
    .header-meta .razon {
      font-size: 10pt;
      font-weight: 700;
      color: var(--blue-base);
      letter-spacing: 0.3px;
      line-height: 1.3;
    }
    .header-meta .tagline {
      font-size: 7.5pt;
      font-weight: 500;
      color: var(--blue-light);
      letter-spacing: 1.2px;
      text-transform: uppercase;
      margin-top: 3pt;
    }
    .header-meta .nit {
      font-size: 8pt;
      color: var(--muted);
      margin-top: 5pt;
      font-family: "Inter", monospace;
    }

    /* Accent bar — regla 80/20 */
    .accent-bar {
      width: calc(100% - 40mm);
      margin: 0 20mm;
      height: 3pt;
      display: flex;
      flex-shrink: 0;
    }
    .accent-bar .blue  { background: var(--blue-base);  flex: 80; }
    .accent-bar .orange{ background: var(--orange-base); flex: 20; }

    /* ===== BODY ===== */
    .body {
      flex: 1;
      padding: 12mm 20mm 12mm 20mm;
      position: relative;
      display: flex;
      flex-direction: column;
    }

    .watermark {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      width: 110mm;
      height: 110mm;
      opacity: 0.045;
      pointer-events: none;
      z-index: 0;
    }
    .watermark img {
      width: 100%;
      height: 100%;
      object-fit: contain;
    }

    .content-area {
      position: relative;
      z-index: 1;
      flex: 1;
      font-size: 11pt;
      line-height: 1.65;
      color: var(--ink);
    }
    .content-area p { margin-bottom: 10pt; }

    /* ===== FOOTER ===== */
    .footer-bar {
      width: calc(100% - 40mm);
      margin: 0 20mm;
      height: 2pt;
      display: flex;
      flex-shrink: 0;
    }
    .footer-bar .orange { background: var(--orange-base); flex: 20; }
    .footer-bar .blue   { background: var(--blue-base);   flex: 80; }

    .footer {
      width: 100%;
      padding: 6mm 20mm 14mm 20mm;
      flex-shrink: 0;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      gap: 12mm;
      font-family: "Inter", Arial, sans-serif;
      font-size: 8pt;
      color: var(--muted);
      line-height: 1.55;
    }
    .footer-col {
      display: flex;
      flex-direction: column;
      gap: 1.5pt;
    }
    .footer-col strong {
      color: var(--blue-base);
      font-weight: 700;
      font-size: 7.5pt;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      margin-bottom: 2pt;
    }
    .footer-col .row {
      display: flex;
      gap: 5pt;
      align-items: center;
    }
    .footer-col .lbl {
      color: var(--orange-base);
      font-weight: 700;
      font-size: 7.5pt;
      width: 12pt;
      flex-shrink: 0;
    }
    .footer-col .val { color: var(--ink); font-size: 8pt; }
    .footer-col .todo {
      color: #B45309;
      background: #FEF3C7;
      padding: 0 4pt;
      border-radius: 2pt;
      font-size: 7.5pt;
      font-weight: 600;
    }

    /* ===== PRINT ===== */
    @media print {
      body { background: white; padding: 0; margin: 0; }
      .page { box-shadow: none; width: 210mm; min-height: 297mm; margin: 0; }
      @page { size: A4; margin: 0; }
    }
  </style>
</head>
<body>
  <div class="page">

    <!-- HEADER -->
    <header class="header">
      <div class="header-logo">
        <img src="''' + LOGO_B64 + '''" alt="Luqra Ingenieria y Soluciones S.A.S" />
      </div>
      <div class="header-meta">
        <div class="razon">Luqra Ingenieria<br/>y Soluciones S.A.S.</div>
        <div class="tagline">Ingenieria integral</div>
        <div class="nit">NIT <span style="color:#B45309;background:#FEF3C7;padding:0 4pt;border-radius:2pt;font-weight:600;">[TODO: confirmar]</span></div>
      </div>
    </header>

    <!-- Accent bar 80/20 -->
    <div class="accent-bar">
      <div class="blue"></div>
      <div class="orange"></div>
    </div>

    <!-- BODY -->
    <div class="body">
      <div class="watermark">
        <img src="''' + LOGO_B64 + '''" alt="" />
      </div>
      <div class="content-area">
        <!-- El contenido del documento se inserta aqui -->
        <p>&nbsp;</p>
      </div>
    </div>

    <!-- Footer accent bar -->
    <div class="footer-bar">
      <div class="orange"></div>
      <div class="blue"></div>
    </div>

    <!-- FOOTER -->
    <footer class="footer">
      <div class="footer-col">
        <strong>Direccion</strong>
        <div class="val"><span class="todo">[TODO: confirmar direccion]</span></div>
        <div class="val">Colombia</div>
      </div>
      <div class="footer-col">
        <strong>Contacto</strong>
        <div class="row"><span class="lbl">T.</span><span class="val todo">[TODO: telefono]</span></div>
        <div class="row"><span class="lbl">M.</span><span class="val todo">[TODO: celular / WhatsApp]</span></div>
      </div>
      <div class="footer-col">
        <strong>Digital</strong>
        <div class="row"><span class="lbl">E.</span><span class="val todo">[TODO: contacto@luqra.com.co]</span></div>
        <div class="row"><span class="lbl">W.</span><span class="val">www.luqra.com.co</span></div>
      </div>
      <div class="footer-col" style="text-align:right;align-items:flex-end;">
        <strong>Lineas operativas</strong>
        <div class="val" style="font-size:7.5pt;line-height:1.6;">
          Transporte &middot; Construccion<br/>
          Energia &middot; Ambiental &middot; Comercio
        </div>
      </div>
    </footer>

  </div>
</body>
</html>'''

with open('hoja-membretada.html', 'w', encoding='utf-8') as f:
    f.write(hoja)


# ============================================================
# TARJETA DE PRESENTACION — 90x55mm Colombia, 2 caras stacked
# ============================================================
tarjeta = '''<!DOCTYPE html>
<html lang="es-CO">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Tarjeta de Presentacion - Luqra Ingenieria y Soluciones S.A.S</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet" />
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --blue-base: #0A2A66;
      --blue-mid:  #123C8C;
      --blue-light:#1F5FBF;
      --orange-base: #FF6A00;
      --orange-mid:  #FF8C1A;
      --ink:    #1A1A1A;
      --muted:  #6B7280;
    }

    body {
      background: #d0d0d0;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: flex-start;
      min-height: 100vh;
      padding: 20px;
      gap: 12px;
      font-family: "Plus Jakarta Sans", "Inter", Arial, sans-serif;
      color: var(--ink);
    }

    .label {
      font-family: "Inter", Arial, sans-serif;
      font-size: 11px;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: #555;
      font-weight: 600;
      margin-top: 8px;
    }

    .card {
      width: 90mm;
      height: 55mm;
      background: #fff;
      box-shadow: 0 4px 22px rgba(0,0,0,0.18);
      position: relative;
      overflow: hidden;
      page-break-inside: avoid;
    }

    /* ============ FRONT ============ */
    .card.front {
      background: var(--blue-base);
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 7mm 10mm;
      position: relative;
    }

    .front .logo-wrap {
      position: relative;
      z-index: 2;
      text-align: center;
      width: 100%;
    }
    .front .logo-wrap img {
      width: 52mm;
      height: auto;
      display: block;
      margin: 0 auto;
      filter: brightness(0) invert(1); /* logo en blanco sobre azul */
      image-rendering: -webkit-optimize-contrast;
    }
    .front .razon {
      font-family: "Plus Jakarta Sans", sans-serif;
      font-size: 7pt;
      font-weight: 600;
      letter-spacing: 3px;
      text-transform: uppercase;
      color: rgba(255,255,255,0.78);
      margin-top: 3mm;
    }

    /* Accent triangle naranja — esquina inferior derecha */
    .front::after {
      content: "";
      position: absolute;
      bottom: 0;
      right: 0;
      width: 14mm;
      height: 14mm;
      background: var(--orange-base);
      clip-path: polygon(100% 0, 100% 100%, 0 100%);
      z-index: 1;
    }
    /* Detalle azul-claro sutil para profundidad */
    .front::before {
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      width: 22mm;
      height: 22mm;
      background: var(--blue-mid);
      clip-path: polygon(0 0, 100% 0, 0 100%);
      opacity: 0.55;
      z-index: 1;
    }

    /* ============ BACK ============ */
    .card.back {
      background: #fff;
      padding: 6mm 7mm 6mm 7mm;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      position: relative;
    }

    /* Mini logo top-left */
    .back .mini-logo {
      position: absolute;
      top: 5mm;
      right: 6mm;
      width: 18mm;
      height: auto;
      opacity: 0.92;
      image-rendering: -webkit-optimize-contrast;
    }

    .back .person {
      max-width: 60mm;
    }
    .back .nombre {
      font-family: "Plus Jakarta Sans", sans-serif;
      font-size: 11pt;
      font-weight: 800;
      color: var(--blue-base);
      letter-spacing: -0.2px;
      line-height: 1.15;
    }
    .back .cargo {
      font-family: "Inter", sans-serif;
      font-size: 7pt;
      font-weight: 600;
      color: var(--blue-light);
      letter-spacing: 1.6px;
      text-transform: uppercase;
      margin-top: 1mm;
    }

    /* Accent bar 80/20 separador */
    .back .bar {
      display: flex;
      height: 1.2pt;
      width: 28mm;
      margin: 2mm 0 2.5mm 0;
    }
    .back .bar .blue   { background: var(--blue-base);   flex: 80; }
    .back .bar .orange { background: var(--orange-base); flex: 20; }

    .back .contact {
      display: flex;
      flex-direction: column;
      gap: 0.6mm;
      font-family: "Inter", sans-serif;
      font-size: 7.2pt;
      color: var(--ink);
      line-height: 1.4;
    }
    .back .contact .row {
      display: flex;
      gap: 2mm;
      align-items: center;
    }
    .back .contact .lbl {
      color: var(--orange-base);
      font-weight: 700;
      font-size: 6.8pt;
      width: 4mm;
      flex-shrink: 0;
      letter-spacing: 0.5px;
    }
    .back .contact .todo {
      color: #B45309;
      background: #FEF3C7;
      padding: 0 1.5mm;
      border-radius: 1pt;
      font-size: 6.8pt;
      font-weight: 600;
    }

    .back .areas {
      font-family: "Inter", sans-serif;
      font-size: 6pt;
      font-weight: 500;
      color: var(--muted);
      letter-spacing: 1.2px;
      text-transform: uppercase;
      margin-top: 1.5mm;
      line-height: 1.4;
    }
    .back .areas .dot {
      color: var(--orange-base);
      font-weight: 700;
      margin: 0 1.5mm;
    }

    /* Footer accent strip naranja */
    .back::after {
      content: "";
      position: absolute;
      bottom: 0;
      left: 0;
      width: 100%;
      height: 1.6mm;
      background: linear-gradient(90deg,
        var(--blue-base)   0%,
        var(--blue-base)  78%,
        var(--orange-base) 78%,
        var(--orange-base) 100%);
    }

    /* ===== PRINT ===== */
    @media print {
      body {
        background: #fff;
        padding: 0;
        margin: 0;
        gap: 6mm;
        align-items: center;
        justify-content: flex-start;
      }
      .label { display: none; }
      .card {
        box-shadow: none;
        margin: 4mm 0;
      }
      @page {
        size: 110mm 140mm; /* hoja con sangrado para imprenta */
        margin: 8mm;
      }
    }
  </style>
</head>
<body>

  <div class="label">Cara frontal &mdash; 90 x 55 mm</div>
  <div class="card front">
    <div class="logo-wrap">
      <img src="''' + LOGO_B64 + '''" alt="Luqra Ingenieria y Soluciones S.A.S" />
      <div class="razon">Ingenieria &amp; Soluciones S.A.S.</div>
    </div>
  </div>

  <div class="label">Cara reverso &mdash; 90 x 55 mm</div>
  <div class="card back">
    <img class="mini-logo" src="''' + LOGO_B64 + '''" alt="" />

    <div class="person">
      <div class="nombre">[TODO: Nombre Apellido]</div>
      <div class="cargo">[TODO: Cargo]</div>
      <div class="bar">
        <div class="blue"></div>
        <div class="orange"></div>
      </div>
    </div>

    <div class="contact">
      <div class="row"><span class="lbl">M.</span><span class="todo">[TODO: +57 ___ ___ ____]</span></div>
      <div class="row"><span class="lbl">E.</span><span class="todo">[TODO: nombre@luqra.com.co]</span></div>
      <div class="row"><span class="lbl">W.</span><span>www.luqra.com.co</span></div>
    </div>

    <div class="areas">
      Transporte<span class="dot">&middot;</span>Construccion<span class="dot">&middot;</span>Energia<span class="dot">&middot;</span>Ambiental<span class="dot">&middot;</span>Comercio internacional
    </div>
  </div>

</body>
</html>'''

with open('tarjeta-presentacion.html', 'w', encoding='utf-8') as f:
    f.write(tarjeta)


# ============================================================
# Reporte tamanos
# ============================================================
print('hoja-membretada.html:     ', os.path.getsize('hoja-membretada.html') // 1024, 'KB')
print('tarjeta-presentacion.html:', os.path.getsize('tarjeta-presentacion.html') // 1024, 'KB')
