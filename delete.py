from pymongo import MongoClient
from pprint import pprint
import pandas as pd

cliente = MongoClient("mongodb://localhost:27017")
db = cliente["VolleyballDB"]

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