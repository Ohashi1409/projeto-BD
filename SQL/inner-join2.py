import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="codeforces-db",
    user="root",
    password="rootpassword"
)
    
cursor = conn.cursor(dictionary=True)

print("\n=== Usuários e seus Grupos ===")

# Objetivo: Listar todos os usuários e os nomes dos grupos dos quais eles são membros.
query = """
SELECT
    u.user_name,
    g.group_name
FROM
    user_table u
INNER JOIN
    user_participates_group upg ON u.id = upg.user_id
INNER JOIN
    group_table g ON upg.group_id = g.group_id
"""

cursor.execute(query)
results = cursor.fetchall()

if results:
    for row in results:
        print(f"Usuário: {row['user_name']} - Grupo: {row['group_name']}")
    print(f"\nTotal: {len(results)} resultados")
else:
    print("Nenhum resultado encontrado ou tabelas vazias.")

cursor.close()
conn.close()