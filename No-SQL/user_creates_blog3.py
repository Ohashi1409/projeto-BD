from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://root:rootpassword@cluster0.wtuzryd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))
database = client.get_database('codeforces')

user = database["User_1_1"]
sample_ids = list(user.distinct('_id')) # pega IDs de tabela já criada

if "Blog_1_array" in database.list_collection_names():
    database.drop_collection("Blog_1_array")

blog = database.create_collection("Blog_1_array")
blogs_entrys = [
  {
    "entry_id": 1,
    "title": "Como resolver problemas utilizando DFS e BFS",
    "user_ids": [
      sample_ids[0],
      sample_ids[1]
    ]
  },
  {
    "entry_id": 2,
    "title": "Principais algoritmos de ordenação",
    "user_ids": [
      sample_ids[1],
      sample_ids[2]
    ]
  },
  {
    "entry_id": 3,
    "title": "Entendendo a complexidade de algoritmos",
    "user_ids": [
      sample_ids[0],
      sample_ids[2]
    ]
  }
]

blog.insert_many(blogs_entrys)

# Qual o nome dos usuários que criaram o blog com o título 'Entendendo a complexidade de algoritmos'?
blog_entry = blog.find_one({"title": "Entendendo a complexidade de algoritmos"})
if blog_entry:
    user_ids = blog_entry.get("user_ids", [])
    users = user.find({"_id": {"$in": user_ids}})
    user_names = [user["user_name"] for user in users]
    print(f"Usuários que criaram o blog: {', '.join(user_names)}")