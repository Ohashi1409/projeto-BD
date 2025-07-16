import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="codeforces-db",
    user="root",
    password="rootpassword"
)
    
cursor = conn.cursor(dictionary=True)

print("\n=== Auditoria de Submissões: Rastreando do Usuário ao Criador do Grupo ===")

# Objetivo: Criar um relatório de rastreabilidade que, para cada submissão, mostra quem a enviou, 
# em qual concurso, a qual grupo o concurso pertence e quem foi o criador daquele grupo.
query = """
SELECT
    u_submitter.user_name AS submitter_name,
    c.contest_name,
    g.group_name,
    u_creator.user_name AS creator_name
FROM
    user_table u_submitter
INNER JOIN
    submission_table s ON u_submitter.id = s.user_id
INNER JOIN
    contest_fazParte cf ON s.submission_id = cf.submission_id
INNER JOIN
    contest_table c ON cf.contest_id = c.contest_id
INNER JOIN
    group_table g ON c.group_id = g.group_id
INNER JOIN
    user_table u_creator ON g.user_id_creator = u_creator.id
LIMIT 20;
"""

cursor.execute(query)
results = cursor.fetchall()

if results:
    for row in results:
        print(f"Usuário da Submissão: {row['submitter_name']}")
        print(f"  Contest: {row['contest_name']}")
        print(f"  Grupo do Contest: {row['group_name']}")
        print(f"  Criador do Grupo: {row['creator_name']}")
        print("-" * 60)

    print(f"\nTotal: {len(results)} resultados")
else:
    print("Nenhum resultado encontrado ou tabelas vazias.")

cursor.close()
conn.close()