from pymongo import MongoClient
from pprint import pprint
import pandas as pd

cliente = MongoClient("mongodb://localhost:27017")
db = cliente["VolleyballDB"]
#premios están ligados a un jugador cuentan con titulo, de que liga son y cuando se entregaron
premios = db["awards"]
#Culturista son los jugadores que se dedican al culturismo, tienen un nombre, un apellido, fecha de nacimiento y no siempre están ligados a un equipo
culturista = db["body_builders"]
#Entredores cuentan con un nombre, un apellido, fecha de nacimiento, peso, altura, y no siempre están ligados a un equipo
entrenadores = db["coaches"]
#paises cuentan con su nombre y siglas de que le representan
paises = db["countries"]
#Partidas cuantan con nombre, fecha, la liga, el numero de set ganado por equipo, y el identificador de ambos equipos.
partidas = db["matches"]
#fisioterapistas que trabajan en clubes
#atributos: id de equipo, id de fisioterapista, nombre, apellido,fecha de nacimiento
fisioterapistas = db["physiotherapists"]
#juadores que juegan en clubes
#atributos: id de jugador, nombre, puntaje, peso, poisicion en la que juega, altura, codigo de pais, fecha de nacimiento
jugadores = db["players"]
#presidentes de los clubes
#atributos: id de presidente, nombre, apellido, id de equipo
presidentes = db["presidents"]
#oficinas de prensa de los clubes
#atributos: numero de oficina de prensa , primer nombre, segundo nombre, apellido, id de equipo
oficina_prensa = db["press_offices"]
#directores deportivos de los clubes
#atributos: id de director deportivo, nombre, apellido, fecha de nacimiento, id de equipo
directores = db["sport_directors"]
#estadios, guarda la ubicación de los estadios, junto con su nombre, año de apertura y capacidad
estadios = db["stadiums"]
#estrategas, guarda el nombre de los estrategas, en algunos casos junto con su fecha de nacimiento y/o id de equipo
estrategas = db["statisticians"]
#administradores, guarda el nombre de los administradores, en algunos casos junto con su id de equipo
administradores = db["team_mangers"]
#equipos, guarda el nombre de los equipos, junto con el año de fundacion,
#codigo de país y ciudad de origen, además del registro de partidos y torneos
equipos = db["teams"]
#transferencias, guarda el nombre del jugador, el equipo de origen y el equipo de destino, y el año de la transferencia
transferencias = db["transfers"]

cursor = estadios.find({})
data = list(cursor)

df = pd.DataFrame(data)

if '_id' in df.columns:
    df = df.drop(columns=['_id'])

print("\nDataFrame de Pandas:")
print(df.head())
print(f"\nNúmero de filas y columnas: {df.shape}")
print("\nInformación del DataFrame:")
df.info()