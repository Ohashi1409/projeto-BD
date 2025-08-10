from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId

uri = "mongodb+srv://root:rootpassword@cluster0.wtuzryd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client.get_database('codeforces')

# Limpar coleção antiga
if 'Submission_Embedded_Levi' in db.list_collection_names():
    db['Submission_Embedded_Levi'].drop()

# User embute array de submissions
submission1 = {
    "submission_ID": 1,
    "submission_time": "2025-08-01T10:00:00Z",
    "time_consumed": 1.2,
    "points": 100,
    "language": "Python"
}
submission2 = {
    "submission_ID": 2,
    "submission_time": "2025-08-01T10:05:00Z",
    "time_consumed": 2.0,
    "points": 80,
    "language": "C++"
}
submission3 = {
    "submission_ID": 3,
    "submission_time": "2025-08-01T10:10:00Z",
    "time_consumed": 1.5,
    "points": 90,
    "language": "Python"
}
user1 = {"_id": ObjectId(), "user_id": 1, "name": "Ana", "submissions": [submission1]}
user2 = {"_id": ObjectId(), "user_id": 2, "name": "Bruno", "submissions": [submission2, submission3]}
db['Submission_Embedded_Levi'].insert_many([user1, user2])

# Consulta: nomes dos usuários que enviaram submission em Python
print("PERGUNTA: Quais usuários enviaram submission em Python?")
print("RESPOSTA:")
usuarios = db['Submission_Embedded_Levi'].find({"submissions.language": "Python"})
print("Usuários que enviaram submission em Python:")
for u in usuarios:
    print(u["name"])
