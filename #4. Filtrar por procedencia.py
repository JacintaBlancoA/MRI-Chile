#5
import pandas as pd
import glob
import os

# 📌 Carpeta con tus archivos Excel
carpeta = r"C:\Users\cuent\Downloads\Excels2023\filtrados"

# Lista para acumular todos los datos
df_total = pd.DataFrame()

# Leer todos los archivos xlsx de la carpeta
for archivo in glob.glob(os.path.join(carpeta, "*.xlsx")):
    df = pd.read_excel(archivo, header=0)
    
    # Asegurarse de que la columna de código sea consistente
    df["CodigoPrestacion"] = pd.to_numeric(df["CodigoPrestacion"], errors="coerce").astype("Int64")
    
    # Asegurarse de que las columnas de atención sean numéricas
    for col in ["Col25", "Col26", "Col27"]:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)
    
    # Acumular
    df_total = pd.concat([df_total, df], ignore_index=True)

# Agrupar por código y sumar cada tipo de atención
resumen = (
    df_total.groupby("CodigoPrestacion")[["Col25", "Col26", "Col27"]]
    .sum()
    .reset_index()
)

# Guardar en un Excel
resumen.to_excel("resumen_por_prestacion2023.xlsx", index=False)

print("Archivo resumen creado correctamente.")
