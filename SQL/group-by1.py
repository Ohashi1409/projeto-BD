import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="codeforces-db",
    user="root",
    password="rootpassword"
)

cursor = conn.cursor(dictionary=True)

print("\n=== Grupos e suas quantidades de usuários ===")

cursor.execute("""
    SELECT GT.group_name, COUNT(*) as QTD
    FROM group_table GT INNER JOIN user_participates_group UPG ON GT.group_id = UPG.group_id
    GROUP BY GT.group_name
""")

results = cursor.fetchall()
for row in results:
    print(f"Grupo: {row['group_name']}, Quantidade: {row['QTD']}")

cursor.close()
conn.close()