from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId

uri = "mongodb+srv://root:rootpassword@cluster0.wtuzryd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.get_database('codeforces')

if "Group_EmbeddedUsers_Heitor" in db.list_collection_names():
    db.drop_collection("Group_EmbeddedUsers_Heitor")

# Coleção de grupos embutindo array de usuários, nome personalizada
groups_embedded_users = db.create_collection('Group_EmbeddedUsers_Heitor')

# Inserir grupos fictícios, cada um embutindo vários usuários
group_docs = [
    {
        "_id": ObjectId(),
        "group_id": 1,
        "group_name": "Estudantes de IA",
        "users": [
            {"user_id": 1, "user_name": "Ana"},
            {"user_id": 3, "user_name": "Carla"},
            {"user_id": 4, "user_name": "Heitor"}
        ]
    },
    {
        "_id": ObjectId(),
        "group_id": 2,
        "group_name": "Gamers de Recife",
        "users": [
            {"user_id": 2, "user_name": "Bruno"}
        ]
    },
    {
        "_id": ObjectId(),
        "group_id": 3,
        "group_name": "Clube do Livro",
        "users": [
            {"user_id": 1, "user_name": "Ana"},
            {"user_id": 4, "user_name": "Heitor"}
        ]
    }
]
groups_embedded_users.insert_many(group_docs)

# Consulta: Quais são os nomes dos usuários que participam do grupo com nome = 'Estudantes de IA'?
print("PERGUNTA: Quais são os nomes dos usuários que participam do grupo com nome = 'Estudantes de IA'?")
print("RESPOSTA:")
group = groups_embedded_users.find_one({"group_name": "Estudantes de IA"})
if group and "users" in group:
    print(f"Usuários que participam do grupo '{group['group_name']}':")
    for user in group["users"]:
        print(f"- {user['user_name']}")
else:
    print("Grupo não encontrado ou sem usuários embutidos.")