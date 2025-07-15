import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="rootpassword",
    database="codeforces-db"
)

cursor = conn.cursor()

print("===Contagem de problemas médios===")
query = """
    SELECT count(*)
    FROM problem_table
    WHERE difficulty = 'medium'
"""

cursor.execute(query)
result = cursor.fetchall()

print(result[0][0])
cursor.close()
conn.close()