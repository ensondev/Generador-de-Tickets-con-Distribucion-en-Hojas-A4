from PIL import Image, ImageDraw, ImageFont
import os

IMAGEN_BASE = "ticket_base.png"
CARPETA_SALIDA = "tickets"

# Fuente nativa de Windows (siempre está disponible)
FUENTE = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 70)

# Coordenadas del rectángulo blanco (ajustadas)
POS_X = 1000
POS_Y = 1800

os.makedirs(CARPETA_SALIDA, exist_ok=True)

for n in range(10000):
    numero = f"N° {n:04d}"

    img = Image.open(IMAGEN_BASE).convert("RGBA")
    draw = ImageDraw.Draw(img)

    draw.text((POS_X, POS_Y), numero, fill="black", font=FUENTE)

    img.save(os.path.join(CARPETA_SALIDA, f"ticket_{n:04d}.png"))

print("LISTO: Se generaron todos los tickets con números visibles.")
