import os

carpeta = r"/Users/d.s/Desktop/projec_gabi/photos"
prefijo = "gabi"
extensiones = (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".heic")

archivos = os.listdir(carpeta)
contador = 0

for archivo in archivos:
    nombre_lower = archivo.lower()
    if nombre_lower.endswith(extensiones):
        extension = os.path.splitext(archivo)[1]
        nuevo_nombre = f"{prefijo}{contador}{extension}"

        ruta_vieja = os.path.join(carpeta, archivo)
        ruta_nueva = os.path.join(carpeta, nuevo_nombre)

        print(f"Renombrando: {archivo} → {nuevo_nombre}")
        os.rename(ruta_vieja, ruta_nueva)
        contador += 1

print("Total renombradas:", contador)
