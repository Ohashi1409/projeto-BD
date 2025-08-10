from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://root:rootpassword@cluster0.wtuzryd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.get_database('codeforces')

db.drop_collection('Groups_Embedded_Josias')

groups_embedded_collection = db.get_collection('Groups_Embedded_Josias')

user_ana = {"user_name": "Ana", "email": "ana@example.com", "rating": 1500}
user_bruno = {"user_name": "Bruno", "email": "bruno@example.com", "rating": 1800}

groups_embedded_collection.insert_many([
    {
        "group_name": "Estudantes de IA",
        "is_private": False,
        "creator": user_ana  
    },
    {
        "group_name": "Gamers de Recife",
        "is_private": False,
        "creator": user_bruno 
    }
])
print("Cenário 2: Dados inseridos com documento embutido.")


print("PERGUNTA: Quais grupos foram criados por cada usuário?")
print("RESPOSTA:")
print("\n--- CONSULTA CENÁRIO 2 ---")


for group in groups_embedded_collection.find():
    creator = group['creator']
    print(f" - {group['group_name']} (Criado por: {creator['user_name']})")