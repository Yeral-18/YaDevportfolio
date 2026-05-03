#!/usr/bin/env python3
"""
generate-brandbook-v2.py — Luqra Ingeniería y Soluciones S.A.S
Generates expanded brandbook.html (1500+ lines, Multiservicios parity)
Uses logo_firma_b64.txt (56KB) for embedding.
Run: python generate-brandbook-v2.py
Output: ../luqra-web/public/internal/brandbook.html + ./brandbook.html
"""

import os

# ── Base paths ──────────────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
B64_FILE   = os.path.join(SCRIPT_DIR, 'logo_firma_b64.txt')
OUTPUTS = [
    os.path.join(SCRIPT_DIR, 'brandbook.html'),
    os.path.join(SCRIPT_DIR, '..', 'luqra-web', 'public', 'internal', 'brandbook.html'),
]

# ── Read logo b64 ────────────────────────────────────────────────────────────
with open(B64_FILE, 'r') as f:
    LOGO_B64 = f.read().strip()

# Ensure it has the data URI prefix
if not LOGO_B64.startswith('data:'):
    LOGO_B64 = 'data:image/png;base64,' + LOGO_B64

# ── HTML Template ────────────────────────────────────────────────────────────
HTML = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Luqra Ingeniería y Soluciones S.A.S — Brandbook 2026</title>
<style>
/* ═══════════════════════════════════════════════════════════
   LUQRA BRANDBOOK v2 — 2026
   Razón social: Luqra Ingeniería y Soluciones S.A.S
   Rebrand de Multiservicios P&J — 2026-05-03
   ═══════════════════════════════════════════════════════════ */

@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

@page {{ size: A4; margin: 0; }}
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: 'Inter', Arial, sans-serif; color: #1A1A1A; background: #fff; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}

