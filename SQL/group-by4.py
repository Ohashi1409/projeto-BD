import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="codeforces-db",
    user="root",
    password="rootpassword"
)

cursor = conn.cursor(dictionary=True)

print(f"\n=== Usuários com mais de duas submissões feitas ===")


cursor.execute("""
    SELECT UT.user_name, COUNT(*) as QTD
    FROM user_table UT
        INNER JOIN submission_table ST ON ST.user_id = UT.id
    GROUP BY UT.user_name
    HAVING COUNT(*) > 2
""")

results = cursor.fetchall()
for row in results:
    print(f"Usuário {row['user_name']} tem {row['QTD']} submissões.")

cursor.close()
conn.close()