from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId

uri = "mongodb+srv://root:rootpassword@cluster0.wtuzryd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client.get_database('codeforces')

# Limpar coleções antigas
for col in ['Users_Levi_1_n', 'Submission_Levi_1_n']:
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
submission3 = {
    "_id": ObjectId(),
    "submission_ID": 3,
    "submission_time": "2025-08-01T10:10:00Z",
    "time_consumed": 1.5,
    "points": 90,
    "language": "Python"
}
db['Submission_Levi_1_n'].insert_many([submission1, submission2, submission3])

# User referencia array de submissions
user1 = {"_id": ObjectId(), "user_id": 1, "name": "Ana", "submissions": [submission1["_id"]]}
user2 = {"_id": ObjectId(), "user_id": 2, "name": "Bruno", "submissions": [submission2["_id"], submission3["_id"]]}
db['Users_Levi_1_n'].insert_many([user1, user2])

# Consulta: nomes dos usuários que enviaram submission em Python
subs = db['Submission_Levi_1_n'].find({"language": "Python"})
sub_ids = [s["_id"] for s in subs]
usuarios = db['Users_Levi_1_n'].find({"submissions": {"$in": sub_ids}})
print("Usuários que enviaram submission em Python:")
for u in usuarios:
    print(u["name"])
