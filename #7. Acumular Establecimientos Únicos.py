#HospTot
import pandas as pd

# 📌 Rutas de tus archivos
archivos = [
    r"C:\Users\cuent\Downloads\Codigo\hospitales_unicos2023.xlsx",
    r"C:\Users\cuent\Downloads\Codigo\hospitales_unicos2024.xlsx",
    r"C:\Users\cuent\Downloads\Codigo\hospitales_unicos2025.xlsx"
]

# Lista para acumular los hospitales
hospitales = []

# Leer cada archivo y acumular los nombres
for archivo in archivos:
    df = pd.read_excel(archivo)
    hospitales.extend(df["Hospital"].dropna().tolist())

# Convertir a conjunto para eliminar duplicados y luego a lista
hospitales_unicos = sorted(set(hospitales))

# Pasar a DataFrame
df_unicos = pd.DataFrame(hospitales_unicos, columns=["Hospital"])

# Guardar en un nuevo Excel
df_unicos.to_excel("hospitales_unicos.xlsx", index=False)

print("Archivo creado con hospitales únicos de los tres archivos.")
