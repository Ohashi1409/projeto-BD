import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="rootpassword",
    database="codeforces-db"
)

cursor = conn.cursor(dictionary=True)

print(f"\n=== Problemas com taxa de acerto maior que 50% ===")

cursor.execute("""
    SELECT P.problem_id, COUNT(*) as total_respostas, P.solved_count
    FROM problem_table P
    INNER JOIN submission_problem SP ON SP.problem_id = P.problem_id
    GROUP BY P.problem_id
    HAVING (P.solved_count / COUNT(*)) > 0.5
""")

result = cursor.fetchall()
for row in result:
    print(f"Problema ID: {row['problem_id']}, " +
          f"Total Respostas: {row['total_respostas']} e Acertos: {row['solved_count']}")

cursor.close()
conn.close()