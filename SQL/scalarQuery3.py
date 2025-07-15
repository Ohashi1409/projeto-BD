import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="rootpassword",
    database="codeforces-db"
)

cursor = conn.cursor()

print("===Nome do contest com maior número de participantes===")
query = """
    SELECT contest_name
    FROM contest_table
    WHERE contest_id = (
        SELECT contest_id
        FROM user_participates_contest
        GROUP BY contest_id
        ORDER BY count(user_id) desc
        LIMIT 1
    ) 
"""

cursor.execute(query)
result = cursor.fetchall()

print(result[0][0])
cursor.close()
conn.close()