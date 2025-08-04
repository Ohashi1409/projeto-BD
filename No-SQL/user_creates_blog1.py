from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://root:rootpassword@cluster0.wtuzryd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))
database = client.get_database('codeforces')

# 1 documento referenciando apenas 1 documento

user = database["User_1_1"]
sample_ids = list(user.distinct('_id')) # pega IDs de tabela já criada

print(f"Sample IDs from User_1_1: {sample_ids}")

if "Blog_1_1" in database.list_collection_names():
    database.drop_collection("Blog_1_1")

blog = database.create_collection("Blog_1_1")
blogs_entrys = [
  {
    "entry_id": 1,
    "title": "Como resolver problemas utilizando DFS e BFS",
    "user_id": sample_ids[0]
  },
  {
    "entry_id": 2,
    "title": "Principais algoritmos de ordenação",
    "user_id": sample_ids[1]
  },
  {
    "entry_id": 3,
    "title": "Entendendo a complexidade de algoritmos",
    "user_id": sample_ids[2]
  }
]

inserted_entrys = blog.insert_many(blogs_entrys).inserted_ids

# Qual o nome do usuário que criou o blog com o ID 1?
user_id = blog.find_one({"entry_id": 1})['user_id']
user_info = user.find_one({"_id": user_id})
print(f"Usuário que criou o blog com ID '1': {user_info['user_name']}")
