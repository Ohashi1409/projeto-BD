import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    database='codeforces-db',
    user='root',
    password='rootpassword'
)

cursor = conn.cursor()

print("=== usuarios sem submissões ===")
query = """
SELECT u.id, u.user_name, u.rating
FROM user_table u
LEFT JOIN submission_table s ON u.id = s.user_id
WHERE s.user_id IS NULL
ORDER BY u.rating DESC;
"""

cursor.execute(query)
results = cursor.fetchall()

for row in results:
    print(f"ID: {row[0]}, Nome: {row[1]}, Rating: {row[2]}")

print(f"\nTotal: {len(results)} usuários")

cursor.close()
conn.close()