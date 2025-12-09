
import pandas as pd
import sqlite3

import duckdb


csv_path = r'C:/Users/cuent/OneDrive/Escritorio/SerieBS2024.csv'


query = f"""
SELECT *
FROM read_csv_auto('{csv_path}')
WHERE CodigoPrestacion = '01014726'
"""

df_filtrado = duckdb.query(query).to_df()

df_filtrado.to_excel("(2024)0405026.xlsx", index=False)

