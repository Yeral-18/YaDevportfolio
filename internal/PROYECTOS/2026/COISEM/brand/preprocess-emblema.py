"""
preprocess-emblema.py — Limpia el emblema antes de vectorizar para quitar las
'texturas en los bordes' que deja vtracer sobre un JPEG ruidoso.
Técnica: upscale (más píxeles → trazado suave) + median filter (quita ruido JPEG)
+ quantize (capas de color limpias) + alpha binario (borde exterior nítido).
"""
from PIL import Image, ImageFilter
import os

here = os.path.dirname(os.path.abspath(__file__))
img = Image.open(os.path.join(here, "emblema-original-limpio.png")).convert("RGBA")

# 1) Upscale 3x con LANCZOS (más resolución para bordes suaves)
img = img.resize((img.width * 3, img.height * 3), Image.LANCZOS)

# 2) Separar alpha; trabajar el color
r, g, b, a = img.split()
rgb = Image.merge("RGB", (r, g, b))

# 3) Median filter → elimina ruido de compresión JPEG (motas en los bordes)
rgb = rgb.filter(ImageFilter.MedianFilter(size=5))
# leve suavizado adicional
rgb = rgb.filter(ImageFilter.SMOOTH_MORE)

# 4) Quantize a 20 colores → vtracer hace capas limpias (no traza cada gradiente sucio)
rgb = rgb.quantize(colors=20, method=Image.MEDIANCUT, dither=Image.NONE).convert("RGB")

# 5) Alpha binario → borde exterior nítido (sin halo semitransparente que textura)
a = a.point(lambda v: 255 if v > 120 else 0)
a = a.filter(ImageFilter.MedianFilter(size=5))  # suaviza el contorno binario

out = Image.merge("RGBA", (*rgb.split(), a))
out.save(os.path.join(here, "emblema-pre.png"))
print("OK emblema-pre:", out.size)
