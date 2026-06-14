"""
rebuild-bv-banner.py — Banner Bureau Veritas: CUADRO ROJO uniforme (rectángulo
sólido completo) con el sello CONTENIDO dentro + 3 ISO + NORSOK 006:2020 +
'BUREAU VERITAS / Certification'. Texto grande (como el original).
"""
from PIL import Image, ImageDraw, ImageFont
import os

here = os.path.dirname(os.path.abspath(__file__))
orig = Image.open(os.path.join(here, "_bv_orig.png")).convert("RGBA")
W, H = orig.size
px = orig.load()
RED = (210, 33, 60, 255)

# 1) Recortar el óvalo del sello (gris, mitad derecha)
sx = []; sy = []
for y in range(0, H, 2):
    for x in range(950, W, 2):
        r, g, b, a = px[x, y]
        if a > 120 and 95 < r < 205 and abs(r - g) < 28 and abs(g - b) < 28:
            sx.append(x); sy.append(y)
oval = orig.crop((min(sx) - 12, min(sy) - 12, max(sx) + 12, max(sy) + 12))

# 2) Geometría del banner (compacto, texto grande)
PAD = 42
LINE = 84                  # renglón ISO/NORSOK
GAP = 32
BV_H = 104
CERT_H = 74
NH = PAD + LINE * 4 + GAP + BV_H + CERT_H + PAD
NW = 1500

# 3) Escalar el óvalo para que quede CONTENIDO en el alto del rojo (con margen)
target_h = NH - 64
scale = target_h / oval.height
oval = oval.resize((int(oval.width * scale), target_h), Image.LANCZOS)
ow, oh = oval.size

# 4) CUADRO ROJO uniforme = todo el lienzo
canvas = Image.new("RGBA", (NW, NH), RED)
draw = ImageDraw.Draw(canvas)

# 5) Sello contenido, a la derecha, centrado vertical (dentro del rojo)
canvas.alpha_composite(oval, (NW - ow - 40, (NH - oh) // 2))

# 6) Texto grande (Arial Bold blanco)
fb = lambda s: ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", s)
fr = lambda s: ImageFont.truetype("C:/Windows/Fonts/arial.ttf", s)
X = 64
y = PAD
for line in ["ISO 9001:2015", "ISO 14001:2015", "ISO 45001:2018", "NORSOK 006:2020"]:
    draw.text((X, y), line, font=fb(64), fill="white")
    y += LINE
y += GAP
draw.text((X, y), "BUREAU VERITAS", font=fb(82), fill="white"); y += BV_H
draw.text((X, y), "Certification", font=fr(60), fill="white")

out = os.path.join(here, "..", "coicem-web", "public", "images", "bureau-veritas.png")
canvas.save(out)
canvas.save(os.path.join(here, "bureau-veritas-norsok.png"))
print("OK banner uniforme:", canvas.size, "| oval:", (ow, oh))
