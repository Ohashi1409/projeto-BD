# Documento referenciando documento

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://root:rootpassword@cluster0.wtuzryd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))
database = client.get_database('codeforces')

# Coleções
contest = database.create_collection('Contest_Heitor')
submission = database.create_collection('Submission_Heitor')

# Inserir contests fictícios
contest_docs = [
    {"contest_id": 1, "contest_name": "Codeforces Round #1"},
    {"contest_id": 2, "contest_name": "Codeforces Round #2"}
]
contest_ids = contest.insert_many(contest_docs).inserted_ids

# Inserir submissions referenciando contest por id
submission_docs = [
    {"submission_id": 1, "user_name": "João", "contest_id": contest_ids[0]},
    {"submission_id": 2, "user_name": "Maria", "contest_id": contest_ids[0]},
    {"submission_id": 3, "user_name": "Carlos", "contest_id": contest_ids[1]}
]
submission.insert_many(submission_docs)

# Consulta: nomes dos usuários que participaram do contest "Codeforces Round #1"
contest_doc = contest.find_one({"contest_name": "Codeforces Round #1"})
result = submission.find({"contest_id": contest_doc["_id"]})
print("Usuários que participaram do contest 'Codeforces Round #1':")
for sub in result:
    print(sub["user_name"])