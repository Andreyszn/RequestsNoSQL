# #insert premio
# premios.insert_one(
#   {
#   "award_id": 99999,
#   "player_id": "p937",
#   "award_name": "Prueba",
#   "league": "Hubert Wagner Memorial",
#   "award_date": 2006
# }
# )

# #insert culturista
# culturista.insert_one(
#   {
#   "body_builder_id": 99999,
#   "first_name": "Prueba",
#   "last_name": "prueba",
#   "birth_date": "5/18/1965",
#   "team_id": "t1674"
#   })

# #insert entrenador
# entrenadores.insert_one(
#   {
#   "first_name": "Prueba",
#   "last_name": "Korbeci",
#   "weight": 0,
#   "height": 0,
#   "birth_date": "7/25/1983",
#   "team_id": "t3843"
#   })

# #insert pais
# paises.insert_one(
#   {
#   "country_code": "PRB",
#   "country_name": "Prueba" 
#   })

# #insert partido
# partidas.insert_one(
#   {
#   "match_id": 99999,
#   "name": "Prueba",
#   "date": "3/9/2023",
#   "league": "Indonesian Proliga",
#   "n_set_team1": 3,
#   "n_set_team2": 0,
#   "first_team_id": "t21660",
#   "second_team_id": "t1867" 
#   })

# #insert fisioterapista
# fisioterapistas.insert_one({
#     "first_name": "Deivis",
#     "last_name": "LaFuente",
#     "birthdate": "2005-01-01",
#     "team_id": "777"
# })

# #insert jugador
# jugadores.insert_one({
#     "player_id": "12345",
#     "name": "Deivis",
#     "ranking": "LaFuente",
#     "weight": 86,
#     "position": "Nose Guard",
#     "height": 168,
#     "country_code": "CR",
#     "birthdate": "2000-05-15",
# })

# #insert presidente
# presidentes.insert_one({
#     "president_id": "12345",
#     "first_name": "Charlie",
#     "last_name": "Johanson",
#     "birthdate": "1970-07-30",
#     "team_id": "12345"
# })

# #insert oficina de prensa
# oficina_prensa.insert_one({
#     "press_office_id": "101",
#     "first_name": "Alanis",
#     "last_name": "Williams",
#     "team_id": "67890"
# })

# #insert director deportivo
# directores.insert_one({
#     "sport_director_id": "12345",
#     "first_name": "Keiron",
#     "last_name": "Johnson",
#     "birthdate": "1985-03-20",
#     "team_id": "67890"
# }) (editado)


#insert estadio
# estadios.insert_one({
#   "stadium_id": "a999",
#   "stadium_name": "la cancha de nances",
#   "country_code": "CR",
#   "town": "Esparza",
#   "opening_year": 2019,
#   "capacity": 15000
# })

#insert estratega
# estrategas.insert_one({
#   "statisticians_id": 99999,
#   "first_name": "kira",
#   "last_name": "Yagami",
#   "birthdate": {
#     "$date": "1996-03-04T00:00:00.000Z"
#   },
#   "team_id": "t17153"
# })

# #insert administrador
# administradores.insert_one({
#   "team_manger_id": 99999,
#   "first_name": "Felipin",
#   "last_name": "Felpudo",
#   "team_id": "t1602",
#   "birthdate": {
#     "$date": "1970-04-20T00:00:00.000Z"
#   }
# })

#insert equipo
# equipos.insert_one({
#   "team_id": 999999,
#   "team_name": "luisillo_Team",
#   "country_code": "CR",
#   "n_matches": 0,
#   "n_tournaments": 0,
#   "town": "Chomes",
#   "founded": ""
# })

#insert transferencia
# transferencias.insert_one({
#   "transfer_id": 99999,
#   "player_name": "Luisillo Cascaste",
#   "first_name": "Luisillo",
#   "last_name": "Cascaste",
#   "date": 2006,
#   "old_team_id": "t2579",
#   "new_team_id": "t1454"
# })