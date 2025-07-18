import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="codeforces-db",
    user="root",
    password="rootpassword"
)

cursor = conn.cursor(dictionary=True)

print("\n=== Grupos e quantidade de contest criados ===")

cursor.execute("""
    SELECT GT.group_name, COUNT(DISTINCT CT.contest_id) as QTD
    FROM group_table GT
    INNER JOIN contest_table CT ON CT.group_id = GT.group_id
    GROUP BY GT.group_name
""")

results = cursor.fetchall()
for row in results:
    print(f"Grupo {row['group_name']} tem {row['QTD']} contests cadastrados.")

cursor.close()
conn.close()