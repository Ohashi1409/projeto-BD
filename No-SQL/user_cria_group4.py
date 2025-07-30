from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://root:rootpassword@cluster0.wtuzryd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.get_database('codeforces')

db.drop_collection('Users_Embedded_Josias')

users_embedded_collection = db.get_collection('Users_Embedded_Josias')

users_embedded_collection.insert_many([
    {
        "user_name": "Ana",
        "email": "ana@example.com",
        "created_groups": [
            {"group_name": "Estudantes de IA", "is_private": False}, 
            {"group_name": "Clube do Livro", "is_private": True}      
        ]
    },
    {
        "user_name": "Bruno",
        "email": "bruno@example.com",
        "created_groups": [
            {"group_name": "Gamers de Recife", "is_private": False}
        ]
    }
])
print("Cenário 4: Dados inseridos com array de documentos embutidos.")

print("\n--- CONSULTA CENÁRIO 4 ---")

for user in users_embedded_collection.find():
    group_names = [group['group_name'] for group in user['created_groups']]
    print(f"{user['user_name']} criou os grupos: {', '.join(group_names) if group_names else 'Nenhum grupo'}")