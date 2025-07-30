from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId

uri = "mongodb+srv://root:rootpassword@cluster0.wtuzryd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client.get_database('codeforces')

# Limpar coleções antigas
for col in ['Users_Levi_1_1', 'Submission_Levi_1_1']:
    if col in db.list_collection_names():
        db[col].drop()

# Criar submissions
submission1 = {
    "_id": ObjectId(),
    "submission_ID": 1,
    "submission_time": "2025-08-01T10:00:00Z",
    "time_consumed": 1.2,
    "points": 100,
    "language": "Python"
}
submission2 = {
    "_id": ObjectId(),
    "submission_ID": 2,
    "submission_time": "2025-08-01T10:05:00Z",
    "time_consumed": 2.0,
    "points": 80,
    "language": "C++"
}
db['Submission_Levi_1_1'].insert_many([submission1, submission2])

# User referencia apenas um submission
users_ref = [
    {"_id": ObjectId(), "user_id": 1, "name": "Ana", "submission_id": submission1["_id"]},
    {"_id": ObjectId(), "user_id": 2, "name": "Bruno", "submission_id": submission2["_id"]}
]
db['Users_Levi_1_1'].insert_many(users_ref)

# Consulta: nomes dos usuários que enviaram submission em Python
print("Usuários que enviaram submission em Python:")
sub = db['Submission_Levi_1_1'].find_one({"language": "Python"})
usuarios = db['Users_Levi_1_1'].find({"submission_id": sub["_id"]})
for u in usuarios:
    print(u["name"])
