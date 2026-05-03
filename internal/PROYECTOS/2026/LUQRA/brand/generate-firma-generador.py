"""Genera firma-generador.html (form interactivo + preview en vivo) para Luqra.

USA logo_firma_b64.txt (logo de 400px, ~50-90KB b64) en vez de logo_b64.txt (1600px, 340KB).
Outlook y Gmail strippean imagenes embebidas como data URI cuando exceden ~100KB en paste.
Multiservicios tenia logo_firma_b64 separado por la misma razon.
"""
with open('logo_firma_b64.txt') as f:
    LOGO_B64 = f.read().strip()

html = '''<!DOCTYPE html>
<html lang="es-CO">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Generador de Firma &mdash; Luqra Ingenieria y Soluciones S.A.S</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    * { box-sizing: border-box; }
    body { font-family: 'Plus Jakarta Sans', sans-serif; }

    .field-group label {
      display: block;
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      color: #64748b;
      margin-bottom: 5px;
    }
    .field-group input {
      width: 100%;
      padding: 9px 12px;
      border: 1.5px solid #e2e8f0;
      border-radius: 8px;
      font-size: 14px;
      color: #1e293b;
      font-family: inherit;
      transition: border-color 0.15s, box-shadow 0.15s;
      outline: none;
      background: #fff;
    }
    .field-group input:focus {
      border-color: #1F5FBF;
      box-shadow: 0 0 0 3px rgba(31,95,191,0.12);
    }

    .btn-copy {
      display: inline-flex;
      align-items: center;
      gap: 7px;
      padding: 10px 18px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      border: none;
      font-family: inherit;
      transition: all 0.15s;
    }
    .btn-primary { background: #0A2A66; color: #fff; }
    .btn-primary:hover { background: #123C8C; }
    .btn-secondary { background: #f1f5f9; color: #334155; border: 1.5px solid #e2e8f0; }
    .btn-secondary:hover { background: #e2e8f0; }

    #toast {
      position: fixed;
      bottom: 28px;
      left: 50%;
      transform: translateX(-50%) translateY(20px);
      background: #0A2A66;
      color: #fff;
      padding: 10px 22px;
      border-radius: 999px;
      font-size: 13px;
      font-weight: 500;
      opacity: 0;
      transition: opacity 0.25s, transform 0.25s;
      pointer-events: none;
      z-index: 9999;
      white-space: nowrap;
    }
    #toast.show { opacity: 1; transform: translateX(-50%) translateY(0); }

    .email-shell { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; overflow: hidden; }
    .email-chrome { background: #fff; border-bottom: 1px solid #e2e8f0; padding: 10px 16px; display: flex; align-items: center; gap: 6px; }
    .email-dot { width: 10px; height: 10px; border-radius: 50%; }
    .email-body { padding: 28px 24px; background: #fff; min-height: 160px; }
    .email-divider-preview { border: none; border-top: 1px dashed #e2e8f0; margin: 18px 0; }

    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: #f1f5f9; }
    ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 3px; }
  </style>
</head>
<body class="bg-slate-100 min-h-screen py-10 px-4">

  <!-- Header -->
  <div class="max-w-6xl mx-auto mb-8">
    <div class="flex items-center gap-3">
      <div class="w-9 h-9 rounded-lg flex items-center justify-center flex-shrink-0" style="background:linear-gradient(135deg,#0A2A66,#FF6A00);">
        <svg width="18" height="18" fill="none" viewBox="0 0 24 24"><path d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </div>
      <div>
        <h1 class="text-lg font-bold text-slate-800 leading-tight">Generador de Firma de Correo</h1>
        <p class="text-xs text-slate-400 font-medium">Luqra Ingenieria y Soluciones S.A.S &mdash; Compatible con Outlook, Gmail y Apple Mail</p>
      </div>
    </div>
  </div>

  <div class="max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-6 items-start">

    <!-- LEFT: Form -->
    <div class="bg-white rounded-2xl shadow-sm border border-slate-200 p-6">
      <h2 class="text-xs font-semibold text-slate-400 uppercase tracking-widest mb-5">Datos del colaborador</h2>

      <div class="space-y-4">
        <div class="field-group">
          <label for="inp-nombre">Nombre completo</label>
          <input type="text" id="inp-nombre" placeholder="Nombre Apellido" value="Nombre Apellido" />
        </div>
        <div class="field-group">
          <label for="inp-cargo">Cargo</label>
          <input type="text" id="inp-cargo" placeholder="Cargo" value="CARGO &mdash; LUQRA INGENIERIA Y SOLUCIONES S.A.S" />
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div class="field-group">
            <label for="inp-tel">Telefono fijo</label>
            <input type="text" id="inp-tel" placeholder="+57 (1) 000 0000" value="" />
          </div>
          <div class="field-group">
            <label for="inp-cel">Celular / WhatsApp</label>
            <input type="text" id="inp-cel" placeholder="+57 300 000 0000" value="" />
          </div>
        </div>
        <div class="field-group">
          <label for="inp-email">Correo electronico</label>
          <input type="text" id="inp-email" placeholder="nombre@luqra.com.co" value="contacto@luqra.com.co" />
        </div>
        <div class="field-group">
          <label for="inp-web">Sitio web</label>
          <input type="text" id="inp-web" placeholder="www.luqra.com.co" value="www.luqra.com.co" />
        </div>
      </div>

      <div class="flex flex-wrap gap-3 mt-6 pt-5 border-t border-slate-100">
        <button class="btn-copy btn-primary" onclick="copyRichSignature()">
          <svg width="15" height="15" fill="none" viewBox="0 0 24 24"><path d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          Copiar Firma (Outlook / Gmail)
        </button>
        <button class="btn-copy btn-secondary" onclick="copyHTMLCode()">
          <svg width="15" height="15" fill="none" viewBox="0 0 24 24"><path d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          Copiar como HTML
        </button>
        <button class="btn-copy btn-secondary" onclick="downloadSignature()">
          <svg width="15" height="15" fill="none" viewBox="0 0 24 24"><path d="M12 4v12m0 0l-4-4m4 4l4-4M4 20h16" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          Descargar (.htm)
        </button>
      </div>

      <div class="mt-5 p-4 bg-blue-50 rounded-xl border border-blue-100">
        <p class="text-xs font-semibold text-blue-800 mb-2">Como usar en Outlook</p>
        <ol class="text-xs text-blue-700 space-y-1 list-decimal list-inside leading-relaxed">
          <li>Haz clic en <strong>Copiar Firma</strong></li>
          <li>Outlook &rarr; Archivo &rarr; Opciones &rarr; Correo &rarr; Firmas</li>
          <li>Crea una firma nueva y pega con <kbd class="bg-blue-100 px-1 rounded font-mono">Ctrl+V</kbd></li>
          <li>Guarda y asigna la firma a tu cuenta</li>
        </ol>
      </div>

      <div class="mt-3 p-4 bg-orange-50 rounded-xl border border-orange-100">
        <p class="text-xs font-semibold text-orange-800 mb-2">Como usar en Gmail</p>
        <ol class="text-xs text-orange-700 space-y-1 list-decimal list-inside leading-relaxed">
          <li>Haz clic en <strong>Copiar Firma</strong></li>
          <li>Gmail &rarr; Configuracion &rarr; Ver toda la configuracion &rarr; General &rarr; Firma</li>
          <li>Nueva firma &rarr; pega con <kbd class="bg-orange-100 px-1 rounded font-mono">Ctrl+V</kbd></li>
          <li>Guarda los cambios al final de la pagina</li>
        </ol>
      </div>
    </div>

    <!-- RIGHT: Preview -->
    <div class="flex flex-col gap-4">
      <div class="flex items-center justify-between">
        <h2 class="text-xs font-semibold text-slate-400 uppercase tracking-widest">Vista previa en vivo</h2>
        <span class="text-xs text-slate-400 bg-white border border-slate-200 rounded-full px-3 py-1 font-medium">Se actualiza al escribir</span>
      </div>

      <div class="email-shell shadow-sm">
        <div class="email-chrome">
          <div class="email-dot" style="background:#fc5f57;"></div>
          <div class="email-dot" style="background:#fdbc2c;"></div>
          <div class="email-dot" style="background:#34c749;"></div>
          <div class="flex-1 mx-3">
            <div class="bg-slate-100 rounded text-xs text-slate-400 text-center py-0.5 px-2 font-medium">Nuevo mensaje &mdash; Vista previa</div>
          </div>
        </div>
        <div class="px-5 pt-4 pb-2 border-b border-slate-100">
          <div class="flex items-center gap-2 py-1.5 border-b border-slate-100">
            <span class="text-xs text-slate-400 w-8 font-medium">Para:</span>
            <span class="text-xs text-slate-500">cliente@empresa.com</span>
          </div>
          <div class="flex items-center gap-2 py-1.5">
            <span class="text-xs text-slate-400 w-8 font-medium">Asunto:</span>
            <span class="text-xs text-slate-500">Cotizacion proyecto</span>
          </div>
        </div>
        <div class="email-body">
          <p class="text-sm text-slate-600 mb-4">Cordial saludo,</p>
          <p class="text-sm text-slate-600 mb-3">Adjunto encontrara la cotizacion solicitada.</p>
          <p class="text-sm text-slate-600 mb-4">Quedo atento a sus comentarios.</p>
          <hr class="email-divider-preview" />
          <div id="signature-preview"></div>
        </div>
      </div>

      <div class="bg-slate-900 rounded-xl p-4 text-xs font-mono text-slate-300 overflow-x-auto" style="max-height:200px;overflow-y:auto;">
        <div class="text-slate-500 mb-2 text-[10px] uppercase tracking-widest font-sans">HTML generado</div>
        <pre id="html-output" style="white-space:pre-wrap;word-break:break-word;line-height:1.5;"></pre>
      </div>
    </div>
  </div>

  <div id="toast"></div>

  <script>
    var LOGO_SRC = ''' + repr(LOGO_B64) + ''';

    var fNombre = document.getElementById('inp-nombre');
    var fCargo  = document.getElementById('inp-cargo');
    var fEmail  = document.getElementById('inp-email');
    var fWeb    = document.getElementById('inp-web');
    var fTel    = document.getElementById('inp-tel');
    var fCel    = document.getElementById('inp-cel');

    function esc(str) {
      return String(str)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;');
    }

    function buildSignature() {
      var nombre   = fNombre.value.trim() || 'Nombre Apellido';
      var cargo    = fCargo.value.trim()  || 'CARGO - LUQRA INGENIERIA Y SOLUCIONES S.A.S';
      var email    = fEmail.value.trim()  || 'contacto@luqra.com.co';
      var web      = fWeb.value.trim()    || 'www.luqra.com.co';
      var tel      = fTel.value.trim();
      var cel      = fCel.value.trim();
      var webClean = web.replace(/^https?:\\/\\//, '');

      var phoneRows = '';
      if (tel) {
        phoneRows +=
          '<tr>' +
            '<td style="padding:0 0 1px 0;font-family:Arial,Helvetica,sans-serif;font-size:12px;color:#1a1a1a;line-height:1.6;">' +
              '<span style="color:#888888;font-size:11px;">Tel:</span>&nbsp;' + esc(tel) +
            '</td>' +
          '</tr>';
      }
      if (cel) {
        phoneRows +=
          '<tr>' +
            '<td style="padding:0 0 1px 0;font-family:Arial,Helvetica,sans-serif;font-size:12px;color:#1a1a1a;line-height:1.6;">' +
              '<span style="color:#888888;font-size:11px;">Cel:</span>&nbsp;' + esc(cel) +
            '</td>' +
          '</tr>';
      }

      return (
        '<table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;font-family:Arial,Helvetica,sans-serif;">' +
          '<tr>' +
            '<td valign="middle" style="padding:0 18px 0 0;vertical-align:middle;">' +
              '<img src="' + LOGO_SRC + '" width="120" alt="Luqra Ingenieria y Soluciones S.A.S"' +
              ' style="display:block;width:120px;height:auto;border:0;outline:none;' +
              'text-decoration:none;image-rendering:-webkit-optimize-contrast;" />' +
            '</td>' +

            '<td style="padding:0;width:2px;background-color:#FF6A00;font-size:0;line-height:0;">&nbsp;</td>' +

            '<td valign="middle" style="padding:0 0 0 18px;vertical-align:middle;">' +
              '<table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;">' +

                '<tr>' +
                  '<td style="padding:0 0 2px 0;font-family:Arial,Helvetica,sans-serif;' +
                  'font-size:16px;font-weight:bold;color:#0A2A66;line-height:1.2;white-space:nowrap;">' +
                    esc(nombre) +
                  '</td>' +
                '</tr>' +

                '<tr>' +
                  '<td style="padding:0 0 6px 0;font-family:Arial,Helvetica,sans-serif;' +
                  'font-size:11px;color:#666666;letter-spacing:1px;text-transform:uppercase;line-height:1.3;">' +
                    esc(cargo) +
                  '</td>' +
                '</tr>' +

                /* Accent bar - 80% azul / 20% naranja */
                '<tr>' +
                  '<td style="padding:0 0 8px 0;">' +
                    '<table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;">' +
                      '<tr>' +
                        '<td style="width:40px;height:3px;background-color:#0A2A66;font-size:0;line-height:0;">&nbsp;</td>' +
                        '<td style="width:20px;height:3px;background-color:#1F5FBF;font-size:0;line-height:0;">&nbsp;</td>' +
                        '<td style="width:16px;height:3px;background-color:#FF6A00;font-size:0;line-height:0;">&nbsp;</td>' +
                      '</tr>' +
                    '</table>' +
                  '</td>' +
                '</tr>' +

                '<tr>' +
                  '<td style="padding:0 0 2px 0;font-family:Arial,Helvetica,sans-serif;font-size:12px;color:#1a1a1a;line-height:1.6;">' +
                    '<a href="mailto:' + esc(email) + '" style="color:#1F5FBF;text-decoration:none;">' + esc(email) + '</a>' +
                  '</td>' +
                '</tr>' +

                '<tr>' +
                  '<td style="padding:0 0 2px 0;font-family:Arial,Helvetica,sans-serif;font-size:12px;color:#1a1a1a;line-height:1.6;">' +
                    '<a href="https://' + esc(webClean) + '" style="color:#1F5FBF;text-decoration:none;">' + esc(webClean) + '</a>' +
                  '</td>' +
                '</tr>' +

                phoneRows +

                '<tr><td style="height:8px;font-size:0;line-height:0;">&nbsp;</td></tr>' +

                '<tr>' +
                  '<td style="padding:0;font-family:Arial,Helvetica,sans-serif;font-size:9px;' +
                  'color:#999999;font-style:italic;letter-spacing:0.5px;line-height:1.4;">' +
                    'Transporte&nbsp;&middot;&nbsp;Construccion&nbsp;&middot;&nbsp;Energia&nbsp;&middot;&nbsp;Ambiental' +
                  '</td>' +
                '</tr>' +

              '</table>' +
            '</td>' +

          '</tr>' +
        '</table>'
      );
    }

    function updatePreview() {
      var html = buildSignature();
      document.getElementById('signature-preview').innerHTML = html;
      document.getElementById('html-output').textContent = html;
    }

    [fNombre, fCargo, fEmail, fWeb, fTel, fCel].forEach(function(el) {
      el.addEventListener('input', updatePreview);
    });

    updatePreview();

    function showToast(msg) {
      var t = document.getElementById('toast');
      t.textContent = msg;
      t.classList.add('show');
      setTimeout(function() { t.classList.remove('show'); }, 2800);
    }

    async function copyRichSignature() {
      var html = buildSignature();
      var plain = document.getElementById('signature-preview').innerText || '';
      try {
        await navigator.clipboard.write([
          new ClipboardItem({
            'text/html':  new Blob([html],  { type: 'text/html' }),
            'text/plain': new Blob([plain], { type: 'text/plain' }),
          })
        ]);
        showToast('Firma copiada - pega en Outlook / Gmail con Ctrl+V');
      } catch (e) {
        var div = document.createElement('div');
        div.innerHTML = html;
        div.style.cssText = 'position:fixed;left:-9999px;top:-9999px;';
        document.body.appendChild(div);
        var sel = window.getSelection();
        var rng = document.createRange();
        rng.selectNodeContents(div);
        sel.removeAllRanges();
        sel.addRange(rng);
        try { document.execCommand('copy'); } catch (e2) { }
        sel.removeAllRanges();
        document.body.removeChild(div);
        showToast('Firma copiada (modo compatibilidad)');
      }
    }

    async function copyHTMLCode() {
      var html = buildSignature();
      try {
        await navigator.clipboard.writeText(html);
        showToast('Codigo HTML copiado al portapapeles');
      } catch (e) {
        var ta = document.createElement('textarea');
        ta.value = html;
        ta.style.cssText = 'position:fixed;left:-9999px;top:-9999px;';
        document.body.appendChild(ta);
        ta.select();
        try { document.execCommand('copy'); } catch (e2) { }
        document.body.removeChild(ta);
        showToast('Codigo HTML copiado (modo compatibilidad)');
      }
    }

    function downloadSignature() {
      var nombre = (fNombre.value.trim() || 'firma').toLowerCase()
        .normalize('NFD').replace(/[\\u0300-\\u036f]/g, '')
        .replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '') || 'firma';
      var sig = buildSignature();
      // Outlook accepts .htm files imported via Insert > Signatures.
      // Wrap in a minimal HTML doc so it is openable standalone too.
      var doc = '<!DOCTYPE html><html><head><meta charset="utf-8"><title>Firma Luqra</title></head><body>' + sig + '</body></html>';
      var blob = new Blob([doc], { type: 'text/html;charset=utf-8' });
      var url = URL.createObjectURL(blob);
      var a = document.createElement('a');
      a.href = url;
      a.download = 'firma-luqra-' + nombre + '.htm';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      setTimeout(function() { URL.revokeObjectURL(url); }, 1000);
      showToast('Archivo descargado - importalo en Outlook como firma');
    }
  </script>

</body>
</html>'''

with open('firma-generador.html','w',encoding='utf-8') as f:
    f.write(html)
import os
print('firma-generador.html:', os.path.getsize('firma-generador.html')//1024, 'KB')
