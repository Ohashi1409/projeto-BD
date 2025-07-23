import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="codeforces-db",
    user="root",
    password="rootpassword"
)
    
cursor = conn.cursor(dictionary=True)

print("\n=== Problemas com nenhuma linguagem suportada cadastrada ===")

query = """
SELECT P.problem_id, P.problem_statement
FROM problem_table P
LEFT JOIN problem_supported_languages L ON (P.problem_id = L.problem_id)
WHERE L.supported_language IS NULL;
"""

cursor.execute(query)
results = cursor.fetchall()

if results:
    for row in results:
        print(f'Problema com ID {row['problem_id']} e descrição "{row['problem_statement']}"')
else:
    print("Nenhum resultado encontrado ou tabelas vazias.")

cursor.close()
conn.close()