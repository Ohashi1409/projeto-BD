import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="codeforces-db",
    user="root",
    password="rootpassword"
)
    
cursor = conn.cursor(dictionary=True)

print("\n=== Submissões em Contests ===")

# Objetivo: Listar o nome do usuário que realizou uma submissão e o nome do concurso em que ela foi feita.
query = """
SELECT
    u.user_name,
    c.contest_name
FROM
    user_table u
INNER JOIN
    submission_table s ON u.id = s.user_id
INNER JOIN
    contest_fazParte cf ON s.submission_id = cf.submission_id
INNER JOIN
    contest_table c ON cf.contest_id = c.contest_id
"""

cursor.execute(query)
results = cursor.fetchall()

if results:
    for row in results:
        print(f"Usuário: {row['user_name']} - Contest: {row['contest_name']}")
    print(f"\nTotal: {len(results)} resultados")
else:
    print("Nenhum resultado encontrado ou tabelas vazias.")

cursor.close()
conn.close()