import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="rootpassword",
    database="codeforces-db"
)

cursor = conn.cursor(dictionary=True)

print(f"\n=== Projetar usuários com problemas aceitos ===")

cursor.execute("""
    SELECT DISTINCT UT.user_name
    FROM user_table UT
    INNER JOIN submission_table ST ON ST.user_id = UT.id
    WHERE (ST.submission_id, 'Accepted') = (SELECT SP.submission_id, SP.status_submission_problem 
                                            FROM submission_problem SP
                                            WHERE SP.submission_id = ST.submission_id)
""")

results = cursor.fetchall()
for row in results:
    print(f"O usuário {row['user_name']} tem problemas aceitos")

cursor.close()
conn.close()