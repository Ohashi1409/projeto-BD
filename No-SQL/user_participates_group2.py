from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId

uri = "mongodb+srv://root:rootpassword@cluster0.wtuzryd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.get_database('codeforces')

# Coleção de participações embutindo apenas um grupo, nome personalizada
participations_embedded = db.create_collection('UserParticipatesGroup_Embedded_Heitor')

# Inserir participações fictícias, cada uma embutindo um grupo
participation_docs = [
    {
        "_id": ObjectId(),
        "user_name": "Ana",
        "group": {"group_id": 1, "group_name": "Estudantes de IA"}
    },
    {
        "_id": ObjectId(),
        "user_name": "Bruno",
        "group": {"group_id": 2, "group_name": "Gamers de Recife"}
    },
    {
        "_id": ObjectId(),
        "user_name": "Carla",
        "group": {"group_id": 1, "group_name": "Estudantes de IA"}
    },
    {
        "_id": ObjectId(),
        "user_name": "Heitor",
        "group": {"group_id": 3, "group_name": "Clube do Livro"}
    },
    {
        "_id": ObjectId(),
        "user_name": "Ana",
        "group": {"group_id": 3, "group_name": "Clube do Livro"}
    }
]
participations_embedded.insert_many(participation_docs)

# Consulta: Quais são os nomes dos usuários que participam do grupo com nome = 'Estudantes de IA'?
result = participations_embedded.find({"group.group_name": "Estudantes de IA"})
print("Usuários que participam do grupo 'Estudantes de IA':")
for participation in result:
    print(f"- {participation['user_name']}")