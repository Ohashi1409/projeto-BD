import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="codeforces-db",
    user="root",
    password="rootpassword"
)
    
cursor = conn.cursor(dictionary=True)

print("\n=== Blogs e seus Autores ===")

# Objetivo: Listar todas as postagens do blog e o nome de usuário do autor que as criou.
query = """
SELECT
    u.user_name,
    b.title
FROM
    user_table u
INNER JOIN
    blog_entry b ON u.id = b.user_id
"""

cursor.execute(query)
results = cursor.fetchall()

if results:
    for row in results:
        print(f"Usuário: {row['user_name']} - Blog: {row['title']}")
    print(f"\nTotal: {len(results)} resultados")
else:
    print("Nenhum resultado encontrado ou tabelas vazias.")

cursor.close()
conn.close()