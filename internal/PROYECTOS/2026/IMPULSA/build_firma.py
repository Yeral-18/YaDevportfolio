"""
Build script: injects the base64 logo into firma-generador.html
Run once with:  python build_firma.py
"""
import pathlib

BASE = pathlib.Path(r"C:\Users\ASUS\APP\YaDevportfolio\internal\PROYECTOS\2026\IMPULSA")

logo_b64 = (BASE / "logo_b64.txt").read_text(encoding="utf-8").strip().replace("\n", "").replace("\r", "")
data_uri  = "data:image/png;base64," + logo_b64

# -----------------------------------------------------------------
HTML = r"""<!DOCTYPE html>
<html lang="es-CO">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Generador de Firma &mdash; Impulsa Social</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            brand: { dark: '#2D5BA0', mid: '#4A90D9', yellow: '#E8A838', gray: '#333333' }
          },
          fontFamily: { sans: ['Inter', 'sans-serif'] }
        }
      }
    }
  </script>
  <style>
    body { font-family: 'Inter', sans-serif; }
    @keyframes fadeInUp {
      from { opacity: 0; transform: translateY(12px); }
      to   { opacity: 1; transform: translateY(0); }
    }
    @keyframes fadeOut { from { opacity:1; } to { opacity:0; } }
    .toast-enter { animation: fadeInUp 0.25s ease forwards; }
    .toast-exit  { animation: fadeOut 0.3s ease forwards; }
    #sig-preview table { border-collapse: collapse; }
    input:focus { outline: none; box-shadow: 0 0 0 3px rgba(45,91,160,0.18); }
  </style>
</head>
<body class="min-h-screen bg-gray-50">

  <!-- ── Header ──────────────────────────────────────────────────── -->
  <header class="bg-white border-b border-gray-200 px-6 py-4">
    <div class="max-w-6xl mx-auto flex items-center gap-3">
      <div class="w-8 h-8 rounded-md flex items-center justify-center" style="background:#2D5BA0;">
        <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
          <path d="M9 2L16 6V12L9 16L2 12V6L9 2Z" fill="white" fill-opacity="0.9"/>
        </svg>
      </div>
      <div>
        <h1 class="text-sm font-semibold text-gray-900 leading-none">Generador de Firma de Correo</h1>
        <p class="text-xs text-gray-400 mt-0.5">Impulsa Social &mdash; Compatible con Outlook, Gmail y Apple Mail</p>
      </div>
      <span class="ml-auto text-xs font-medium px-2.5 py-1 rounded-full bg-green-50 text-green-700 border border-green-200">
        Listo para usar
      </span>
    </div>
  </header>

  <!-- ── Main layout ──────────────────────────────────────────────── -->
  <main id="main-content" class="max-w-6xl mx-auto px-6 py-8">
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 items-start">

      <!-- Left: Form ─────────────────────────────────────────────── -->
      <div class="bg-white rounded-2xl border border-gray-200 shadow-sm p-6">
        <h2 class="text-sm font-semibold text-gray-700 mb-5 flex items-center gap-2">
          <svg class="w-4 h-4" style="color:#2D5BA0" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
          </svg>
          Datos del colaborador
        </h2>
        <div class="space-y-4">
          <div>
            <label for="f-nombre" class="block text-xs font-medium text-gray-600 mb-1.5">Nombre completo</label>
            <input id="f-nombre" type="text" value="JUNER LINDADO JAIMES"
              class="w-full text-sm border border-gray-200 rounded-lg px-3 py-2.5 text-gray-800 bg-gray-50 focus:bg-white transition-shadow"
              placeholder="JUAN PEREZ GOMEZ" />
          </div>
          <div>
            <label for="f-cargo" class="block text-xs font-medium text-gray-600 mb-1.5">Cargo</label>
            <input id="f-cargo" type="text" value="REPRESENTANTE LEGAL IMPULSA SOCIAL"
              class="w-full text-sm border border-gray-200 rounded-lg px-3 py-2.5 text-gray-800 bg-gray-50 focus:bg-white transition-shadow"
              placeholder="DIRECTOR COMERCIAL" />
          </div>
          <div>
            <label for="f-email" class="block text-xs font-medium text-gray-600 mb-1.5">Correo electr&oacute;nico</label>
            <input id="f-email" type="email" value="impulsasocial@gmail.com"
              class="w-full text-sm border border-gray-200 rounded-lg px-3 py-2.5 text-gray-800 bg-gray-50 focus:bg-white transition-shadow"
              placeholder="nombre@impulsasocial.com" />
          </div>
          <div>
            <label for="f-web" class="block text-xs font-medium text-gray-600 mb-1.5">Sitio web</label>
            <input id="f-web" type="text" value="www.impulsasocial.com"
              class="w-full text-sm border border-gray-200 rounded-lg px-3 py-2.5 text-gray-800 bg-gray-50 focus:bg-white transition-shadow"
              placeholder="www.impulsasocial.com" />
          </div>
          <div>
            <label for="f-telefono" class="block text-xs font-medium text-gray-600 mb-1.5">Tel&eacute;fono / WhatsApp</label>
            <input id="f-telefono" type="tel" value="3118807410"
              class="w-full text-sm border border-gray-200 rounded-lg px-3 py-2.5 text-gray-800 bg-gray-50 focus:bg-white transition-shadow"
              placeholder="3001234567" />
          </div>
        </div>
        <p class="mt-5 text-xs text-gray-400 leading-relaxed">
          Los cambios se reflejan en tiempo real en la previsualizaci&oacute;n.
          Copia la firma y p&eacute;gala directamente en Outlook, Gmail o Apple Mail.
        </p>
      </div>

      <!-- Right: Preview + Actions ────────────────────────────────── -->
      <div class="space-y-4">

        <!-- Preview -->
        <div class="bg-white rounded-2xl border border-gray-200 shadow-sm p-6">
          <div class="flex items-center justify-between mb-5">
            <h2 class="text-sm font-semibold text-gray-700 flex items-center gap-2">
              <svg class="w-4 h-4" style="color:#2D5BA0" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
                <path stroke-linecap="round" stroke-linejoin="round" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
              </svg>
              Vista previa
            </h2>
            <span class="text-xs text-gray-400">Escala real</span>
          </div>
          <!-- Simulated email -->
          <div class="bg-gray-50 rounded-xl border border-gray-100 p-4">
            <div class="border-b border-gray-200 pb-3 mb-3">
              <p class="text-xs text-gray-500">
                <span class="font-medium text-gray-700">De:</span>
                <span id="preview-from">JUNER LINDADO JAIMES &lt;impulsasocial@gmail.com&gt;</span>
              </p>
              <p class="text-xs text-gray-500 mt-1">
                <span class="font-medium text-gray-700">Asunto:</span>
                Reuni&oacute;n de seguimiento &mdash; Propuesta Q1
              </p>
            </div>
            <p class="text-xs text-gray-500 mb-4 leading-relaxed">
              Cordial saludo,<br><br>
              Adjunto encontrar&aacute; el documento solicitado. Quedo atento a cualquier inquietud.<br><br>
              Saludos,
            </p>
            <div id="sig-preview"></div>
          </div>
        </div>

        <!-- Actions -->
        <div class="bg-white rounded-2xl border border-gray-200 shadow-sm p-5">
          <h3 class="text-xs font-semibold text-gray-600 uppercase tracking-wide mb-3">Acciones</h3>
          <div class="flex flex-col sm:flex-row gap-3">
            <button onclick="copyRich()"
              class="flex-1 flex items-center justify-center gap-2 text-sm font-semibold text-white rounded-xl px-4 py-3 transition-all active:scale-95 cursor-pointer"
              style="background:linear-gradient(135deg,#2D5BA0 0%,#4A90D9 100%);box-shadow:0 2px 12px rgba(45,91,160,0.35);">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"/>
              </svg>
              Copiar Firma
            </button>
            <button onclick="copyHTML()"
              class="flex-1 flex items-center justify-center gap-2 text-sm font-semibold text-gray-700 rounded-xl px-4 py-3 border-2 border-gray-200 hover:border-gray-300 hover:bg-gray-50 transition-all active:scale-95 cursor-pointer">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"/>
              </svg>
              Copiar como HTML
            </button>
          </div>
          <div class="mt-4 space-y-2">
            <div class="flex gap-2 items-start text-xs text-gray-500">
              <span class="font-bold shrink-0" style="color:#2D5BA0;">Outlook:</span>
              <span>Nuevo correo &rarr; Insertar &rarr; Firma &rarr; Nueva &rarr; pegar con Ctrl+V</span>
            </div>
            <div class="flex gap-2 items-start text-xs text-gray-500">
              <span class="font-bold shrink-0" style="color:#2D5BA0;">Gmail:</span>
              <span>Configuraci&oacute;n &rarr; Ver toda la configuraci&oacute;n &rarr; Firma &rarr; pegar con Ctrl+V</span>
            </div>
            <div class="flex gap-2 items-start text-xs text-gray-500">
              <span class="font-bold shrink-0" style="color:#2D5BA0;">Apple Mail:</span>
              <span>Preferencias &rarr; Firmas &rarr; pegar la firma en el campo de texto</span>
            </div>
          </div>
        </div>

      </div>
    </div>
  </main>

  <!-- Toast -->
  <div id="toast" class="fixed bottom-6 left-1/2 -translate-x-1/2 z-50 hidden" style="min-width:280px;">
    <div id="toast-inner" class="flex items-center gap-2.5 text-sm font-semibold text-white px-5 py-3 rounded-xl shadow-xl" style="background:#2D5BA0;">
      <svg class="w-4 h-4 shrink-0" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/>
      </svg>
      <span id="toast-msg">Copiado</span>
    </div>
  </div>

  <script>
    /* ================================================================
       LOGO — injected at build time
    ================================================================ */
    const LOGO_SRC = 'PLACEHOLDER_DATA_URI';

    /* ================================================================
       Build pure-inline signature HTML  (table layout, Outlook-safe)
    ================================================================ */
    function buildSig(d) {
      const webHref    = d.web.startsWith('http') ? d.web : 'https://' + d.web;
      const webDisplay = d.web.replace(/^https?:\/\//, '');
      return `<table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;font-family:Arial,Helvetica,sans-serif;max-width:520px;">
<tr>
  <td valign="middle" style="padding:0 18px 0 0;vertical-align:middle;">
    <img src="${LOGO_SRC}" alt="Impulsa Social" width="120"
      style="display:block;width:120px;height:auto;border:0;outline:none;text-decoration:none;" />
  </td>
  <td width="2" style="width:2px;padding:0;vertical-align:middle;">
    <table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;">
      <tr><td width="2" height="27" style="width:2px;height:27px;font-size:0;line-height:0;background:#2D5BA0;">&nbsp;</td></tr>
      <tr><td width="2" height="27" style="width:2px;height:27px;font-size:0;line-height:0;background:#4A90D9;">&nbsp;</td></tr>
      <tr><td width="2" height="14" style="width:2px;height:14px;font-size:0;line-height:0;background:#E8A838;">&nbsp;</td></tr>
    </table>
  </td>
  <td valign="middle" style="padding:0 0 0 18px;vertical-align:middle;">
    <p style="margin:0 0 2px 0;padding:0;font-family:Arial,Helvetica,sans-serif;font-size:16px;font-weight:700;color:#1a1a1a;line-height:1.25;">${d.nombre}</p>
    <p style="margin:0 0 9px 0;padding:0;font-family:Arial,Helvetica,sans-serif;font-size:10px;font-weight:600;color:#777777;text-transform:uppercase;letter-spacing:0.09em;line-height:1.3;">${d.cargo}</p>
    <table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;margin:0 0 9px 0;">
      <tr>
        <td width="26" height="2" style="width:26px;height:2px;font-size:0;line-height:0;background:#2D5BA0;">&nbsp;</td>
        <td width="14" height="2" style="width:14px;height:2px;font-size:0;line-height:0;background:#4A90D9;">&nbsp;</td>
        <td width="8"  height="2" style="width:8px;height:2px;font-size:0;line-height:0;background:#E8A838;">&nbsp;</td>
      </tr>
    </table>
    <p style="margin:0 0 3px 0;padding:0;font-family:Arial,Helvetica,sans-serif;font-size:12px;color:#333333;line-height:1.45;">
      <a href="mailto:${d.email}" style="color:#2D5BA0;text-decoration:none;font-family:Arial,Helvetica,sans-serif;font-size:12px;">${d.email}</a>
    </p>
    <p style="margin:0 0 3px 0;padding:0;font-family:Arial,Helvetica,sans-serif;font-size:12px;color:#333333;line-height:1.45;">
      <a href="${webHref}" target="_blank" style="color:#2D5BA0;text-decoration:none;font-family:Arial,Helvetica,sans-serif;font-size:12px;">${webDisplay}</a>
    </p>
    <p style="margin:0;padding:0;font-family:Arial,Helvetica,sans-serif;font-size:12px;color:#333333;line-height:1.45;">
      <span style="color:#777777;font-family:Arial,Helvetica,sans-serif;font-size:12px;">Telf:&nbsp;</span><span style="color:#1a1a1a;font-family:Arial,Helvetica,sans-serif;font-size:12px;">${d.telefono}</span>
    </p>
  </td>
</tr>
</table>`;
    }

    /* ================================================================
       Helpers
    ================================================================ */
    function getData() {
      return {
        nombre:   document.getElementById('f-nombre').value.trim()  || 'NOMBRE APELLIDO',
        cargo:    document.getElementById('f-cargo').value.trim()    || 'CARGO',
        email:    document.getElementById('f-email').value.trim()    || 'correo@impulsasocial.com',
        web:      document.getElementById('f-web').value.trim()      || 'www.impulsasocial.com',
        telefono: document.getElementById('f-telefono').value.trim() || '000 000 0000',
      };
    }

    function updatePreview() {
      const d = getData();
      document.getElementById('sig-preview').innerHTML = buildSig(d);
      document.getElementById('preview-from').textContent = d.nombre + ' <' + d.email + '>';
    }

    /* ================================================================
       Copy as rich HTML  (pastes formatted into email clients)
    ================================================================ */
    async function copyRich() {
      const html = buildSig(getData());
      try {
        await navigator.clipboard.write([new ClipboardItem({ 'text/html': new Blob([html], { type: 'text/html' }) })]);
        showToast('Firma copiada. Pégala en tu cliente de correo.');
      } catch (_) { fallbackRich(html); }
    }

    function fallbackRich(html) {
      const div = document.createElement('div');
      div.style.cssText = 'position:fixed;top:0;left:0;width:0;height:0;overflow:hidden;opacity:0;';
      div.innerHTML = html;
      document.body.appendChild(div);
      const r = document.createRange();
      r.selectNodeContents(div);
      const s = window.getSelection();
      s.removeAllRanges(); s.addRange(r);
      try {
        document.execCommand('copy');
        showToast('Firma copiada. Pégala en tu cliente de correo.');
      } catch (_) { showToast('No se pudo copiar. Usa el botón HTML.', true); }
      s.removeAllRanges();
      document.body.removeChild(div);
    }

    /* ================================================================
       Copy raw HTML code
    ================================================================ */
    async function copyHTML() {
      const html = buildSig(getData());
      try {
        await navigator.clipboard.writeText(html);
        showToast('Código HTML copiado al portapapeles.');
      } catch (_) {
        const ta = document.createElement('textarea');
        ta.style.cssText = 'position:fixed;top:0;left:0;width:2px;height:2px;opacity:0;';
        ta.value = html;
        document.body.appendChild(ta);
        ta.focus(); ta.select();
        try {
          document.execCommand('copy');
          showToast('Código HTML copiado al portapapeles.');
        } catch (_2) { showToast('No se pudo copiar automáticamente.', true); }
        document.body.removeChild(ta);
      }
    }

    /* ================================================================
       Toast
    ================================================================ */
    let _tt = null;
    function showToast(msg, err=false) {
      const t = document.getElementById('toast');
      const i = document.getElementById('toast-inner');
      document.getElementById('toast-msg').textContent = msg;
      i.style.background = err ? '#dc2626' : '#2D5BA0';
      t.classList.remove('hidden');
      i.className = 'flex items-center gap-2.5 text-sm font-semibold text-white px-5 py-3 rounded-xl shadow-xl toast-enter';
      clearTimeout(_tt);
      _tt = setTimeout(() => {
        i.className = 'flex items-center gap-2.5 text-sm font-semibold text-white px-5 py-3 rounded-xl shadow-xl toast-exit';
        setTimeout(() => t.classList.add('hidden'), 320);
      }, 2800);
    }

    /* ================================================================
       Init
    ================================================================ */
    ['f-nombre','f-cargo','f-email','f-web','f-telefono'].forEach(id =>
      document.getElementById(id).addEventListener('input', updatePreview)
    );
    updatePreview();
  </script>
</body>
</html>
"""

# Inject the data URI
final = HTML.replace("'PLACEHOLDER_DATA_URI'", "'" + data_uri + "'")

out = BASE / "firma-generador.html"
out.write_text(final, encoding="utf-8")
print(f"Written: {out}")
print(f"File size: {out.stat().st_size:,} bytes")
