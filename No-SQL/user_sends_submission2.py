from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId

uri = "mongodb+srv://root:rootpassword@cluster0.wtuzryd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client.get_database('codeforces')

# Limpar coleção antiga
if 'User_Embedded_Levi' in db.list_collection_names():
    db['User_Embedded_Levi'].drop()

# User embute apenas um submission
user1 = {
    "_id": ObjectId(),
    "user_id": 1,
    "name": "Ana",
    "submission": {
        "submission_ID": 1,
        "submission_time": "2025-08-01T10:00:00Z",
        "time_consumed": 1.2,
        "points": 100,
        "language": "Python"
    }
}
user2 = {
    "_id": ObjectId(),
    "user_id": 2,
    "name": "Bruno",
    "submission": {
        "submission_ID": 2,
        "submission_time": "2025-08-01T10:05:00Z",
        "time_consumed": 2.0,
        "points": 80,
        "language": "C++"
    }
}
db['User_Embedded_Levi'].insert_many([user1, user2])

# Consulta: nomes dos usuários que enviaram submission em Python
print("PERGUNTA: Quais usuários enviaram submission em Python?")
print("RESPOSTA:")
print("Usuários que enviaram submission em Python:")
usuarios = db['User_Embedded_Levi'].find({"submission.language": "Python"})
for u in usuarios:
    print(u["name"])
