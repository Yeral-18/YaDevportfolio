"""
clean-original.py — Limpia el JPEG original del logo COICEM para vectorizar.
Quita el fondo negro (→ transparente), recorta al contenido, y separa:
  - logo-original-limpio.png  (lockup completo: emblema + wordmark)
  - emblema-original-limpio.png (solo el isotipo circular, mitad izquierda)
Salida en alta resolución para que la vectorización conserve el detalle.
"""
from PIL import Image
import os

SRC = "../WhatsApp Image 2026-06-12 at 8.10.47 AM.jpeg"
here = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(here, SRC)

img = Image.open(src).convert("RGBA")
W, H = img.size
px = img.load()

# 1) Fondo negro → transparente (luma bajo)
THRESH = 34
for y in range(H):
    for x in range(W):
        r, g, b, a = px[x, y]
        luma = 0.299 * r + 0.587 * g + 0.114 * b
        if luma < THRESH:
            # alpha proporcional cerca del umbral (borde suave)
            if luma < 18:
                px[x, y] = (r, g, b, 0)
            else:
                px[x, y] = (r, g, b, int((luma - 18) * 255 / (THRESH - 18)))

# 2) Bounding box del contenido (lockup completo)
bbox = img.getbbox()
lockup = img.crop(bbox)
lockup.save(os.path.join(here, "logo-original-limpio.png"))
print("OK lockup:", lockup.size)

# 3) Emblema solo: recortar la porción circular izquierda del lockup
lw, lh = lockup.size
emblema = lockup.crop((0, 0, int(lh * 1.05), lh))  # cuadrado izquierdo
emblema = emblema.crop(emblema.getbbox())
emblema.save(os.path.join(here, "emblema-original-limpio.png"))
print("OK emblema:", emblema.size)
