import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="rootpassword",
    database="codeforces-db"
)

cursor = conn.cursor(dictionary=True)

print(f"\n=== Selecionar submissões com a mesma data e linguagem ===")

cursor.execute("""
    SELECT ST1.submission_id
    FROM submission_table ST1
    WHERE (DATE_FORMAT(ST1.submission_time, '%Y-%m-%d'), ST1.submission_language) = ANY (SELECT DATE_FORMAT(ST2.submission_time, '%Y-%m-%d'), ST2.submission_language
                                                                                 FROM submission_table ST2
                                                                                 WHERE ST2.submission_id != ST1.submission_id);
""")

result = cursor.fetchall()
for row in result:
    print(f"Submision ID: {row['submission_id']}, ")

cursor.close()
conn.close()