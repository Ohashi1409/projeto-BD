import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="codeforces-db",
    user="root",
    password="rootpassword"
)

cursor = conn.cursor(dictionary=True)

print(f"\n=== Grupos com contests que iniciam a partir de 20 horas ===")

cursor.execute("""
    SELECT GT.group_name, COUNT(*) as QTD
    FROM group_table GT
        INNER JOIN contest_table CT ON CT.group_id = GT.group_id
    WHERE TIME(CT.startTime) >= '20:00:00'
    GROUP BY GT.group_name
""")

results = cursor.fetchall()
for row in results:
    print(f"Grupo {row['group_name']} tem {row['QTD']} contests que iniciam a partir das 20 horas.")

cursor.close()
conn.close()