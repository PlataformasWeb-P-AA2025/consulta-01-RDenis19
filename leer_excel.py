import pandas as pd
from conexion_base import obtener_coleccion

# Obtener la colección de MongoDB donde se guardarán los datos
coleccion = obtener_coleccion()

# Lista de archivos Excel con su año correspondiente
archivos = [("data/2022.xlsx", 2022), ("data/2023.xlsx", 2023)]

# Recorrer cada archivo y su año para leer y guardar en la base
for archivo, anio in archivos:
    # Lee el archivo Excel en un DataFrame
    df = pd.read_excel(archivo)
    # Agrege una columna "Año" para identificar el año de los datos
    df["Año"] = anio
    # Convierte el DataFrame a una lista de diccionarios para MongoDB
    data = df.to_dict(orient="records")
    # Insertar todos los registros en la colección de MongoDB
    coleccion.insert_many(data)

print("Datos insertados correctamente.")
