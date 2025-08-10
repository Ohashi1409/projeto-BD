from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://root:rootpassword@cluster0.wtuzryd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
database = client.get_database('codeforces')

if "Problem_1_embedded" in database.list_collection_names():
    database.drop_collection("Problem_1_embedded")

# 1 documento embutindo 1 documento
problem_embedded = database.create_collection('Problem_1_embedded')

problems_emb1_docs = [
     {
        "problem_id": 1,
        "difficulty": "Fácil",
        "problem_index": 92,
        "points": 100,
        "solved_count": 10,
        "problem_statement": "Dado dois inteiros, some-os.",
        "test_case_1": {
            "test_case_disc": "Test Case 1.1",
            "test_case_input": "2 3",
            "test_case_output": "5"
        },
        "test_case 2": {
            "test_case_disc": "Test Case 1.2",
            "test_case_input": "5 7",
            "test_case_output": "12"
        },
        "test_case_3": {
            "test_case_disc": "Test Case 1.3",
            "test_case_input": "10 20",
            "test_case_output": "30"
        }
    },
    {
        "problem_id": 2,
        "difficulty": "Médio",
        "problem_index": 93,
        "points": 200,
        "solved_count": 5,
        "problem_statement": "Dado três inteiros, multiplique-os.",
        "test_case_1": {
            "test_case_disc": "Test Case 2.1",
            "test_case_input": "2 3 4",
            "test_case_output": "24"
        },
        "test_case 2": {
            "test_case_disc": "Test Case 2.2",
            "test_case_input": "1 5 6",
            "test_case_output": "30"
        },
        "test_case_3": {
            "test_case_disc": "Test Case 2.3",
            "test_case_input": "7 8 9",
            "test_case_output": "504"
        }
    },
    {
        "problem_id": 3,
        "difficulty": "Difícil",
        "problem_index": 94,
        "points": 300,
        "solved_count": 2,
        "problem_statement": "Dado quatro inteiros, encontre o maior.",
        "test_case_1": {
            "test_case_disc": "Test Case 3.1",
            "test_case_input": "1 2 3 4",
            "test_case_output": "4"
        },
        "test_case 2": {
            "test_case_disc": "Test Case 3.2",
            "test_case_input": "10 20 30 40",
            "test_case_output": "40"
        },
        "test_case_3": {
            "test_case_disc": "Test Case 3.3",
            "test_case_input": "5 15 25 35",
            "test_case_output": "35"
        }
    }
]
problem_embedded.insert_many(problems_emb1_docs)

# Quais os test cases do problema 2?
print("PERGUNTA: Quais os test cases do problema 2?")
print("RESPOSTA:")
problem_2 = problem_embedded.find_one({"problem_id": 2})
# Exibir os test cases do problema 2
for key in problem_2:
    if key.startswith("test_case"):
        test_case = problem_2[key]
        print(f"Test Case: {test_case['test_case_disc']}, Input: {test_case['test_case_input']}, Output: {test_case['test_case_output']}")