import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="codeforces-db",
    user="root",
    password="rootpassword"
)
    
cursor = conn.cursor(dictionary=True)

print("\n=== Usuários que nunca participaram de nenhum contest ===")

query = """
SELECT U.user_name
FROM user_table U LEFT OUTER JOIN user_participates_contest P ON (U.id = P.user_id)
WHERE P.user_id IS NULL
"""

cursor.execute(query)
results = cursor.fetchall()

if results:
    for row in results:
        print("Usuário: ", row['user_name'])
else:
    print("Nenhum resultado encontrado ou tabelas vazias.")

cursor.close()
conn.close()