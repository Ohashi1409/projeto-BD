from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://root:rootpassword@cluster0.wtuzryd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
database = client.get_database('codeforces')

if "User_1_N_Ohashi" in database.list_collection_names():
    database.drop_collection("User_1_N_Ohashi")
if "Contest_1_N_Ohashi" in database.list_collection_names():
    database.drop_collection("Contest_1_N_Ohashi")

user = database.create_collection("User_1_N_Ohashi")
contest = database.create_collection("Contest_1_N_Ohashi")

contest_docs = [
    {
      "contest_id": 6,
      "group_id": 101,
      "user_id_creator": "user_21",
      "is_private": 0,
      "startTime": "2025-06-15 14:00:00",
      "frozen_contest": 0,
      "contest_duration": "02:00:00",
      "contest_name": "Aquecimento Maratona Pernambucana"
    },
    {
      "contest_id": 7,
      "group_id": 101,
      "user_id_creator": "user_21",
      "is_private": 1,
      "startTime": "2025-07-20 14:00:00",
      "frozen_contest": 1,
      "contest_duration": "02:30:00",
      "contest_name": "Desafio de Algoritmos I - Privado"
    },
    {
      "contest_id": 8,
      "group_id": 102,
      "user_id_creator": "user_21",
      "is_private": 0,
      "startTime": "2025-08-10 10:00:00",
      "frozen_contest": 0,
      "contest_duration": "03:00:00",
      "contest_name": "Simulado Aberto - Estrutura de Dados"
    },
    {
      "contest_id": 9,
      "group_id": 201,
      "user_id_creator": "user_22",
      "is_private": 0,
      "startTime": "2025-05-01 19:00:00",
      "frozen_contest": 0,
      "contest_duration": "01:30:00",
      "contest_name": "Speedrun de Problemas Fáceis"
    },
    {
      "contest_id": 10,
      "group_id": 201,
      "user_id_creator": "user_22",
      "is_private": 1,
      "startTime": "2025-06-05 19:00:00",
      "frozen_contest": 0,
      "contest_duration": "05:00:00",
      "contest_name": "Contest Longo da Techspace"
    },
    {
      "contest_id": 11,
      "group_id": 202,
      "user_id_creator": "user_22",
      "is_private": 0,
      "startTime": "2025-08-01 18:00:00",
      "frozen_contest": 0,
      "contest_duration": "02:00:00",
      "contest_name": "Preparatório Olinda Codefest"
    },
    {
      "contest_id": 12,
      "group_id": 301,
      "user_id_creator": "user_23",
      "is_private": 0,
      "startTime": "2025-07-01 10:00:00",
      "frozen_contest": 0,
      "contest_duration": "04:00:00",
      "contest_name": "Global Code Challenge - UK Round"
    },
    {
      "contest_id": 13,
      "group_id": 301,
      "user_id_creator": "user_23",
      "is_private": 0,
      "startTime": "2025-07-15 10:00:00",
      "frozen_contest": 1,
      "contest_duration": "04:00:00",
      "contest_name": "Summer Coding Cup 2025"
    },
    {
      "contest_id": 14,
      "group_id": 302,
      "user_id_creator": "user_23",
      "is_private": 1,
      "startTime": "2025-09-01 09:00:00",
      "frozen_contest": 0,
      "contest_duration": "03:30:00",
      "contest_name": "GlobalCode Internal Trials"
    }
]
contest_ids = contest.insert_many(contest_docs).inserted_ids

user_docs = [
  {
    "id": "user_21",
    "user_name": "Carlos Andrade",
    "email": "carlos.andrade.dev@jmail.com",
    "rating": 1988,
    "password": "c@rlos#21!",
    "user_city": "Recife",
    "user_country": "Brazil",
    "user_state": "Pernambuco",
    "registration_date": "2025-07-29 20:15:00",
    "created_contests": [
        contest_ids[0],
        contest_ids[1],
        contest_ids[2]
    ]
  },
  {
    "id": "user_22",
    "user_name": "Sofia Costa",
    "email": "sofiacosta@techspace.org",
    "rating": 2450,
    "password": "s0fia_C0sta",
    "user_city": "Olinda",
    "user_country": "Brazil",
    "user_state": "Pernambuco",
    "registration_date": "2024-03-12 11:30:22",
    "created_contests": [
      contest_ids[3],
      contest_ids[4],
      contest_ids[5]
    ]
  },
  {
    "id": "user_23",
    "user_name": "John Miller",
    "email": "j.miller@globalcode.net",
    "rating": 2890,
    "password": "m1ll3rJ#@n",
    "user_city": "Lisbon",
    "user_country": "Portugal",
    "user_state": "Lisboa",
    "registration_date": "2023-09-01 18:45:07",
    "created_contests": [
      contest_ids[6],
      contest_ids[7],
      contest_ids[8]
    ]
  }
]
user.insert_many(user_docs)

user = database.get_collection("User_1_N_Ohashi")
contest = database.get_collection("Contest_1_N_Ohashi")

# Quais os contests do user 23 ?
print("PERGUNTA: Quais os contests do user 23?")
print("RESPOSTA:")
contests_user_1 = list(user.find({"id": "user_23"}))
if contests_user_1:
    for contests in contests_user_1[0]['created_contests'] :
        contest_info = contest.find_one({"_id": contests})
        print(f"contest_id: {contest_info['contest_id']}, group_id: {contest_info['group_id']}, is_private: {contest_info['is_private']}, startTime: {contest_info['startTime']}, frozen_contest: {contest_info['frozen_contest']}, contest_duration: {contest_info['contest_duration']}, contest_name: {contest_info['contest_name']}")
else:
    print("Usuário user_23 não encontrado")
