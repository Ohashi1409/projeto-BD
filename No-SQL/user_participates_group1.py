from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId

uri = "mongodb+srv://root:rootpassword@cluster0.wtuzryd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.get_database('codeforces')

if "User_Ref_Group_Heitor" in db.list_collection_names():
    db.drop_collection("User_Ref_Group_Heitor")
if "Group_Ref_User_Heitor" in db.list_collection_names():
    db.drop_collection("Group_Ref_User_Heitor")
if "UserParticipatesGroup_Ref_Heitor" in db.list_collection_names():
    db.drop_collection("UserParticipatesGroup_Ref_Heitor")

# Coleções explicativas com seu nome
users = db.create_collection('User_Ref_Group_Heitor')
groups = db.create_collection('Group_Ref_User_Heitor')
participations = db.create_collection('UserParticipatesGroup_Ref_Heitor')

# Inserir grupos fictícios
group_docs = [
    {"_id": ObjectId(), "group_id": 1, "group_name": "Estudantes de IA"},
    {"_id": ObjectId(), "group_id": 2, "group_name": "Gamers de Recife"},
    {"_id": ObjectId(), "group_id": 3, "group_name": "Clube do Livro"}
]
groups.insert_many(group_docs)

# Inserir usuários fictícios
user_docs = [
    {"_id": ObjectId(), "user_id": 1, "user_name": "Ana"},
    {"_id": ObjectId(), "user_id": 2, "user_name": "Bruno"},
    {"_id": ObjectId(), "user_id": 3, "user_name": "Carla"},
    {"_id": ObjectId(), "user_id": 4, "user_name": "Heitor"}
]
users.insert_many(user_docs)

# Inserir participações (referenciando user e group por id)
participation_docs = [
    {"_id": ObjectId(), "user_id": user_docs[0]["_id"], "group_id": group_docs[0]["_id"]},
    {"_id": ObjectId(), "user_id": user_docs[1]["_id"], "group_id": group_docs[1]["_id"]},
    {"_id": ObjectId(), "user_id": user_docs[2]["_id"], "group_id": group_docs[0]["_id"]},
    {"_id": ObjectId(), "user_id": user_docs[3]["_id"], "group_id": group_docs[2]["_id"]},
    {"_id": ObjectId(), "user_id": user_docs[0]["_id"], "group_id": group_docs[2]["_id"]}
]
participations.insert_many(participation_docs)

# Consulta: Quais são os nomes dos usuários que participam do grupo com nome = 'Estudantes de IA'?
print("PERGUNTA: Quais são os nomes dos usuários que participam do grupo com nome = 'Estudantes de IA'?")
print("RESPOSTA:")
group = groups.find_one({"group_name": "Estudantes de IA"})
if group:
    participations_cursor = participations.find({"group_id": group["_id"]})
    print(f"Usuários que participam do grupo '{group['group_name']}':")
    for participation in participations_cursor:
        user = users.find_one({"_id": participation["user_id"]})
        print(f"- {user['user_name']}")
else:
    print("Grupo não encontrado.")