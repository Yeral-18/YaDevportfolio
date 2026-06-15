"""Genera hoja-membretada.html + tarjeta-presentacion.html para COICEM S.A.S.

- Estilo BRUTALIST industrial: bordes duros, labels mono, titulares uppercase,
  grafito/negro + naranja hi-vis. NADA de gradientes suaves ni esquinas redondeadas.
- A4 print-ready autocontenido con logo b64 embebido.
- Tarjeta 90x55mm (estandar Colombia), frente + reverso en una pagina.
- Tipografia: Archivo (display expandida), IBM Plex Sans (cuerpo), IBM Plex Mono (specs).
- Contacto PENDIENTE: placeholders editables [ ... ] que el cliente rellena.
"""
import os, shutil

here = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(here, 'logo-firma-b64.txt')) as f:
    # Este archivo YA trae el prefijo data:image/png;base64,...
    LOGO_B64 = f.read().strip()

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com" />'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />'
         '<link href="https://fonts.googleapis.com/css2?'
         'family=Archivo:wght@600;700;800;900&'
         'family=IBM+Plex+Sans:wght@400;500;600;700&'
         'family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet" />')


# ============================================================
# HOJA MEMBRETADA — A4 vertical, brutalist industrial
# ============================================================
hoja = '''<!DOCTYPE html>
<html lang="es-CO">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Hoja Membretada - COICEM S.A.S</title>
  ''' + FONTS + '''
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --blue:   #025199;
      --blue-l: #3B8FD9;
      --orange: #F79204;
      --metal:  #313F50;
      --ink:    #0B0E14;
      --muted:  #6B7785;
      --hair:   #D5DBE2;
      --mono: "IBM Plex Mono", "Courier New", monospace;
      --sans: "IBM Plex Sans", Arial, sans-serif;
      --disp: "Archivo", "Arial Narrow", sans-serif;
    }

    body {
      background: #c4c8cd;
      display: flex; justify-content: center; align-items: flex-start;
      min-height: 100vh; padding: 20px;
      font-family: var(--sans); color: var(--ink);
    }

    .page {
      width: 210mm; min-height: 297mm; background: #fff;
      position: relative; overflow: hidden;
      box-shadow: 0 6px 40px rgba(0,0,0,0.28);
      display: flex; flex-direction: column;
    }

    /* ===== left spine — barra vertical naranja brutalist ===== */
    .spine { position: absolute; top: 0; left: 0; width: 6mm; height: 100%;
             background: var(--orange); z-index: 3; }
    .spine::after { content: ""; position: absolute; top: 0; left: 6mm;
             width: 1.4mm; height: 100%; background: var(--ink); }

    /* ===== HEADER ===== */
    .header {
      padding: 16mm 18mm 8mm 22mm;
      display: flex; justify-content: space-between; align-items: flex-start;
      gap: 14mm; flex-shrink: 0;
    }
    .header-logo img { width: 56mm; height: auto; display: block;
      image-rendering: -webkit-optimize-contrast; }

    .header-meta { text-align: right; border-left: 2.5pt solid var(--orange);
      padding-left: 6mm; }
    .header-meta .razon {
      font-family: var(--disp); font-size: 13pt; font-weight: 800;
      color: var(--blue); letter-spacing: 0.5px; line-height: 1.05;
      text-transform: uppercase;
    }
    .header-meta .tagline {
      font-family: var(--mono); font-size: 7pt; font-weight: 500;
      color: var(--metal); letter-spacing: 2px; text-transform: uppercase;
      margin-top: 4pt;
    }
    .header-meta .nit {
      font-family: var(--mono); font-size: 7.5pt; color: var(--muted);
      margin-top: 7pt;
    }

    /* ===== heavy rule — bloques duros 80/20 ===== */
    .rule-strong { display: flex; height: 4pt; margin: 0 18mm 0 22mm; flex-shrink: 0; }
    .rule-strong .a { background: var(--ink);    flex: 62; }
    .rule-strong .b { background: var(--metal);  flex: 22; }
    .rule-strong .c { background: var(--orange); flex: 16; }

    /* ===== BODY ===== */
    .body { flex: 1; padding: 12mm 18mm 12mm 22mm; position: relative;
      display: flex; flex-direction: column; }

    .watermark { position: absolute; top: 50%; left: 50%;
      transform: translate(-50%, -50%); width: 105mm; height: 105mm;
      opacity: 0.05; pointer-events: none; z-index: 0; }
    .watermark img { width: 100%; height: 100%; object-fit: contain; }

    .content-area { position: relative; z-index: 1; flex: 1;
      font-size: 11pt; line-height: 1.7; color: var(--ink); }
    .content-area p { margin-bottom: 10pt; }

    /* etiqueta mono de seccion (ejemplo brutalist) */
    .doc-ref { font-family: var(--mono); font-size: 7.5pt; color: var(--muted);
      letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 14pt;
      border: 1pt solid var(--hair); display: inline-block; padding: 3pt 8pt; }

    /* ===== FOOTER — banda grafito, labels mono ===== */
    .footer { background: var(--ink); color: #C7D0DA; flex-shrink: 0;
      padding: 8mm 18mm 9mm 22mm; position: relative; }
    .footer::before { content: ""; position: absolute; top: 0; left: 0;
      width: 100%; height: 3pt;
      background: linear-gradient(90deg, var(--orange) 0 16%, var(--metal) 16% 100%); }

    .footer-grid { display: grid; grid-template-columns: 1.2fr 1fr 1fr 1.1fr;
      gap: 8mm; }
    .footer-col strong { display: block; font-family: var(--mono);
      color: var(--orange); font-size: 7pt; letter-spacing: 1.8px;
      text-transform: uppercase; margin-bottom: 5pt; }
    .footer-col .val { font-family: var(--sans); font-size: 8pt;
      color: #E2E8EF; line-height: 1.6; }
    .footer-col .row { display: flex; gap: 5pt; align-items: baseline;
      margin-bottom: 1.5pt; }
    .footer-col .lbl { font-family: var(--mono); color: var(--blue-l);
      font-size: 7pt; width: 11pt; flex-shrink: 0; }
    .footer-col .todo { color: #FBBF55; background: rgba(247,146,4,0.12);
      border: 0.7pt solid rgba(247,146,4,0.4); padding: 0 4pt;
      font-size: 7.5pt; }

    .certs { margin-top: 7mm; padding-top: 5mm; border-top: 1pt solid #1E2733;
      display: flex; flex-wrap: wrap; gap: 6pt; align-items: center; }
    .certs .clbl { font-family: var(--mono); font-size: 6.5pt; color: var(--muted);
      letter-spacing: 1.5px; text-transform: uppercase; margin-right: 4pt; }
    .certs .chip { font-family: var(--mono); font-size: 7pt; color: #C7D0DA;
      border: 0.8pt solid #2A3645; padding: 2.5pt 7pt; letter-spacing: 0.4px; }
    .certs .bv { color: var(--orange); border-color: rgba(247,146,4,0.5); }

    @media print {
      body { background: #fff; padding: 0; margin: 0; }
      .page { box-shadow: none; width: 210mm; min-height: 297mm; margin: 0; }
      @page { size: A4; margin: 0; }
    }
  </style>
</head>
<body>
  <div class="page">
    <div class="spine"></div>

    <header class="header">
      <div class="header-logo">
        <img src="''' + LOGO_B64 + '''" alt="COICEM S.A.S" />
      </div>
      <div class="header-meta">
        <div class="razon">COICEM<br/>S.A.S</div>
        <div class="tagline">Servicio Mantenimiento Especializado</div>
        <div class="nit">NIT <span style="color:#B45309;">[Pendiente]</span></div>
      </div>
    </header>

    <div class="rule-strong"><div class="a"></div><div class="b"></div><div class="c"></div></div>

    <div class="body">
      <div class="watermark"><img src="''' + LOGO_B64 + '''" alt="" /></div>
      <div class="content-area">
        <div class="doc-ref">Doc. [Ref] &nbsp;//&nbsp; [Ciudad], [Fecha]</div>
        <p>&nbsp;</p>
      </div>
    </div>

    <footer class="footer">
      <div class="footer-grid">
        <div class="footer-col">
          <strong>Ubicacion</strong>
          <div class="val"><span class="todo">[Direccion]</span></div>
          <div class="val">Colombia</div>
        </div>
        <div class="footer-col">
          <strong>Contacto</strong>
          <div class="row"><span class="lbl">T.</span><span class="val todo">[+57 ...]</span></div>
          <div class="row"><span class="lbl">M.</span><span class="val todo">[+57 ...]</span></div>
        </div>
        <div class="footer-col">
          <strong>Digital</strong>
          <div class="row"><span class="lbl">E.</span><span class="val todo">[correo@coicem.com]</span></div>
          <div class="row"><span class="lbl">W.</span><span class="val">coicem.com</span></div>
        </div>
        <div class="footer-col">
          <strong>Areas operativas</strong>
          <div class="val" style="font-size:7.5pt;line-height:1.55;">
            Operacion &middot; Mantenimiento<br/>
            Construccion &middot; Energia<br/>
            Infraestructura
          </div>
        </div>
      </div>
      <div class="certs">
        <span class="clbl">Certificados</span>
        <span class="chip">ISO 9001:2015</span>
        <span class="chip">ISO 14001:2015</span>
        <span class="chip">ISO 45001:2018</span>
        <span class="chip bv">NORSOK 006:2020</span>
        <span class="chip bv">Bureau Veritas</span>
      </div>
    </footer>
  </div>
</body>
</html>'''

