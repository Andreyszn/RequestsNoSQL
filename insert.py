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

#insert premio
premios.insert_one(
  {
  "award_id": 99999,
  "player_id": "p937",
  "award_name": "Prueba",
  "league": "Hubert Wagner Memorial",
  "award_date": 2006
}
)

#insert culturista
culturista.insert_one(
  {
  "body_builder_id": 99999,
  "first_name": "Prueba",
  "last_name": "prueba",
  "birth_date": "5/18/1965",
  "team_id": "t1674"
  })


#insert entrenador
entrenadores.insert_one(
  {
  "first_name": "Prueba",
  "last_name": "Korbeci",
  "weight": 0,
  "height": 0,
  "birth_date": "7/25/1983",
  "team_id": "t3843"
  })

#insert pais
paises.insert_one(
  {
  "country_code": "PRB",
  "country_name": "Prueba" 
  })

#insert partido
partidas.insert_one(
  {
  "match_id": 99999,
  "name": "Prueba",
  "date": "3/9/2023",
  "league": "Indonesian Proliga",
  "n_set_team1": 3,
  "n_set_team2": 0,
  "first_team_id": "t21660",
  "second_team_id": "t1867" 
  })

#insert fisioterapista
fisioterapistas.insert_one({
    "first_name": "Deivis",
    "last_name": "LaFuente",
    "birthdate": "2005-01-01",
    "team_id": "777"
})

#insert jugador
jugadores.insert_one({
    "player_id": "12345",
    "name": "Deivis",
    "ranking": "LaFuente",
    "weight": 86,
    "position": "Nose Guard",
    "height": 168,
    "country_code": "CR",
    "birthdate": "2000-05-15",
})

#insert presidente
presidentes.insert_one({
    "president_id": "12345",
    "first_name": "Charlie",
    "last_name": "Johanson",
    "birthdate": "1970-07-30",
    "team_id": "12345"
})

#insert oficina de prensa
oficina_prensa.insert_one({
    "press_office_id": "101",
    "first_name": "Alanis",
    "last_name": "Williams",
    "team_id": "67890"
})

#insert director deportivo
directores.insert_one({
    "sport_director_id": "12345",
    "first_name": "Keiron",
    "last_name": "Johnson",
    "birthdate": "1985-03-20",
    "team_id": "67890"
})


#insert estadio
estadios.insert_one({
  "stadium_id": "a999",
  "stadium_name": "la cancha de nances",
  "country_code": "CR",
  "town": "Esparza",
  "opening_year": 2019,
  "capacity": 15000
})

#insert estratega
estrategas.insert_one({
  "statisticians_id": 99999,
  "first_name": "kira",
  "last_name": "Yagami",
  "birthdate": {
    "$date": "1996-03-04T00:00:00.000Z"
  },
  "team_id": "t17153"
})

# #insert administrador
administradores.insert_one({
  "team_manger_id": 99999,
  "first_name": "Felipin",
  "last_name": "Felpudo",
  "team_id": "t1602",
  "birthdate": {
    "$date": "1970-04-20T00:00:00.000Z"
  }
})

#insert equipo
equipos.insert_one({
  "team_id": 999999,
  "team_name": "luisillo_Team",
  "country_code": "CR",
  "n_matches": 0,
  "n_tournaments": 0,
  "town": "Chomes",
  "founded": ""
})

#insert transferencia
transferencias.insert_one({
  "transfer_id": 99999,
  "player_name": "Luisillo Cascaste",
  "first_name": "Luisillo",
  "last_name": "Cascaste",
  "date": 2006,
  "old_team_id": "t2579",
  "new_team_id": "t1454"
})