from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId

uri = "mongodb+srv://root:rootpassword@cluster0.wtuzryd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.get_database('codeforces')

if "User_ArrayRef_Group_Heitor" in db.list_collection_names():
    db.drop_collection("User_ArrayRef_Group_Heitor")
if "Group_ArrayRef_User_Heitor" in db.list_collection_names():
    db.drop_collection("Group_ArrayRef_User_Heitor")

# Coleções explicativas com seu nome
users = db.create_collection('User_ArrayRef_Group_Heitor')
groups = db.create_collection('Group_ArrayRef_User_Heitor')

# Inserir usuários fictícios
user_docs = [
    {"_id": ObjectId(), "user_id": 1, "user_name": "Ana"},
    {"_id": ObjectId(), "user_id": 2, "user_name": "Bruno"},
    {"_id": ObjectId(), "user_id": 3, "user_name": "Carla"},
    {"_id": ObjectId(), "user_id": 4, "user_name": "Heitor"}
]
user_ids = users.insert_many(user_docs).inserted_ids

# Inserir grupos com array de referências para usuários participantes
group_docs = [
    {
        "_id": ObjectId(),
        "group_id": 1,
        "group_name": "Estudantes de IA",
        "user_ids": [user_ids[0], user_ids[2], user_ids[3]]
    },
    {
        "_id": ObjectId(),
        "group_id": 2,
        "group_name": "Gamers de Recife",
        "user_ids": [user_ids[1]]
    },
    {
        "_id": ObjectId(),
        "group_id": 3,
        "group_name": "Clube do Livro",
        "user_ids": [user_ids[0], user_ids[3]]
    }
]
groups.insert_many(group_docs)

# Consulta: Quais são os nomes dos usuários que participam do grupo com nome = 'Estudantes de IA'?
print("PERGUNTA: Quais são os nomes dos usuários que participam do grupo com nome = 'Estudantes de IA'?")
print("RESPOSTA:")
group = groups.find_one({"group_name": "Estudantes de IA"})
if group and "user_ids" in group:
    user_cursor = users.find({"_id": {"$in": group["user_ids"]}})
    print(f"Usuários que participam do grupo '{group['group_name']}':")
    for user in user_cursor:
        print(f"- {user['user_name']}")
else:
    print("Grupo não encontrado ou sem usuários referenciados.")