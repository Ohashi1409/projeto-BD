from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://root:rootpassword@cluster0.wtuzryd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))
database = client.get_database('codeforces')

if "User_1_1" in database.list_collection_names():
    database.drop_collection("User_1_1")
if "Contest_1_1" in database.list_collection_names():
    database.drop_collection("Contest_1_1")

# 1 documento referenciando apenas 1 documento
user = database.create_collection("User_1_1")
contest = database.create_collection("Contest_1_1")

user_docs = [
  {
    "id": "user_1",
    "user_name": "Alyssa Wright",
    "email": "rebeccalopez@crosby-harvey.com",
    "rating": 1140,
    "password": "3%UZ4W4dP(",
    "user_city": "East Carly",
    "user_country": "Tonga",
    "user_state": "Kansas",
    "registration_date": "2023-08-14 19:24:35"
  },
  {
    "id": "user_2",
    "user_name": "Jacob Gaines",
    "email": "qswanson@harris-francis.biz",
    "rating": 1153,
    "password": "X7UJCm!x(Z",
    "user_city": "Aliciaside",
    "user_country": "Wallis and Futuna",
    "user_state": "North Dakota",
    "registration_date": "2023-06-22 13:06:43"
  },
  {
    "id": "user_3",
    "user_name": "Lauren Chavez",
    "email": "jwillis@king.biz",
    "rating": 2431,
    "password": "J+ah@9Bl78",
    "user_city": "Gomezchester",
    "user_country": "Cameroon",
    "user_state": "Alaska",
    "registration_date": "2021-06-18 14:45:55"
  }
]
user_ids = user.insert_many(user_docs).inserted_ids

contest_docs = [
  {
    "contest_id": 6,
    "group_id": 101,
    "user_id_creator": user_ids[0],
    "is_private": 0,
    "startTime": "2025-06-15 14:00:00",
    "frozen_contest": 0,
    "contest_duration": "02:00:00",
    "contest_name": "Aquecimento Maratona Pernambucana"
  },
  {
    "contest_id": 7,
    "group_id": 101,
    "user_id_creator": user_ids[0],
    "is_private": 1,
    "startTime": "2025-07-20 14:00:00",
    "frozen_contest": 1,
    "contest_duration": "02:30:00",
    "contest_name": "Desafio de Algoritmos I - Privado"
  },
  {
    "contest_id": 8,
    "group_id": 102,
    "user_id_creator": user_ids[0],
    "is_private": 0,
    "startTime": "2025-08-10 10:00:00",
    "frozen_contest": 0,
    "contest_duration": "03:00:00",
    "contest_name": "Simulado Aberto - Estrutura de Dados"
  },
  {
    "contest_id": 9,
    "group_id": 201,
    "user_id_creator": user_ids[1],
    "is_private": 0,
    "startTime": "2025-05-01 19:00:00",
    "frozen_contest": 0,
    "contest_duration": "01:30:00",
    "contest_name": "Speedrun de Problemas Fáceis"
  },
  {
    "contest_id": 10,
    "group_id": 201,
    "user_id_creator": user_ids[1],
    "is_private": 1,
    "startTime": "2025-06-05 19:00:00",
    "frozen_contest": 0,
    "contest_duration": "05:00:00",
    "contest_name": "Contest Longo da Techspace"
  },
  {
    "contest_id": 11,
    "group_id": 202,
    "user_id_creator": user_ids[1],
    "is_private": 0,
    "startTime": "2025-08-01 18:00:00",
    "frozen_contest": 0,
    "contest_duration": "02:00:00",
    "contest_name": "Preparatório Olinda Codefest"
  },
  {
    "contest_id": 12,
    "group_id": 301,
    "user_id_creator": user_ids[2],
    "is_private": 0,
    "startTime": "2025-07-01 10:00:00",
    "frozen_contest": 0,
    "contest_duration": "04:00:00",
    "contest_name": "Global Code Challenge - UK Round"
  },
  {
    "contest_id": 13,
    "group_id": 301,
    "user_id_creator": user_ids[2],
    "is_private": 0,
    "startTime": "2025-07-15 10:00:00",
    "frozen_contest": 1,
    "contest_duration": "04:00:00",
    "contest_name": "Summer Coding Cup 2025"
  },
  {
    "contest_id": 14,
    "group_id": 302,
    "user_id_creator": user_ids[2],
    "is_private": 1,
    "startTime": "2025-09-01 09:00:00",
    "frozen_contest": 0,
    "contest_duration": "03:30:00",
    "contest_name": "GlobalCode Internal Trials"
  }
]
contest_ids = contest.insert_many(contest_docs).inserted_ids

# Quais os contest criados pelo usuário 1 ?
print("PERGUNTA: Quais os contest criados pelo usuário 1?")
print("RESPOSTA:")
contests_user_1 = list(contest.find({"user_id_creator": user_ids[0]}))
for contests in contests_user_1:
  print(f"contest_id:{contests['contest_id']}, group_id:{contests['group_id']}, is_private:{contests['is_private']}, startTime:{contests['startTime']}, frozen_contest:{contests['frozen_contest']}, contest_duration:{contests['contest_duration']}, contest_name:{contests['contest_name']}")