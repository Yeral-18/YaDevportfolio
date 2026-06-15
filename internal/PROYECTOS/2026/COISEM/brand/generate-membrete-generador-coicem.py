"""Genera hoja-membretada-generador.html para COICEM S.A.S.

Form interactivo con preview A4 en vivo + descarga .doc (Word editable) + imprimir/PDF.
Estetica brutalist industrial (azul #025199 + naranja hi-vis #F79204, labels mono).
Logo desde logo-firma-b64.txt (ya con prefijo data:). Contacto PENDIENTE: placeholders.
"""
import os, shutil

here = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(here, 'logo-firma-b64.txt')) as f:
    LOGO_B64 = f.read().strip()  # ya trae prefijo data:image/png;base64,

html = '''<!DOCTYPE html>
<html lang="es-CO">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Generador de Membrete &mdash; COICEM S.A.S</title>
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800;900&family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet" />
<script src="https://cdn.tailwindcss.com"></script>
<style>
* { box-sizing: border-box; }
body { font-family: 'IBM Plex Sans', sans-serif; }
.disp { font-family: 'Archivo', sans-serif; }
.mono { font-family: 'IBM Plex Mono', monospace; }

.field-group label { display:block; font-family:'IBM Plex Mono',monospace; font-size:10px; font-weight:500; letter-spacing:0.12em; text-transform:uppercase; color:#6B7785; margin-bottom:5px; }
.field-group input, .field-group textarea {
  width:100%; padding:9px 12px; border:1.5px solid #D5DBE2; border-radius:0;
  font-size:14px; color:#0B0E14; font-family:inherit; outline:none; background:#fff;
  transition: border-color 0.15s, box-shadow 0.15s;
}
.field-group textarea { min-height:120px; resize:vertical; line-height:1.5; }
.field-group input:focus, .field-group textarea:focus {
  border-color:#025199; box-shadow:0 0 0 3px rgba(2,81,153,0.12);
}

.btn { display:inline-flex; align-items:center; gap:7px; padding:10px 18px; border-radius:0; font-size:13px; font-weight:600; cursor:pointer; border:none; font-family:inherit; transition:all 0.15s; }
.btn-primary { background:#025199; color:#fff; }
.btn-primary:hover { background:#0B0E14; }
.btn-secondary { background:#F79204; color:#0B0E14; }
.btn-secondary:hover { background:#d97e02; }
.btn-ghost { background:#EEF1F4; color:#313F50; border:1.5px solid #D5DBE2; }
.btn-ghost:hover { background:#E0E5EA; }

#toast { position:fixed; bottom:28px; left:50%; transform:translateX(-50%) translateY(20px); background:#0B0E14; color:#fff; padding:10px 22px; border-radius:0; font-size:13px; font-weight:500; opacity:0; transition:opacity 0.25s, transform 0.25s; pointer-events:none; z-index:9999; white-space:nowrap; border-left:4px solid #F79204; }
#toast.show { opacity:1; transform:translateX(-50%) translateY(0); }

/* ----- Preview membrete (mismo styling brutalist que hoja-membretada.html) ----- */
.preview-shell { background:#f4f5f7; border:1px solid #D5DBE2; overflow:hidden; }
.preview-page { width:100%; aspect-ratio:1/1.414; background:white; padding:18px 22px 0 26px; position:relative; box-shadow:0 2px 8px rgba(0,0,0,0.08); display:flex; flex-direction:column; }
.preview-page::before { content:''; position:absolute; top:0; left:0; width:6px; height:100%; background:#F79204; }

.mb-header { display:flex; align-items:flex-start; justify-content:space-between; padding:2px 0 10px; gap:14px; }
.mb-header img { max-height:56px; width:auto; }
.mb-header-info { text-align:right; }
.mb-header-info strong { color:#025199; font-family:'Archivo',sans-serif; font-size:12px; display:block; font-weight:800; letter-spacing:0.4px; text-transform:uppercase; line-height:1; }
.mb-header-info span { font-family:'IBM Plex Mono',monospace; font-size:7px; color:#313F50; letter-spacing:1.4px; text-transform:uppercase; display:block; margin-top:3px; }

.mb-rule { display:flex; height:3px; margin:0 0 8px; }
.mb-rule .a { background:#0B0E14; flex:62; } .mb-rule .b { background:#313F50; flex:22; } .mb-rule .c { background:#F79204; flex:16; }

.mb-meta { font-family:'IBM Plex Mono',monospace; font-size:7.5px; color:#6B7785; letter-spacing:0.8px; text-transform:uppercase; border:1px solid #E3E7EC; display:inline-block; padding:3px 7px; margin:2px 0 8px; }

.mb-dest { padding:4px 0; font-size:8.5px; font-family:'IBM Plex Sans',sans-serif; color:#0B0E14; line-height:1.5; }
.mb-dest strong { color:#025199; }
.mb-asunto { padding:4px 0 8px; font-size:8.5px; font-family:'IBM Plex Sans',sans-serif; color:#0B0E14; }
.mb-asunto strong { color:#025199; }

.mb-body { flex:1; padding:4px 0; font-family:'IBM Plex Sans',sans-serif; font-size:8.5px; color:#0B0E14; line-height:1.7; white-space:pre-wrap; }

.mb-footer { background:#0B0E14; color:#C7D0DA; margin:8px -22px 0 -26px; padding:10px 22px 10px 26px; position:relative; }
.mb-footer::before { content:''; position:absolute; top:0; left:0; width:100%; height:3px; background:linear-gradient(90deg,#F79204 0 16%,#313F50 16% 100%); }
.mb-footer-grid { display:grid; grid-template-columns:1.2fr 1fr 1fr 1.1fr; gap:8px; }
.mb-footer-grid strong { color:#F79204; display:block; font-family:'IBM Plex Mono',monospace; font-size:6.5px; margin-bottom:3px; letter-spacing:1.4px; text-transform:uppercase; }
.mb-footer-grid div { font-size:7px; line-height:1.5; color:#E2E8EF; }
.mb-certs { margin-top:7px; padding-top:6px; border-top:1px solid #1E2733; font-family:'IBM Plex Mono',monospace; font-size:6px; color:#9aa3ad; letter-spacing:0.6px; }
.mb-certs b { color:#F79204; font-weight:500; }

.mb-watermark { position:absolute; top:46%; left:50%; transform:translate(-50%,-50%) rotate(-22deg); opacity:0.04; font-family:'Archivo',sans-serif; font-weight:900; font-size:84px; color:#025199; pointer-events:none; user-select:none; letter-spacing:4px; }
</style>
</head>
<body class="min-h-screen py-10 px-4" style="background:#E4E8EC;">

<div class="max-w-6xl mx-auto mb-6">
  <div class="flex items-center gap-3">
    <div class="w-9 h-9 flex items-center justify-center" style="background:#0B0E14;border-left:4px solid #F79204;">
      <svg width="18" height="18" fill="none" viewBox="0 0 24 24"><path d="M19 21H5a2 2 0 01-2-2V5a2 2 0 012-2h11l5 5v11a2 2 0 01-2 2z M17 3v5h5 M9 13h6 M9 17h6 M9 9h2" stroke="#F79204" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
    </div>
    <div>
      <h1 class="disp text-lg font-extrabold text-slate-900 leading-tight uppercase tracking-wide">Generador de Hoja Membretada</h1>
      <p class="mono text-xs text-slate-500">COICEM S.A.S &mdash; Descarga en Word o imprime PDF</p>
    </div>
  </div>
</div>

<div class="max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-6 items-start">

  <!-- LEFT: Form -->
  <div class="bg-white shadow-sm border border-slate-200 p-6" style="border-top:4px solid #025199;">
    <h2 class="mono text-xs font-semibold text-slate-400 uppercase tracking-widest mb-5">Datos del documento</h2>

    <div class="space-y-4">
      <div class="grid grid-cols-2 gap-3">
        <div class="field-group">
          <label for="inp-ciudad">Ciudad</label>
          <input type="text" id="inp-ciudad" placeholder="[Ciudad]" value="" />
        </div>
        <div class="field-group">
          <label for="inp-fecha">Fecha</label>
          <input type="date" id="inp-fecha" />
        </div>
      </div>

      <div class="field-group">
        <label for="inp-destinatario">Destinatario</label>
        <input type="text" id="inp-destinatario" placeholder="Nombre / Empresa destinataria" value="Senor(a) / Empresa" />
      </div>
      <div class="field-group">
        <label for="inp-cargo">Cargo</label>
        <input type="text" id="inp-cargo" placeholder="Cargo" value="" />
      </div>
      <div class="field-group">
        <label for="inp-direccion">Direccion</label>
        <input type="text" id="inp-direccion" placeholder="Ciudad" value="Ciudad" />
      </div>
      <div class="field-group">
        <label for="inp-asunto">Asunto</label>
        <input type="text" id="inp-asunto" placeholder="Asunto del documento" value="" />
      </div>
      <div class="field-group">
        <label for="inp-cuerpo">Cuerpo del documento</label>
        <textarea id="inp-cuerpo" rows="10" placeholder="Cordial saludo,&#10;&#10;Por medio de la presente...&#10;&#10;Quedamos atentos a sus comentarios.&#10;&#10;Cordialmente,&#10;[Nombre y cargo]"></textarea>
      </div>
    </div>

    <div class="flex flex-wrap gap-3 mt-6 pt-5 border-t border-slate-100">
      <button class="btn btn-primary" onclick="downloadDoc()">
        <svg width="15" height="15" fill="none" viewBox="0 0 24 24"><path d="M12 4v12m0 0l-4-4m4 4l4-4M4 20h16" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
        Descargar Word (.doc)
      </button>
      <button class="btn btn-secondary" onclick="window.print()">
        <svg width="15" height="15" fill="none" viewBox="0 0 24 24"><path d="M6 9V2h12v7 M6 18H4a2 2 0 01-2-2v-5a2 2 0 012-2h16a2 2 0 012 2v5a2 2 0 01-2 2h-2 M6 14h12v8H6z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
        Imprimir / PDF
      </button>
      <button class="btn btn-ghost" onclick="copyHTML()">
        <svg width="15" height="15" fill="none" viewBox="0 0 24 24"><path d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
        Copiar HTML
      </button>
    </div>

    <div class="mt-5 p-4 border border-slate-200" style="background:#F2F6FA;border-left:4px solid #025199;">
      <p class="mono text-xs font-semibold text-slate-700 mb-2 uppercase tracking-wide">Como usar en Word</p>
      <ol class="text-xs text-slate-600 space-y-1 list-decimal list-inside leading-relaxed">
        <li>Llena los campos del documento.</li>
        <li>Click en <strong>Descargar Word (.doc)</strong>.</li>
        <li>Abre el archivo descargado en Microsoft Word &mdash; quedara editable.</li>
        <li>Word puede mostrar un aviso por ser HTML; haz click en <strong>Habilitar edicion</strong>.</li>
      </ol>
    </div>
  </div>

  <!-- RIGHT: Preview -->
  <div class="flex flex-col gap-4">
    <div class="flex items-center justify-between">
      <h2 class="mono text-xs font-semibold text-slate-400 uppercase tracking-widest">Vista previa A4</h2>
      <span class="mono text-xs text-slate-400 bg-white border border-slate-200 px-3 py-1 font-medium">Se actualiza al escribir</span>
    </div>

    <div class="preview-shell shadow-sm">
      <div id="membrete-preview" class="preview-page">

        <div class="mb-header">
          <img src="''' + LOGO_B64 + '''" alt="COICEM S.A.S" />
          <div class="mb-header-info">
            <strong>COICEM S.A.S</strong>
            <span>Servicio Mantenimiento Especializado</span>
          </div>
        </div>

        <div class="mb-rule"><div class="a"></div><div class="b"></div><div class="c"></div></div>

        <div class="mb-meta">
          <span id="prev-ciudad">[Ciudad]</span>, <span id="prev-fecha">&mdash;</span>
        </div>

        <div class="mb-dest">
          <strong>Senor(a):</strong><br/>
          <span id="prev-destinatario">&mdash;</span><br/>
          <span id="prev-cargo" style="color:#6B7785;">&mdash;</span><br/>
          <span id="prev-direccion">Ciudad</span>
        </div>

        <div class="mb-asunto"><strong>Asunto:</strong> <span id="prev-asunto">&mdash;</span></div>

        <div class="mb-watermark">COICEM</div>

        <div class="mb-body" id="prev-cuerpo">[Escriba el contenido del documento aqui]</div>

        <div class="mb-footer">
          <div class="mb-footer-grid">
            <div><strong>Ubicacion</strong>[Direccion]<br/>Colombia</div>
            <div><strong>Contacto</strong>T. [+57 ...]<br/>M. [+57 ...]</div>
            <div><strong>Digital</strong>[correo@coicem.com]<br/>coicem.com</div>
            <div><strong>Areas</strong>Operacion &middot; Mantenimiento<br/>Construccion &middot; Energia &middot; Infraestructura</div>
          </div>
          <div class="mb-certs">ISO 9001:2015 &middot; 14001:2015 &middot; 45001:2018 &middot; <b>NORSOK 006:2020</b> &middot; Bureau Veritas &middot; NIT: [Pendiente]</div>
        </div>
      </div>
    </div>
  </div>
</div>

<div id="toast"></div>

<script>
const today = new Date().toISOString().slice(0,10);
document.getElementById('inp-fecha').value = today;

const fields = ['ciudad','fecha','destinatario','cargo','direccion','asunto','cuerpo'];
fields.forEach(function(name) {
  document.getElementById('inp-' + name).addEventListener('input', updatePreview);
});

function fmtDate(iso) {
  if (!iso) return '\\u2014';
  const [y,m,d] = iso.split('-');
  const meses = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre'];
  return d + ' de ' + meses[parseInt(m,10)-1] + ' de ' + y;
}

function updatePreview() {
  document.getElementById('prev-ciudad').textContent = document.getElementById('inp-ciudad').value || '[Ciudad]';
  document.getElementById('prev-fecha').textContent = fmtDate(document.getElementById('inp-fecha').value);
  document.getElementById('prev-destinatario').textContent = document.getElementById('inp-destinatario').value || '\\u2014';
  document.getElementById('prev-cargo').textContent = document.getElementById('inp-cargo').value || '\\u2014';
  document.getElementById('prev-direccion').textContent = document.getElementById('inp-direccion').value || 'Ciudad';
  document.getElementById('prev-asunto').textContent = document.getElementById('inp-asunto').value || '\\u2014';
  const body = document.getElementById('inp-cuerpo').value;
  const bodyEl = document.getElementById('prev-cuerpo');
  if (body.trim()) {
    bodyEl.textContent = body;
  } else {
    bodyEl.innerHTML = '<span style="color:#cbd5e1;">[Escriba el contenido del documento aqui]</span>';
  }
}
updatePreview();

function showToast(msg) {
  const t = document.getElementById('toast');
  t.textContent = msg; t.classList.add('show');
  setTimeout(function(){ t.classList.remove('show'); }, 2800);
}

function buildDocHTML() {
  const preview = document.getElementById('membrete-preview').outerHTML;
  const styles = document.querySelector('style').textContent;
  return '<html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:w="urn:schemas-microsoft-com:office:word" xmlns="http://www.w3.org/TR/REC-html40">' +
         '<head><meta charset="utf-8"><title>Membrete COICEM</title>' +
         '<!--[if gte mso 9]><xml><w:WordDocument><w:View>Print</w:View><w:Zoom>100</w:Zoom></w:WordDocument></xml><![endif]-->' +
         '<style>' + styles + '@page { size: A4; margin: 1.5cm; }</style>' +
         '</head><body>' + preview + '</body></html>';
}

function downloadDoc() {
  const docHtml = buildDocHTML();
  const blob = new Blob(['\\ufeff', docHtml], { type: 'application/msword' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  const date = document.getElementById('inp-fecha').value || 'hoy';
  a.href = url; a.download = 'membrete-coicem-' + date + '.doc';
  document.body.appendChild(a); a.click(); document.body.removeChild(a);
  setTimeout(function(){ URL.revokeObjectURL(url); }, 1000);
  showToast('Descargado - abrelo en Microsoft Word');
}

async function copyHTML() {
  const docHtml = buildDocHTML();
  try {
    await navigator.clipboard.writeText(docHtml);
    showToast('HTML copiado al portapapeles');
  } catch (e) {
    const ta = document.createElement('textarea');
    ta.value = docHtml; ta.style.cssText = 'position:fixed;left:-9999px';
    document.body.appendChild(ta); ta.select();
    document.execCommand('copy'); document.body.removeChild(ta);
    showToast('HTML copiado (modo compatibilidad)');
  }
}
</script>

</body>
</html>'''

with open(os.path.join(here, 'hoja-membretada-generador.html'), 'w', encoding='utf-8') as f:
    f.write(html)

dst = os.path.join(here, '..', 'coicem-web', 'public', 'internal')
os.makedirs(dst, exist_ok=True)
shutil.copy(os.path.join(here, 'hoja-membretada-generador.html'), os.path.join(dst, 'hoja-membretada-generador.html'))
print('hoja-membretada-generador.html:', os.path.getsize(os.path.join(here, 'hoja-membretada-generador.html')) // 1024, 'KB')
print('copiado a public/internal/')
