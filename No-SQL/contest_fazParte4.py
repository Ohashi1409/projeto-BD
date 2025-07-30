# Documento embutindo vários documentos

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://root:rootpassword@cluster0.wtuzryd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))
database = client.get_database('codeforces')

# Coleção de contests embutindo array de submissions
contest_emb = database.create_collection('Contest_N_embedded_Heitor')

# Inserir contests fictícios embutindo vários submissions
contest_emb_docs = [
    {
        "contest_id": 1,
        "contest_name": "Codeforces Round #1",
        "submissions": [
            {"submission_id": 1, "user_name": "João"},
            {"submission_id": 2, "user_name": "Maria"}
        ]
    },
    {
        "contest_id": 2,
        "contest_name": "Codeforces Round #2",
        "submissions": [
            {"submission_id": 3, "user_name": "Carlos"}
        ]
    }
]
contest_emb.insert_many(contest_emb_docs)

# Consulta: nomes dos usuários que participaram do contest "Codeforces Round #1"
contest_doc = contest_emb.find_one({"contest_name": "Codeforces Round #1"})
print("Usuários que participaram do contest 'Codeforces Round #1':")
for sub in contest_doc["submissions"]:
    print(sub["user_name"])