with open(os.path.join(here, 'hoja-membretada.html'), 'w', encoding='utf-8') as f:
    f.write(hoja)


# ============================================================
# TARJETA DE PRESENTACION — 90x55mm, 2 caras, brutalist
# ============================================================
tarjeta = '''<!DOCTYPE html>
<html lang="es-CO">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Tarjeta de Presentacion - COICEM S.A.S</title>
  ''' + FONTS + '''
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --blue:   #025199;
      --blue-l: #3B8FD9;
      --orange: #F79204;
      --metal:  #313F50;
      --ink:    #0B0E14;
      --muted:  #6B7785;
      --mono: "IBM Plex Mono", "Courier New", monospace;
      --sans: "IBM Plex Sans", Arial, sans-serif;
      --disp: "Archivo", "Arial Narrow", sans-serif;
    }

    body { background: #c4c8cd; display: flex; flex-direction: column;
      align-items: center; min-height: 100vh; padding: 24px; gap: 10px;
      font-family: var(--sans); color: var(--ink); }

    .label { font-family: var(--mono); font-size: 10px; letter-spacing: 2px;
      text-transform: uppercase; color: #5b636c; font-weight: 500; margin-top: 8px; }

    .card { width: 90mm; height: 55mm; background: #fff;
      box-shadow: 0 4px 22px rgba(0,0,0,0.22); position: relative;
      overflow: hidden; page-break-inside: avoid; }

    /* ============ FRONT — base oscura brutalist ============ */
    .card.front { background: var(--ink); display: flex; align-items: center;
      justify-content: center; padding: 8mm 10mm; }
    /* esquina superior izq: bloque grafito duro */
    .front::before { content: ""; position: absolute; top: 0; left: 0;
      width: 26mm; height: 8mm; background: var(--metal); z-index: 1; }
    /* franja inferior naranja hi-vis */
    .front::after { content: ""; position: absolute; bottom: 0; left: 0;
      width: 100%; height: 5mm; z-index: 1;
      background: linear-gradient(90deg, var(--orange) 0 20mm, var(--ink) 20mm 100%); }
    .front .logo-wrap { position: relative; z-index: 2; text-align: center; width: 100%; }
    .front .logo-wrap img { width: 54mm; height: auto; display: block; margin: 0 auto;
      image-rendering: -webkit-optimize-contrast; }
    .front .razon { font-family: var(--mono); font-size: 6.5pt; font-weight: 500;
      letter-spacing: 3px; text-transform: uppercase;
      color: rgba(199,208,218,0.78); margin-top: 4mm; }

    /* ============ BACK — blanco brutalist ============ */
    .card.back { background: #fff; padding: 6mm 7mm 7mm 7mm; display: flex;
      flex-direction: column; justify-content: space-between;
      border-left: 2.5mm solid var(--orange); }
    .back .mini-logo { position: absolute; top: 5mm; right: 6mm; width: 22mm;
      height: auto; opacity: 0.95; image-rendering: -webkit-optimize-contrast; }

    .back .person { max-width: 56mm; }
    .back .nombre { font-family: var(--disp); font-size: 12pt; font-weight: 800;
      color: var(--ink); letter-spacing: 0.2px; line-height: 1.05;
      text-transform: uppercase; }
    .back .cargo { font-family: var(--mono); font-size: 6.5pt; font-weight: 500;
      color: var(--blue); letter-spacing: 1.6px; text-transform: uppercase;
      margin-top: 1.5mm; }

    .back .bar { display: flex; height: 1.6pt; width: 30mm; margin: 2.5mm 0; }
    .back .bar .a { background: var(--ink);    flex: 60; }
    .back .bar .b { background: var(--metal);  flex: 22; }
    .back .bar .c { background: var(--orange); flex: 18; }

    .back .contact { display: flex; flex-direction: column; gap: 0.7mm;
      font-family: var(--mono); font-size: 7pt; color: var(--ink); line-height: 1.4; }
    .back .contact .row { display: flex; gap: 2mm; align-items: baseline; }
    .back .contact .lbl { color: var(--orange); font-weight: 600; font-size: 6.6pt;
      width: 4mm; flex-shrink: 0; }
    .back .contact .todo { color: #B45309; background: rgba(247,146,4,0.10);
      border: 0.6pt solid rgba(247,146,4,0.45); padding: 0 1.5mm; font-size: 6.6pt; }

    .back .areas { font-family: var(--mono); font-size: 5.2pt; font-weight: 500;
      color: var(--muted); letter-spacing: 0.6px; text-transform: uppercase;
      margin-top: 2mm; line-height: 1.6; }
    .back .areas .dot { color: var(--orange); font-weight: 700; margin: 0 1mm; }

    .back .certs { font-family: var(--mono); font-size: 5pt; color: #9aa3ad;
      letter-spacing: 0.8px; margin-top: 1.2mm; }

    /* franja inferior dura azul/naranja */
    .back::after { content: ""; position: absolute; bottom: 0; left: 0; width: 100%;
      height: 1.8mm; background: linear-gradient(90deg,
        var(--ink) 0 60%, var(--metal) 60% 80%, var(--orange) 80% 100%); }

    @media print {
      body { background: #fff; padding: 0; margin: 0; gap: 6mm; }
      .label { display: none; }
      .card { box-shadow: none; margin: 4mm 0; }
      @page { size: 110mm 140mm; margin: 8mm; }
    }
  </style>
</head>
<body>

  <div class="label">Cara frontal &mdash; 90 x 55 mm</div>
  <div class="card front">
    <div class="logo-wrap">
      <img src="''' + LOGO_B64 + '''" alt="COICEM S.A.S" />
      <div class="razon">Servicio Mantenimiento Especializado</div>
    </div>
  </div>

  <div class="label">Cara reverso &mdash; 90 x 55 mm</div>
  <div class="card back">
    <img class="mini-logo" src="''' + LOGO_B64 + '''" alt="" />

    <div class="person">
      <div class="nombre">[Nombre Apellido]</div>
      <div class="cargo">[Cargo]</div>
      <div class="bar"><div class="a"></div><div class="b"></div><div class="c"></div></div>
    </div>

    <div class="contact">
      <div class="row"><span class="lbl">M.</span><span class="todo">[+57 ___ ___ ____]</span></div>
      <div class="row"><span class="lbl">E.</span><span class="todo">[nombre@coicem.com]</span></div>
      <div class="row"><span class="lbl">W.</span><span>coicem.com</span></div>
    </div>

    <div>
      <div class="areas">
        Operacion<span class="dot">&middot;</span>Mantenimiento<span class="dot">&middot;</span>Construccion<br/>Energia<span class="dot">&middot;</span>Infraestructura
      </div>
      <div class="certs">ISO 9001 &middot; 14001 &middot; 45001 &middot; NORSOK 006:2020 &middot; Bureau Veritas</div>
    </div>
  </div>

</body>
</html>'''

with open(os.path.join(here, 'tarjeta-presentacion.html'), 'w', encoding='utf-8') as f:
    f.write(tarjeta)


# ============================================================
# Copia a public/internal/ + reporte
# ============================================================
dst = os.path.join(here, '..', 'coicem-web', 'public', 'internal')
os.makedirs(dst, exist_ok=True)
for name in ('hoja-membretada.html', 'tarjeta-presentacion.html'):
    shutil.copy(os.path.join(here, name), os.path.join(dst, name))
    print(name + ':', os.path.getsize(os.path.join(here, name)) // 1024, 'KB')
print('copiados a public/internal/')
