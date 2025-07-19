import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="rootpassword",
    database="codeforces-db"
)

cursor = conn.cursor(dictionary=True)

print(f"\n=== Selecionar contests com mesma data de início e duração de outro contest ===")

cursor.execute("""
    SELECT C1.contest_name
    FROM contest_table C1
    WHERE (C1.startTime, C1.contest_duration) = ANY (SELECT C2.startTime, C2.contest_duration
                                              FROM contest_table C2
                                              WHERE C2.contest_id != C1.contest_id)
""")

result = cursor.fetchall()
for row in result:
    print(f"Contest ID: {row['contest_name']}, ")

cursor.close()
conn.close()