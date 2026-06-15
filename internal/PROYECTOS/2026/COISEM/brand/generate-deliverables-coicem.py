"""Genera firma-correo.html para COICEM S.A.S (reemplaza la actual, nivel Luqra).

- Tabla email-safe (Arial), compatible Outlook / Gmail / Apple Mail.
- Logo desde logo-firma-b64.txt (<=50KB, ya con prefijo data:) — Outlook/Gmail
  strippean imagenes embebidas que exceden ~100KB, por eso NO se usa el lockup grande.
- Estilo brutalist: barra de acento dura azul/grafito/naranja, labels mono-ish,
  fila de certificaciones Bureau Veritas.
- Contacto PENDIENTE: placeholders [ ... ] editables.
"""
import os, shutil

here = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(here, 'logo-firma-b64.txt')) as f:
    LOGO_B64 = f.read().strip()  # ya trae prefijo data:image/png;base64,

sig = '''<!DOCTYPE html>
<html lang="es-CO"><head><meta charset="utf-8"><title>Firma de correo - COICEM S.A.S</title></head>
<body style="margin:0;padding:24px;background:#f4f5f7;font-family:Arial,Helvetica,sans-serif;">

<p style="font-size:12px;color:#6B7785;max-width:560px;margin:0 0 16px;line-height:1.5;">
  Copie la tabla de abajo y peguela como firma en Outlook / Gmail. Reemplace los campos entre corchetes [ ].
</p>

<table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;background:#ffffff;font-family:Arial,Helvetica,sans-serif;color:#0B0E14;border:1px solid #E3E7EC;">
  <tr>
    <td valign="middle" style="padding:18px 24px 18px 20px;vertical-align:middle;background:#FFFFFF;">
      <img src="''' + LOGO_B64 + '''" width="190" alt="COICEM S.A.S"
        style="display:block;width:190px;height:auto;border:0;outline:none;text-decoration:none;image-rendering:-webkit-optimize-contrast;" />
    </td>

    <td style="padding:0;width:3px;background-color:#F79204;font-size:0;line-height:0;">&nbsp;</td>

    <td valign="middle" style="padding:16px 22px;vertical-align:middle;">
      <table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;">

        <tr>
          <td style="padding:0 0 2px 0;font-family:Arial,Helvetica,sans-serif;font-size:16px;font-weight:bold;color:#025199;line-height:1.15;letter-spacing:0.3px;">
            [Nombre Apellido]
          </td>
        </tr>
        <tr>
          <td style="padding:0 0 7px 0;font-family:'Courier New',monospace;font-size:11px;color:#313F50;letter-spacing:1px;text-transform:uppercase;line-height:1.3;">
            [Cargo] &middot; COICEM S.A.S
          </td>
        </tr>

        <!-- barra de acento dura — azul / grafito / naranja -->
        <tr>
          <td style="padding:0 0 9px 0;">
            <table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;">
              <tr>
                <td style="width:42px;height:3px;background-color:#025199;font-size:0;line-height:0;">&nbsp;</td>
                <td style="width:16px;height:3px;background-color:#313F50;font-size:0;line-height:0;">&nbsp;</td>
                <td style="width:14px;height:3px;background-color:#F79204;font-size:0;line-height:0;">&nbsp;</td>
              </tr>
            </table>
          </td>
        </tr>

        <tr>
          <td style="padding:0 0 2px 0;font-family:Arial,Helvetica,sans-serif;font-size:12px;color:#0B0E14;line-height:1.6;">
            <span style="color:#888888;font-family:'Courier New',monospace;font-size:10px;">M.</span>&nbsp;[+57 ___ ___ ____]
          </td>
        </tr>
        <tr>
          <td style="padding:0 0 2px 0;font-family:Arial,Helvetica,sans-serif;font-size:12px;color:#0B0E14;line-height:1.6;">
            <span style="color:#888888;font-family:'Courier New',monospace;font-size:10px;">E.</span>&nbsp;<a href="mailto:[correo@coicem.com]" style="color:#025199;text-decoration:none;">[correo@coicem.com]</a>
          </td>
        </tr>
        <tr>
          <td style="padding:0 0 8px 0;font-family:Arial,Helvetica,sans-serif;font-size:12px;color:#0B0E14;line-height:1.6;">
            <span style="color:#888888;font-family:'Courier New',monospace;font-size:10px;">W.</span>&nbsp;<a href="https://coicem.com" style="color:#025199;text-decoration:none;">coicem.com</a>
          </td>
        </tr>

        <tr>
          <td style="padding:0 0 4px 0;font-family:Arial,Helvetica,sans-serif;font-size:9px;color:#6B7785;font-style:italic;letter-spacing:0.4px;line-height:1.4;">
            Operacion &middot; Mantenimiento &middot; Construccion &middot; Energia &middot; Infraestructura
          </td>
        </tr>
        <tr>
          <td style="padding:0;font-family:'Courier New',monospace;font-size:8.5px;color:#9aa3ad;letter-spacing:0.6px;line-height:1.4;">
            ISO 9001 &middot; 14001 &middot; 45001 &middot; <span style="color:#F79204;">NORSOK 006:2020</span> &middot; Bureau Veritas
          </td>
        </tr>

      </table>
    </td>
  </tr>
</table>

</body></html>'''

with open(os.path.join(here, 'firma-correo.html'), 'w', encoding='utf-8') as f:
    f.write(sig)

dst = os.path.join(here, '..', 'coicem-web', 'public', 'internal')
os.makedirs(dst, exist_ok=True)
shutil.copy(os.path.join(here, 'firma-correo.html'), os.path.join(dst, 'firma-correo.html'))
print('firma-correo.html:', os.path.getsize(os.path.join(here, 'firma-correo.html')) // 1024, 'KB')
print('copiado a public/internal/')
