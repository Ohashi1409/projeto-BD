from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://root:rootpassword@cluster0.wtuzryd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
database = client.get_database('codeforces')

# 1:1 documento
problem = database.create_collection('Problem_1_1')
testCase = database.create_collection('TestCase_1_1')

problem_docs = [
    {
        "problem_id": 1,
        "difficulty": "Fácil",
        "problem_index": 92,
        "points": 100,
        "solved_count": 10,
        "problem_statement": "Dado dois inteiros, some-os."
    },
    {
        "problem_id": 2,
        "difficulty": "Médio",
        "problem_index": 93,
        "points": 200,
        "solved_count": 5,
        "problem_statement": "Dado três inteiros, multiplique-os."
    },
    {
        "problem_id": 3,
        "difficulty": "Difícil",
        "problem_index": 94,
        "points": 300,
        "solved_count": 2,
        "problem_statement": "Dado quatro inteiros, encontre o maior."
    }
]
problem_ids = problem.insert_many(problem_docs).inserted_ids

test_case_docs = [
    # Test cases for problem 1
    {
        "test_case_disc": "Test Case 1.1",
        "test_case_input": "2 3",
        "test_case_output": "5",
        "problem_id": problem_ids[0]
    },
    {
        "test_case_disc": "Test Case 1.2",
        "test_case_input": "5 7",
        "test_case_output": "12",
        "problem_id": problem_ids[0]
    },
    {
        "test_case_disc": "Test Case 1.3",
        "test_case_input": "10 20",
        "test_case_output": "30",
        "problem_id": problem_ids[0]
    },
    # Test cases for problem 2
    {
        "test_case_disc": "Test Case 2.1",
        "test_case_input": "2 3 4",
        "test_case_output": "24",
        "problem_id": problem_ids[1]
    },
    {
        "test_case_disc": "Test Case 2.2",
        "test_case_input": "1 5 6",
        "test_case_output": "30",
        "problem_id": problem_ids[1]
    },
    {
        "test_case_disc": "Test Case 2.3",
        "test_case_input": "7 8 9",
        "test_case_output": "504",
        "problem_id": problem_ids[1]
    },
    # Test cases for problem 3
    {
        "test_case_disc": "Test Case 3.1",
        "test_case_input": "1 2 3 4",
        "test_case_output": "4",
        "problem_id": problem_ids[2]
    },
    {
        "test_case_disc": "Test Case 3.2",
        "test_case_input": "10 20 30 40",
        "test_case_output": "40",
        "problem_id": problem_ids[2]
    },
    {
        "test_case_disc": "Test Case 3.3",
        "test_case_input": "5 15 25 35",
        "test_case_output": "35",
        "problem_id": problem_ids[2]
    }
]
testCase.insert_many(test_case_docs)

#Quais os test cases do problema 1?
test_cases_problem_1 = list(testCase.find({"problem_id": problem_ids[0]}))
# Exibir os test cases do problema 1
for test_case in test_cases_problem_1:
    print(f"Test Case: {test_case['test_case_disc']}, Input: {test_case['test_case_input']}, Output: {test_case['test_case_output']}")