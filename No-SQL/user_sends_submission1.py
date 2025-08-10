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

# Criar usuários primeiro
users = [
    {"_id": ObjectId(), "user_id": 1, "name": "Ana"},
    {"_id": ObjectId(), "user_id": 2, "name": "Bruno"}
]
db['Users_Levi_1_1'].insert_many(users)

# Submissions referenciam os usuários
submission1 = {
    "_id": ObjectId(),
    "submission_ID": 1,
    "submission_time": "2025-08-01T10:00:00Z",
    "time_consumed": 1.2,
    "points": 100,
    "language": "Python",
    "user_id": users[0]["_id"]
}
submission2 = {
    "_id": ObjectId(),
    "submission_ID": 2,
    "submission_time": "2025-08-01T10:05:00Z",
    "time_consumed": 2.0,
    "points": 80,
    "language": "C++",
    "user_id": users[1]["_id"]
}
db['Submission_Levi_1_1'].insert_many([submission1, submission2])

print("PERGUNTA: Quais usuários enviaram submission em Python?")
print("RESPOSTA:")
print("Usuários que enviaram submission em Python:")
subs = db['Submission_Levi_1_1'].find({"language": "Python"})
for sub in subs:
    user = db['Users_Levi_1_1'].find_one({"_id": sub["user_id"]})
    print(user["name"])
