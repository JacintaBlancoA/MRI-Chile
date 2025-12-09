import pandas as pd
import glob
import os

# Ruta a tu carpeta (ajusta a la tuya)
carpeta = r"C:\Users\cuent\Downloads\Excels2"

# Buscar todos los archivos .xlsx que se llamen 01.xlsx, 02.xlsx, ..., 42.xlsx
archivos = sorted(glob.glob(os.path.join(carpeta, "*.xlsx")))

# Nombre de la columna que quieres filtrar
columna_filtro = "Col01"  # cámbiala al nombre real de tu columna

for archivo in archivos:
    print(f"Procesando {archivo}...")

    # Leer archivo
    df = pd.read_excel(archivo)

    # Filtrar filas (conservar solo las que NO son 0 en esa columna)
    df_filtrado = df[df[columna_filtro] != 0]

    # Crear nombre de salida (por ejemplo en subcarpeta "filtrados")
    salida = os.path.join(carpeta, "filtrados")
    os.makedirs(salida, exist_ok=True)
    nombre_salida = os.path.join(salida, os.path.basename(archivo))

    # Guardar archivo reducido
    df_filtrado.to_excel(nombre_salida, index=False)

print("✅ Listo: todos los archivos filtrados guardados en la carpeta 'filtrados'")


