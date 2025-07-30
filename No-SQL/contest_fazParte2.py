# Documento embutindo apenanas um documento

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://root:rootpassword@cluster0.wtuzryd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))
database = client.get_database('codeforces')

# Coleção de submissions com contest embutido
submission_emb = database.create_collection('Submission_1_1_embedded_Heitor')

# Inserir submissions fictícias embutindo contest
submission_emb_docs = [
    {
        "submission_id": 1,
        "user_name": "João",
        "contest": {"contest_id": 1, "contest_name": "Codeforces Round #1"}
    },
    {
        "submission_id": 2,
        "user_name": "Maria",
        "contest": {"contest_id": 1, "contest_name": "Codeforces Round #1"}
    },
    {
        "submission_id": 3,
        "user_name": "Carlos",
        "contest": {"contest_id": 2, "contest_name": "Codeforces Round #2"}
    }
]
submission_emb.insert_many(submission_emb_docs)

# Consulta: nomes dos usuários que participaram do contest "Codeforces Round #1"
result = submission_emb.find({"contest.contest_name": "Codeforces Round #1"})
print("Usuários que participaram do contest 'Codeforces Round #1':")
for sub in result:
    print(sub["user_name"])