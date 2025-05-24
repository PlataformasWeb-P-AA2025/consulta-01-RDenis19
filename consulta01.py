from conexion_base import obtener_coleccion

# Obtiene la colección de la base de datos
coleccion = obtener_coleccion()

print("Primeros 10 partidos del 2023 en la ronda 'Quarterfinals' con el Ganador de la Ronda y el Perdedor:\n")

# Busca partidos del año 2023 en la ronda Quarterfinals 
# Ordena por fecha ascendente y solo presenta los 10 primeras resultados
resultados = coleccion.find({
    "Año": 2023,
    "Round": "Quarterfinals"
}).sort("Date", 1).limit(10)

for partido in resultados:
    print(f"Winner: {partido.get('Winner')} - Loser: {partido.get('Loser')} - Round: {partido.get('Round')}")
