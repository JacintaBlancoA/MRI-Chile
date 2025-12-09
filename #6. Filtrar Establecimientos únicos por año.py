#FiltrarHosp
import pandas as pd

# 📌 Cargar tu Excel
archivo = r"C:\Users\cuent\Downloads\Codigo\prestaciones_establecimientos_desglosadas2023.xlsx"
df = pd.read_excel(archivo)

# 📌 Supongamos que la columna se llama "Hospital"
hospitales_unicos = df["Nombre Oficial"].dropna().unique()   # elimina duplicados y nulos

# Convertimos a DataFrame para guardarlo en Excel
df_unicos = pd.DataFrame(hospitales_unicos, columns=["Hospital"])

# 📌 Guardar en un nuevo archivo
df_unicos.to_excel("hospitales_unicos2023.xlsx", index=False)

print("Archivo creado con hospitales únicos.")
