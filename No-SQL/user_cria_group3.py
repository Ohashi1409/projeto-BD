from pymongo import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
 
uri = "mongodb+srv://root:rootpassword@cluster0.wtuzryd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.get_database('codeforces')

db.drop_collection('Users_1_n_Josias')
db.drop_collection('Groups_1_n_Josias')

users_collection = db.get_collection('Users_1_n_Josias')
groups_collection = db.get_collection('Groups_1_n_Josias')

group1_id = groups_collection.insert_one({"group_name": "Estudantes de IA", "is_private": False}).inserted_id
group2_id = groups_collection.insert_one({"group_name": "Clube do Livro", "is_private": True}).inserted_id
group3_id = groups_collection.insert_one({"group_name": "Gamers de Recife", "is_private": False}).inserted_id

users_collection.insert_many([
    {
        "user_name": "Ana",
        "email": "ana@example.com",
        "created_groups_ids": [group1_id, group2_id] 
    },
    {
        "user_name": "Bruno",
        "email": "bruno@example.com",
        "created_groups_ids": [group3_id] 
    }
])
print("Cenário 3: Dados inseridos com array de referências.")

print("\n--- CONSULTA CENÁRIO 3 ---")

for user in users_collection.find():
    group_names = []
    for group_id in user['created_groups_ids']:
        group = groups_collection.find_one({"_id": ObjectId(group_id)})
        if group:
            group_names.append(group['group_name'])
    
    print(f"{user['user_name']} criou os grupos: {', '.join(group_names) if group_names else 'Nenhum grupo'}")