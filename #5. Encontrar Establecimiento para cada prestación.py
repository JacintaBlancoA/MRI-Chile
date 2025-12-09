#3

import pandas as pd
import glob
import os

# 📌 Ruta a la carpeta de excels filtrados
carpeta = r"C:\Users\cuent\Downloads\Excels2025"

# 📌 Ruta al archivo que contiene el diccionario
archivo_diccionario = r"C:\Users\cuent\Downloads\Copia-de-Establecimientos-DEIS-MINSAL-18-02-2025.xlsx"


# Cargar hoja específica del diccionario
# (si no sabes el nombre de la hoja puedes usar sheet_name=None para ver todas)
diccionario = pd.read_excel(archivo_diccionario, sheet_name="B ESTABLECIMIENTO_2025-02-18 ",header=1)
print(diccionario.columns.tolist())

# Nos aseguramos que las columnas se lean bien
diccionario = diccionario[["Código Vigente", "Nombre Oficial"]]

# Convertir a números enteros seguros
diccionario["Código Vigente"] = pd.to_numeric(diccionario["Código Vigente"], errors="coerce").astype("Int64")

resultados = []


df_total = pd.DataFrame()

for archivo in glob.glob(os.path.join(carpeta, "*.xlsx")):
    df = pd.read_excel(archivo, header=0)
    
    # Asegurar que IdEstablecimiento sea str
    df["IdEstablecimiento"] = pd.to_numeric(df["IdEstablecimiento"], errors="coerce").astype("Int64")
    
    # Unir con el diccionario para obtener el nombre oficial
    df = df.merge(diccionario, left_on="IdEstablecimiento", right_on="Código Vigente", how="left")
    
    # Acumular
    df_total = pd.concat([df_total, df], ignore_index=True)

# === 3. Agrupar por prestación y mostrar establecimientos ===
prestaciones_establecimientos = (
    df_total.groupby("CodigoPrestacion")["Nombre Oficial"]
    .unique()  # valores distintos por prestación
    .reset_index()
)

# ✨ Desglosar la lista en filas individuales
prestaciones_establecimientos = prestaciones_establecimientos.explode("Nombre Oficial")

# Guardar en Excel
prestaciones_establecimientos.to_excel("prestaciones_establecimientos_desglosadas2025.xlsx", index=False)

print("Archivo creado correctamente con cada establecimiento en una fila.")