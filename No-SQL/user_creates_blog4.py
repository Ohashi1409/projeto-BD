from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://root:rootpassword@cluster0.wtuzryd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))
database = client.get_database('codeforces')

user = database["User_1_1"]
# pegar todos os objetos de usuários
sample_users = list(user.find({}))

if "Blog_1_Embedded" in database.list_collection_names():
    database.drop_collection("Blog_1_Embedded")

blog = database.create_collection("Blog_1_Embedded")
blogs_entrys = [
  {
    "entry_id": 1,
    "title": "Como resolver problemas utilizando DFS e BFS",
    "author1": sample_users[0],
    "author2": sample_users[1]
  },
  {
    "entry_id": 2,
    "title": "Principais algoritmos de ordenação",
    "author1": sample_users[1],
    "author2": sample_users[2]
  },
  {
    "entry_id": 3,
    "title": "Entendendo a complexidade de algoritmos",
    "author1": sample_users[0],
    "author2": sample_users[2]
  }
]

blog.insert_many(blogs_entrys)

# Qual o email dos usuários que criaram o blog com o título 'Principais algoritmos de ordenação'?
blog_entry = blog.find_one({"title": "Principais algoritmos de ordenação"})
if blog_entry:
    author1 = blog_entry.get("author1", {})
    author2 = blog_entry.get("author2", {})
    author_emails = [author1.get("email"), author2.get("email")]
    print(f"Emails dos usuários que criaram o blog: {author_emails[0]}, {author_emails[1]}")
