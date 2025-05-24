from pymongo import MongoClient

def obtener_coleccion():
    client = MongoClient('mongodb://localhost:27017')
    db = client["Consulta"]
    return db["datos_excel"]
