import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="rootpassword",
    database="codeforces-db"
)

cursor = conn.cursor()

print("======Usuarios que participam de algum grupo======")

query = """
    SELECT id, user_name, email
    FROM user_table
    WHERE id IN (
    SELECT user_id
    FROM user_participates_group
    );
    """

cursor.execute(query)
results = cursor.fetchall()

for i in range(len(results)):
    print(f"Id: {results[i][0]}, Nome: {results[i][1]}, Email: {results[i][2]}")


cursor.close()
conn.close()

