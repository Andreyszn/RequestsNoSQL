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

#update premio
premios.update_one(
  {"award_id": 99997},
  {"$set": {
    "player_id": "p1234",
    "award_name": "Updated Award",
    "league": "Updated League",
    "award_date": 2023
  }}
)

#update culturista
culturista.update_one(
  {"body_builder_id": 99999},
  {"$set": {
    "first_name": "Updated Name",
    "last_name": "Updated Last Name",
    "birth_date": "1/1/2000",
    "team_id": "t1234"
  }}
)

#update entrenador
entrenadores.update_one(
  {"first_name": "Prueba", "last_name": "Korbeci"},
  {"$set": {
    "weight": 80,
    "height": 190,
    "birth_date": "8/15/1985",
    "team_id": "t5678"
  }}
)

#update pais
paises.update_one(
  {"country_code": "PRB"},
  {"$set": {
    "country_name": "Updated Country"
  }}
)

#update partido
partidas.update_one(
  {"match_id": 99999},
  {"$set": {
    "name": "Updated Match",
    "date": "4/1/2023",
    "league": "Updated League",
    "n_set_team1": 2,
    "n_set_team2": 3,
    "first_team_id": "t1234",
    "second_team_id": "t5678"
  }}
)

#update fisioterapista
fisioterapistas.update_one(
    {"first_name": "Deivis", "last_name": "LaFuente"},
    {"$set": {
        "birth_date": "1991-01-01",
        "team_id": "12345"
    }}
)

#update jugador
jugadores.update_one(
    {"player_id": 12345},
    {"$set": {
        "name": "Updated Player",
        "ranking": "Updated Ranking",
        "weight": 75,
        "position": "Outside Hitter",
        "height": 185,
        "country_code": "USA",
        "birth_date": "1996-06-20"
    }}
)

#update presidente
presidentes.update_one(
    {"president_id": 12345},
    {"$set": {
      "first_name": "Charlie",
      "last_name": "Brown",
      "birth_date": "1970-07-30",
      "team_id": "67890"
      }}
    )

#update oficina de prensa
oficina_prensa.update_one(
    {"press_office_id": 12345},
    {"$set": {
        "first_name": "Updated First Name",
        "last_name": "Updated Last Name",
        "team_id": "12345"
    }}
)

#update director deportivo
directores.update_one(
    {"sport_director_id": 12345},
    {"$set": {
        "first_name": "Updated First Name",
        "last_name": "Updated Last Name",
        "birth_date": "1986-04-15",
        "team_id": "12345"
    }}
)

#update estadio
estadios.update_one(
    {"stadium_id": "a999"},
    {"$set": {
        "stadium_name": "Updated Stadium Name",
        "country_code": "CR",
        "town": "Updated Town",
        "opening_year": 2020,
        "capacity": 20000
    }}
)

#update estratega
estrategas.update_one(
    {"statisticians_id": 99999},
    {"$set": {
        "first_name": "Updated Kira",
        "last_name": "Updated Yagami",
        "birthdate": {
            "$date": "1997-04-04T00:00:00.000Z"
        },
        "team_id": "t12345"
    }}
)

#update administrador

#update equipo
equipos.update_one(
    {"team_id": 999999},
    {"$set": {
        "team_name": "Updated Team Name",
        "country_code": "CR",
        "n_matches": 10,
        "n_tournaments": 5,
        "town": "Updated Town",
        "founded": 2000
    }}
)

#update transferencia
transferencias.update_one(
    {"transfer_id": 99999},
    {"$set": {
        "player_name": "Updated Player Name",
        "first_name": "Updated First Name",
        "last_name": "Updated Last Name",
        "date": 2023,
        "old_team_id": "t1234",
        "new_team_id": "t5678"
    }}
)