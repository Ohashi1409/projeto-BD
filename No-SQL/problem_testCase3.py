from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://root:rootpassword@cluster0.wtuzryd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
database = client.get_database('codeforces')

if "Problem_1_N" in database.list_collection_names():
    database.drop_collection("Problem_1_N")
if "TestCase_1_N" in database.list_collection_names():
    database.drop_collection("TestCase_1_N")

# # 1 documento com várias referências para outros documentos
problem = database.create_collection('Problem_1_N')
testCase = database.create_collection('TestCase_1_N')

test_case_docs = [
    # Test cases for problem 1
    {
        "test_case_disc": "Test Case 1.1",
        "test_case_input": "2 3",
        "test_case_output": "5"
    },
    {
        "test_case_disc": "Test Case 1.2",
        "test_case_input": "5 7",
        "test_case_output": "12"
    },
    {
        "test_case_disc": "Test Case 1.3",
        "test_case_input": "10 20",
        "test_case_output": "30"
    },
    # Test cases for problem 2
    {
        "test_case_disc": "Test Case 2.1",
        "test_case_input": "2 3 4",
        "test_case_output": "24"
    },
    {
        "test_case_disc": "Test Case 2.2",
        "test_case_input": "1 5 6",
        "test_case_output": "30"
    },
    {
        "test_case_disc": "Test Case 2.3",
        "test_case_input": "7 8 9",
        "test_case_output": "504"
    },
    # Test cases for problem 3
    {
        "test_case_disc": "Test Case 3.1",
        "test_case_input": "1 2 3 4",
        "test_case_output": "4"
    },
    {
        "test_case_disc": "Test Case 3.2",
        "test_case_input": "10 20 30 40",
        "test_case_output": "40"
    },
    {
        "test_case_disc": "Test Case 3.3",
        "test_case_input": "5 15 25 35",
        "test_case_output": "35"
    }
]
testCasesIds = testCase.insert_many(test_case_docs).inserted_ids

problem_docs = [
    {
        "problem_id": 1,
        "difficulty": "Fácil",
        "problem_index": 92,
        "points": 100,
        "solved_count": 10,
        "problem_statement": "Dado dois inteiros, some-os.",
        "test_cases": [
            testCasesIds[0],
            testCasesIds[1],
            testCasesIds[2]
        ]
    },
    {
        "problem_id": 2,
        "difficulty": "Médio",
        "problem_index": 93,
        "points": 200,
        "solved_count": 5,
        "problem_statement": "Dado três inteiros, multiplique-os.",
        "test_cases": [
            testCasesIds[3],
            testCasesIds[4],
            testCasesIds[5]
        ]
    },
    {
        "problem_id": 3,
        "difficulty": "Difícil",
        "problem_index": 94,
        "points": 300,
        "solved_count": 2,
        "problem_statement": "Dado quatro inteiros, encontre o maior.",
        "test_cases": [
            testCasesIds[6],
            testCasesIds[7],
            testCasesIds[8]
        ]
    }
]
problem.insert_many(problem_docs)

problem = database.get_collection('Problem_1_N')
testCase = database.get_collection('TestCase_1_N')

#Quais os test cases do problema 1?
print("PERGUNTA: Quais os test cases do problema 1?")
print("RESPOSTA:")
test_cases_problem_1 = list(problem.find({"problem_id": 1}))
# Exibir os test cases do problema 1
for test_case in test_cases_problem_1[0]['test_cases']:
    test_case_info = testCase.find_one({"_id": test_case})
    print(f"Test Case: {test_case_info['test_case_disc']}, Input: {test_case_info['test_case_input']}, Output: {test_case_info['test_case_output']}")