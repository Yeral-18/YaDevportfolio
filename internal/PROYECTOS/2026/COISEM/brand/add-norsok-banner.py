"""
add-norsok-banner.py — Añade 'NORSOK 006:2020' al banner Bureau Veritas existente
(que ya trae ISO 9001/14001/45001), conservando el sello BV original.
Inserta una franja roja con la línea nueva tras ISO 45001 y recentra el sello.
"""
from PIL import Image, ImageDraw, ImageFont
import os

here = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(here, "..", "coicem-web", "public", "images", "bureau-veritas.png")
b = Image.open(src).convert("RGBA")
W, H = b.size

# Líneas ISO detectadas: 156-219, 258-320, 361-424 (espaciado ~102). Gap hasta BV(506).
ISO_X = 88                 # x de inicio del texto ISO
LINE_H = 102               # espaciado entre líneas ISO
Y_AFTER_ISO3 = 424         # fin de ISO 45001:2018
X_SPLIT = int(W * 0.56)    # límite texto | sello

# Punto de inserción: justo después de ISO 45001
y_split = Y_AFTER_ISO3 + 12
new_H = H + LINE_H

# Franja roja: copiar una fila del área roja limpia (gap y=470) y estirarla
red_row = b.crop((0, 470, X_SPLIT, 471)).resize((X_SPLIT, LINE_H))

canvas = Image.new("RGBA", (W, new_H), (0, 0, 0, 0))
# 1) Parte superior izquierda (hasta ISO 45001 incl.)
canvas.paste(b.crop((0, 0, X_SPLIT, y_split)), (0, 0))
# 2) Franja roja para NORSOK
canvas.paste(red_row, (0, y_split))
# 3) Parte inferior izquierda (BUREAU VERITAS Certification), desplazada
canvas.paste(b.crop((0, y_split, X_SPLIT, H)), (0, y_split + LINE_H))
# 4) Sello (lado derecho completo) recentrado verticalmente
seal = b.crop((X_SPLIT, 0, W, H))
canvas.paste(seal, (X_SPLIT, (new_H - H) // 2), seal)

# 5) Texto NORSOK 006:2020 (Arial Bold, blanco, igual altura que las ISO)
draw = ImageDraw.Draw(canvas)
font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 70)
# alinear baseline aprox como las ISO (texto dentro de la franja)
ty = y_split + (LINE_H - 70) // 2 - 4
draw.text((ISO_X, ty), "NORSOK 006:2020", font=font, fill=(255, 255, 255, 255))

out = os.path.join(here, "bureau-veritas-norsok.png")
canvas.save(out)
print("OK", canvas.size, "->", os.path.basename(out))
