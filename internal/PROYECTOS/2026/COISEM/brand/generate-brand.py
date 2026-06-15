"""
generate-brand.py — Entregables de marca de COICEM (autocontenidos, base64).
Genera: brandbook.html (manual de marca) + firma-correo.html.
Usa el logo elegido (logo-coicem-final.png, de Envato coicem-05).
"""
from PIL import Image
import io, base64, os

here = os.path.dirname(os.path.abspath(__file__))
def b64(img):
    buf = io.BytesIO(); img.save(buf, 'PNG', optimize=True)
    return 'data:image/png;base64,' + base64.b64encode(buf.getvalue()).decode()

logo = Image.open(os.path.join(here, 'logo-coicem-final.png')).convert('RGBA')
W, H = logo.size
# lockup ~720px (transparente) para el brandbook
lockup = logo.resize((720, int(H*720/W)), Image.LANCZOS)
# emblema (isotipo) — usar el emblema DEDICADO (envato-emblema.svg limpio), no recortar el lockup
emb = Image.open(os.path.join(here, 'emblema-isotipo.png')).convert('RGBA').resize((340, 340), Image.LANCZOS)
# firma ~360px
firma = logo.resize((360, int(H*360/W)), Image.LANCZOS)

B_LOCKUP, B_EMB, B_FIRMA = b64(lockup), b64(emb), b64(firma)

# ── Paleta y tipografía ──
PAL = [
    ('Azul COICEM', '#025199', 'RGB 2·81·153'),
    ('Naranja hi-vis', '#F79204', 'RGB 247·146·4'),
    ('Grafito / metal', '#313F50', 'RGB 49·63·80'),
    ('Base oscura', '#0B0E14', 'RGB 11·14·20'),
    ('Azul claro', '#3B8FD9', 'texto sobre oscuro'),
    ('Blanco', '#FFFFFF', 'RGB 255·255·255'),
]
CERTS = ['ISO 9001:2015', 'ISO 14001:2015', 'ISO 45001:2018', 'NORSOK 006:2020']

# ════════ BRANDBOOK ════════
swatches = ''.join(f'''
  <div class="sw"><div class="sw__c" style="background:{hexv};{'border:1px solid #ddd' if hexv=='#FFFFFF' else ''}"></div>
  <div class="sw__t"><b>{name}</b>{hexv}<br><span>{rgb}</span></div></div>''' for name, hexv, rgb in PAL)
chips = ''.join(f'<li>{c}</li>' for c in CERTS)

