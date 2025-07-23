import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="codeforces-db",
    user="root",
    password="rootpassword"
)
    
cursor = conn.cursor(dictionary=True)

print("\n=== Mostra todos os usuários e seus grupos, se houver ===")

query = """
SELECT U.user_name, GROUP_CONCAT(G.group_name SEPARATOR ', ') AS group_names
FROM user_table U
LEFT JOIN user_participates_group UG ON (U.id = UG.user_id)
LEFT JOIN group_table G ON (UG.group_id = G.group_id)
GROUP BY U.user_name
ORDER BY U.user_name;
"""

cursor.execute(query)
results = cursor.fetchall()

if results:
    current_user = None
    for row in results:
        if row['group_names'] is None:
            print(f'O usuário {row['user_name']} não está em grupo nenhum...')
        else:
            print(f'O usuário {row['user_name']} está nos grupo(s): {row['group_names']}')
else:
    print("Nenhum resultado encontrado ou tabelas vazias.")

cursor.close()
conn.close()