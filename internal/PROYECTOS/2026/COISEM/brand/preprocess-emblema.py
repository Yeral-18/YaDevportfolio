"""
preprocess-emblema.py — Limpieza BALANCEADA del emblema antes de vectorizar.
Limpia el borde exterior (alpha) sin destruir los colores (grises metálicos).
Lección: blur fuerte + quantize bajo vuelve los grises MARRONES. Mantener suave.
"""
from PIL import Image, ImageFilter
import os

here = os.path.dirname(os.path.abspath(__file__))
img = Image.open(os.path.join(here, "emblema-original-limpio.png")).convert("RGBA")

# 1) Upscale 3x
img = img.resize((img.width * 3, img.height * 3), Image.LANCZOS)
r, g, b, a = img.split()

# 2) COLOR: blur MUY suave + quantize alto (preserva grises metálicos)
rgb = Image.merge("RGB", (r, g, b))
rgb = rgb.filter(ImageFilter.GaussianBlur(0.8))
rgb = rgb.quantize(colors=32, method=Image.MEDIANCUT, dither=Image.NONE).convert("RGB")

# 3) ALPHA: el trabajo principal — contorno exterior nítido sin halo.
#    binario → median (motas) → apertura ligera (limpia el borde sucio) → blur leve
a = a.point(lambda v: 255 if v > 130 else 0)
a = a.filter(ImageFilter.MedianFilter(7))
a = a.filter(ImageFilter.MinFilter(3))   # erosiona 1px (come halo)
a = a.filter(ImageFilter.MaxFilter(3))   # dilata 1px (recupera)
a = a.filter(ImageFilter.GaussianBlur(1.0))

out = Image.merge("RGBA", (*rgb.split(), a))
out.save(os.path.join(here, "emblema-pre.png"))
print("OK emblema-pre:", out.size)
