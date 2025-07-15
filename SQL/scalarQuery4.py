import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="rootpassword",
    database="codeforces-db"
)

cursor = conn.cursor()

print("===Linguagem de programação mais utilizada em submissões de problemas difíceis===")
query = """
    SELECT submission_language
    FROM submission_table
    WHERE problem_id IN (
        SELECT problem_id
        FROM problem_table
        WHERE difficulty = 'hard'
    )
    GROUP BY submission_language
    ORDER BY count(*) DESC
    LIMIT 1;
"""

cursor.execute(query)
result = cursor.fetchall()

print(result[0][0])
cursor.close()
conn.close()