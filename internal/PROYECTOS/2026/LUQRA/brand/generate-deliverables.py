"""Genera firma-correo.html + brandbook.html con logo b64 embebido."""
import os
with open('logo_b64.txt') as f:
    LOGO_B64 = f.read().strip()

# Email signature
sig = '''<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>Firma Luqra</title></head>
<body style="margin:0;padding:0;font-family:Arial,Helvetica,sans-serif;">
<table cellpadding="0" cellspacing="0" border="0" style="font-family:Arial,Helvetica,sans-serif;color:#1A1A1A;font-size:13px;line-height:1.5;">
  <tr>
    <td style="padding-right:18px;border-right:2px solid #FF6A00;vertical-align:top;">
      <img src="''' + LOGO_B64 + '''" alt="Luqra" width="160" style="display:block;">
    </td>
    <td style="padding-left:18px;vertical-align:top;">
      <div style="font-size:15px;font-weight:bold;color:#0A2A66;letter-spacing:0.5px;">[NOMBRE COMPLETO]</div>
      <div style="font-size:12px;color:#1F5FBF;margin-top:2px;">[CARGO]</div>
      <div style="margin-top:10px;font-size:12px;color:#1A1A1A;">
        <div><span style="color:#FF6A00;font-weight:bold;">M.</span> [+57 ___ ___ ____]</div>
        <div><span style="color:#FF6A00;font-weight:bold;">E.</span> [correo@luqra.com.co]</div>
        <div><span style="color:#FF6A00;font-weight:bold;">W.</span> luqra.com.co</div>
      </div>
      <div style="margin-top:10px;font-size:11px;color:#666;font-style:italic;">
        Luqra Ingenieria y Soluciones S.A.S. &middot; Transporte &middot; Construccion &middot; Energia &middot; Ambiental
      </div>
    </td>
  </tr>
</table>
</body></html>'''
with open('firma-correo.html','w',encoding='utf-8') as f:
    f.write(sig)

