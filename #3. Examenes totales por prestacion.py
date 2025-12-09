#2
import pandas as pd
import glob
import os

# Ruta a tu carpeta con los excels filtrados
carpeta = r"C:\Users\cuent\Downloads\Excels2025"

# Buscar todos los archivos filtrados
archivos = glob.glob(os.path.join(carpeta, "*.xlsx"))

columna_suma = "Col03"  
suma_col03 = []   # lista donde guardaremos los resultados

for archivo in archivos:
    try:
        df = pd.read_excel(archivo)

        if columna_suma not in df.columns:
            print(f"⚠️ El archivo {archivo} no tiene la columna '{columna_suma}'")
            continue

        # Sumar la columna Col03
        total = df[columna_suma].sum()

        # Guardar el valor en la lista junto con el nombre del archivo
        suma_col03.append((os.path.basename(archivo), total))

    except Exception as e:
        print(f"❌ Error en {archivo}: {e}")

# Mostrar resultados
for nombre, total in suma_col03:
    print(f"{nombre} {total}")
