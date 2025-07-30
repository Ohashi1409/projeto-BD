# Documento com um array de referências para documentos

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://root:rootpassword@cluster0.wtuzryd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))
database = client.get_database('codeforces')

# Coleções
contest_arr_ref = database.create_collection('Contest_N_Ref_Heitor')
submission_arr_ref = database.create_collection('Submission_N_Ref_Heitor')

# Inserir submissions fictícias
submission_docs = [
    {"submission_id": 1, "user_name": "João"},
    {"submission_id": 2, "user_name": "Maria"},
    {"submission_id": 3, "user_name": "Carlos"}
]
submission_ids = submission_arr_ref.insert_many(submission_docs).inserted_ids

# Inserir contests com array de referências para submissions
contest_docs = [
    {
        "contest_id": 1,
        "contest_name": "Codeforces Round #1",
        "submission_ids": [submission_ids[0], submission_ids[1]]
    },
    {
        "contest_id": 2,
        "contest_name": "Codeforces Round #2",
        "submission_ids": [submission_ids[2]]
    }
]
contest_arr_ref.insert_many(contest_docs)

# Consulta: nomes dos usuários que participaram do contest "Codeforces Round #1"
contest_doc = contest_arr_ref.find_one({"contest_name": "Codeforces Round #1"})
result = submission_arr_ref.find({"_id": {"$in": contest_doc["submission_ids"]}})
print("Usuários que participaram do contest 'Codeforces Round #1':")
for sub in result:
    print(sub["user_name"])