# Brandbook (A4 print-ready, autocontenido con logo b64)
bb = '''<!DOCTYPE html>
<html lang="es"><head>
<meta charset="utf-8">
<title>Luqra - Brandbook</title>
<style>
@page { size: A4; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Inter', Arial, sans-serif; color: #1A1A1A; background: #fff; }
.page { width: 210mm; min-height: 297mm; padding: 25mm; page-break-after: always; position: relative; }
.page:last-child { page-break-after: auto; }
h1 { font-size: 36pt; font-weight: 800; color: #0A2A66; letter-spacing: -0.5pt; margin-bottom: 8pt; }
h2 { font-size: 18pt; font-weight: 700; color: #0A2A66; margin: 20pt 0 10pt; padding-bottom: 6pt; border-bottom: 2px solid #FF6A00; }
h3 { font-size: 12pt; font-weight: 700; color: #1F5FBF; margin: 12pt 0 6pt; text-transform: uppercase; letter-spacing: 1pt; }
p { font-size: 10pt; line-height: 1.6; margin-bottom: 8pt; }
.cover { display: flex; flex-direction: column; justify-content: center; align-items: center; min-height: 247mm; text-align: center; }
.cover img { max-width: 70%; margin-bottom: 30pt; }
.cover .meta { color: #666; font-size: 10pt; margin-top: 20pt; }
.swatch-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12pt; margin: 12pt 0; }
.swatch { border-radius: 6pt; overflow: hidden; box-shadow: 0 1pt 3pt rgba(0,0,0,0.08); }
.swatch .color { height: 80pt; }
.swatch .label { padding: 8pt 10pt; background: #fff; }
.swatch .name { font-size: 9pt; font-weight: 700; color: #0A2A66; }
.swatch .hex { font-family: 'JetBrains Mono', monospace; font-size: 9pt; color: #666; margin-top: 2pt; }
.swatch .use { font-size: 8pt; color: #888; margin-top: 4pt; }
.rule { background: #F5F7FA; border-left: 4px solid #FF6A00; padding: 12pt 16pt; margin: 12pt 0; font-size: 10pt; }
.rule strong { color: #0A2A66; }
.dont, .do { padding: 10pt 14pt; border-radius: 6pt; margin: 8pt 0; font-size: 9pt; }
.do { background: #E8F5E9; border-left: 3px solid #4CAF50; }
.dont { background: #FFEBEE; border-left: 3px solid #F44336; }
.proportions { display: flex; height: 40pt; border-radius: 4pt; overflow: hidden; margin: 8pt 0; }
.prop-blue { background: #0A2A66; flex: 80; display: flex; align-items: center; justify-content: center; color: #fff; font-size: 10pt; font-weight: 700; }
.prop-orange { background: #FF6A00; flex: 20; display: flex; align-items: center; justify-content: center; color: #fff; font-size: 10pt; font-weight: 700; }
ul { margin: 8pt 0 8pt 20pt; font-size: 10pt; line-height: 1.7; }
.logo-display { background: #fff; border: 1pt solid #eee; padding: 30pt; text-align: center; border-radius: 6pt; margin: 12pt 0; }
.logo-display img { max-width: 80%; }
.footer { position: absolute; bottom: 12mm; left: 25mm; right: 25mm; display: flex; justify-content: space-between; font-size: 8pt; color: #999; padding-top: 6pt; border-top: 1px solid #eee; }
</style></head>
<body>

<section class="page cover">
  <img src="''' + LOGO_B64 + '''" alt="Luqra">
  <h1 style="margin-top:20pt;">Brandbook</h1>
  <p style="font-size:12pt;color:#1F5FBF;margin-top:8pt;">Manual de identidad visual</p>
  <div class="meta">Luqra Ingenieria y Soluciones S.A.S.<br>Version 1.0 &middot; 2026</div>
</section>

<section class="page">
  <h1>Identidad</h1>
  <h2>Quienes somos</h2>
  <p><strong>Luqra Ingenieria y Soluciones S.A.S.</strong> es una empresa colombiana de ingenieria integral que opera en cinco ejes: transporte y logistica, construccion de obra civil y arquitectonica, energias renovables, gestion ambiental, y comercio internacional de equipos e insumos.</p>
  <p>Trabajamos con entidades publicas y privadas, participando en licitaciones, consorcios y uniones temporales para ejecutar proyectos que combinan rigor ingenieril con vision sostenible.</p>
  <h2>Personalidad de marca</h2>
  <ul>
    <li><strong>Seria.</strong> Comunicamos con tono institucional, tecnico, sin frivolidades.</li>
    <li><strong>Confiable.</strong> Identidad visual transmite estabilidad y experiencia.</li>
    <li><strong>Dinamica.</strong> Acento naranja senala movimiento y modernidad sin restar formalidad.</li>
    <li><strong>Integral.</strong> Cinco ejes operativos coordinados, no servicios sueltos.</li>
  </ul>
  <div class="footer"><span>Luqra &middot; Brandbook</span><span>02</span></div>
</section>

<section class="page">
  <h1>Logo</h1>
  <div class="logo-display"><img src="''' + LOGO_B64 + '''" alt="Luqra logo principal"></div>
  <p>El logo principal combina <strong>LUQRA</strong> en azul corporativo con la letra <strong>Q</strong> en naranja, integrando huellas de neumatico bajo U y Q (transporte) y un triangulo naranja en R (energia/montana). El subtitulo "INGENIERIA &amp; SOLUCIONES S.A.S." va flanqueado por dos barras naranjas.</p>
  <h2>Espacio minimo</h2>
  <p>Mantener un margen libre alrededor del logo equivalente a la altura de la letra L. No invadir ese espacio con texto u otros elementos.</p>
  <h2>Tamano minimo</h2>
  <ul>
    <li>Digital: 120 px de ancho.</li>
    <li>Impreso: 25 mm de ancho.</li>
  </ul>
  <div class="footer"><span>Luqra &middot; Brandbook</span><span>03</span></div>
</section>

<section class="page">
  <h1>Paleta</h1>
  <h2>Azul corporativo - 80%</h2>
  <p style="margin-bottom:14pt;">Seriedad, ingenieria, confianza. Color dominante. Para textos, headings, fondos corporativos y papeleria.</p>
  <div class="swatch-grid">
    <div class="swatch"><div class="color" style="background:#0A2A66;"></div><div class="label"><div class="name">Azul base</div><div class="hex">#0A2A66</div><div class="use">Texto LUQRA, headings</div></div></div>
    <div class="swatch"><div class="color" style="background:#123C8C;"></div><div class="label"><div class="name">Azul medio</div><div class="hex">#123C8C</div><div class="use">Transiciones, gradientes</div></div></div>
    <div class="swatch"><div class="color" style="background:#1F5FBF;"></div><div class="label"><div class="name">Azul claro</div><div class="hex">#1F5FBF</div><div class="use">Detalles, links, brillos</div></div></div>
  </div>
  <h2>Naranja - 20%</h2>
  <p style="margin-bottom:14pt;">Impacto y recordacion. Es acento, NUNCA dominante. Para letra Q, CTAs, iconos destacados.</p>
  <div class="swatch-grid">
    <div class="swatch"><div class="color" style="background:#FF6A00;"></div><div class="label"><div class="name">Naranja base</div><div class="hex">#FF6A00</div><div class="use">Letra Q, CTAs principales</div></div></div>
    <div class="swatch"><div class="color" style="background:#FF8C1A;"></div><div class="label"><div class="name">Naranja medio</div><div class="hex">#FF8C1A</div><div class="use">Transiciones, gradientes</div></div></div>
    <div class="swatch"><div class="color" style="background:#FFA533;"></div><div class="label"><div class="name">Naranja claro</div><div class="hex">#FFA533</div><div class="use">Brillos, hover, destacados</div></div></div>
  </div>
  <h2>Complementarios</h2>
  <div class="swatch-grid" style="grid-template-columns: repeat(2, 1fr);">
    <div class="swatch"><div class="color" style="background:#FFFFFF;border:1pt solid #eee;"></div><div class="label"><div class="name">Blanco</div><div class="hex">#FFFFFF</div><div class="use">Fondos principales</div></div></div>
    <div class="swatch"><div class="color" style="background:#1A1A1A;"></div><div class="label"><div class="name">Gris oscuro</div><div class="hex">#1A1A1A</div><div class="use">Texto secundario, muted</div></div></div>
  </div>
  <div class="footer"><span>Luqra &middot; Brandbook</span><span>04</span></div>
</section>

<section class="page">
  <h1>Proporciones</h1>
  <h2>Regla 80/20</h2>
  <div class="proportions"><div class="prop-blue">80% Azul</div><div class="prop-orange">20% Naranja</div></div>
  <div class="rule"><strong>Inviolable:</strong> el naranja NO debe dominar en ninguna pieza. Es el acento que hace memorable la marca. Si una pieza se ve mas naranja que azul, redisenar.</div>
  <h2>Que SI hacer</h2>
  <div class="do"><strong>Si:</strong> usar el naranja para CTAs principales, iconos destacados, la letra Q en titulares.</div>
  <div class="do"><strong>Si:</strong> mantener fondos blancos o azul oscuro como base principal.</div>
  <div class="do"><strong>Si:</strong> respetar el espacio libre alrededor del logo.</div>
  <div class="do"><strong>Si:</strong> usar la familia de azules en gradientes para fondos hero o transiciones.</div>
  <h2>Que NO hacer</h2>
  <div class="dont"><strong>No:</strong> aplicar fondos naranjas extensos. Rompe el 80/20.</div>
  <div class="dont"><strong>No:</strong> alterar los colores del logo (no cambiar el azul ni el naranja por otros tonos).</div>
  <div class="dont"><strong>No:</strong> ubicar el logo sobre fondos de bajo contraste sin overlay.</div>
  <div class="dont"><strong>No:</strong> deformar, rotar o aplicar efectos pesados al logo.</div>
  <div class="dont"><strong>No:</strong> reemplazar la tipografia del logo por otra fuente.</div>
  <div class="footer"><span>Luqra &middot; Brandbook</span><span>05</span></div>
</section>

<section class="page">
  <h1>Tipografia</h1>
  <p>La tipografia oficial se confirmara en la siguiente fase. Tres combinaciones candidatas, todas con <strong>Inter</strong> para texto corrido:</p>
  <h2>Opcion A - Plus Jakarta Sans + Inter <span style="color:#FF6A00;font-size:10pt;">(recomendada)</span></h2>
  <p>Heredada del sitio anterior. Mantiene continuidad operativa sin sacrificar modernidad. Excelente legibilidad en mobile.</p>
  <h2>Opcion B - Sora + Inter</h2>
  <p>Mas geometrica, vibe tech. Buen match con la identidad ingenieril.</p>
  <h2>Opcion C - Manrope + Inter</h2>
  <p>Humanista y calida. Suaviza el azul institucional sin perder seriedad.</p>
  <h3>Body en todos los casos</h3>
  <p>Inter para todo el cuerpo. Pesos 400/500/600. Para numeros tecnicos, codigos de seguimiento y referencias se usa <span style="font-family:'JetBrains Mono',monospace;background:#F5F7FA;padding:1pt 4pt;border-radius:3pt;">JetBrains Mono</span>.</p>
  <div class="footer"><span>Luqra &middot; Brandbook</span><span>06</span></div>
</section>

<section class="page">
  <h1>Areas operativas</h1>
  <p>Cinco ejes coordinados. La comunicacion visual debe reflejar la integralidad - no son servicios sueltos.</p>
  <h3>1. Transporte y logistica</h3>
  <p>Carga terrestre local, regional, nacional e internacional. Operacion logistica integral: almacenamiento, distribucion, manejo de mercancias, alquiler de equipos y maquinaria.</p>
  <h3>2. Construccion</h3>
  <p>Obra civil y arquitectonica. Mantenimiento, interventoria y consultoria. Infraestructura y proyectos inmobiliarios.</p>
  <h3>3. Energia</h3>
  <p>Sistemas electricos, energias renovables, redes de distribucion.</p>
  <h3>4. Gestion ambiental</h3>
  <p>Saneamiento basico, manejo de residuos, recuperacion ambiental, tratamiento de suelos y aguas.</p>
  <h3>5. Comercio internacional</h3>
  <p>Suministro, importacion, exportacion y comercializacion de materiales, equipos e insumos.</p>
  <h2 style="margin-top:24pt;">Tipos de cliente</h2>
  <ul>
    <li>Entidades publicas (licitaciones, contratacion estatal).</li>
    <li>Empresas privadas (proyectos contratados directamente).</li>
    <li>Consorcios y uniones temporales (alianzas estrategicas).</li>
  </ul>
  <div class="footer"><span>Luqra &middot; Brandbook</span><span>07</span></div>
</section>

</body></html>'''
with open('brandbook.html','w',encoding='utf-8') as f:
    f.write(bb)

print('firma-correo.html:', os.path.getsize('firma-correo.html')//1024, 'KB')
print('brandbook.html:', os.path.getsize('brandbook.html')//1024, 'KB')
