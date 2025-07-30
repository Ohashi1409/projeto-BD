from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://root:rootpassword@cluster0.wtuzryd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
database = client.get_database('codeforces')

user_embedded = database.create_collection('User_1_Embedded')

user_emb1_docs = [
    {
        "id": "user_21",
        "user_name": "Carlos Andrade",
        "email": "carlos.andrade.dev@jmail.com",
        "rating": 1988,
        "user_city": "Recife",
        "user_country": "Brazil",
        "registration_date": "2025-07-29 20:15:00",
        "contest_1": {
            "contest_id": 6,
            "group_id": 101,
            "is_private": 0,
            "startTime": "2025-06-15 14:00:00",
            "frozen_contest": 0,
            "contest_duration": "02:00:00",
            "contest_name": "Aquecimento Maratona Pernambucana"
        },
        "contest_2": {
            "contest_id": 7,
            "group_id": 101,
            "is_private": 1,
            "startTime": "2025-07-20 14:00:00",
            "frozen_contest": 1,
            "contest_duration": "02:30:00",
            "contest_name": "Desafio de Algoritmos I - Privado"
        },
        "contest_3": {
            "contest_id": 8,
            "group_id": 102,
            "is_private": 0,
            "startTime": "2025-08-10 10:00:00",
            "frozen_contest": 0,
            "contest_duration": "03:00:00",
            "contest_name": "Simulado Aberto - Estrutura de Dados"
        }
    },
    {
        "id": "user_22",
        "user_name": "Sofia Costa",
        "email": "sofiacosta@techspace.org",
        "rating": 2450,
        "user_city": "Olinda",
        "user_country": "Brazil",
        "registration_date": "2024-03-12 11:30:22",
        "contest_1": {
            "contest_id": 9,
            "group_id": 201,
            "is_private": 0,
            "startTime": "2025-05-01 19:00:00",
            "frozen_contest": 0,
            "contest_duration": "01:30:00",
            "contest_name": "Speedrun de Problemas Fáceis"
        },
        "contest_2": {
            "contest_id": 10,
            "group_id": 201,
            "is_private": 1,
            "startTime": "2025-06-05 19:00:00",
            "frozen_contest": 0,
            "contest_duration": "05:00:00",
            "contest_name": "Contest Longo da Techspace"
        },
        "contest_3": {
            "contest_id": 11,
            "group_id": 202,
            "is_private": 0,
            "startTime": "2025-08-01 18:00:00",
            "frozen_contest": 0,
            "contest_duration": "02:00:00",
            "contest_name": "Preparatório Olinda Codefest"
        }
    },
    {
        "id": "user_23",
        "user_name": "John Miller",
        "email": "j.miller@globalcode.net",
        "rating": 2890,
        "user_city": "Lisbon",
        "user_country": "Portugal",
        "registration_date": "2023-09-01 18:45:07",
        "contest_1": {
            "contest_id": 12,
            "group_id": 301,
            "is_private": 0,
            "startTime": "2025-07-01 10:00:00",
            "frozen_contest": 0,
            "contest_duration": "04:00:00",
            "contest_name": "Global Code Challenge - UK Round"
        },
        "contest_2": {
            "contest_id": 13,
            "group_id": 301,
            "is_private": 0,
            "startTime": "2025-07-15 10:00:00",
            "frozen_contest": 1,
            "contest_duration": "04:00:00",
            "contest_name": "Summer Coding Cup 2025"
        },
        "contest_3": {
            "contest_id": 14,
            "group_id": 302,
            "is_private": 1,
            "startTime": "2025-09-01 09:00:00",
            "frozen_contest": 0,
            "contest_duration": "03:30:00",
            "contest_name": "GlobalCode Internal Trials"
        }
    }
]
user_embedded.insert_many(user_emb1_docs)

# Quais os contests do user 22 ?
user2 = user_embedded.find_one({"id": "user_22"})
for key in user2:
    if key.starswith("contest"):
        contest = user2[key]
        print(f"contest_id:{contest['contest_id']}, group_id:{contest['group_id']}, is_private:{contest['is_private']}, startTime:{contest['startTime']}, frozen_contest:{contest['frozen_contest']}, contest_duration:{contest['contest_duration']}, contest_name:{contest['contest_name']}")