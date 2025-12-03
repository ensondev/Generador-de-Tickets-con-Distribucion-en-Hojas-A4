from PIL import Image
import os
import math

# Carpeta donde están los tickets generados
CARPETA_TICKETS = "tickets"

# Carpeta donde se guardarán las hojas A4
SALIDA = "hojas"
os.makedirs(SALIDA, exist_ok=True)

# Tamaño de hoja A4 a 300 DPI
A4_WIDTH = 2480
A4_HEIGHT = 3508

# Columnas y filas por hoja
COLS = 4
ROWS = 4
TICKETS_POR_HOJA = COLS * ROWS

# Leer lista de tickets
tickets = sorted([f for f in os.listdir(CARPETA_TICKETS) if f.endswith(".png")])
total = len(tickets)
hojas_necesarias = math.ceil(total / TICKETS_POR_HOJA)

print(f"Total tickets: {total}")
print(f"Hojas necesarias: {hojas_necesarias}")

# Crear cada hoja
for h in range(hojas_necesarias):
    # Crear hoja A4 en blanco
    hoja = Image.new("RGB", (A4_WIDTH, A4_HEIGHT), "white")

    # Tickets para esta hoja
    inicio = h * TICKETS_POR_HOJA
    fin = inicio + TICKETS_POR_HOJA
    subset = tickets[inicio:fin]

    print(f"Procesando hoja {h+1}/{hojas_necesarias}...")

    # Calcular el tamaño máximo para cada ticket sin deformar
    cell_w = A4_WIDTH // COLS
    cell_h = A4_HEIGHT // ROWS

    for i, tk in enumerate(subset):
        img = Image.open(os.path.join(CARPETA_TICKETS, tk))

        # Escalar proporcionalmente
        img.thumbnail((cell_w, cell_h))

        # Calcular posición en la grilla
        row = i // COLS
        col = i % COLS

        x = col * cell_w + (cell_w - img.width) // 2
        y = row * cell_h + (cell_h - img.height) // 2

        hoja.paste(img, (x, y))

    # Guardar como PDF o PNG
    salida_archivo = os.path.join(SALIDA, f"hoja_{h+1:04d}.pdf")
    hoja.save(salida_archivo, "PDF")

print("Todas las hojas han sido generadas.")
