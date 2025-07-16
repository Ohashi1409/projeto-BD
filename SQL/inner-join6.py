import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="codeforces-db",
    user="root",
    password="rootpassword"
)
    
cursor = conn.cursor(dictionary=True)

print("\n=== Detalhamento Completo de Submissões ===")

# Objetivo: Listar o nome do usuário, a data da submissão, detalhes do problema, 
# o status do veredito e o nome do concurso.
query = """
SELECT
    u.user_name,
    s.submission_time,
    p.problem_index,
    p.points,
    sp.status_submission_problem,
    c.contest_name
FROM
    user_table u
INNER JOIN
    submission_table s ON u.id = s.user_id
INNER JOIN
    problem_table p ON s.problem_id = p.problem_id
INNER JOIN
    submission_problem sp ON s.submission_id = sp.submission_id
INNER JOIN
    verdict_table v ON sp.verdict_id = v.verdict_id
INNER JOIN
    contest_fazParte cf ON s.submission_id = cf.submission_id
INNER JOIN
    contest_table c ON cf.contest_id = c.contest_id
ORDER BY
    s.submission_time DESC
LIMIT 20
"""

cursor.execute(query)
results = cursor.fetchall()

if results:
    for row in results:
        print(f"Usuário: {row['user_name']}")
        print(f"  Submissão em: {row['submission_time']}")
        print(f"  Problema: {row['problem_index']} ({row['points']} pontos)")
        print(f"  Status: {row['status_submission_problem']}")
        print(f"  Contest: {row['contest_name']}")
        print("-" * 50)
    print(f"\nTotal: {len(results)} resultados")
else:
    print("Nenhum resultado encontrado ou tabelas vazias.")

cursor.close()
conn.close()