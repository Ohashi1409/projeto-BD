import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="rootpassword",
    database="codeforces-db"
)

cursor = conn.cursor()

print("===Usuários que são criadores de contests ou grupos===")
query = """
    SELECT DISTINCT id, user_name, email
    FROM user_table
    WHERE id in (
        SELECT user_id_creator 
        FROM group_table 
        UNION
        SELECT user_id_creator
        FROM contest_table
    )
"""

cursor.execute(query)
results = cursor.fetchall()

for rows in results:
    print(f"ID: {rows[0]}, Nome: {rows[1]}, Email: {rows[2]}") 

print(f"\nTotal: {len(results)} usuários")

cursor.close()
conn.close()