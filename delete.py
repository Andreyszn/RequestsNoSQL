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

#delete premio
premios.delete_one({"award_id": 99999})

#delete culturista
culturista.delete_one({"body_builder_id": 99999})

#delete entrenador
entrenadores.delete_one({"first_name": "Prueba", "last_name": "Korbeci"})

#delete pais
paises.delete_one({"country_code": "PRB"})

#delete partido
partidas.delete_one({"match_id": 99999})

#delete fisioterapista
fisioterapistas.delete_one({"first_name": "Deivis", "last_name": "LaFuente"})

#delete jugador
jugadores.delete_one({"player_id": 12345})

#delete presidente
presidentes.delete_one({"president_id": 12345})

#delete oficina de prensa
oficina_prensa.delete_one({"press_office_id": 12345}) 

#delete director deportivo
directores.delete_one({"sport_director_id": 12345}) 

#delete estadio
estadios.delete_one({"stadium_id": "a999"}) 

#delete estratega
estrategas.delete_one({"statisticians_id": 99999})

#delete administrador
administradores.delete_one({"team_manger_id": 99999})

#delete equipo
equipos.delete_one({"team_id": 999999})

#delete transferencia
transferencias.delete_one({"transfer_id": 99999})