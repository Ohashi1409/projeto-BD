from pymongo import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId

uri = "mongodb+srv://root:rootpassword@cluster0.wtuzryd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.get_database('codeforces')

db.drop_collection('Users_Josias_1_1')
db.drop_collection('Groups_Josias_1_1')

users_collection = db.get_collection('Users_Josias_1_1')
groups_collection = db.get_collection('Groups_Josias_1_1')

user_ana_id = users_collection.insert_one({
    "user_name": "Ana",
    "email": "ana@example.com",
    "rating": 1500
}).inserted_id

user_bruno_id = users_collection.insert_one({
    "user_name": "Bruno",
    "email": "bruno@example.com",
    "rating": 1800
}).inserted_id


groups_collection.insert_many([
    {
        "group_name": "Estudantes de IA",
        "is_private": False,
        "user_id_creator": user_ana_id  
    },
    {
        "group_name": "Clube do Livro",
        "is_private": True,
        "user_id_creator": user_ana_id  
    },
    {
        "group_name": "Gamers de Recife",
        "is_private": False,
        "user_id_creator": user_bruno_id 
    }
])

print("Cenário 1: Dados inseridos com referência.")


print("\n--- CONSULTA CENÁRIO 1 ---")


for group in groups_collection.find():
    creator = users_collection.find_one({"_id": group['user_id_creator']})
    creator_name = creator['user_name'] if creator else "Usuário não encontrado"
    print(f" - {group['group_name']} (Criado por: {creator_name})")