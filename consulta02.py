from conexion_base import obtener_coleccion

# Obtener la colección de la base de datos
coleccion = obtener_coleccion()

print("Primeros 10 partidos del 2022 ganados por Nadal R. y en el torneo en que los gano:\n")


# Busca partidos del 2022 donde ganó Nadal R.
# Muestra solo los campos Winner y Tournament solo los 10 primeros
resultados = coleccion.find(
    {"Año": 2022, "Winner": "Nadal R."},
    {"_id": 0, "Winner": 1, "Tournament": 1}  
).limit(10)

for partido in resultados:
    print(f"Winner: {partido.get('Winner')} - Tournament: {partido.get('Tournament')}")
