import os
from pillow_heif import register_heif_opener
from PIL import Image

# Habilitar soporte HEIC
register_heif_opener()

carpeta = r"/Users/d.s/Desktop/project_gabi/img"  # cambia si es necesario

for archivo in os.listdir(carpeta):
    if archivo.lower().endswith(".heic"):
        ruta_heic = os.path.join(carpeta, archivo)
        ruta_jpg = os.path.join(carpeta, archivo.rsplit(".", 1)[0] + ".jpg")

        print(f"Convirtiendo: {archivo} → {os.path.basename(ruta_jpg)}")

        imagen = Image.open(ruta_heic)
        imagen = imagen.convert("RGB")  # necesario para JPG
        imagen.save(ruta_jpg, "JPEG", quality=90)

print("Conversión completada.")
