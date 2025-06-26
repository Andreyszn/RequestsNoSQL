from matplotlib import pyplot as plt
from pymongo import MongoClient
from pprint import pprint
import pandas as pd

cliente = MongoClient("mongodb://localhost:27017")
db = cliente["VolleyBallDB"]

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

#1. Estadio con mayor capacidad
mayor_estadio = list(estadios.aggregate([
    {
        "$sort": {"capacity": -1}
    },
    {
        "$limit": 1
    },
    {
        "$project": {
            "_id": 0,
            "nombre_estadio": "$name",
            "capacidad": "$capacity"
        }
    }
]))
pprint("El estadio con mayor capacidad es: ")
pprint(mayor_estadio)

#2. total de equipos por pais
equipos_por_pais = equipos.aggregate([
    {"$group": {"_id": "$country_code", "total_equipos": {"$sum": 1}}},
    {"$sort": {"_id": 1}}])
print("\nTotal de equipos por país:")
pprint(list(equipos_por_pais))

#3. mostrar todos los partidos ganados por el equipo VfB Friedrichshafen (team_id: "t1960")
partidos_vfb = partidas.aggregate([
    {"$match": {"$or": [{"first_team_id": "t1960"}, {"second_team_id": "t1960"}]}},
    {"$addFields": {
        "vfb_friedrichshafen_won": {
            "$cond": {
                "if": { "$eq": ["$first_team_id", "t1960"] },
                "then": { "$gt": ["$n_set_team1", "$n_set_team2"] }, 
                "else": { "$gt": ["$n_set_team2", "$n_set_team1"] }
            }
        }
    }},
    {"$match": {"vfb_friedrichshafen_won": True}},
    {"$project": {
        "_id": 0,
        "date": 1,
        "league": 1,
        "first_team_id": 1,
        "second_team_id": 1,
        "n_set_team1": 1,
        "n_set_team2": 1
    }},
    {"$sort": {"date": -1}}])
print("\nPartidos ganados por el equipo VfB Friedrichshafen:")
pprint(list(partidos_vfb))

#4. Cual ha sido el equipo del que se han ido más jugadores y cuantos han sido
pprint(list(equipos.aggregate([
    {
        "$lookup": {
            "from": "transfers",
            "localField": "team_id",
            "foreignField": "old_team_id",
            "as": "transfers"
        }
    },
    {
        "$project": {
            "team_name": 1,
            "n_transfers": {"$size": "$transfers"}
        }
    },
    {
        "$sort": {"n_transfers": -1}
    },
    {
        "$limit": 1
    }
])))

#5. Cual es es el pais con más jugadores en el ranking 2000
topRank = list(jugadores.aggregate([
    {
        "$match": {
            "ranking": {"$lte": 2000}
        }
    },
    {
        "$group": {
            "_id": "$country_code",
            "count": {"$sum": 1}
        }
    },
    {
        "$sort": {"count": -1}
    },
    {
        "$limit": 1
    },
    {
        "$lookup": {
            "from": "countries",
            "localField": "_id",
            "foreignField": "country_code",
            "as": "country_info"
        }
    },
    {
        "$unwind": "$country_info"
    },
    {
        "$project": {
            "country_name": "$country_info.name",
            "count" : 1
        }
    }
]))
pprint("El país con más jugadores en el ranking 2000 es ")
pprint(topRank)

#6. Obteniene el país cuyos jugadores han ganado más premios y cuántos premios tiene ese país
result = list(jugadores.aggregate([
    {
        "$lookup": {
            "from": "awards",
            "localField": "player_id",
            "foreignField": "player_id",
            "as": "awards"
        }
    },
    {
        "$group": {
            "_id": "$country_code",
            "total_awards": {"$sum": {"$size": "$awards"}}
        }
    },
    {
        "$sort": {"total_awards": -1}
    },
    {
        "$limit": 1
    },
    {
        "$lookup": {
            "from": "countries",
            "localField": "_id",
            "foreignField": "country_code",
            "as": "country_info"
        }
    },
    {
        "$unwind": "$country_info"
    },
    {
        "$project": {
            "country_name": "$country_info.name",
            "total_awards": 1
        }
    }
]))
pprint("El paise con más premios es ")
pprint(result)


#Visualizaciones

print("\nGráfico de barras: Número de transferencias por año")
canciones_por_año = transferencias.aggregate([{"$group": {"_id": "$date", "cantidad": {"$sum": 1}}}, {"$sort": {"_id": 1}}])
años = [] 
cantidades = []
for doc in canciones_por_año:
    años.append(doc["_id"])
    cantidades.append(doc["cantidad"])
plt.bar(años, cantidades)
plt.xlabel("Año")
plt.ylabel("Número de transferencias")
plt.title("Número de transferencias por Año")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()