#!/usr/bin/env python3
"""
generate-brandbook-coicem.py — COICEM S.A.S
Genera un brandbook A4 multipágina (paridad con Luqra), estilo BRUTALIST INDUSTRIAL.

- Estructura adaptada de LUQRA/brand/generate-brandbook-v2.py (misma completitud).
- Lenguaje visual BRUTALIST: bordes duros (radius 0), sin sombras blandas, labels
  mono uppercase, titulares Archivo Expanded uppercase, base grafito/negro,
  naranja hi-vis (#F79204) como único acento, rejilla de columnas técnica.
- Logo lockup: brand/logo-firma-b64.txt (ya trae prefijo data:).
- Isotipo: brand/emblema-isotipo.png → base64 embebido vía PIL.

Run: python generate-brandbook-coicem.py
Output:
  ./brandbook.html
  ../coicem-web/public/internal/brandbook.html
"""

import os, io, base64
from PIL import Image

# ── Base paths ──────────────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
B64_FILE   = os.path.join(SCRIPT_DIR, 'logo-firma-b64.txt')
EMB_FILE   = os.path.join(SCRIPT_DIR, 'emblema-isotipo.png')
OUTPUTS = [
    os.path.join(SCRIPT_DIR, 'brandbook.html'),
    os.path.join(SCRIPT_DIR, '..', 'coicem-web', 'public', 'internal', 'brandbook.html'),
]

# ── Logo lockup (data URI ya incluido) ──────────────────────────────────────
with open(B64_FILE, 'r', encoding='utf-8') as f:
    LOGO_B64 = f.read().strip()
if not LOGO_B64.startswith('data:'):
    LOGO_B64 = 'data:image/png;base64,' + LOGO_B64

# ── Isotipo (emblema) → base64 ───────────────────────────────────────────────
def png_b64(path, size=None):
    img = Image.open(path).convert('RGBA')
    if size:
        w, h = img.size
        img = img.resize((size, int(h * size / w)), Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, 'PNG', optimize=True)
    return 'data:image/png;base64,' + base64.b64encode(buf.getvalue()).decode()

EMB_B64 = png_b64(EMB_FILE, 360)

