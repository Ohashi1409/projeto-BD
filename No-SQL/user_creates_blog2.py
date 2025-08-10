from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://root:rootpassword@cluster0.wtuzryd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))
database = client.get_database('codeforces')

if "User_1_Embedded_Blog" in database.list_collection_names():
    database.drop_collection("User_1_Embedded_Blog")
user_embedded_blog = database.create_collection('User_1_Embedded_Blog')

# 1 usuário possui apenas um blog
user_emb1_docs = [
    {
        "id": "user_1",
        "user_name": "Carlos Andrade",
        "email": "carlos.andrade.dev@jmail.com",
        "rating": 1988,
        "user_city": "Recife",
        "user_country": "Brazil",
        "user_state": "Pernambuco",
        "registration_date": "2025-07-29 20:15:00",
        "blog": {
          "entry_id": 1,
          "title": "Principais algoritmos de ordenação",
        }
    },
    {   
        "id": "user_2",
        "user_name": "Sofia Costa",
        "email": "sofiacosta@techspace.org",
        "rating": 2450,
        "user_city": "Olinda",
        "user_country": "Brazil",
        "user_state": "Pernambuco",
        "registration_date": "2024-03-12 11:30:22",
        "blog": {
          "entry_id": 2,
          "title": "Estruturas de Dados em Python",
        }
    },
    {
        "id": "user_3",
        "user_name": "John Miller",
        "email": "j.miller@globalcode.net",
        "rating": 2890,
        "user_city": "Lisbon",
        "user_country": "Portugal",
        "user_state": "Lisboa",
        "registration_date": "2023-09-01 18:45:07",
        "blog": {
          "entry_id": 3,
          "title": "Desvendando algoritmos de Busca",
        }
    }
]
user_embedded_blog.insert_many(user_emb1_docs)

# Qual o título do blog escrito pelo usuário com nome 'John Miller'?
print("PERGUNTA: Qual o título do blog escrito pelo usuário com nome 'John Miller'?")
print("RESPOSTA:")
user = user_embedded_blog.find_one({"user_name": "John Miller"})
if user:
    print(f"Título do blog: {user['blog']['title']}")