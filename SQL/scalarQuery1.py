import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="rootpassword",
    database="codeforces-db"
)

cursor = conn.cursor()

print("===Nome do usuário que possui o maior rating===")
query = """
    SELECT user_name
    FROM user_table
    WHERE rating = (
        SELECT MAX(rating)
        FROM user_table
    )
"""

cursor.execute(query)
result = cursor.fetchall()
print(result[0][0])

cursor.close()
conn.close()