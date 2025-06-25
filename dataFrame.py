from pymongo import MongoClient
from pprint import pprint
import pandas as pd

cliente = MongoClient("mongodb://localhost:27017")
db = cliente["VolleyballDB"]

colecciones = {
    "premios": db["awards"],
    "culturista": db["body_builders"],
    "entrenadores": db["coaches"],
    "paises": db["countries"],
    "partidas": db["matches"],
    "fisioterapistas": db["physiotherapists"],
    "jugadores": db["players"],
    "presidentes": db["presidents"],
    "oficina_prensa": db["press_offices"],
    "directores": db["sport_directors"],
    "estadios": db["stadiums"],
    "estrategas": db["statisticians"],
    "administradores": db["team_mangers"],
    "equipos": db["teams"],
    "transferencias": db["transfers"]
}

dataframes = {}

for nombre, coleccion in colecciones.items():
    df = pd.DataFrame(coleccion.find())
    df.drop(columns=['_id'], inplace=True, errors='ignore')
    dataframes[nombre] = df
    print(f"\n Nombre del DataFrame: {nombre}")
    print(df.head())
    print(f"Dimensiones (filas, columnas): {df.shape}")
    print("Información general:")
    df.info()