# ── HTML Template ────────────────────────────────────────────────────────────
HTML = f"""<!DOCTYPE html>
<html lang="es-CO">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>COICEM S.A.S — Manual de Identidad Visual 2026</title>
<style>
/* ═══════════════════════════════════════════════════════════
   COICEM BRANDBOOK — 2026
   Razón social: COICEM S.A.S
   Estilo: BRUTALIST INDUSTRIAL · bordes duros · hi-vis #F79204
   ═══════════════════════════════════════════════════════════ */

@import url('https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700;800;900&family=IBM+Plex+Sans:wght@300;400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap');

@page {{ size: A4; margin: 0; }}
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: 'IBM Plex Sans', Arial, sans-serif; color: #0B0E14; background: #fff; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}

/* ── Page shell ── */
.page {{ width: 210mm; min-height: 297mm; padding: 18mm 20mm; page-break-after: always; position: relative; overflow: hidden; background: #EDEDE8; }}
.page:last-child {{ page-break-after: auto; }}
.page--dark  {{ background: #0B0E14; color: #EDEDE8; }}
.page--black {{ background: #000000; color: #EDEDE8; }}
.page--white {{ background: #FFFFFF; }}

/* ── Typography (Archivo Expanded emulado vía width axis + tracking) ── */
.display {{ font-family: 'Archivo Expanded', 'Archivo', 'Arial Black', sans-serif; font-stretch: expanded; text-transform: uppercase; }}
h1 {{ font-family: 'Archivo Expanded', 'Archivo', 'Arial Black', sans-serif; font-stretch: expanded; font-size: 34pt; font-weight: 900; color: #0B0E14; letter-spacing: 0.01em; margin-bottom: 8pt; line-height: 0.98; text-transform: uppercase; }}
h2 {{ font-family: 'Archivo Expanded', 'Archivo', 'Arial Black', sans-serif; font-stretch: expanded; font-size: 19pt; font-weight: 800; color: #0B0E14; margin: 18pt 0 12pt; padding-bottom: 8pt; border-bottom: 2pt solid #0B0E14; line-height: 1.05; text-transform: uppercase; letter-spacing: 0.01em; }}
h3 {{ font-family: 'IBM Plex Mono', monospace; font-size: 9pt; font-weight: 600; color: #025199; margin: 14pt 0 6pt; text-transform: uppercase; letter-spacing: 0.16em; }}
h4 {{ font-family: 'Archivo', sans-serif; font-size: 10pt; font-weight: 700; color: #0B0E14; margin: 8pt 0 4pt; text-transform: uppercase; letter-spacing: 0.04em; }}
p {{ font-size: 9.5pt; line-height: 1.65; margin-bottom: 7pt; color: #313F50; }}
.page--dark p, .page--black p {{ color: rgba(237,237,232,0.78); }}
.page--dark h1, .page--dark h2, .page--black h1, .page--black h2 {{ color: #EDEDE8; border-bottom-color: #F79204; }}
.page--dark h3, .page--black h3 {{ color: #3B8FD9; }}
.page--dark h4, .page--black h4 {{ color: #EDEDE8; }}

/* ── Labels / monospace ── */
.label {{ font-family: 'IBM Plex Mono', monospace; font-size: 7.5pt; font-weight: 600; text-transform: uppercase; letter-spacing: 0.2em; color: #025199; margin-bottom: 10pt; display: flex; align-items: center; gap: 8pt; }}
.label::before {{ content: ''; display: block; width: 16pt; height: 8pt; background: #F79204; flex-shrink: 0; }}
.label--white {{ color: #4B6881; }}
.mono {{ font-family: 'IBM Plex Mono', monospace; }}
.hivis {{ color: #F79204; }}
.blue {{ color: #025199; }}

.divider {{ height: 1pt; background: #C7CBC6; margin: 12pt 0; }}
.divider--dark {{ background: #313F50; }}

/* ── Rule / callout (hard, hi-vis left bar) ── */
.rule {{ background: #FFFFFF; border: 1pt solid #0B0E14; border-left: 6pt solid #F79204; padding: 10pt 14pt; margin: 12pt 0; font-size: 9pt; color: #313F50; }}
.rule strong {{ color: #0B0E14; }}
.rule--dark {{ background: #161B22; border: 1pt solid #313F50; border-left: 6pt solid #F79204; color: rgba(237,237,232,0.8); }}
.rule--dark strong {{ color: #F79204; }}

/* ── Do / Don't (hard squares, no radius) ── */
.do {{ background: #FFFFFF; border: 1pt solid #1B7A3D; border-left: 5pt solid #1B7A3D; padding: 8pt 12pt; margin: 6pt 0; font-size: 8.5pt; color: #313F50; }}
.do::before {{ content: '[ SI ] '; font-family: 'IBM Plex Mono', monospace; font-weight: 600; color: #1B7A3D; }}
.dont {{ background: #FFFFFF; border: 1pt solid #B3261E; border-left: 5pt solid #B3261E; padding: 8pt 12pt; margin: 6pt 0; font-size: 8.5pt; color: #313F50; }}
.dont::before {{ content: '[ NO ] '; font-family: 'IBM Plex Mono', monospace; font-weight: 600; color: #B3261E; }}

/* ── Cover ── */
.cover {{ padding: 0; background: #0B0E14; color: #EDEDE8; display: flex; flex-direction: column; }}
.cover-grid {{ position: absolute; inset: 0; display: grid; grid-template-columns: repeat(4, 1fr); pointer-events: none; z-index: 0; }}
.cover-grid span {{ border-left: 1pt solid #313F50; opacity: 0.45; }}
.cover-grid span:last-child {{ border-right: 1pt solid #313F50; }}
.cover-hatch {{ position: absolute; inset: 0; background: repeating-linear-gradient(45deg, transparent 0 14pt, rgba(49,63,80,0.10) 14pt 15pt); pointer-events: none; z-index: 0; }}
.cover-corner {{ position: absolute; top: 0; right: 0; width: 0; height: 0; border-top: 70pt solid #F79204; border-left: 70pt solid transparent; z-index: 2; }}
.cover-top {{ position: relative; z-index: 3; padding: 18mm 20mm 0; display: flex; justify-content: space-between; align-items: flex-start; }}
.cover-top .mono {{ font-size: 7.5pt; letter-spacing: 0.2em; color: #4B6881; text-transform: uppercase; line-height: 1.8; }}
.cover-mid {{ position: relative; z-index: 3; flex: 1; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 0 20mm; gap: 22pt; }}
.cover-mid img {{ max-width: 280pt; }}
.cover-bar {{ width: 80pt; height: 5pt; background: #F79204; }}
.cover-mid h1 {{ color: #EDEDE8; font-size: 26pt; letter-spacing: 0.02em; margin: 0; line-height: 1.0; }}
.cover-sub {{ font-family: 'IBM Plex Mono', monospace; font-size: 9pt; color: #4B6881; letter-spacing: 0.28em; text-transform: uppercase; }}
.cover-chips {{ display: flex; gap: 0; flex-wrap: wrap; justify-content: center; border: 1pt solid #313F50; }}
.cover-chip {{ font-family: 'IBM Plex Mono', monospace; font-size: 7.5pt; font-weight: 500; color: #EDEDE8; letter-spacing: 0.1em; text-transform: uppercase; padding: 7pt 12pt; border-right: 1pt solid #313F50; }}
.cover-chip:last-child {{ border-right: 0; }}
.cover-chip.is-accent {{ color: #F79204; }}
.cover-bottom {{ position: relative; z-index: 3; padding: 0 20mm 16mm; display: flex; justify-content: space-between; align-items: flex-end; border-top: 1pt solid #313F50; margin: 0 20mm; padding-top: 10pt; }}
.cover-bottom .mono {{ font-size: 7pt; letter-spacing: 0.16em; color: #4B6881; text-transform: uppercase; }}

/* ── Color swatches (square, hard border) ── */
.swatch-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 0; margin: 12pt 0; border: 1pt solid #0B0E14; }}
.swatch-grid--6 {{ grid-template-columns: repeat(6, 1fr); }}
.swatch {{ border-right: 1pt solid #0B0E14; }}
.swatch:last-child {{ border-right: 0; }}
.swatch .color {{ height: 64pt; border-bottom: 1pt solid #0B0E14; }}
.swatch .label-wrap {{ padding: 7pt 9pt; background: #fff; }}
.swatch .sw-name {{ font-family: 'Archivo', sans-serif; font-size: 8pt; font-weight: 700; color: #0B0E14; text-transform: uppercase; letter-spacing: 0.03em; }}
.swatch .sw-hex {{ font-family: 'IBM Plex Mono', monospace; font-size: 8pt; color: #025199; margin-top: 2pt; }}
.swatch .sw-use {{ font-size: 7pt; color: #6b7280; margin-top: 3pt; line-height: 1.35; }}

/* ── Proportions bar (hard segments) ── */
.proportions {{ display: flex; height: 34pt; border: 1pt solid #0B0E14; margin: 12pt 0; }}
.prop-seg {{ display: flex; align-items: center; justify-content: center; font-family: 'IBM Plex Mono', monospace; font-size: 8pt; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase; border-right: 1pt solid #0B0E14; }}
.prop-seg:last-child {{ border-right: 0; }}
.prop-blue  {{ background: #025199; color: #fff; }}
.prop-metal {{ background: #313F50; color: #EDEDE8; }}
.prop-hivis {{ background: #F79204; color: #000; }}

/* ── Type specimens ── */
.type-specimen {{ margin: 10pt 0; padding: 14pt 16pt; background: #FFFFFF; border: 1pt solid #0B0E14; border-left: 5pt solid #025199; }}
.type-spec-name {{ font-family: 'IBM Plex Mono', monospace; font-size: 7.5pt; color: #4B6881; text-transform: uppercase; letter-spacing: 0.14em; margin-bottom: 6pt; }}
.type-weights {{ display: flex; flex-direction: column; gap: 5pt; margin-top: 8pt; }}
.type-weight-row {{ display: flex; align-items: baseline; gap: 12pt; }}
.type-weight-label {{ font-family: 'IBM Plex Mono', monospace; font-size: 7.5pt; color: #4B6881; width: 30pt; flex-shrink: 0; }}

/* ── Logo variants ── */
.logo-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 0; margin: 12pt 0; border: 1pt solid #0B0E14; }}
.logo-box {{ padding: 22pt; display: flex; flex-direction: column; align-items: center; gap: 12pt; border-right: 1pt solid #0B0E14; border-bottom: 1pt solid #0B0E14; }}
.logo-box:nth-child(2n) {{ border-right: 0; }}
.logo-box:nth-child(n+3) {{ border-bottom: 0; }}
.logo-box img {{ max-width: 150pt; max-height: 56pt; object-fit: contain; }}
.logo-box-label {{ font-family: 'IBM Plex Mono', monospace; font-size: 7pt; color: #6b7280; text-align: center; text-transform: uppercase; letter-spacing: 0.1em; line-height: 1.5; }}
.logo-box--white {{ background: #FFFFFF; }}
.logo-box--dark  {{ background: #0B0E14; }}
.logo-box--black {{ background: #000000; }}
.logo-box--metal {{ background: #313F50; }}
.logo-box--blue  {{ background: #025199; }}

/* ── Isotype row ── */
.iso-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 0; border: 1pt solid #0B0E14; margin: 10pt 0; }}
.iso-box {{ padding: 18pt; display: flex; flex-direction: column; align-items: center; gap: 10pt; border-right: 1pt solid #0B0E14; }}
.iso-box:last-child {{ border-right: 0; }}
.iso-box img {{ object-fit: contain; }}
.iso-box span {{ font-family: 'IBM Plex Mono', monospace; font-size: 7pt; color: #6b7280; text-transform: uppercase; letter-spacing: 0.1em; }}

/* ── Spec / data table ── */
.spec-table {{ width: 100%; border-collapse: collapse; margin: 10pt 0; font-size: 8.5pt; border: 1pt solid #0B0E14; }}
.spec-table th {{ background: #0B0E14; color: #EDEDE8; padding: 7pt 10pt; text-align: left; font-family: 'IBM Plex Mono', monospace; font-size: 7.5pt; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; }}
.spec-table td {{ padding: 7pt 10pt; border-bottom: 1pt solid #C7CBC6; border-right: 1pt solid #C7CBC6; color: #313F50; }}
.spec-table tr:nth-child(even) td {{ background: #F4F5F2; }}
.spec-table .v-yes {{ color: #1B7A3D; font-weight: 600; }}
.spec-table .v-no  {{ color: #B3261E; font-weight: 600; }}
.spec-table .mono {{ font-family: 'IBM Plex Mono', monospace; }}

/* ── Pattern swatches ── */
.pattern-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 0; margin: 10pt 0; border: 1pt solid #0B0E14; }}
.pattern-box {{ height: 84pt; position: relative; overflow: hidden; border-right: 1pt solid #0B0E14; display: flex; align-items: flex-end; padding: 8pt; }}
.pattern-box:last-child {{ border-right: 0; }}
.pattern-label {{ font-family: 'IBM Plex Mono', monospace; font-size: 7pt; background: #000; color: #F79204; padding: 3pt 6pt; text-transform: uppercase; letter-spacing: 0.08em; }}
.pat-hatch {{ background-color: #0B0E14; background-image: repeating-linear-gradient(45deg, transparent 0 11px, rgba(49,63,80,0.5) 11px 12px); }}
.pat-rules {{ background-color: #0B0E14; background-image: repeating-linear-gradient(90deg, transparent 0 23px, rgba(49,63,80,0.6) 23px 24px); }}
.pat-grid  {{ background-color: #0B0E14; background-image: linear-gradient(rgba(49,63,80,0.5) 1px, transparent 1px), linear-gradient(90deg, rgba(49,63,80,0.5) 1px, transparent 1px); background-size: 16pt 16pt; }}

/* ── Mockups (hard) ── */
.mockup-row {{ display: grid; grid-template-columns: 1fr 1fr; gap: 12pt; margin: 12pt 0; }}
.card-front {{ background: #0B0E14; padding: 14pt 16pt; min-height: 64pt; display: flex; flex-direction: column; justify-content: space-between; position: relative; border: 1pt solid #0B0E14; }}
.card-front::after {{ content: ''; position: absolute; bottom: 0; left: 0; right: 0; height: 4pt; background: #F79204; }}
.card-front img {{ max-width: 100pt; max-height: 28pt; object-fit: contain; }}
.card-front .card-name {{ font-family: 'Archivo', sans-serif; font-size: 8pt; font-weight: 700; color: #EDEDE8; margin: 0; text-transform: uppercase; letter-spacing: 0.04em; }}
.card-front .card-role {{ font-family: 'IBM Plex Mono', monospace; font-size: 7pt; color: #4B6881; margin: 0; }}
.card-back {{ background: #EDEDE8; padding: 14pt 16pt; min-height: 64pt; display: flex; flex-direction: column; justify-content: center; gap: 6pt; border: 1pt solid #0B0E14; }}
.card-back .cb-item {{ display: flex; align-items: center; gap: 6pt; font-family: 'IBM Plex Mono', monospace; font-size: 7.5pt; color: #313F50; }}
.card-back .cb-dot {{ width: 6pt; height: 6pt; background: #F79204; flex-shrink: 0; }}

.signage-box {{ background: #0B0E14; padding: 22pt; display: flex; flex-direction: column; align-items: center; gap: 12pt; min-height: 84pt; justify-content: center; border: 1pt solid #0B0E14; position: relative; }}
.signage-box::before {{ content: ''; position: absolute; top: 0; left: 0; width: 28pt; height: 5pt; background: #F79204; }}
.signage-box img {{ max-width: 160pt; max-height: 56pt; object-fit: contain; }}
.signage-sub {{ font-family: 'IBM Plex Mono', monospace; font-size: 7pt; color: #4B6881; letter-spacing: 0.2em; text-transform: uppercase; text-align: center; }}

/* ── Icon grid ── */
.icon-grid {{ display: grid; grid-template-columns: repeat(6, 1fr); gap: 0; margin: 10pt 0; border: 1pt solid #0B0E14; }}
.icon-box {{ display: flex; flex-direction: column; align-items: center; gap: 6pt; padding: 12pt 6pt; background: #FFFFFF; border-right: 1pt solid #0B0E14; }}
.icon-box:last-child {{ border-right: 0; }}
.icon-box svg {{ color: #025199; }}
.icon-box span {{ font-family: 'IBM Plex Mono', monospace; font-size: 6pt; color: #6b7280; text-align: center; text-transform: uppercase; letter-spacing: 0.06em; }}

/* ── Certification chips ── */
.cert-grid {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 0; margin: 12pt 0; border: 1pt solid #0B0E14; }}
.cert-cell {{ padding: 14pt 16pt; border-right: 1pt solid #0B0E14; border-bottom: 1pt solid #0B0E14; }}
.cert-cell:nth-child(2n) {{ border-right: 0; }}
.cert-cell:nth-child(n+3) {{ border-bottom: 0; }}
.cert-code {{ font-family: 'IBM Plex Mono', monospace; font-size: 12pt; font-weight: 600; color: #025199; letter-spacing: 0.02em; }}
.cert-scope {{ font-size: 8.5pt; color: #313F50; margin-top: 4pt; }}

/* ── Eje / area cells ── */
.eje-grid {{ display: grid; grid-template-columns: repeat(5, 1fr); gap: 0; margin-top: 8pt; border: 1pt solid #313F50; }}
.eje-cell {{ padding: 12pt 8pt; text-align: center; border-right: 1pt solid #313F50; }}
.eje-cell:last-child {{ border-right: 0; }}
.eje-n {{ font-family: 'IBM Plex Mono', monospace; font-size: 8pt; font-weight: 600; color: #F79204; margin-bottom: 4pt; }}
.eje-name {{ font-family: 'Archivo', sans-serif; font-size: 8.5pt; font-weight: 700; color: #EDEDE8; text-transform: uppercase; letter-spacing: 0.03em; line-height: 1.25; }}

/* ── Page chrome ── */
.page-watermark {{ position: absolute; bottom: 10mm; right: 20mm; font-family: 'IBM Plex Mono', monospace; font-size: 7pt; color: rgba(11,14,20,0.22); letter-spacing: 0.12em; text-transform: uppercase; }}
.page-watermark--dark {{ color: rgba(237,237,232,0.18); }}
.page-number {{ position: absolute; bottom: 10mm; left: 20mm; font-family: 'IBM Plex Mono', monospace; font-size: 7pt; color: #025199; letter-spacing: 0.1em; }}
.page-number--dark {{ color: #3B8FD9; }}
.corner-accent {{ position: absolute; top: 0; right: 0; width: 0; height: 0; border-top: 40pt solid #F79204; border-left: 40pt solid transparent; z-index: 2; }}

/* ── Index / ToC ── */
.toc {{ display: flex; flex-direction: column; gap: 0; margin-top: 16pt; border-top: 1pt solid #0B0E14; }}
.toc-item {{ display: flex; align-items: baseline; gap: 8pt; padding: 8pt 0; border-bottom: 1pt solid #C7CBC6; }}
.toc-num {{ font-family: 'IBM Plex Mono', monospace; font-size: 8pt; color: #F79204; font-weight: 600; width: 20pt; flex-shrink: 0; }}
.toc-title {{ font-family: 'Archivo', sans-serif; font-size: 9.5pt; font-weight: 600; color: #0B0E14; flex: 1; text-transform: uppercase; letter-spacing: 0.02em; }}
.toc-dots {{ flex: 1; border-bottom: 1pt dotted #9aa0a6; margin: 0 4pt; align-self: flex-end; height: 8pt; }}
.toc-pg {{ font-family: 'IBM Plex Mono', monospace; font-size: 8pt; color: #4B6881; }}

/* ── Screen preview ── */
@media screen {{
  body {{ background: #2a2e33; padding: 20px; }}
  .page {{ margin: 0 auto 24px; box-shadow: 0 4px 32px rgba(0,0,0,0.4); }}
}}
</style>
</head>
<body>

<!-- ═══ PAGE 1 — COVER ═══ -->
<div class="page cover">
  <div class="cover-grid"><span></span><span></span><span></span><span></span></div>
  <div class="cover-hatch"></div>
  <div class="cover-corner"></div>

  <div class="cover-top">
    <div class="mono">COICEM&nbsp;S.A.S<br>MANUAL DE MARCA</div>
    <div class="mono" style="text-align:right;">REF · BRAND-2026<br>DOC · 01 / 15</div>
  </div>

  <div class="cover-mid">
    <img src="{LOGO_B64}" alt="COICEM S.A.S">
    <div class="cover-bar"></div>
    <div>
      <h1>Manual de<br>Identidad Visual</h1>
      <p class="cover-sub" style="margin-top:10pt;">Brandbook Corporativo · v1</p>
    </div>
    <div class="cover-chips">
      <span class="cover-chip">Operación</span>
      <span class="cover-chip">Mantenimiento</span>
      <span class="cover-chip is-accent">Construcción</span>
      <span class="cover-chip">Energía</span>
      <span class="cover-chip">Infraestructura</span>
    </div>
  </div>

  <div class="cover-bottom">
    <div class="mono">COICEM S.A.S · SERVICIO MANTENIMIENTO ESPECIALIZADO</div>
    <div class="mono">COICEM.COM · COLOMBIA · 2026</div>
  </div>
</div>


<!-- ═══ PAGE 2 — ÍNDICE ═══ -->
<div class="page page--white">
  <div class="corner-accent"></div>
  <div class="page-watermark">COICEM Brandbook 2026</div>
  <div class="page-number">02</div>

  <div class="label">Contenido</div>
  <h1>Índice</h1>

  <div class="toc">
    <div class="toc-item"><span class="toc-num">01</span><span class="toc-title">Identidad Corporativa</span><span class="toc-dots"></span><span class="toc-pg">03</span></div>
    <div class="toc-item"><span class="toc-num">02</span><span class="toc-title">Logo — Versiones y Variantes</span><span class="toc-dots"></span><span class="toc-pg">04</span></div>
    <div class="toc-item"><span class="toc-num">03</span><span class="toc-title">Isotipo / Emblema</span><span class="toc-dots"></span><span class="toc-pg">05</span></div>
    <div class="toc-item"><span class="toc-num">04</span><span class="toc-title">Área de Protección y Escala</span><span class="toc-dots"></span><span class="toc-pg">06</span></div>
    <div class="toc-item"><span class="toc-num">05</span><span class="toc-title">Paleta de Colores</span><span class="toc-dots"></span><span class="toc-pg">07</span></div>
    <div class="toc-item"><span class="toc-num">06</span><span class="toc-title">Sistema Tipográfico</span><span class="toc-dots"></span><span class="toc-pg">08</span></div>
    <div class="toc-item"><span class="toc-num">07</span><span class="toc-title">Iconografía</span><span class="toc-dots"></span><span class="toc-pg">09</span></div>
    <div class="toc-item"><span class="toc-num">08</span><span class="toc-title">Patrones Gráficos y Cursor</span><span class="toc-dots"></span><span class="toc-pg">10</span></div>
    <div class="toc-item"><span class="toc-num">09</span><span class="toc-title">Certificaciones</span><span class="toc-dots"></span><span class="toc-pg">11</span></div>
    <div class="toc-item"><span class="toc-num">10</span><span class="toc-title">Aplicaciones — Papelería</span><span class="toc-dots"></span><span class="toc-pg">12</span></div>
    <div class="toc-item"><span class="toc-num">11</span><span class="toc-title">Aplicaciones — Digital y Señalética</span><span class="toc-dots"></span><span class="toc-pg">13</span></div>
    <div class="toc-item"><span class="toc-num">12</span><span class="toc-title">Tono de Comunicación</span><span class="toc-dots"></span><span class="toc-pg">14</span></div>
    <div class="toc-item"><span class="toc-num">13</span><span class="toc-title">Usos Incorrectos — Don'ts</span><span class="toc-dots"></span><span class="toc-pg">15</span></div>
    <div class="toc-item"><span class="toc-num">14</span><span class="toc-title">Firma de Correo</span><span class="toc-dots"></span><span class="toc-pg">16</span></div>
  </div>

  <div class="rule" style="margin-top:20pt;">
    <strong>Nota de versión:</strong> Brandbook v1. La tipografía del wordmark y la paleta son una reconstrucción provisional extraída del logo entregado; al recibir el logo vectorial original del cliente se re-extraen los colores y se actualiza este manual, los tokens y la firma.
  </div>
</div>


<!-- ═══ PAGE 3 — IDENTIDAD CORPORATIVA ═══ -->
<div class="page page--dark">
  <div class="page-watermark page-watermark--dark">COICEM Brandbook 2026</div>
  <div class="page-number page-number--dark">03</div>

  <div class="label label--white">01 — Identidad</div>
  <h2>Quiénes somos</h2>

  <div style="display:grid;grid-template-columns:1fr 1fr;gap:20pt;margin-top:12pt;">
    <div>
      <h3>Razón Social</h3>
      <p class="display" style="font-size:15pt;font-weight:900;color:#EDEDE8;line-height:1.05;margin:0;">COICEM S.A.S</p>
      <p class="mono" style="font-size:8pt;color:#4B6881;letter-spacing:0.16em;text-transform:uppercase;margin-top:4pt;">Servicio Mantenimiento Especializado</p>
      <div class="divider divider--dark"></div>
      <h3>Sector</h3>
      <p>Mantenimiento industrial especializado para los sectores <strong style="color:#F79204;">petrolero, petroquímico y energético</strong>, con líneas de construcción e infraestructura. Aliado técnico para proyectos de alto impacto del sector industrial y civil.</p>
      <h3>Valores</h3>
      <p>Excelencia operativa · Innovación constante · Seguridad industrial · Gestión ambiental responsable · Conocimiento técnico de vanguardia</p>
    </div>
    <div>
      <h3>Misión</h3>
      <p>Diseñamos y ejecutamos soluciones integrales de operación, mantenimiento, construcción, energía e infraestructura, respaldadas por servicios técnicos avanzados y gestión ambiental responsable, para optimizar la productividad y sostenibilidad de los proyectos del sector industrial, energético y civil.</p>
      <h3>Visión</h3>
      <p>Para el año 2030, ser reconocida como la empresa líder en Colombia en soluciones integrales de ingeniería, energía e infraestructura industrial, destacándonos por la excelencia operativa, la innovación y el compromiso con la sostenibilidad. <em style="color:#4B6881;font-size:8pt;">Meta: 2030.</em></p>
    </div>
  </div>

  <div class="divider divider--dark" style="margin-top:16pt;"></div>

  <h3>Cinco áreas operativas</h3>
  <div class="eje-grid">
    <div class="eje-cell"><div class="eje-n">01</div><div class="eje-name">Operación</div></div>
    <div class="eje-cell"><div class="eje-n">02</div><div class="eje-name">Mantenimiento</div></div>
    <div class="eje-cell"><div class="eje-n">03</div><div class="eje-name">Construcción</div></div>
    <div class="eje-cell"><div class="eje-n">04</div><div class="eje-name">Energía</div></div>
    <div class="eje-cell"><div class="eje-n">05</div><div class="eje-name">Infraestructura</div></div>
  </div>
</div>


<!-- ═══ PAGE 4 — LOGO VARIANTES ═══ -->
<div class="page page--white">
  <div class="corner-accent"></div>
  <div class="page-watermark">COICEM Brandbook 2026</div>
  <div class="page-number">04</div>

  <div class="label">02 — Logo</div>
  <h2>Versiones y variantes</h2>

  <p>El logo de COICEM es un <strong>lockup</strong>: el emblema circular (engranaje + herramientas: llave y destornillador, sobre instalación industrial) acompañado del wordmark <strong>COICEM</strong> en azul y <strong>SAS</strong> en naranja hi-vis. Se usa siempre en sus versiones autorizadas, sin recomponer ni separar sus elementos arbitrariamente.</p>

  <div class="logo-grid">
    <div class="logo-box logo-box--white">
      <img src="{LOGO_B64}" alt="Logo COICEM — fondo blanco">
      <span class="logo-box-label">Versión principal<br>Fondo blanco #FFFFFF</span>
    </div>
    <div class="logo-box logo-box--dark">
      <img src="{LOGO_B64}" alt="Logo COICEM — fondo grafito">
      <span class="logo-box-label" style="color:#6b7280;">Fondo base oscura<br>#0B0E14 (grafito)</span>
    </div>
    <div class="logo-box logo-box--black">
      <img src="{LOGO_B64}" alt="Logo COICEM — fondo negro">
      <span class="logo-box-label" style="color:#6b7280;">Fondo negro<br>#000000 (on-brand)</span>
    </div>
    <div class="logo-box logo-box--metal">
      <img src="{LOGO_B64}" alt="Logo COICEM — fondo metal">
      <span class="logo-box-label" style="color:#cfd6dd;">Fondo metal / grafito<br>#313F50</span>
    </div>
  </div>

  <div class="rule">
    <strong>Regla de integridad:</strong> El lockup se usa completo. El negro <span class="mono">#000000</span> ES un color de marca (es el fondo del emblema original), por lo que el logo se asienta de forma nativa sobre fondos oscuros sin marco ni caja blanca.
  </div>
</div>


<!-- ═══ PAGE 5 — ISOTIPO ═══ -->
<div class="page">
  <div class="corner-accent"></div>
  <div class="page-watermark">COICEM Brandbook 2026</div>
  <div class="page-number">05</div>

  <div class="label">03 — Isotipo</div>
  <h2>Isotipo / Emblema</h2>

  <p>El <strong>emblema</strong> (engranaje con herramientas dentro del círculo) funciona como símbolo aislado de la marca: favicon, avatar de app, perfil social, sello y bordado. Se usa solo cuando el nombre "COICEM" es reconocible por contexto; nunca reemplaza al lockup completo en papelería formal.</p>

  <div class="iso-grid">
    <div class="iso-box logo-box--white" style="border-bottom:0;">
      <img src="{EMB_B64}" alt="Isotipo COICEM" style="max-width:120pt;max-height:120pt;">
      <span>Positivo · fondo claro</span>
    </div>
    <div class="iso-box logo-box--dark" style="border-bottom:0;">
      <img src="{EMB_B64}" alt="Isotipo COICEM negativo" style="max-width:120pt;max-height:120pt;">
      <span style="color:#6b7280;">Negativo · fondo oscuro</span>
    </div>
    <div class="iso-box logo-box--white" style="border-bottom:0;">
      <img src="{EMB_B64}" alt="Isotipo COICEM favicon" style="max-width:48pt;max-height:48pt;">
      <span>Favicon · 48 / 32 / 16 px</span>
    </div>
  </div>

  <h3>Reglas del isotipo</h3>
  <div class="do">Usar el isotipo como favicon, avatar y sello cuando el espacio es reducido</div>
  <div class="do">Mantener el emblema dentro de su círculo, sin recortar los dientes del engranaje</div>
  <div class="dont">Usar el isotipo en lugar del lockup en documentos formales o portadas</div>
  <div class="dont">Extraer la llave o el destornillador como ícono suelto fuera del círculo</div>

  <div class="rule" style="margin-top:14pt;">
    <strong>Tamaño mínimo del isotipo:</strong> 24px / 8mm (favicon 16px aceptable). Por debajo, la mecánica del engranaje pierde definición.
  </div>
</div>


<!-- ═══ PAGE 6 — ÁREA DE PROTECCIÓN Y ESCALA ═══ -->
<div class="page page--white">
  <div class="corner-accent"></div>
  <div class="page-watermark">COICEM Brandbook 2026</div>
  <div class="page-number">06</div>

  <div class="label">04 — Logo</div>
  <h2>Área de protección y escala</h2>

  <h3>Espacio de protección</h3>
  <p>Se respeta un margen libre alrededor del lockup equivalente a la altura de un <strong>diente del engranaje</strong> del emblema (unidad X). Ningún texto, imagen ni borde invade esa zona.</p>

  <div style="display:flex;align-items:center;justify-content:center;padding:24pt;margin:12pt 0;border:1pt dashed #F79204;background:#fff;position:relative;">
    <div style="position:absolute;top:5pt;left:6pt;font-family:'IBM Plex Mono',monospace;font-size:7pt;color:#F79204;letter-spacing:0.1em;">X = ALTURA DE DIENTE</div>
    <img src="{LOGO_B64}" alt="Logo COICEM con área de protección" style="max-width:180pt;max-height:64pt;object-fit:contain;">
  </div>

  <h3>Escala de tamaños autorizados</h3>
  <table class="spec-table">
    <tr><th>Soporte</th><th>Ancho mínimo</th><th>Resolución</th><th>Formato</th></tr>
    <tr><td>Digital — web / app</td><td class="mono">160px</td><td class="mono">72–96 dpi</td><td>PNG / SVG</td></tr>
    <tr><td>Navbar web</td><td class="mono">200px</td><td class="mono">96+ dpi (2×)</td><td>PNG transparente</td></tr>
    <tr><td>Firma de correo</td><td class="mono">200px</td><td class="mono">72 dpi</td><td>PNG (base64)</td></tr>
    <tr><td>Papelería impresa</td><td class="mono">32mm</td><td class="mono">300 dpi</td><td>PNG / PDF vector</td></tr>
    <tr><td>Vehículos (vinil)</td><td class="mono">200mm</td><td class="mono">150 dpi final</td><td>PDF vector</td></tr>
    <tr><td>Señalética exterior</td><td class="mono">300mm</td><td class="mono">72 dpi final</td><td>PDF vector</td></tr>
  </table>

  <div class="rule" style="margin-top:14pt;">
    <strong>Nota:</strong> El lockup nunca se usa a menos de 32mm de ancho en impresión ni 160px en digital. Por debajo de esas medidas, usar solo el isotipo.
  </div>
</div>


<!-- ═══ PAGE 7 — PALETA ═══ -->
<div class="page page--white">
  <div class="corner-accent"></div>
  <div class="page-watermark">COICEM Brandbook 2026</div>
  <div class="page-number">07</div>

  <div class="label">05 — Color</div>
  <h2>Paleta de colores</h2>

  <div class="proportions">
    <div class="prop-seg prop-blue" style="flex:60;">60% · ESTRUCTURA AZUL / OSCURO</div>
    <div class="prop-seg prop-metal" style="flex:30;">30% · METAL</div>
    <div class="prop-seg prop-hivis" style="flex:10;">10% · HI-VIS</div>
  </div>

  <div class="rule" style="margin-bottom:14pt;">
    <strong>Regla de proporción:</strong> El sistema se asienta sobre azul corporativo, grafito y base oscura. El <span class="hivis">naranja hi-vis</span> es señal de seguridad y acento de conversión — funciona como el chaleco reflectivo en planta: nunca domina, siempre destaca. Si el naranja supera ~10% visual, la pieza se rediseña.
  </div>

  <h3>Estructura — Azul corporativo y base oscura</h3>
  <div class="swatch-grid">
    <div class="swatch"><div class="color" style="background:#025199;"></div><div class="label-wrap"><div class="sw-name">Azul COICEM</div><div class="sw-hex">#025199</div><div class="sw-use">Wordmark, titulares mono, autoridad</div></div></div>
    <div class="swatch"><div class="color" style="background:#3B8FD9;"></div><div class="label-wrap"><div class="sw-name">Azul Claro</div><div class="sw-hex">#3B8FD9</div><div class="sw-use">Texto / links sobre fondo oscuro</div></div></div>
    <div class="swatch"><div class="color" style="background:#0B0E14;"></div><div class="label-wrap"><div class="sw-name">Base Oscura</div><div class="sw-hex">#0B0E14</div><div class="sw-use">Fondos hero, footer, grafito brutalist</div></div></div>
  </div>

  <h3>Acento — Naranja hi-vis</h3>
  <div class="swatch-grid">
    <div class="swatch"><div class="color" style="background:#F79204;"></div><div class="label-wrap"><div class="sw-name">Naranja Hi-Vis</div><div class="sw-hex">#F79204</div><div class="sw-use">CTAs, "SAS", acentos, barras de seguridad</div></div></div>
    <div class="swatch"><div class="color" style="background:#FFA222;"></div><div class="label-wrap"><div class="sw-name">Naranja Claro</div><div class="sw-hex">#FFA222</div><div class="sw-use">Hover, brillos sobre oscuro</div></div></div>
    <div class="swatch"><div class="color" style="background:#DB7E00;"></div><div class="label-wrap"><div class="sw-name">Naranja Hover</div><div class="sw-hex">#DB7E00</div><div class="sw-use">Estado pressed / hover de CTA</div></div></div>
  </div>

  <h3>Metal y neutros</h3>
  <div class="swatch-grid swatch-grid--6" style="margin-top:8pt;">
    <div class="swatch"><div class="color" style="background:#313F50;"></div><div class="label-wrap"><div class="sw-name">Metal</div><div class="sw-hex">#313F50</div><div class="sw-use">Bordes, engranaje</div></div></div>
    <div class="swatch"><div class="color" style="background:#4B6881;"></div><div class="label-wrap"><div class="sw-name">Metal Claro</div><div class="sw-hex">#4B6881</div><div class="sw-use">Texto mono, meta</div></div></div>
    <div class="swatch"><div class="color" style="background:#161B22;"></div><div class="label-wrap"><div class="sw-name">Panel</div><div class="sw-hex">#161B22</div><div class="sw-use">Bloques brutalist</div></div></div>
    <div class="swatch"><div class="color" style="background:#000000;"></div><div class="label-wrap"><div class="sw-name">Negro</div><div class="sw-hex">#000000</div><div class="sw-use">Fondo del emblema</div></div></div>
    <div class="swatch"><div class="color" style="background:#EDEDE8;"></div><div class="label-wrap"><div class="sw-name">Concreto</div><div class="sw-hex">#EDEDE8</div><div class="sw-use">Off-white, fondos claros</div></div></div>
    <div class="swatch"><div class="color" style="background:#FFFFFF;border-bottom:1pt solid #0B0E14;"></div><div class="label-wrap"><div class="sw-name">Blanco</div><div class="sw-hex">#FFFFFF</div><div class="sw-use">Superficies, texto inverso</div></div></div>
  </div>

  <p class="mono" style="font-size:7pt;color:#4B6881;margin-top:10pt;letter-spacing:0.08em;">PALETA PROVISIONAL v1 · EXTRAÍDA DEL LOGO · RE-EXTRAER AL RECIBIR EL VECTOR ORIGINAL</p>
</div>


<!-- ═══ PAGE 8 — TIPOGRAFÍA ═══ -->
<div class="page page--white">
  <div class="corner-accent"></div>
  <div class="page-watermark">COICEM Brandbook 2026</div>
  <div class="page-number">08</div>

  <div class="label">06 — Tipografía</div>
  <h2>Sistema tipográfico</h2>

  <p>COICEM usa tres familias que equilibran presencia industrial, legibilidad técnica y precisión de datos. Lenguaje de señalética y hoja de datos: titulares anchos en mayúsculas, cuerpo neutral y datos en monoespaciada.</p>

  <div class="type-specimen">
    <div class="type-spec-name">Display / Titulares — Archivo Expanded</div>
    <p class="display" style="font-size:26pt;font-weight:900;color:#0B0E14;line-height:0.98;margin:0;">MANTENIMIENTO INDUSTRIAL</p>
    <p class="display" style="font-size:13pt;font-weight:700;color:#025199;margin:4pt 0 0;">DE PRECISIÓN PARA LA OPERACIÓN</p>
    <div class="type-weights">
      <div class="type-weight-row"><span class="type-weight-label">700</span><span class="display" style="font-weight:700;font-size:10pt;color:#313F50;">Bold — subtítulos de sección</span></div>
      <div class="type-weight-row"><span class="type-weight-label">800</span><span class="display" style="font-weight:800;font-size:10pt;color:#0B0E14;">Extrabold — H2 / títulos de página</span></div>
      <div class="type-weight-row"><span class="type-weight-label">900</span><span class="display" style="font-weight:900;font-size:10pt;color:#0B0E14;">Black — hero / H1, señalética</span></div>
    </div>
    <p class="mono" style="font-size:7pt;color:#4B6881;margin-top:8pt;">Fallback: 'Archivo' (width expanded) → 'Arial Black'. Autohospedar 'Archivo Expanded' en producción.</p>
  </div>

  <div class="type-specimen" style="border-left-color:#313F50;">
    <div class="type-spec-name">Body / Texto corrido — IBM Plex Sans</div>
    <p style="font-family:'IBM Plex Sans',sans-serif;font-size:10pt;font-weight:400;color:#313F50;line-height:1.6;margin:0;">COICEM ejecuta mantenimiento industrial especializado —predictivo, preventivo y correctivo— de equipos estáticos y rotativos en facilidades de producción de los sectores petrolero, petroquímico y energético.</p>
    <div class="type-weights">
      <div class="type-weight-row"><span class="type-weight-label">400</span><span style="font-family:'IBM Plex Sans';font-weight:400;font-size:10pt;color:#313F50;">Regular — párrafos, descripciones</span></div>
      <div class="type-weight-row"><span class="type-weight-label">500</span><span style="font-family:'IBM Plex Sans';font-weight:500;font-size:10pt;color:#313F50;">Medium — labels, navegación</span></div>
      <div class="type-weight-row"><span class="type-weight-label">700</span><span style="font-family:'IBM Plex Sans';font-weight:700;font-size:10pt;color:#0B0E14;">Bold — énfasis en párrafo</span></div>
    </div>
  </div>

  <div class="type-specimen" style="border-left-color:#F79204;">
    <div class="type-spec-name">Monospace / Datos técnicos — IBM Plex Mono</div>
    <p class="mono" style="font-size:10pt;font-weight:400;color:#313F50;margin:0;">REF · COICEM-HERO-01 · #F79204 · ISO 9001:2015 · COICEM.COM</p>
    <div class="type-weights">
      <div class="type-weight-row"><span class="type-weight-label">400</span><span class="mono" style="font-weight:400;font-size:10pt;color:#313F50;">Regular — refs, specs, coordenadas, fechas</span></div>
      <div class="type-weight-row"><span class="type-weight-label">600</span><span class="mono" style="font-weight:600;font-size:10pt;color:#313F50;">Semibold — eyebrows, telemetría, códigos</span></div>
    </div>
  </div>
</div>


<!-- ═══ PAGE 9 — ICONOGRAFÍA ═══ -->
<div class="page">
  <div class="corner-accent"></div>
  <div class="page-watermark">COICEM Brandbook 2026</div>
  <div class="page-number">09</div>

  <div class="label">07 — Iconografía</div>
  <h2>Lineamientos de iconografía</h2>

  <p>COICEM usa íconos <strong>outlined (contorno)</strong> de trazo recto y terminaciones cuadradas, coherentes con el lenguaje brutalist-industrial. Estilo técnico de plano: nunca filled, nunca duotone, nunca mezclados.</p>

  <h3>Estilo autorizado — Outlined, 1.75px, terminación cuadrada</h3>
  <div class="icon-grid">
    <div class="icon-box">
      <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="square" stroke-linejoin="miter"><circle cx="12" cy="12" r="9"/><path d="M12 12l5-3"/><path d="M12 3v2M12 19v2M3 12h2M19 12h2"/></svg>
      <span>Operación</span>
    </div>
    <div class="icon-box">
      <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="square" stroke-linejoin="miter"><path d="M14 6a3.5 3.5 0 0 0-4.7 4.2L3 16.5 5.5 19l6.3-6.3A3.5 3.5 0 0 0 16 8l-2 2-2-2 2-2z"/></svg>
      <span>Mantenimiento</span>
    </div>
    <div class="icon-box">
      <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="square" stroke-linejoin="miter"><path d="M4 21V8l9-4v17"/><path d="M13 9h7v12"/><path d="M7 12h2M7 15h2M16 13h1M16 16h1"/></svg>
      <span>Construcción</span>
    </div>
    <div class="icon-box">
      <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="square" stroke-linejoin="miter"><path d="M13 2L4 14h7l-1 8 9-12h-7l1-8z"/></svg>
      <span>Energía</span>
    </div>
    <div class="icon-box">
      <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="square" stroke-linejoin="miter"><path d="M3 21V10l6-3v3l6-3v3l6-3v11z"/><path d="M3 21h18"/></svg>
      <span>Infraestructura</span>
    </div>
    <div class="icon-box">
      <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="square" stroke-linejoin="miter"><path d="M12 3l8 3v6c0 5-4 8-8 9-4-1-8-4-8-9V6l8-3z"/><path d="M9 12l2 2 4-4"/></svg>
      <span>Calidad / HSE</span>
    </div>
  </div>

  <div class="divider"></div>

  <h3>Reglas de uso</h3>
  <table class="spec-table">
    <tr><th>Atributo</th><th>Valor correcto</th><th>Prohibido</th></tr>
    <tr><td>Estilo</td><td class="v-yes">Outlined (contorno)</td><td class="v-no">Filled, duotone</td></tr>
    <tr><td>Peso del trazo</td><td class="v-yes">1.75px – 2px</td><td class="v-no">Menos de 1.5px, más de 2.5px</td></tr>
    <tr><td>Terminaciones</td><td class="v-yes">Square / miter (cuadradas)</td><td class="v-no">Round (redondeadas)</td></tr>
    <tr><td>Color</td><td class="v-yes">#025199 sobre claro · #F79204 sobre oscuro</td><td class="v-no">Mezcla de colores en un mismo ícono</td></tr>
    <tr><td>Biblioteca</td><td class="v-yes">Lucide / Phosphor (líneas)</td><td class="v-no">Material filled, Font Awesome solid</td></tr>
  </table>

  <div class="rule" style="margin-top:12pt;">
    <strong>Tamaño mínimo:</strong> 16px / 12pt en digital; 8mm en impresión. Sobre fondo oscuro, el ícono va en hi-vis o azul claro para garantizar contraste AA.
  </div>
</div>


<!-- ═══ PAGE 10 — PATRONES GRÁFICOS Y CURSOR ═══ -->
<div class="page page--white">
  <div class="corner-accent"></div>
  <div class="page-watermark">COICEM Brandbook 2026</div>
  <div class="page-number">10</div>

  <div class="label">08 — Patrones</div>
  <h2>Patrones gráficos y cursor</h2>

  <p>COICEM se apoya en tres texturas de fondo derivadas del lenguaje de plano técnico / hoja de datos. Se usan como capas secundarias sobre fondos oscuros, nunca sobre texto de lectura.</p>

  <div class="pattern-grid">
    <div class="pattern-box pat-hatch"><span class="pattern-label">Diagonal Hatch 45°</span></div>
    <div class="pattern-box pat-rules"><span class="pattern-label">Column Rules</span></div>
    <div class="pattern-box pat-grid"><span class="pattern-label">Blueprint Grid</span></div>
  </div>

  <h3>Bloques duros — Transición de sección</h3>
  <p>A diferencia de las ondas orgánicas de otros proyectos, COICEM separa secciones con <strong>bordes duros de 1px</strong> y bandas hi-vis. El corte es recto y maquinado: sin curvas, sin degradados suaves.</p>

  <div style="height:56pt;position:relative;overflow:hidden;margin:12pt 0;border:1pt solid #0B0E14;">
    <div style="position:absolute;inset:0;background:#0B0E14;"></div>
    <div style="position:absolute;bottom:0;left:0;right:0;height:6pt;background:#F79204;"></div>
    <div style="position:absolute;top:8pt;left:12pt;font-family:'IBM Plex Mono',monospace;font-size:7pt;color:#4B6881;letter-spacing:0.1em;">SECCIÓN OSCURA · BORDE DURO + BANDA HI-VIS</div>
  </div>

  <h3>Reglas de uso de patrones</h3>
  <div class="do">Usar diagonal hatch a baja opacidad sobre paneles grafito (como en el hero)</div>
  <div class="do">Usar column rules para reforzar la rejilla editorial de 4 columnas</div>
  <div class="dont">Usar patrones bajo texto de lectura prolongada</div>
  <div class="dont">Suavizar los cortes con curvas, ondas o degradados</div>

  <h3 style="margin-top:14pt;">Cursor signature — Retícula / Crosshair</h3>
  <p>En web, el cursor nativo se reemplaza por una <strong>retícula de calibre</strong> en hi-vis (cruz + punto + lectura de coordenadas en mono). Es un instrumento de medición, no el cursor-engranaje (prohibido, pertenece a otro proyecto). En touch (pointer: coarse) se desactiva.</p>

  <div style="display:inline-flex;align-items:center;justify-content:center;width:64pt;height:64pt;background:#0B0E14;position:relative;border:1pt solid #0B0E14;">
    <span style="position:absolute;width:26pt;height:1pt;background:#F79204;"></span>
    <span style="position:absolute;width:1pt;height:26pt;background:#F79204;"></span>
    <span style="position:absolute;width:5pt;height:5pt;border:1pt solid #F79204;"></span>
    <span class="mono" style="position:absolute;left:34pt;top:34pt;font-size:6pt;color:#4B6881;">418,260</span>
  </div>
  <p style="display:inline-block;vertical-align:middle;margin-left:12pt;font-size:8.5pt;color:#6b7280;">Estado base — desktop pointer:fine. Lerp 0.22; reduced-motion sigue directo.</p>
</div>


<!-- ═══ PAGE 11 — CERTIFICACIONES ═══ -->
<div class="page page--dark">
  <div class="page-watermark page-watermark--dark">COICEM Brandbook 2026</div>
  <div class="page-number page-number--dark">11</div>

  <div class="label label--white">09 — Certificaciones</div>
  <h2>Sistema de gestión certificado</h2>

  <p>COICEM opera bajo un sistema de gestión integral certificado por <strong style="color:#F79204;">Bureau Veritas (BVQI Colombia Ltda.)</strong>. Los sellos se exhiben en footer del sitio, propuestas, papelería y señalética. Se usan siempre con su número de norma y año, sin alterar logotipos de los entes certificadores.</p>

  <div class="cert-grid">
    <div class="cert-cell"><div class="cert-code">ISO 9001:2015</div><div class="cert-scope" style="color:rgba(237,237,232,0.7);">Sistema de Gestión de Calidad</div></div>
    <div class="cert-cell"><div class="cert-code">ISO 14001:2015</div><div class="cert-scope" style="color:rgba(237,237,232,0.7);">Sistema de Gestión Ambiental</div></div>
    <div class="cert-cell"><div class="cert-code">ISO 45001:2018</div><div class="cert-scope" style="color:rgba(237,237,232,0.7);">Seguridad y Salud en el Trabajo</div></div>
    <div class="cert-cell"><div class="cert-code">NORSOK 006:2020</div><div class="cert-scope" style="color:rgba(237,237,232,0.7);">Estándar petrolero · ambiente de trabajo</div></div>
  </div>

  <div class="rule rule--dark" style="margin-top:14pt;">
    <strong>Uso de los sellos:</strong> Mostrar como bloque mono uppercase o con los logotipos oficiales de Bureau Veritas. Nunca recolorear, deformar ni afirmar certificaciones no vigentes. Verificar la vigencia del certificado antes de cada publicación.
  </div>

  <h3 style="margin-top:16pt;">Banda de cumplimiento (footer / propuestas)</h3>
  <div style="display:flex;border:1pt solid #313F50;margin-top:8pt;">
    <div class="mono" style="flex:1;text-align:center;padding:10pt 6pt;border-right:1pt solid #313F50;color:#3B8FD9;font-size:8pt;letter-spacing:0.08em;">ISO 9001</div>
    <div class="mono" style="flex:1;text-align:center;padding:10pt 6pt;border-right:1pt solid #313F50;color:#3B8FD9;font-size:8pt;letter-spacing:0.08em;">ISO 14001</div>
    <div class="mono" style="flex:1;text-align:center;padding:10pt 6pt;border-right:1pt solid #313F50;color:#3B8FD9;font-size:8pt;letter-spacing:0.08em;">ISO 45001</div>
    <div class="mono" style="flex:1;text-align:center;padding:10pt 6pt;border-right:1pt solid #313F50;color:#F79204;font-size:8pt;letter-spacing:0.08em;">NORSOK 006</div>
    <div class="mono" style="flex:1.4;text-align:center;padding:10pt 6pt;color:#4B6881;font-size:8pt;letter-spacing:0.08em;">BUREAU VERITAS</div>
  </div>
</div>


<!-- ═══ PAGE 12 — PAPELERÍA ═══ -->
<div class="page page--white">
  <div class="corner-accent"></div>
  <div class="page-watermark">COICEM Brandbook 2026</div>
  <div class="page-number">12</div>

  <div class="label">10 — Aplicaciones</div>
  <h2>Papelería corporativa</h2>

  <h3>Tarjeta de presentación — 90 × 55mm</h3>
  <p>Frente: base oscura grafito, lockup, banda hi-vis inferior, nombre/cargo. Reverso: concreto off-white, datos de contacto en mono.</p>

  <div class="mockup-row" style="max-width:320pt;">
    <div class="card-front">
      <img src="{LOGO_B64}" alt="Logo COICEM tarjeta">
      <div>
        <p class="card-name">[Nombre del colaborador]</p>
        <p class="card-role">[Cargo / Posición]</p>
      </div>
    </div>
    <div class="card-back">
      <div class="cb-item"><div class="cb-dot"></div>[+57 000 000 0000]</div>
      <div class="cb-item"><div class="cb-dot"></div>[correo@coicem.com]</div>
      <div class="cb-item"><div class="cb-dot"></div>[Dirección — pendiente]</div>
      <div class="cb-item"><div class="cb-dot"></div>coicem.com</div>
    </div>
  </div>

  <div style="margin-top:4pt;padding:6pt 10pt;background:#fff;border:1pt solid #F79204;border-left:5pt solid #F79204;font-family:'IBM Plex Mono',monospace;font-size:7pt;color:#B36400;letter-spacing:0.04em;">
    CONTACTO PENDIENTE · EDITABLE — REEMPLAZAR [ ] CON DATOS REALES ANTES DE IMPRIMIR.
  </div>

  <div class="divider" style="margin-top:16pt;"></div>

  <h3>Hoja membretada A4</h3>
  <p>Cabecera grafito con lockup y banda hi-vis; pie con datos de contacto en mono; cuerpo blanco con watermark del isotipo al 5% centrado.</p>

  <div style="margin:10pt 0;border:1pt solid #0B0E14;background:#fff;min-height:130pt;display:flex;flex-direction:column;max-width:300pt;">
    <div style="background:#0B0E14;padding:10pt 14pt;display:flex;align-items:center;justify-content:space-between;">
      <img src="{LOGO_B64}" alt="Logo COICEM membrete" style="max-width:96pt;max-height:28pt;object-fit:contain;">
      <div style="text-align:right;">
        <p class="mono" style="font-size:6.5pt;color:#4B6881;margin:0;">NIT: [PENDIENTE]</p>
        <p class="mono" style="font-size:6.5pt;color:#4B6881;margin:0;">COICEM.COM</p>
      </div>
    </div>
    <div style="height:4pt;background:#F79204;"></div>
    <div style="padding:12pt 14pt;min-height:64pt;position:relative;display:flex;align-items:center;justify-content:center;">
      <img src="{EMB_B64}" alt="watermark" style="position:absolute;max-width:60pt;opacity:0.05;">
      <p class="mono" style="font-size:7.5pt;color:#9aa0a6;margin:0;position:relative;">[ ÁREA DE CONTENIDO DEL DOCUMENTO ]</p>
    </div>
    <div style="background:#EDEDE8;padding:6pt 14pt;border-top:1pt solid #0B0E14;">
      <p class="mono" style="font-size:6pt;color:#6b7280;margin:0;text-align:center;letter-spacing:0.04em;">COICEM S.A.S · SERVICIO MANTENIMIENTO ESPECIALIZADO · [CONTACTO PENDIENTE] · COICEM.COM</p>
    </div>
  </div>
</div>


<!-- ═══ PAGE 13 — DIGITAL / SEÑALÉTICA ═══ -->
<div class="page">
  <div class="corner-accent"></div>
  <div class="page-watermark">COICEM Brandbook 2026</div>
  <div class="page-number">13</div>

  <div class="label">11 — Aplicaciones</div>
  <h2>Digital y señalética</h2>

  <h3>Señalética exterior — fachada</h3>
  <div class="signage-box" style="max-width:300pt;margin:10pt auto;">
    <img src="{LOGO_B64}" alt="Logo COICEM señalética">
    <div class="signage-sub">COICEM S.A.S · MANTENIMIENTO INDUSTRIAL</div>
  </div>
  <p class="mono" style="font-size:7.5pt;color:#6b7280;text-align:center;margin-top:4pt;">Fondo grafito con lockup y banda hi-vis. Material: ACM o lámina retroiluminada, bordes rectos.</p>

  <div class="divider"></div>

  <h3>Aplicación en vehículo / EPP</h3>
  <div style="background:#000;border:1pt solid #0B0E14;padding:16pt 20pt;margin:10pt 0;display:flex;align-items:center;gap:16pt;">
    <div style="flex:1;">
      <div style="background:#0B0E14;border:1pt solid #313F50;padding:10pt;display:inline-block;position:relative;">
        <div style="position:absolute;top:0;left:0;width:18pt;height:4pt;background:#F79204;"></div>
        <img src="{LOGO_B64}" alt="Logo COICEM vehículo" style="max-width:110pt;max-height:36pt;object-fit:contain;">
      </div>
    </div>
    <div style="flex:1;">
      <p class="mono" style="font-size:8pt;color:#4B6881;line-height:1.6;">Lockup sobre panel grafito lateral. Ancho mínimo en vehículo: 200mm. Casco y chaleco hi-vis #F79204 con isotipo bordado al pecho. Cumplir EPP y reflectividad de planta.</p>
    </div>
  </div>

  <div class="divider"></div>

  <h3>OG Image — redes sociales (1200 × 630px)</h3>
  <div style="background:#0B0E14;border:1pt solid #0B0E14;padding:22pt;display:flex;align-items:center;justify-content:center;min-height:64pt;margin:10pt 0;position:relative;">
    <div style="position:absolute;inset:0;background:repeating-linear-gradient(45deg,transparent 0 12px,rgba(49,63,80,0.12) 12px 13px);"></div>
    <img src="{LOGO_B64}" alt="OG Image COICEM" style="max-width:190pt;max-height:60pt;object-fit:contain;position:relative;">
  </div>
  <p class="mono" style="font-size:7.5pt;color:#6b7280;">Lockup centrado sobre base oscura con hatch sutil. JPEG 95% para WhatsApp/Facebook; PNG para LinkedIn.</p>

  <div class="rule" style="margin-top:14pt;">
    <strong>Uniforme / EPP:</strong> Camisa o overol grafito (#0B0E14 / #313F50) con isotipo bordado al pecho izquierdo en hilo azul #025199 + naranja #F79204. Casco y chaleco en hi-vis #F79204 para visibilidad en planta. Bordado mínimo: 50mm ancho.
  </div>
</div>


<!-- ═══ PAGE 14 — TONO DE COMUNICACIÓN ═══ -->
<div class="page page--white">
  <div class="corner-accent"></div>
  <div class="page-watermark">COICEM Brandbook 2026</div>
  <div class="page-number">14</div>

  <div class="label">12 — Comunicación</div>
  <h2>Tono de comunicación</h2>

  <p>COICEM se dirige a gerencias de operación y mantenimiento, interventores, contratantes del sector petrolero/energético y tomadores de decisión técnica. El tono es <strong>técnico, sobrio y operativo</strong>, nunca informal ni autobombo.</p>

  <h3>Personalidad de marca</h3>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:0;margin:10pt 0;border:1pt solid #0B0E14;">
    <div style="padding:12pt;border-right:1pt solid #0B0E14;border-top:4pt solid #025199;">
      <h4>Técnico</h4>
      <p style="font-size:8.5pt;">Preciso y específico. Usa términos correctos del sector O&amp;M: predictivo, parada de planta, integridad de activos, disponibilidad.</p>
    </div>
    <div style="padding:12pt;border-right:1pt solid #0B0E14;border-top:4pt solid #313F50;">
      <h4>Sobrio</h4>
      <p style="font-size:8.5pt;">Sin superlativos vacíos. La autoridad viene de las certificaciones y la operación, no de adjetivos.</p>
    </div>
    <div style="padding:12pt;border-top:4pt solid #F79204;">
      <h4>Operativo</h4>
      <p style="font-size:8.5pt;">Orientado a resultados: continuidad, seguridad, cumplimiento. Frases cortas, voz activa.</p>
    </div>
  </div>

  <div class="divider"></div>

  <h3>Guía de redacción</h3>
  <table class="spec-table">
    <tr><th>Contexto</th><th class="v-yes">Usar</th><th class="v-no">Evitar</th></tr>
    <tr><td>CTAs / Botones</td><td class="v-yes">Cotizar, Ver áreas, Solicitar visita</td><td class="v-no">Click aquí, ¡Contáctanos!</td></tr>
    <tr><td>Headings</td><td class="v-yes">Mantenimiento industrial de precisión</td><td class="v-no">¡Los mejores de Colombia!</td></tr>
    <tr><td>Descripciones</td><td class="v-yes">Ejecutamos paradas de planta bajo estándar NORSOK</td><td class="v-no">Hacemos todo tipo de mantenimientos</td></tr>
    <tr><td>Cifras</td><td class="v-yes">Solo publicar cifras confirmadas (o mostrar "—")</td><td class="v-no">Inventar telemetría o estadísticas</td></tr>
    <tr><td>Emails</td><td class="v-yes">Estimado señor(a) + apellido; Cordialmente</td><td class="v-no">Hola! · Saludos equipo</td></tr>
  </table>

  <div class="rule" style="margin-top:14pt;">
    <strong>Regla de escritura:</strong> En la primera mención de un documento, "COICEM S.A.S"; después, "COICEM". En texto corrido nunca se escribe en versalitas decorativas. El dominio siempre es <span class="mono">coicem.com</span> (nunca "coisem").
  </div>
</div>


<!-- ═══ PAGE 15 — DON'TS ═══ -->
<div class="page page--white">
  <div class="corner-accent"></div>
  <div class="page-watermark">COICEM Brandbook 2026</div>
  <div class="page-number">15</div>

  <div class="label">13 — Don'ts</div>
  <h2>Usos incorrectos del sistema</h2>

  <p>Los siguientes errores degradan la identidad de COICEM y se evitan en todos los soportes.</p>

  <h3>Logo — Don'ts</h3>
  <div class="dont">No deformar, estirar ni rotar el lockup ni el emblema</div>
  <div class="dont">No aplicar sombras, bisel, relieve o glow sobre el logo</div>
  <div class="dont">No recolorear (ej. wordmark naranja, "SAS" azul, engranaje verde)</div>
  <div class="dont">No encajar el logo en una caja blanca al ir sobre fondo oscuro — el negro es on-brand</div>
  <div class="dont">No separar el emblema del wordmark salvo en los usos de isotipo autorizados</div>

  <div class="divider" style="margin-top:12pt;"></div>

  <h3>Color — Don'ts</h3>
  <div class="dont">No usar el naranja hi-vis como color dominante (&gt;10% visual)</div>
  <div class="dont">No usar colores fuera de la paleta aprobada</div>
  <div class="dont">No usar azul claro #3B8FD9 como texto pequeño sobre blanco (contraste insuficiente)</div>
  <div class="dont">No introducir degradados suaves: el sistema es de bloques planos y bordes duros</div>

  <div class="divider" style="margin-top:12pt;"></div>

  <h3>Tipografía — Don'ts</h3>
  <div class="dont">No usar bordes redondeados ni terminaciones round (rompe el lenguaje brutalist)</div>
  <div class="dont">No usar Comic Sans, Impact, Papyrus ni fuentes decorativas</div>
  <div class="dont">No mezclar más de dos pesos en la misma línea de texto</div>
  <div class="dont">No usar mayúsculas en párrafos largos (&gt;3 palabras) fuera de titulares display</div>

  <div class="divider" style="margin-top:12pt;"></div>

  <h3>Tono — Don'ts</h3>
  <div class="dont">No publicar telemetría o estadísticas sin datos confirmados por el cliente</div>
  <div class="dont">No usar emojis en documentos corporativos, emails formales ni en el sitio</div>
  <div class="dont">No escribir "coisem" — el dominio y la marca son COICEM / coicem.com</div>
</div>


<!-- ═══ PAGE 16 — FIRMA DE CORREO ═══ -->
<div class="page page--white">
  <div class="corner-accent"></div>
  <div class="page-watermark">COICEM Brandbook 2026</div>
  <div class="page-number">16</div>

  <div class="label">14 — Digital</div>
  <h2>Firma de correo electrónico</h2>

  <p>La firma corporativa de COICEM mantiene el sistema brutalist: lockup, barra hi-vis vertical, datos en mono. Se genera desde el panel interno del sitio (Generador de Firma).</p>

  <div style="background:#fff;border:1pt solid #0B0E14;padding:16pt 20pt;margin:12pt 0;max-width:400pt;">
    <div style="display:flex;align-items:flex-start;gap:14pt;">
      <img src="{LOGO_B64}" alt="Logo COICEM firma" style="max-width:120pt;max-height:42pt;object-fit:contain;">
      <div style="flex:1;border-left:4pt solid #F79204;padding-left:14pt;">
        <p class="display" style="font-size:10pt;font-weight:800;color:#0B0E14;margin:0 0 2pt;">[Nombre Completo]</p>
        <p class="mono" style="font-size:8pt;color:#4B6881;margin:0 0 6pt;">[Cargo] · COICEM S.A.S</p>
        <p class="mono" style="font-size:8pt;color:#313F50;margin:0 0 2pt;">[+57 000 000 0000]</p>
        <p class="mono" style="font-size:8pt;margin:0 0 2pt;"><a href="mailto:[correo@coicem.com]" style="color:#025199;text-decoration:none;">[correo@coicem.com]</a></p>
        <p class="mono" style="font-size:8pt;margin:0;"><a href="https://coicem.com" style="color:#F79204;text-decoration:none;">coicem.com</a></p>
      </div>
    </div>
    <div style="height:4pt;background:#F79204;margin-top:12pt;"></div>
    <p class="mono" style="font-size:6.5pt;color:#6b7280;margin-top:6pt;letter-spacing:0.06em;">ISO 9001 · 14001 · 45001 · NORSOK 006 · BUREAU VERITAS</p>
  </div>

  <div class="rule">
    <strong>Cómo usar:</strong> Abrir el panel interno del sitio (botón lateral), clic en "Firma de Correo", completar los campos y copiar el HTML al cliente de correo (Outlook → Firma → HTML). Reemplazar los campos <span class="mono">[ ]</span> con datos reales del colaborador.
  </div>

  <div class="divider" style="margin-top:20pt;"></div>

  <h3>Cierre del brandbook</h3>
  <p>Este manual se consulta antes de cualquier producción de materiales de comunicación para COICEM S.A.S. Para variantes no contempladas, consultar con el equipo de diseño de <strong>YaDev</strong>. Recordar: paleta y wordmark son provisionales v1 hasta recibir el logo vectorial original del cliente.</p>

  <div style="display:flex;align-items:center;justify-content:space-between;margin-top:16pt;padding:12pt 16pt;background:#0B0E14;border-left:6pt solid #F79204;">
    <div>
      <p class="mono" style="font-size:8pt;color:#4B6881;margin:0;letter-spacing:0.1em;text-transform:uppercase;">Diseñado y desarrollado por</p>
      <p class="display" style="font-size:14pt;font-weight:900;color:#F79204;margin:2pt 0 0;letter-spacing:0.04em;">YADEV</p>
    </div>
    <div style="text-align:right;">
      <p class="mono" style="font-size:7pt;color:#4B6881;margin:0;">VERSIÓN 1.0 — 2026</p>
      <p class="mono" style="font-size:7pt;color:#4B6881;margin:0;">COICEM.COM</p>
    </div>
  </div>
</div>

</body>
</html>"""

# ── Write outputs ────────────────────────────────────────────────────────────
for output_path in OUTPUTS:
    output_path = os.path.normpath(output_path)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(HTML)
    size_kb = len(HTML.encode('utf-8')) / 1024
    print(f"Written: {output_path}")
    print(f"  Size: {size_kb:.1f} KB")

print("\nCOICEM brandbook generated successfully (16 pages).")