/* ── Page shell ── */
.page {{ width: 210mm; min-height: 297mm; padding: 18mm 20mm; page-break-after: always; position: relative; overflow: hidden; }}
.page:last-child {{ page-break-after: auto; }}
.page--dark {{ background: #060F24; color: white; }}
.page--blue {{ background: #0A2A66; color: white; }}
.page--light {{ background: #F4F6FA; }}

/* ── Typography ── */
h1 {{ font-family: 'Plus Jakarta Sans', sans-serif; font-size: 36pt; font-weight: 800; color: #0A2A66; letter-spacing: -0.04em; margin-bottom: 8pt; line-height: 1.1; }}
h2 {{ font-family: 'Plus Jakarta Sans', sans-serif; font-size: 20pt; font-weight: 800; color: #0A2A66; margin: 20pt 0 10pt; padding-bottom: 8pt; border-bottom: 2px solid #FF6A00; line-height: 1.2; }}
h3 {{ font-family: 'Plus Jakarta Sans', sans-serif; font-size: 11pt; font-weight: 700; color: #1F5FBF; margin: 12pt 0 6pt; text-transform: uppercase; letter-spacing: 0.12em; }}
h4 {{ font-family: 'Plus Jakarta Sans', sans-serif; font-size: 10pt; font-weight: 700; color: #0A2A66; margin: 8pt 0 4pt; }}
p {{ font-size: 9.5pt; line-height: 1.7; margin-bottom: 7pt; color: #374151; }}
.page--dark p, .page--dark h2, .page--dark h3, .page--dark h4 {{ color: rgba(255,255,255,0.85); }}
.page--dark h2 {{ border-bottom-color: rgba(255,106,0,0.5); }}
.page--blue p {{ color: rgba(255,255,255,0.8); }}

/* ── Utility ── */
.label {{ font-family: 'Plus Jakarta Sans', sans-serif; font-size: 7.5pt; font-weight: 700; text-transform: uppercase; letter-spacing: 0.2em; color: #123C8C; margin-bottom: 8pt; display: flex; align-items: center; gap: 6pt; }}
.label::before {{ content: ''; display: block; width: 20pt; height: 2pt; background: #FF6A00; border-radius: 1pt; flex-shrink: 0; }}
.label--white {{ color: rgba(255,255,255,0.6); }}
.label--white::before {{ background: rgba(255,106,0,0.7); }}

.orange {{ color: #FF6A00; }}
.blue {{ color: #123C8C; }}
.white {{ color: white; }}

.accent-bar {{ height: 4pt; background: linear-gradient(90deg, #0A2A66 0%, #1F5FBF 40%, #FF6A00 100%); border-radius: 2pt; margin: 8pt 0; }}
.divider {{ height: 1pt; background: #e8eef8; margin: 12pt 0; }}
.divider--dark {{ background: rgba(255,255,255,0.08); }}

.rule {{ background: #F4F6FA; border-left: 4pt solid #FF6A00; padding: 10pt 14pt; margin: 10pt 0; font-size: 9pt; border-radius: 0 4pt 4pt 0; }}
.rule strong {{ color: #0A2A66; }}
.rule--dark {{ background: rgba(255,106,0,0.06); border-left-color: #FF6A00; }}
.rule--dark strong {{ color: #FFA533; }}

.do {{ background: #E8F5E9; border-left: 3pt solid #4CAF50; padding: 8pt 12pt; border-radius: 0 4pt 4pt 0; margin: 6pt 0; font-size: 8.5pt; }}
.do::before {{ content: 'SI  '; font-weight: 700; color: #2E7D32; }}
.dont {{ background: #FFEBEE; border-left: 3pt solid #F44336; padding: 8pt 12pt; border-radius: 0 4pt 4pt 0; margin: 6pt 0; font-size: 8.5pt; }}
.dont::before {{ content: 'NO  '; font-weight: 700; color: #C62828; }}

/* ── Cover ── */
.cover {{ display: flex; flex-direction: column; justify-content: center; align-items: center; min-height: 261mm; text-align: center; background: linear-gradient(160deg, #060F24 0%, #0A2A66 60%, #123C8C 100%); position: relative; overflow: hidden; }}
.cover-dot-grid {{ position: absolute; inset: 0; background-image: radial-gradient(circle, rgba(31,95,191,0.3) 1px, transparent 1px); background-size: 28pt 28pt; pointer-events: none; }}
.cover-glow {{ position: absolute; top: -6rem; left: 50%; transform: translateX(-50%); width: 400pt; height: 200pt; background: radial-gradient(ellipse at center top, rgba(255,106,0,0.18) 0%, transparent 70%); pointer-events: none; }}
.cover-inner {{ position: relative; z-index: 2; display: flex; flex-direction: column; align-items: center; gap: 24pt; padding: 0 24pt; }}
.cover img {{ max-width: 280pt; filter: brightness(1.1) drop-shadow(0 2pt 12pt rgba(0,0,0,0.4)); }}
.cover-divider {{ width: 60pt; height: 2pt; background: linear-gradient(90deg, #FF6A00, #FFA533); border-radius: 1pt; }}
.cover h1 {{ color: white; font-size: 28pt; letter-spacing: -0.03em; margin: 0; }}
.cover-sub {{ font-family: 'Plus Jakarta Sans', sans-serif; font-size: 10pt; color: rgba(255,255,255,0.5); letter-spacing: 0.15em; text-transform: uppercase; font-weight: 600; }}
.cover-meta {{ font-family: 'JetBrains Mono', monospace; font-size: 8pt; color: rgba(255,255,255,0.25); letter-spacing: 0.1em; margin-top: 20pt; }}
.cover-chip {{ display: inline-flex; align-items: center; gap: 5pt; background: rgba(255,106,0,0.12); border: 1pt solid rgba(255,106,0,0.25); border-radius: 99pt; padding: 4pt 10pt; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 8pt; font-weight: 600; color: #FFA533; letter-spacing: 0.08em; }}
.cover-chips {{ display: flex; gap: 6pt; flex-wrap: wrap; justify-content: center; }}

/* ── Color swatches ── */
.swatch-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 10pt; margin: 12pt 0; }}
.swatch-grid--6 {{ grid-template-columns: repeat(6, 1fr); }}
.swatch {{ border-radius: 6pt; overflow: hidden; box-shadow: 0 1pt 4pt rgba(0,0,0,0.08); }}
.swatch .color {{ height: 70pt; }}
.swatch .label-wrap {{ padding: 7pt 9pt; background: #fff; }}
.swatch .sw-name {{ font-family: 'Plus Jakarta Sans', sans-serif; font-size: 8pt; font-weight: 700; color: #0A2A66; }}
.swatch .sw-hex {{ font-family: 'JetBrains Mono', monospace; font-size: 8pt; color: #6b7280; margin-top: 2pt; }}
.swatch .sw-use {{ font-size: 7.5pt; color: #9ca3af; margin-top: 3pt; line-height: 1.4; }}

/* ── Proportions ── */
.proportions {{ display: flex; height: 36pt; border-radius: 4pt; overflow: hidden; margin: 10pt 0; }}
.prop-blue {{ background: #0A2A66; display: flex; align-items: center; justify-content: center; font-size: 9pt; font-weight: 700; color: white; letter-spacing: 0.05em; }}
.prop-orange {{ background: #FF6A00; display: flex; align-items: center; justify-content: center; font-size: 9pt; font-weight: 700; color: white; letter-spacing: 0.05em; }}

/* ── Typography specimens ── */
.type-specimen {{ margin: 10pt 0; padding: 14pt 16pt; background: #F4F6FA; border-radius: 6pt; border-left: 3pt solid #123C8C; }}
.type-spec-name {{ font-family: 'JetBrains Mono', monospace; font-size: 7.5pt; color: #9ca3af; text-transform: uppercase; letter-spacing: 0.12em; margin-bottom: 6pt; }}
.type-spec-sample {{ line-height: 1.2; }}
.type-weights {{ display: flex; flex-direction: column; gap: 5pt; margin-top: 8pt; }}
.type-weight-row {{ display: flex; align-items: baseline; gap: 12pt; }}
.type-weight-label {{ font-family: 'JetBrains Mono', monospace; font-size: 7.5pt; color: #9ca3af; width: 30pt; flex-shrink: 0; }}

/* ── Logo variants grid ── */
.logo-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 12pt; margin: 12pt 0; }}
.logo-box {{ border-radius: 8pt; padding: 20pt; display: flex; flex-direction: column; align-items: center; gap: 10pt; }}
.logo-box img {{ max-width: 120pt; max-height: 60pt; object-fit: contain; }}
.logo-box-label {{ font-family: 'JetBrains Mono', monospace; font-size: 7.5pt; color: #9ca3af; text-align: center; text-transform: uppercase; letter-spacing: 0.1em; }}
.logo-box--white {{ background: white; border: 1pt solid #e8eef8; }}
.logo-box--dark {{ background: #060F24; }}
.logo-box--blue {{ background: #0A2A66; }}
.logo-box--light {{ background: #F4F6FA; border: 1pt solid #e8eef8; }}

/* ── Spacing scale ── */
.spacing-scale {{ display: flex; flex-direction: column; gap: 6pt; margin: 10pt 0; }}
.spacing-row {{ display: flex; align-items: center; gap: 10pt; }}
.spacing-label {{ font-family: 'JetBrains Mono', monospace; font-size: 7.5pt; color: #9ca3af; width: 28pt; text-align: right; flex-shrink: 0; }}
.spacing-bar {{ background: #0A2A66; border-radius: 2pt; height: 8pt; }}
.spacing-value {{ font-size: 7.5pt; color: #6b7280; }}

/* ── Pattern swatches ── */
.pattern-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 10pt; margin: 10pt 0; }}
.pattern-box {{ height: 80pt; border-radius: 6pt; position: relative; overflow: hidden; border: 1pt solid #e8eef8; display: flex; align-items: flex-end; padding: 8pt; }}
.pattern-label {{ font-family: 'JetBrains Mono', monospace; font-size: 7.5pt; background: rgba(0,0,0,0.6); color: white; padding: 3pt 6pt; border-radius: 3pt; text-transform: uppercase; letter-spacing: 0.08em; }}
.pattern-dots {{ background-image: radial-gradient(circle, rgba(31,95,191,0.45) 1px, transparent 1px); background-size: 12pt 12pt; background-color: #060F24; }}
.pattern-diagonal {{ background: repeating-linear-gradient(45deg, transparent, transparent 10pt, rgba(31,95,191,0.1) 10pt, rgba(31,95,191,0.1) 11pt); background-color: #060F24; }}
.pattern-mesh {{ background: linear-gradient(160deg, #060F24 0%, #0A2A66 60%, #123C8C 100%); }}

/* ── Application mockups ── */
.mockup-row {{ display: grid; grid-template-columns: 1fr 1fr; gap: 12pt; margin: 12pt 0; }}
.mockup-box {{ border-radius: 8pt; overflow: hidden; box-shadow: 0 4pt 16pt rgba(0,0,0,0.1); }}

/* Business card */
.card-front {{ background: #0A2A66; padding: 14pt 16pt; min-height: 60pt; display: flex; flex-direction: column; justify-content: space-between; position: relative; overflow: hidden; }}
.card-front::after {{ content: ''; position: absolute; bottom: 0; left: 0; right: 0; height: 3pt; background: linear-gradient(90deg, #FF6A00, #FFA533); }}
.card-front img {{ max-width: 90pt; max-height: 28pt; object-fit: contain; filter: brightness(1.15); }}
.card-front .card-name {{ font-family: 'Plus Jakarta Sans', sans-serif; font-size: 8pt; font-weight: 700; color: white; margin: 0; }}
.card-front .card-role {{ font-family: 'Plus Jakarta Sans', sans-serif; font-size: 7pt; color: rgba(255,255,255,0.5); margin: 0; }}
.card-back {{ background: #F4F6FA; padding: 14pt 16pt; min-height: 60pt; display: flex; flex-direction: column; justify-content: center; gap: 5pt; border: 1pt solid #e8eef8; }}
.card-back .cb-item {{ display: flex; align-items: center; gap: 6pt; font-size: 7.5pt; color: #4b5563; }}
.card-back .cb-dot {{ width: 4pt; height: 4pt; border-radius: 50%; background: #FF6A00; flex-shrink: 0; }}

/* Signage mockup */
.signage-box {{ background: #0A2A66; padding: 20pt; display: flex; flex-direction: column; align-items: center; gap: 12pt; min-height: 80pt; justify-content: center; border-radius: 8pt; }}
.signage-box img {{ max-width: 130pt; max-height: 50pt; object-fit: contain; filter: brightness(1.15); }}
.signage-sub {{ font-family: 'Plus Jakarta Sans', sans-serif; font-size: 7pt; color: rgba(255,255,255,0.4); letter-spacing: 0.2em; text-transform: uppercase; text-align: center; }}

/* ── Iconography guidelines ── */
.icon-grid {{ display: grid; grid-template-columns: repeat(6, 1fr); gap: 8pt; margin: 10pt 0; }}
.icon-box {{ display: flex; flex-direction: column; align-items: center; gap: 5pt; padding: 8pt; background: #F4F6FA; border-radius: 6pt; }}
.icon-box svg {{ color: #123C8C; }}
.icon-box span {{ font-size: 6.5pt; color: #9ca3af; text-align: center; }}

/* ── Voice & tone table ── */
.voice-table {{ width: 100%; border-collapse: collapse; margin: 10pt 0; font-size: 8.5pt; }}
.voice-table th {{ background: #0A2A66; color: white; padding: 7pt 10pt; text-align: left; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 7.5pt; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; }}
.voice-table td {{ padding: 7pt 10pt; border-bottom: 1pt solid #e8eef8; }}
.voice-table tr:nth-child(even) td {{ background: #F9FAFB; }}
.voice-table .v-yes {{ color: #166534; font-weight: 600; }}
.voice-table .v-no {{ color: #991B1B; font-weight: 600; }}

/* ── Page header/footer watermark ── */
.page-watermark {{ position: absolute; bottom: 10mm; right: 18mm; font-family: 'JetBrains Mono', monospace; font-size: 7pt; color: rgba(10,42,102,0.12); letter-spacing: 0.1em; text-transform: uppercase; }}
.page-watermark--dark {{ color: rgba(255,255,255,0.07); }}
.page-number {{ position: absolute; bottom: 10mm; left: 20mm; font-family: 'JetBrains Mono', monospace; font-size: 7pt; color: rgba(10,42,102,0.3); }}
.page-number--dark {{ color: rgba(255,255,255,0.2); }}

/* Corner accent */
.corner-accent {{ position: absolute; top: 0; right: 0; width: 0; height: 0; border-top: 40pt solid #FF6A00; border-left: 40pt solid transparent; opacity: 0.15; }}
.corner-accent--dark {{ opacity: 0.2; }}

/* ── Index / ToC ── */
.toc {{ display: flex; flex-direction: column; gap: 6pt; margin-top: 16pt; }}
.toc-item {{ display: flex; align-items: baseline; gap: 6pt; padding: 6pt 0; border-bottom: 1pt solid #e8eef8; }}
.toc-num {{ font-family: 'JetBrains Mono', monospace; font-size: 8pt; color: #FF6A00; font-weight: 500; width: 16pt; flex-shrink: 0; }}
.toc-title {{ font-family: 'Plus Jakarta Sans', sans-serif; font-size: 9pt; font-weight: 600; color: #0A2A66; flex: 1; }}
.toc-dots {{ flex: 1; border-bottom: 1pt dotted #e8eef8; margin: 0 4pt; align-self: flex-end; height: 8pt; }}
.toc-pg {{ font-family: 'JetBrains Mono', monospace; font-size: 8pt; color: #9ca3af; }}

/* ── Responsive preview (not print) ── */
@media screen {{
  body {{ background: #e8eef8; padding: 20px; }}
  .page {{ margin: 0 auto 24px; box-shadow: 0 4px 32px rgba(0,0,0,0.12); }}
}}
</style>
</head>
<body>

<!-- ══════════════════════════════════════════════════
     PAGE 1 — COVER
════════════════════════════════════════���═══════════ -->
<div class="page cover">
  <div class="cover-dot-grid"></div>
  <div class="cover-glow"></div>
  <div class="cover-inner">
    <img src="{LOGO_B64}" alt="Luqra Ingeniería y Soluciones S.A.S">
    <div class="cover-divider"></div>
    <div>
      <h1 class="white" style="font-size:22pt;letter-spacing:-0.03em;">Manual de Identidad Visual</h1>
      <p class="cover-sub">Brandbook Corporativo</p>
    </div>
    <div class="cover-chips">
      <span class="cover-chip">Transporte &amp; Logística</span>
      <span class="cover-chip">Construcción Civil</span>
      <span class="cover-chip">Energías Renovables</span>
      <span class="cover-chip">Gestión Ambiental</span>
      <span class="cover-chip">Comercio Internacional</span>
    </div>
    <p class="cover-meta">Luqra Ingeniería y Soluciones S.A.S · Barrancabermeja, Colombia · 2026</p>
  </div>
</div>


<!-- ══════════════════════════════════════════════════
     PAGE 2 — ÍNDICE
════════════════════════════════════════════════════ -->
<div class="page">
  <div class="corner-accent"></div>
  <div class="page-watermark">Luqra Brandbook 2026</div>
  <div class="page-number">02</div>

  <div class="label">Contenido</div>
  <h1>Índice</h1>
  <div class="accent-bar"></div>

  <div class="toc">
    <div class="toc-item">
      <span class="toc-num">01</span>
      <span class="toc-title">Identidad Corporativa</span>
      <span class="toc-dots"></span>
      <span class="toc-pg">03</span>
    </div>
    <div class="toc-item">
      <span class="toc-num">02</span>
      <span class="toc-title">Logo — Versiones y Variantes</span>
      <span class="toc-dots"></span>
      <span class="toc-pg">04</span>
    </div>
    <div class="toc-item">
      <span class="toc-num">03</span>
      <span class="toc-title">Espacio Mínimo y Escala de Tamaños</span>
      <span class="toc-dots"></span>
      <span class="toc-pg">05</span>
    </div>
    <div class="toc-item">
      <span class="toc-num">04</span>
      <span class="toc-title">Paleta de Colores — Regla 80/20</span>
      <span class="toc-dots"></span>
      <span class="toc-pg">06</span>
    </div>
    <div class="toc-item">
      <span class="toc-num">05</span>
      <span class="toc-title">Tipografía</span>
      <span class="toc-dots"></span>
      <span class="toc-pg">07</span>
    </div>
    <div class="toc-item">
      <span class="toc-num">06</span>
      <span class="toc-title">Iconografía</span>
      <span class="toc-dots"></span>
      <span class="toc-pg">08</span>
    </div>
    <div class="toc-item">
      <span class="toc-num">07</span>
      <span class="toc-title">Patrones Gráficos</span>
      <span class="toc-dots"></span>
      <span class="toc-pg">09</span>
    </div>
    <div class="toc-item">
      <span class="toc-num">08</span>
      <span class="toc-title">Aplicaciones — Papelería Corporativa</span>
      <span class="toc-dots"></span>
      <span class="toc-pg">10</span>
    </div>
    <div class="toc-item">
      <span class="toc-num">09</span>
      <span class="toc-title">Aplicaciones — Digital y Señalética</span>
      <span class="toc-dots"></span>
      <span class="toc-pg">11</span>
    </div>
    <div class="toc-item">
      <span class="toc-num">10</span>
      <span class="toc-title">Tono de Comunicación</span>
      <span class="toc-dots"></span>
      <span class="toc-pg">12</span>
    </div>
    <div class="toc-item">
      <span class="toc-num">11</span>
      <span class="toc-title">Usos Incorrectos — Don'ts Visuales</span>
      <span class="toc-dots"></span>
      <span class="toc-pg">13</span>
    </div>
    <div class="toc-item">
      <span class="toc-num">12</span>
      <span class="toc-title">Firma de Correo</span>
      <span class="toc-dots"></span>
      <span class="toc-pg">14</span>
    </div>
  </div>
</div>


<!-- ══════════════════════════════════════════════════
     PAGE 3 — IDENTIDAD CORPORATIVA
════════════════════════════════════════════════════ -->
<div class="page page--dark">
  <div class="corner-accent corner-accent--dark"></div>
  <div class="page-watermark page-watermark--dark">Luqra Brandbook 2026</div>
  <div class="page-number page-number--dark">03</div>

  <div class="label label--white">01 — Identidad</div>
  <h2 style="color:white;border-bottom-color:rgba(255,106,0,0.4);">Quiénes somos</h2>

  <div style="display:grid;grid-template-columns:1fr 1fr;gap:20pt;margin-top:12pt;">
    <div>
      <h3 style="color:#FFA533;">Razón Social</h3>
      <p style="font-size:13pt;font-family:'Plus Jakarta Sans',sans-serif;font-weight:800;color:white;letter-spacing:-0.02em;line-height:1.2;">Luqra Ingeniería<br>y Soluciones S.A.S</p>
      <div class="divider divider--dark"></div>
      <h3 style="color:#FFA533;">Origen</h3>
      <p>Luqra es el rebrand de <strong style="color:#FFA533;">Multiservicios P&amp;J</strong>, anunciado en mayo 2026. Misma empresa, mismo equipo operativo — nueva razón social, nueva identidad visual y scope corporativo ampliado.</p>
    </div>
    <div>
      <h3 style="color:#FFA533;">Misión</h3>
      <p>Prestar servicios de ingeniería integral con calidad técnica, cumplimiento normativo y responsabilidad ambiental, contribuyendo al desarrollo productivo de Colombia.</p>
      <h3 style="color:#FFA533;">Visión</h3>
      <p>Ser reconocidos como el aliado estratégico de referencia para proyectos de ingeniería integral en la región Caribe y Santanderes al 2030. <em style="color:rgba(255,255,255,0.4);font-size:8pt;">TODO: confirmar año meta con cliente.</em></p>
      <h3 style="color:#FFA533;">Valores</h3>
      <p>Integridad · Innovación técnica · Responsabilidad ambiental · Seguridad laboral · Vocación de servicio</p>
    </div>
  </div>

  <div class="divider divider--dark" style="margin-top:16pt;"></div>

  <h3 style="color:#FFA533;">Cinco ejes operativos</h3>
  <div style="display:grid;grid-template-columns:repeat(5,1fr);gap:8pt;margin-top:8pt;">
    <div style="background:rgba(18,60,140,0.35);border:1pt solid rgba(31,95,191,0.25);border-radius:6pt;padding:10pt 8pt;text-align:center;">
      <p style="font-size:8pt;font-weight:700;color:#FFA533;margin-bottom:4pt;text-transform:uppercase;letter-spacing:0.06em;">01</p>
      <p style="font-size:8.5pt;color:white;font-weight:600;line-height:1.3;margin:0;">Transporte y Logística</p>
    </div>
    <div style="background:rgba(18,60,140,0.35);border:1pt solid rgba(31,95,191,0.25);border-radius:6pt;padding:10pt 8pt;text-align:center;">
      <p style="font-size:8pt;font-weight:700;color:#FFA533;margin-bottom:4pt;text-transform:uppercase;letter-spacing:0.06em;">02</p>
      <p style="font-size:8.5pt;color:white;font-weight:600;line-height:1.3;margin:0;">Construcción Civil</p>
    </div>
    <div style="background:rgba(18,60,140,0.35);border:1pt solid rgba(31,95,191,0.25);border-radius:6pt;padding:10pt 8pt;text-align:center;">
      <p style="font-size:8pt;font-weight:700;color:#FF6A00;margin-bottom:4pt;text-transform:uppercase;letter-spacing:0.06em;">03</p>
      <p style="font-size:8.5pt;color:white;font-weight:600;line-height:1.3;margin:0;">Energías Renovables</p>
    </div>
    <div style="background:rgba(18,60,140,0.35);border:1pt solid rgba(31,95,191,0.25);border-radius:6pt;padding:10pt 8pt;text-align:center;">
      <p style="font-size:8pt;font-weight:700;color:#FFA533;margin-bottom:4pt;text-transform:uppercase;letter-spacing:0.06em;">04</p>
      <p style="font-size:8.5pt;color:white;font-weight:600;line-height:1.3;margin:0;">Gestión Ambiental</p>
    </div>
    <div style="background:rgba(18,60,140,0.35);border:1pt solid rgba(31,95,191,0.25);border-radius:6pt;padding:10pt 8pt;text-align:center;">
      <p style="font-size:8pt;font-weight:700;color:#FFA533;margin-bottom:4pt;text-transform:uppercase;letter-spacing:0.06em;">05</p>
      <p style="font-size:8.5pt;color:white;font-weight:600;line-height:1.3;margin:0;">Comercio Internacional</p>
    </div>
  </div>
</div>


<!-- ══════════════════════════════════════════════════
     PAGE 4 — LOGO VARIANTES
════════════════════════════════════════════════════ -->
<div class="page">
  <div class="corner-accent"></div>
  <div class="page-watermark">Luqra Brandbook 2026</div>
  <div class="page-number">04</div>

  <div class="label">02 — Logo</div>
  <h2>Versiones y variantes del logo</h2>

  <p>El logo de Luqra combina la tipografía de marca en azul corporativo con la <strong>Q naranja</strong> como elemento diferenciador, las huellas de neumático (herencia transporte) y el triángulo naranja en la R (energía / montaña). Se debe usar en sus versiones autorizadas.</p>

  <div class="logo-grid">
    <div class="logo-box logo-box--white">
      <img src="{LOGO_B64}" alt="Logo Luqra — fondo blanco">
      <span class="logo-box-label">Versión principal<br>Fondo blanco</span>
    </div>
    <div class="logo-box logo-box--dark">
      <img src="{LOGO_B64}" alt="Logo Luqra — fondo oscuro" style="filter:brightness(1.2);">
      <span class="logo-box-label" style="color:rgba(255,255,255,0.45);">Fondo oscuro<br>Filter brightness 1.2</span>
    </div>
    <div class="logo-box logo-box--blue">
      <img src="{LOGO_B64}" alt="Logo Luqra — fondo azul" style="filter:brightness(1.15);">
      <span class="logo-box-label" style="color:rgba(255,255,255,0.45);">Fondo azul corporativo<br>Filter brightness 1.15</span>
    </div>
    <div class="logo-box logo-box--light">
      <img src="{LOGO_B64}" alt="Logo Luqra — fondo gris claro">
      <span class="logo-box-label">Fondo gris corporativo<br>#F4F6FA</span>
    </div>
  </div>

  <div class="rule">
    <strong>Isotipo:</strong> La Q naranja y las huellas de neumático pueden usarse de forma aislada como avatar/ícono de app/perfil únicamente cuando el nombre "Luqra" sea reconocible por contexto. Nunca como reemplazo del logo completo en papelería formal.
  </div>
</div>


<!-- ══════════════════════════════════════════════════
     PAGE 5 — ESPACIO MÍNIMO Y ESCALA
════════════════════════════════════════════════════ -->
<div class="page page--light">
  <div class="corner-accent"></div>
  <div class="page-watermark">Luqra Brandbook 2026</div>
  <div class="page-number">05</div>

  <div class="label">03 — Logo</div>
  <h2>Espacio mínimo y escala de tamaños</h2>

  <!-- Clear space demo -->
  <h3>Espacio de protección</h3>
  <p>Se debe respetar un espacio libre alrededor del logo equivalente a la altura de la "L" mayúscula del logo (unidad X). Esto garantiza legibilidad y presencia visual en cualquier soporte.</p>

  <div style="display:flex;align-items:center;justify-content:center;padding:24pt;margin:12pt 0;border:2pt dashed rgba(255,106,0,0.3);border-radius:8pt;background:white;position:relative;">
    <div style="position:absolute;top:4pt;left:4pt;font-family:'JetBrains Mono',monospace;font-size:7pt;color:rgba(255,106,0,0.6);">X = altura de mayúscula</div>
    <img src="{LOGO_B64}" alt="Logo con espacio de protección" style="max-width:160pt;max-height:60pt;object-fit:contain;">
  </div>

  <h3>Escala de tamaños autorizados</h3>
  <table class="voice-table" style="margin-top:8pt;">
    <tr>
      <th>Soporte</th>
      <th>Ancho mínimo</th>
      <th>Resolución</th>
      <th>Formato</th>
    </tr>
    <tr>
      <td>Digital — web/app</td>
      <td>120px</td>
      <td>72–96 dpi</td>
      <td>PNG / SVG</td>
    </tr>
    <tr>
      <td>Navbar web</td>
      <td>200px</td>
      <td>96+ dpi (2x)</td>
      <td>PNG transparente</td>
    </tr>
    <tr>
      <td>Firma de correo</td>
      <td>160px</td>
      <td>72 dpi</td>
      <td>PNG (base64 embed)</td>
    </tr>
    <tr>
      <td>Papelería impresa</td>
      <td>35mm</td>
      <td>300 dpi</td>
      <td>PNG / PDF vectorizado</td>
    </tr>
    <tr>
      <td>Vehículos (vinil)</td>
      <td>200mm</td>
      <td>150 dpi a tamaño final</td>
      <td>PDF vectorizado</td>
    </tr>
    <tr>
      <td>Señalética exterior</td>
      <td>300mm</td>
      <td>72 dpi a tamaño final</td>
      <td>PDF vectorizado</td>
    </tr>
  </table>

  <div class="rule" style="margin-top:16pt;">
    <strong>Nota:</strong> El logo NUNCA debe usarse a menos de 35mm de ancho en impresión o menos de 120px en digital. Por debajo de estas medidas, usar solo el isotipo (Q naranja).
  </div>
</div>


<!-- ══════════════════════════════════════════════════
     PAGE 6 — PALETA DE COLORES
════════════════════════════════════════════════════ -->
<div class="page">
  <div class="corner-accent"></div>
  <div class="page-watermark">Luqra Brandbook 2026</div>
  <div class="page-number">06</div>

  <div class="label">04 — Color</div>
  <h2>Paleta de colores — Regla 80/20</h2>

  <!-- Proportions bar -->
  <div class="proportions" style="margin:14pt 0;">
    <div class="prop-blue" style="flex:80;">80% — Azul corporativo</div>
    <div class="prop-orange" style="flex:20;">20% — Naranja acento</div>
  </div>

  <div class="rule" style="margin-bottom:14pt;">
    <strong>Regla inviolable:</strong> El 80% de cualquier pieza de comunicación debe ser azul corporativo o blanco. El naranja es acento — NO puede dominar. Si el naranja supera el 20% visual, la pieza debe rediseñarse.
  </div>

  <h3>Azul corporativo (80%)</h3>
  <div class="swatch-grid">
    <div class="swatch">
      <div class="color" style="background:#0A2A66;"></div>
      <div class="label-wrap">
        <div class="sw-name">Blue Base</div>
        <div class="sw-hex">#0A2A66</div>
        <div class="sw-use">Headings, fondos principales, navbar</div>
      </div>
    </div>
    <div class="swatch">
      <div class="color" style="background:#123C8C;"></div>
      <div class="label-wrap">
        <div class="sw-name">Blue Mid</div>
        <div class="sw-hex">#123C8C</div>
        <div class="sw-use">Gradientes, textos secundarios, botones secundarios</div>
      </div>
    </div>
    <div class="swatch">
      <div class="color" style="background:#1F5FBF;"></div>
      <div class="label-wrap">
        <div class="sw-name">Blue Light</div>
        <div class="sw-hex">#1F5FBF</div>
        <div class="sw-use">Brillos, acentos azul, dot-grid backgrounds</div>
      </div>
    </div>
  </div>

  <h3>Naranja acento (20%)</h3>
  <div class="swatch-grid">
    <div class="swatch">
      <div class="color" style="background:#FF6A00;"></div>
      <div class="label-wrap">
        <div class="sw-name">Orange Base</div>
        <div class="sw-hex">#FF6A00</div>
        <div class="sw-use">CTAs principales, la Q del logo, líneas acento</div>
      </div>
    </div>
    <div class="swatch">
      <div class="color" style="background:#FF8C1A;"></div>
      <div class="label-wrap">
        <div class="sw-name">Orange Mid</div>
        <div class="sw-hex">#FF8C1A</div>
        <div class="sw-use">Hover states, gradientes naranja</div>
      </div>
    </div>
    <div class="swatch">
      <div class="color" style="background:#FFA533;"></div>
      <div class="label-wrap">
        <div class="sw-name">Orange Light</div>
        <div class="sw-hex">#FFA533</div>
        <div class="sw-use">Brillos, accent text gradient, iconos sobre oscuro</div>
      </div>
    </div>
  </div>

  <h3>Complementarios</h3>
  <div class="swatch-grid swatch-grid--6" style="margin-top:8pt;">
    <div class="swatch">
      <div class="color" style="background:#FFFFFF;border:1pt solid #e8eef8;"></div>
      <div class="label-wrap"><div class="sw-name">White</div><div class="sw-hex">#FFFFFF</div><div class="sw-use">Fondos, texto inverso</div></div>
    </div>
    <div class="swatch">
      <div class="color" style="background:#F4F6FA;"></div>
      <div class="label-wrap"><div class="sw-name">Light</div><div class="sw-hex">#F4F6FA</div><div class="sw-use">Fondos alternos</div></div>
    </div>
    <div class="swatch">
      <div class="color" style="background:#e8eef8;"></div>
      <div class="label-wrap"><div class="sw-name">Blue-50</div><div class="sw-hex">#e8eef8</div><div class="sw-use">Borders, fondos pillar</div></div>
    </div>
    <div class="swatch">
      <div class="color" style="background:#1A1A1A;"></div>
      <div class="label-wrap"><div class="sw-name">Dark</div><div class="sw-hex">#1A1A1A</div><div class="sw-use">Texto general</div></div>
    </div>
    <div class="swatch">
      <div class="color" style="background:#060F24;"></div>
      <div class="label-wrap"><div class="sw-name">Navy Deep</div><div class="sw-hex">#060F24</div><div class="sw-use">Fondos hero, footer, servicios</div></div>
    </div>
    <div class="swatch">
      <div class="color" style="background:#6b7280;"></div>
      <div class="label-wrap"><div class="sw-name">Gray-500</div><div class="sw-hex">#6b7280</div><div class="sw-use">Texto terciario, meta</div></div>
    </div>
  </div>
</div>


<!-- ══════════════════════════════════════════════════
     PAGE 7 — TIPOGRAFÍA
════════════════════════════════════════════════════ -->
<div class="page">
  <div class="corner-accent"></div>
  <div class="page-watermark">Luqra Brandbook 2026</div>
  <div class="page-number">07</div>

  <div class="label">05 — Tipografía</div>
  <h2>Sistema tipográfico</h2>

  <p>Luqra usa tres familias complementarias que equilibran seriedad corporativa, legibilidad digital y precisión técnica.</p>

  <!-- Plus Jakarta Sans -->
  <div class="type-specimen">
    <div class="type-spec-name">Display / Headings — Plus Jakarta Sans</div>
    <div class="type-spec-sample">
      <p style="font-family:'Plus Jakarta Sans',sans-serif;font-size:28pt;font-weight:800;color:#0A2A66;line-height:1.1;letter-spacing:-0.04em;margin:0;">Luqra Ingeniería</p>
      <p style="font-family:'Plus Jakarta Sans',sans-serif;font-size:16pt;font-weight:600;color:#123C8C;margin:4pt 0 0;">Soluciones de Ingeniería Integral para Colombia</p>
    </div>
    <div class="type-weights">
      <div class="type-weight-row">
        <span class="type-weight-label">300</span>
        <span style="font-family:'Plus Jakarta Sans',sans-serif;font-weight:300;font-size:10pt;color:#374151;">Texto ligero — secciones descriptivas</span>
      </div>
      <div class="type-weight-row">
        <span class="type-weight-label">500</span>
        <span style="font-family:'Plus Jakarta Sans',sans-serif;font-weight:500;font-size:10pt;color:#374151;">Texto medio — etiquetas, navegación</span>
      </div>
      <div class="type-weight-row">
        <span class="type-weight-label">600</span>
        <span style="font-family:'Plus Jakarta Sans',sans-serif;font-weight:600;font-size:10pt;color:#374151;">Semibold — textos de interfaz, botones secundarios</span>
      </div>
      <div class="type-weight-row">
        <span class="type-weight-label">700</span>
        <span style="font-family:'Plus Jakarta Sans',sans-serif;font-weight:700;font-size:10pt;color:#0A2A66;">Bold — títulos de sección h2/h3</span>
      </div>
      <div class="type-weight-row">
        <span class="type-weight-label">800</span>
        <span style="font-family:'Plus Jakarta Sans',sans-serif;font-weight:800;font-size:10pt;color:#0A2A66;">Extrabold — hero headings, títulos principales</span>
      </div>
    </div>
  </div>

  <!-- Inter -->
  <div class="type-specimen">
    <div class="type-spec-name">Body / Texto corrido — Inter</div>
    <div class="type-spec-sample">
      <p style="font-family:'Inter',sans-serif;font-size:10pt;font-weight:400;color:#374151;line-height:1.7;margin:0;">La prestación de servicios de transporte terrestre automotor de carga (local, regional, nacional e internacional) forma parte de las actividades principales de Luqra Ingeniería y Soluciones S.A.S.</p>
    </div>
    <div class="type-weights">
      <div class="type-weight-row">
        <span class="type-weight-label">400</span>
        <span style="font-family:'Inter',sans-serif;font-weight:400;font-size:10pt;color:#374151;">Regular — párrafos, descripciones, body copy</span>
      </div>
      <div class="type-weight-row">
        <span class="type-weight-label">500</span>
        <span style="font-family:'Inter',sans-serif;font-weight:500;font-size:10pt;color:#374151;">Medium — labels de formulario, meta information</span>
      </div>
      <div class="type-weight-row">
        <span class="type-weight-label">600</span>
        <span style="font-family:'Inter',sans-serif;font-weight:600;font-size:#374151;font-size:10pt;">Semibold — énfasis dentro de párrafos</span>
      </div>
    </div>
  </div>

  <!-- JetBrains Mono -->
  <div class="type-specimen">
    <div class="type-spec-name">Monospace / Datos técnicos — JetBrains Mono</div>
    <div class="type-spec-sample">
      <p style="font-family:'JetBrains Mono',monospace;font-size:10pt;font-weight:400;color:#374151;margin:0;">PRJ-2026-001 · #FF6A00 · luqra.com.co · ISO 9001:2015</p>
    </div>
    <div class="type-weights">
      <div class="type-weight-row">
        <span class="type-weight-label">400</span>
        <span style="font-family:'JetBrains Mono',monospace;font-weight:400;font-size:10pt;color:#374151;">Regular — IDs de proyecto, códigos técnicos, fechas</span>
      </div>
      <div class="type-weight-row">
        <span class="type-weight-label">500</span>
        <span style="font-family:'JetBrains Mono',monospace;font-weight:500;font-size:10pt;color:#374151;">Medium — números de seguimiento, datos de tabla</span>
      </div>
    </div>
  </div>
</div>


<!-- ══════════════════════════════════════════════════
     PAGE 8 — ICONOGRAFÍA
════════════════════════════════════════════════════ -->
<div class="page page--light">
  <div class="corner-accent"></div>
  <div class="page-watermark">Luqra Brandbook 2026</div>
  <div class="page-number">08</div>

  <div class="label">06 — Iconografía</div>
  <h2>Lineamientos de iconografía</h2>

  <p>Luqra utiliza íconos de estilo <strong>outlined (contorno)</strong> consistentes con el estilo visual moderno y técnico de la marca. Nunca mezclar estilos.</p>

  <h3>Estilo autorizado — Outlined, 1.5px stroke</h3>
  <div class="icon-grid">
    <div class="icon-box">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
        <path d="M1 3h15v13H1z"/><path d="M16 8h4l3 3v5h-7V8z"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/>
      </svg>
      <span>Transporte</span>
    </div>
    <div class="icon-box">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
        <rect x="4" y="2" width="16" height="20" rx="2"/><path d="M9 22v-4h6v4"/><path d="M8 6h.01M16 6h.01M12 6h.01M12 10h.01M12 14h.01"/>
      </svg>
      <span>Construcción</span>
    </div>
    <div class="icon-box">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
        <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>
      </svg>
      <span>Energía</span>
    </div>
    <div class="icon-box">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
        <path d="M11 20A7 7 0 0 1 9.8 6.9C15.5 4.9 20 .5 20 .5s-4.4 4.5-2.4 10.2A7 7 0 0 1 11 20z"/>
      </svg>
      <span>Ambiental</span>
    </div>
    <div class="icon-box">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
      </svg>
      <span>Comercio</span>
    </div>
    <div class="icon-box">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
        <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 11 14 15 10"/>
      </svg>
      <span>Calidad</span>
    </div>
  </div>

  <div class="divider"></div>

  <h3>Reglas de uso</h3>
  <table class="voice-table">
    <tr>
      <th>Atributo</th>
      <th>Valor correcto</th>
      <th>Prohibido</th>
    </tr>
    <tr>
      <td>Estilo</td>
      <td class="v-yes">Outlined (contorno)</td>
      <td class="v-no">Filled, duotone</td>
    </tr>
    <tr>
      <td>Peso del trazo</td>
      <td class="v-yes">1.5px – 2px</td>
      <td class="v-no">Menos de 1px, más de 2.5px</td>
    </tr>
    <tr>
      <td>Terminaciones</td>
      <td class="v-yes">Round (redondeadas)</td>
      <td class="v-no">Square, butt</td>
    </tr>
    <tr>
      <td>Color</td>
      <td class="v-yes">#123C8C sobre fondo claro; #FF8C1A sobre fondo oscuro</td>
      <td class="v-no">Mezcla de colores dentro de un mismo ícono</td>
    </tr>
    <tr>
      <td>Biblioteca</td>
      <td class="v-yes">Lucide Icons (recomendado)</td>
      <td class="v-no">Material Design filled, Font Awesome solid</td>
    </tr>
  </table>

  <div class="rule" style="margin-top:12pt;">
    <strong>Tamaño mínimo:</strong> 16px / 12pt en digital. En impresión, no menos de 8mm para garantizar legibilidad.
  </div>
</div>


<!-- ══════════════════════════════════════════════════
     PAGE 9 — PATRONES GRÁFICOS
════════════════════════════════════════════════════ -->
<div class="page">
  <div class="corner-accent"></div>
  <div class="page-watermark">Luqra Brandbook 2026</div>
  <div class="page-number">09</div>

  <div class="label">07 — Patrones</div>
  <h2>Patrones gráficos y texturas</h2>

  <p>Luqra cuenta con tres patrones de fondo que refuerzan el posicionamiento técnico-ingenieril. Se usan exclusivamente como elementos secundarios de fondo, nunca sobre texto importante.</p>

  <div class="pattern-grid">
    <div class="pattern-box pattern-dots">
      <span class="pattern-label">Blueprint Dot-Grid</span>
    </div>
    <div class="pattern-box pattern-diagonal">
      <span class="pattern-label">Diagonal Lines</span>
    </div>
    <div class="pattern-box pattern-mesh">
      <span class="pattern-label">Gradient Mesh</span>
    </div>
  </div>

  <h3>Cortes diagonales — Transición de sección</h3>
  <p>Luqra usa cortes diagonales afilados (clip-path) como divisores entre secciones de color diferente. Este es el elemento de diferenciación visual principal respecto a otros proyectos YaDev (que usan waves).</p>

  <div style="height:60pt;position:relative;overflow:hidden;margin:12pt 0;border-radius:6pt;">
    <div style="position:absolute;inset:0;background:linear-gradient(160deg,#060F24,#0A2A66);"></div>
    <div style="position:absolute;bottom:0;left:0;right:0;height:40pt;background:#F4F6FA;clip-path:polygon(0 100%, 100% 0%, 100% 100%);"></div>
    <div style="position:absolute;top:8pt;left:12pt;font-family:'JetBrains Mono',monospace;font-size:7pt;color:rgba(255,255,255,0.5);">Sección oscura → Sección clara</div>
  </div>

  <h3>Reglas de uso de patrones</h3>
  <div class="do">Usar dot-grid como capa de baja opacidad (máx. 0.35) sobre fondos navy</div>
  <div class="do">Usar gradient mesh como fondo de secciones hero con radial orange glow en el 20%</div>
  <div class="do">Usar diagonal cuts para transiciones entre secciones de diferente valor</div>
  <div class="dont">Usar patrones sobre texto de lectura prolongada</div>
  <div class="dont">Usar diagonal cuts sobre otras diagonales en la misma transición</div>
  <div class="dont">Saturar con múltiples patrones en la misma página</div>

  <h3 style="margin-top:14pt;">Cursor signature — Triángulo Luqra</h3>
  <p>En la versión web, el cursor nativo se reemplaza por dos triángulos concéntricos: outer azul (#0A2A66) sin relleno, inner naranja (#FF6A00) sólido. Al pasar sobre elementos interactivos, el inner rota 45° y el outer escala a 22px. En mobile (pointer: coarse) se desactiva.</p>

  <div style="display:inline-flex;align-items:center;justify-content:center;width:60pt;height:60pt;background:#F4F6FA;border-radius:50%;position:relative;">
    <svg width="22" height="22" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg" style="position:absolute;">
      <polygon points="10,1 19,18 1,18" fill="none" stroke="#0A2A66" stroke-width="1.5" stroke-linejoin="round"/>
    </svg>
    <svg width="9" height="9" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
      <polygon points="10,1 19,18 1,18" fill="#FF6A00"/>
    </svg>
  </div>
  <p style="display:inline-block;vertical-align:middle;margin-left:12pt;font-size:8.5pt;color:#6b7280;">Estado base — desktop pointer:fine únicamente</p>
</div>


<!-- ══════════════════════════════════════════════════
     PAGE 10 — APLICACIONES PAPELERÍA
════════════════════════════════════════════════════ -->
<div class="page">
  <div class="corner-accent"></div>
  <div class="page-watermark">Luqra Brandbook 2026</div>
  <div class="page-number">10</div>

  <div class="label">08 — Aplicaciones</div>
  <h2>Papelería corporativa</h2>

  <h3>Tarjeta de presentación — 90 × 55mm (Colombia)</h3>
  <p>Frente: fondo azul corporativo, logo blanco, nombre/cargo. Reverso: fondo blanco/gris, datos de contacto.</p>

  <div class="mockup-row" style="max-width:300pt;">
    <!-- Frente -->
    <div class="card-front">
      <img src="{LOGO_B64}" alt="Logo Luqra">
      <div>
        <p class="card-name">TODO: Nombre del colaborador</p>
        <p class="card-role">TODO: Cargo</p>
      </div>
    </div>
    <!-- Reverso -->
    <div class="card-back">
      <div class="cb-item"><div class="cb-dot"></div>TODO: Teléfono · Ext. XXX</div>
      <div class="cb-item"><div class="cb-dot"></div>TODO@luqra.com.co</div>
      <div class="cb-item"><div class="cb-dot"></div>TODO: Dirección · Barrancabermeja</div>
      <div class="cb-item"><div class="cb-dot"></div>luqra.com.co</div>
    </div>
  </div>

  <div style="margin-top:4pt;padding:6pt 10pt;background:#fff3e6;border-radius:4pt;font-size:7.5pt;color:#FF6A00;border:1pt solid rgba(255,106,0,0.2);">
    TODO: Confirmar nombre, cargo, teléfono, dirección y correo del colaborador con el cliente antes de imprimir.
  </div>

  <div class="divider" style="margin-top:16pt;"></div>

  <h3>Hoja membretada A4</h3>
  <p>Cabecera azul corporativo con logo, pie de página con datos de contacto, área de escritura blanca con watermark sutil (logo al 6% de opacidad centrado).</p>

  <div style="display:flex;gap:10pt;margin:10pt 0;">
    <div style="flex:1;background:white;border:1pt solid #e8eef8;border-radius:6pt;overflow:hidden;min-height:120pt;box-shadow:0 2pt 8pt rgba(0,0,0,0.06);">
      <!-- Header -->
      <div style="background:#0A2A66;padding:10pt 14pt;display:flex;align-items:center;justify-content:space-between;">
        <img src="{LOGO_B64}" alt="Logo Luqra" style="max-width:90pt;max-height:28pt;object-fit:contain;filter:brightness(1.15);">
        <div style="text-align:right;">
          <p style="font-family:'JetBrains Mono',monospace;font-size:6.5pt;color:rgba(255,255,255,0.45);margin:0;">NIT: TODO</p>
          <p style="font-family:'JetBrains Mono',monospace;font-size:6.5pt;color:rgba(255,255,255,0.45);margin:0;">Barrancabermeja, Santander</p>
        </div>
      </div>
      <!-- Orange accent bar -->
      <div style="height:3pt;background:linear-gradient(90deg,#FF6A00,#FFA533);"></div>
      <!-- Body area -->
      <div style="padding:10pt 14pt;min-height:60pt;position:relative;">
        <p style="font-size:7pt;color:#e8eef8;text-align:center;position:absolute;inset:0;display:flex;align-items:center;justify-content:center;pointer-events:none;font-family:'Plus Jakarta Sans',sans-serif;font-weight:800;font-size:22pt;opacity:0.04;color:#0A2A66;">LUQRA</p>
        <p style="font-size:7.5pt;color:#9ca3af;font-style:italic;">Área de contenido — texto del documento aquí</p>
      </div>
      <!-- Footer -->
      <div style="background:#F4F6FA;padding:6pt 14pt;border-top:1pt solid #e8eef8;">
        <p style="font-size:6.5pt;color:#9ca3af;margin:0;text-align:center;">Luqra Ingeniería y Soluciones S.A.S · TODO: Dirección · TODO: Tel · TODO@luqra.com.co · luqra.com.co</p>
      </div>
    </div>
  </div>
</div>


<!-- ══════════════════════════════════════════════════
     PAGE 11 — APLICACIONES DIGITAL / SEÑALÉTICA
════════════════════════════════════════════════════ -->
<div class="page page--light">
  <div class="corner-accent"></div>
  <div class="page-watermark">Luqra Brandbook 2026</div>
  <div class="page-number">11</div>

  <div class="label">09 — Aplicaciones</div>
  <h2>Digital y señalética</h2>

  <h3>Señalética exterior — fachada de oficina</h3>
  <div class="signage-box" style="max-width:280pt;margin:10pt auto;">
    <img src="{LOGO_B64}" alt="Logo Luqra señalética" style="max-width:160pt;max-height:60pt;object-fit:contain;filter:brightness(1.15);">
    <div class="signage-sub">Luqra Ingeniería y Soluciones S.A.S</div>
  </div>
  <p style="font-size:8pt;color:#9ca3af;text-align:center;margin-top:4pt;">Simulación — fondo azul navy con logo en blanco/naranja. Material sugerido: ACM o lona retroiluminada.</p>

  <div class="divider"></div>

  <h3>Aplicación en vehículo</h3>
  <div style="background:#1A1A1A;border-radius:8pt;padding:16pt 20pt;margin:10pt 0;display:flex;align-items:center;gap:16pt;">
    <div style="flex:1;">
      <div style="background:#0A2A66;border-radius:4pt;padding:10pt;display:inline-block;">
        <img src="{LOGO_B64}" alt="Logo Luqra vehículo" style="max-width:100pt;max-height:36pt;object-fit:contain;filter:brightness(1.15);">
      </div>
    </div>
    <div style="flex:1;">
      <p style="font-family:'Plus Jakarta Sans',sans-serif;font-size:8pt;color:rgba(255,255,255,0.5);line-height:1.5;">Logo sobre panel azul lateral. Ancho mínimo en vehículo: 200mm. Incluir número de teléfono y web debajo del logo en Inter 500.</p>
    </div>
  </div>

  <div class="divider"></div>

  <h3>OG Image — redes sociales (1200 × 630px)</h3>
  <div style="background:linear-gradient(160deg,#060F24,#0A2A66);border-radius:6pt;padding:20pt;display:flex;align-items:center;justify-content:center;min-height:60pt;margin:10pt 0;">
    <img src="{LOGO_B64}" alt="OG Image Luqra" style="max-width:180pt;max-height:60pt;object-fit:contain;filter:brightness(1.15);">
  </div>
  <p style="font-size:8pt;color:#9ca3af;">Logo centrado sobre fondo gradient mesh. Fondo: #060F24 → #0A2A66. Formatos: JPEG 95% quality para WhatsApp/Facebook; PNG para LinkedIn.</p>

  <div class="rule" style="margin-top:16pt;">
    <strong>Uniforme bordado:</strong> Logo bordado en hilo azul #0A2A66 sobre uniforme gris claro o azul corporativo. La Q naranja se borda en hilo naranja #FF6A00. Tamaño mínimo de bordado: 50mm ancho.
    <br><em style="color:#9ca3af;font-size:8pt;display:block;margin-top:4pt;">TODO: Confirmar colores de uniforme preferidos con cliente.</em>
  </div>
</div>


<!-- ══════════════════════════════════════════════════
     PAGE 12 — TONO DE COMUNICACIÓN
════════════════════════════════════════════════════ -->
<div class="page">
  <div class="corner-accent"></div>
  <div class="page-watermark">Luqra Brandbook 2026</div>
  <div class="page-number">12</div>

  <div class="label">10 — Comunicación</div>
  <h2>Tono de comunicación</h2>

  <p>Luqra se dirige a contratantes del sector público y privado, gerentes de proyectos, interventores y tomadores de decisión técnica. El tono debe ser <strong>institucional, técnico y claro</strong>, nunca informal ni sobreentusiasta.</p>

  <h3>Personalidad de marca</h3>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10pt;margin:10pt 0;">
    <div style="background:#F4F6FA;border-radius:6pt;padding:12pt;border-top:3pt solid #0A2A66;">
      <h4>Institucional</h4>
      <p style="font-size:8.5pt;">Habla como una empresa seria, con experiencia en contratos públicos. Usa términos técnicos correctos del sector.</p>
    </div>
    <div style="background:#F4F6FA;border-radius:6pt;padding:12pt;border-top:3pt solid #123C8C;">
      <h4>Técnico</h4>
      <p style="font-size:8.5pt;">Preciso y específico. Menciona certificaciones, normativas RETIE/RETILAP, marcos legales de contratación pública cuando aplique.</p>
    </div>
    <div style="background:#F4F6FA;border-radius:6pt;padding:12pt;border-top:3pt solid #FF6A00;">
      <h4>Claro</h4>
      <p style="font-size:8.5pt;">Sin ambigüedades. Frases cortas. El potencial cliente debe entender exactamente qué hace Luqra y por qué debería contratar.</p>
    </div>
  </div>

  <div class="divider"></div>

  <h3>Guía de redacción</h3>
  <table class="voice-table">
    <tr>
      <th>Contexto</th>
      <th class="v-yes">Usar</th>
      <th class="v-no">Evitar</th>
    </tr>
    <tr>
      <td>CTAs / Botones</td>
      <td class="v-yes">Cotizar, Solicitar, Enviar propuesta</td>
      <td class="v-no">Click aquí, ¡Contáctanos!, Llena el formulario</td>
    </tr>
    <tr>
      <td>Headings</td>
      <td class="v-yes">Ingeniería integral para proyectos de alto impacto</td>
      <td class="v-no">¡Somos los mejores! · La empresa #1 de Colombia</td>
    </tr>
    <tr>
      <td>Descripciones</td>
      <td class="v-yes">Ejecutamos proyectos de construcción civil bajo los estándares NSR-10</td>
      <td class="v-no">Hacemos todo tipo de construcciones, muy buenos</td>
    </tr>
    <tr>
      <td>Emails</td>
      <td class="v-yes">Estimado señor(a) + apellido; Cordialmente</td>
      <td class="v-no">Hola! · Saludos equipo · Ciao</td>
    </tr>
    <tr>
      <td>Cifras</td>
      <td class="v-yes">Solo publicar cifras confirmadas con el cliente</td>
      <td class="v-no">Inventar o estimar estadísticas sin datos reales</td>
    </tr>
  </table>

  <div class="rule" style="margin-top:14pt;">
    <strong>Regla de escritura:</strong> Siempre escribir "Luqra Ingeniería y Soluciones S.A.S" en la primera mención de un documento. En menciones posteriores: "Luqra" (sin mayúscula adicional). Nunca "LUQRA" en texto corrido.
  </div>
</div>


<!-- ══════════════════════════════════════════════════
     PAGE 13 — DON'TS VISUALES
════════════════════════════════════════════════════ -->
<div class="page">
  <div class="corner-accent"></div>
  <div class="page-watermark">Luqra Brandbook 2026</div>
  <div class="page-number">13</div>

  <div class="label">11 — Don'ts</div>
  <h2>Usos incorrectos del sistema visual</h2>

  <p>Los siguientes errores degradan la identidad de Luqra y deben evitarse en todos los soportes de comunicación.</p>

  <h3>Logo — Don'ts</h3>
  <div class="dont">No deformar o estirar el logo en ningún eje</div>
  <div class="dont">No aplicar efectos de sombra, bisel, relieve o glow sobre el logo</div>
  <div class="dont">No cambiar los colores corporativos del logo (ej. Q en azul, texto en naranja)</div>
  <div class="dont">No colocar el logo sobre fondos con poco contraste (grises medios, amarillo claro)</div>
  <div class="dont">No rotar ni inclinar el logo</div>
  <div class="dont">No usar versiones JPG con fondo blanco sobre fondos de color (siempre PNG transparente)</div>

  <div class="divider" style="margin-top:14pt;"></div>

  <h3>Color — Don'ts</h3>
  <div class="dont">No usar el naranja como color dominante en más del 20% de la pieza</div>
  <div class="dont">No usar colores fuera de la paleta aprobada sin autorización</div>
  <div class="dont">No combinar azul claro (#1F5FBF) con naranja base (#FF6A00) en textos pequeños — contraste insuficiente</div>
  <div class="dont">No usar gradientes inventados que no estén en las guías (solo los tres gradientes aprobados)</div>

  <div class="divider" style="margin-top:14pt;"></div>

  <h3>Tipografía — Don'ts</h3>
  <div class="dont">No usar más de dos pesos tipográficos en la misma línea de texto</div>
  <div class="dont">No usar Comic Sans, Impact, Papyrus ni fuentes decorativas en ningún soporte corporativo</div>
  <div class="dont">No usar letra capitalizada (mayúsculas) en párrafos de más de 3 palabras</div>
  <div class="dont">No aplicar letter-spacing negativo en texto bajo 12pt</div>

  <div class="divider" style="margin-top:14pt;"></div>

  <h3>Tono — Don'ts</h3>
  <div class="dont">No publicar estadísticas sin datos confirmados por el cliente</div>
  <div class="dont">No usar emojis en documentos corporativos, emails formales ni en el sitio web</div>
  <div class="dont">No usar lenguaje informativo que mezcle tuteo y usted en el mismo texto</div>
</div>


<!-- ══════════════════════════════════════════════════
     PAGE 14 — FIRMA DE CORREO
════════════════════════════════════════════════════ -->
<div class="page page--light">
  <div class="corner-accent"></div>
  <div class="page-watermark">Luqra Brandbook 2026</div>
  <div class="page-number">14</div>

  <div class="label">12 — Digital</div>
  <h2>Firma de correo electrónico</h2>

  <p>La firma corporativa de Luqra mantiene el sistema visual 80/20. Se genera automáticamente desde el Generador de Firma incluido en el panel interno del sitio web.</p>

  <!-- Firma preview -->
  <div style="background:white;border:1pt solid #e8eef8;border-radius:8pt;padding:16pt 20pt;margin:12pt 0;max-width:400pt;box-shadow:0 2pt 8pt rgba(0,0,0,0.06);">
    <div style="display:flex;align-items:flex-start;gap:14pt;">
      <img src="{LOGO_B64}" alt="Logo Luqra firma" style="max-width:110pt;max-height:40pt;object-fit:contain;">
      <div style="flex:1;border-left:1pt solid #e8eef8;padding-left:14pt;">
        <p style="font-family:'Plus Jakarta Sans',sans-serif;font-size:10pt;font-weight:700;color:#0A2A66;margin:0 0 2pt;">TODO: Nombre completo</p>
        <p style="font-family:'Plus Jakarta Sans',sans-serif;font-size:8pt;color:#6b7280;margin:0 0 6pt;">TODO: Cargo | Luqra Ingeniería y Soluciones S.A.S</p>
        <p style="font-size:8pt;color:#6b7280;margin:0 0 2pt;">TODO: +57 300 000 0000</p>
        <p style="font-size:8pt;margin:0 0 2pt;"><a href="mailto:TODO@luqra.com.co" style="color:#123C8C;text-decoration:none;">TODO@luqra.com.co</a></p>
        <p style="font-size:8pt;margin:0;"><a href="https://luqra.com.co" style="color:#FF6A00;text-decoration:none;">luqra.com.co</a></p>
      </div>
    </div>
    <div style="height:2pt;background:linear-gradient(90deg,#FF6A00,#FFA533,#0A2A66);border-radius:1pt;margin-top:12pt;"></div>
  </div>

  <div class="rule">
    <strong>Cómo usar:</strong> Abrir el panel interno del sitio web (botón lateral izquierdo azul), hacer clic en "Firma de Correo", completar los campos y copiar el HTML generado al cliente de correo (Outlook → Firma → HTML).
  </div>

  <div class="divider" style="margin-top:20pt;"></div>

  <h3>Cierre del brandbook</h3>
  <p>Este manual debe consultarse antes de cualquier producción de materiales de comunicación para Luqra Ingeniería y Soluciones S.A.S. Para variantes no contempladas, consultar con el equipo de diseño de <strong>YA Dev</strong>.</p>

  <div style="display:flex;align-items:center;justify-content:space-between;margin-top:16pt;padding:10pt 14pt;background:#0A2A66;border-radius:8pt;">
    <div>
      <p style="font-family:'Plus Jakarta Sans',sans-serif;font-size:9pt;font-weight:700;color:white;margin:0;">Diseñado y desarrollado por</p>
      <p style="font-family:'Plus Jakarta Sans',sans-serif;font-size:11pt;font-weight:800;color:#FFA533;margin:0;letter-spacing:-0.02em;">YA Dev</p>
    </div>
    <div style="text-align:right;">
      <p style="font-family:'JetBrains Mono',monospace;font-size:7pt;color:rgba(255,255,255,0.35);margin:0;">Versión 2.0 — Mayo 2026</p>
      <p style="font-family:'JetBrains Mono',monospace;font-size:7pt;color:rgba(255,255,255,0.35);margin:0;">luqra.com.co</p>
    </div>
  </div>
</div>

</body>
</html>"""

# ── Write outputs ──────────────────────────────────────────────���─────────────
for output_path in OUTPUTS:
    output_path = os.path.normpath(output_path)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(HTML)
    lines = HTML.count('\\n') + 1
    size_kb = len(HTML.encode('utf-8')) / 1024
    print(f"Written: {output_path}")
    print(f"  Approx lines: {lines}")
    print(f"  Size: {size_kb:.1f} KB")

print("\nBrandbook v2 generated successfully!")