brandbook = f'''<!doctype html><html lang="es-CO"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>COICEM S.A.S — Manual de Marca</title>
<style>
:root{{--blue:#025199;--orange:#F79204;--metal:#313F50;--ink:#0B0E14;--mono:'Courier New',monospace;--sans:Arial,Helvetica,sans-serif}}
*{{box-sizing:border-box}} body{{margin:0;background:#ECEFF2;color:var(--ink);font-family:var(--sans);line-height:1.55}}
.page{{max-width:900px;margin:0 auto;background:#fff}}
header{{background:var(--ink);padding:46px 56px;border-bottom:6px solid var(--orange);text-align:center}}
header img{{max-width:420px;width:80%}} header p{{color:#8A99AB;font-family:var(--mono);font-size:12px;letter-spacing:.18em;text-transform:uppercase;margin:18px 0 0}}
section{{padding:40px 56px;border-bottom:1px solid #E3E7EC}}
h2{{font-family:var(--mono);font-size:13px;letter-spacing:.16em;text-transform:uppercase;color:var(--blue);margin:0 0 24px;border-bottom:1px solid #E3E7EC;padding-bottom:10px}}
.grid2{{display:grid;grid-template-columns:1fr 1fr;gap:24px}} .grid3{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:18px}}
.box{{border:1px solid #E3E7EC;min-height:130px;display:flex;align-items:center;justify-content:center;padding:20px}}
.box img{{max-width:100%}} .box--dark{{background:var(--ink)}} .cap{{font-family:var(--mono);font-size:11px;color:#888;text-transform:uppercase;margin-top:8px;letter-spacing:.06em}}
.sw{{display:flex;gap:12px;align-items:center;margin-bottom:14px}} .sw__c{{width:64px;height:64px;flex-shrink:0}} .sw__t{{font-family:var(--mono);font-size:12px}} .sw__t b{{display:block;font-family:var(--sans);font-size:13px}} .sw__t span{{color:#999}}
ul.cert{{list-style:none;padding:0;display:flex;flex-wrap:wrap;gap:8px}} ul.cert li{{border:1px solid var(--blue);color:var(--blue);font-family:var(--mono);font-size:12px;padding:5px 11px}}
.rule{{font-weight:bold;margin:0 0 8px}} .ok{{color:#1B7A3D}} .no{{color:#B3261E}} ul{{margin:0;padding-left:18px}} li{{margin:5px 0}}
.note{{font-family:var(--mono);font-size:11px;color:#999}}
@media print{{body{{background:#fff}}.page{{max-width:none}}}}
</style></head><body><div class="page">
<header><img src="{B_LOCKUP}" alt="COICEM S.A.S"><p>Manual de Marca · v1 · 2026</p></header>

<section><h2>01 · Logo</h2><div class="grid2">
<div><div class="box"><img src="{B_LOCKUP}"></div><p class="cap">Sobre fondo claro</p></div>
<div><div class="box box--dark"><img src="{B_LOCKUP}"></div><p class="cap">Sobre fondo oscuro</p></div>
</div><p class="note" style="margin-top:18px">Logo vectorial de la marca. No deformar, recolorear ni añadir efectos.</p></section>

<section><h2>02 · Isotipo (símbolo)</h2><div class="grid3">
<div><div class="box"><img src="{B_EMB}" style="max-width:130px"></div><p class="cap">Isotipo</p></div>
<div><div class="box box--dark"><img src="{B_EMB}" style="max-width:130px"></div><p class="cap">Negativo</p></div>
<div><div class="box"><img src="{B_EMB}" style="max-width:64px"></div><p class="cap">Favicon / app</p></div>
</div></section>

<section><h2>03 · Área de protección y tamaño mínimo</h2><div class="grid2">
<div style="border:1px dashed #aaa;padding:36px;display:flex;justify-content:center"><img src="{B_EMB}" style="max-width:120px"></div>
<div><p class="rule">Tamaño mínimo</p><ul>
<li>Isotipo: <b>24&nbsp;px</b> / 8&nbsp;mm (favicon 16&nbsp;px ok).</li>
<li>Logo horizontal: <b>120&nbsp;px</b> / 32&nbsp;mm de ancho (tagline legible).</li>
<li>Bajo ese tamaño, usar solo el isotipo.</li></ul>
<p class="rule" style="margin-top:16px">Área de protección</p><ul><li>Margen libre = altura de un diente del engranaje alrededor.</li></ul></div>
</div></section>

<section><h2>04 · Paleta</h2><div class="grid2">{swatches}</div></section>

<section><h2>05 · Tipografía</h2><div class="grid2">
<div><p style="font-size:32px;font-weight:800;margin:0;letter-spacing:.02em">Archivo Expanded</p><p class="cap">Display / titulares — señalética industrial.</p></div>
<div><p style="font-size:21px;margin:0">IBM Plex Sans · <span style="font-family:var(--mono)">IBM Plex Mono</span></p><p class="cap">Cuerpo (Sans) y datos técnicos (Mono).</p></div>
</div></section>

<section><h2>06 · Certificaciones</h2><ul class="cert">{chips}</ul>
<p class="note" style="margin-top:14px">Certificado por Bureau Veritas (BVQI Colombia Ltda.).</p></section>

<section><h2>07 · Usos</h2><div class="grid2">
<div><p class="rule ok">✓ Correcto</p><ul><li>Respetar el área de protección.</li><li>Versión clara u oscura según el fondo.</li><li>Escalar uniforme, colores de marca exactos.</li></ul></div>
<div><p class="rule no">✗ Incorrecto</p><ul><li>Deformar, rotar o inclinar.</li><li>Recolorear o añadir sombras/efectos.</li><li>Fondos sin contraste suficiente.</li></ul></div>
</div></section>

<section style="border-bottom:0"><p class="note">COICEM S.A.S · Manual de marca preparado por YaDev.</p></section>
</div></body></html>'''

open(os.path.join(here, 'brandbook.html'), 'w', encoding='utf-8').write(brandbook)
print('OK brandbook.html')

# ════════ FIRMA DE CORREO ════════
firma_html = f'''<!doctype html><html lang="es-CO"><head><meta charset="utf-8">
<title>COICEM — Firma de correo</title></head>
<body style="margin:0;background:#f4f4f4;padding:24px;font-family:Arial,sans-serif">
<p style="font-size:13px;color:#666">Copie la tabla de abajo y péguela en su firma de correo (Outlook/Gmail). Reemplace los campos entre [ ].</p>
<table cellpadding="0" cellspacing="0" style="max-width:520px;border-collapse:collapse;background:#fff">
<tr>
<td style="vertical-align:middle;padding:18px 20px;border-right:3px solid #F79204">
<img src="{B_FIRMA}" width="200" style="display:block;width:200px;height:auto" alt="COICEM S.A.S"></td>
<td style="vertical-align:middle;padding:18px 22px">
<div style="font-size:16px;font-weight:bold;color:#025199">[Nombre Apellido]</div>
<div style="font-size:12px;color:#313F50;margin:2px 0 10px">[Cargo] · COICEM S.A.S</div>
<div style="font-size:12px;color:#444;line-height:1.7">
📧 [correo@coicem.com]<br>
📱 [+57 300 000 0000]<br>
🌐 coicem.com</div>
<div style="font-size:10px;color:#999;margin-top:8px;letter-spacing:.04em">ISO 9001 · 14001 · 45001 · NORSOK · Bureau Veritas</div>
</td></tr></table></body></html>'''

open(os.path.join(here, 'firma-correo.html'), 'w', encoding='utf-8').write(firma_html)
print('OK firma-correo.html')

# copiar a public/internal/ para el panel YaDev
dst = os.path.join(here, '..', 'coicem-web', 'public', 'internal')
os.makedirs(dst, exist_ok=True)
import shutil
shutil.copy(os.path.join(here, 'brandbook.html'), os.path.join(dst, 'brandbook.html'))
shutil.copy(os.path.join(here, 'firma-correo.html'), os.path.join(dst, 'firma-correo.html'))
print('OK copiados a public/internal/')
