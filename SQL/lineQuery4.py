import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="rootpassword",
    database="codeforces-db"
)

cursor = conn.cursor(dictionary=True)

print(f"\n=== Selecionar grupos com a mesma quantidade de users e contests do grupo 'Perform Group 1' ===")

cursor.execute("""
    SELECT GT1.group_name, COUNT(UG.user_id) AS user_count, COUNT(DISTINCT CT.contest_id) AS contest_count
    FROM group_table GT1
    INNER JOIN user_participates_group UG ON UG.group_id = GT1.group_id
    INNER JOIN contest_table CT ON CT.group_id = GT1.group_id
    GROUP BY GT1.group_name
    HAVING (user_count, contest_count) = (
        SELECT COUNT(UG2.user_id), COUNT(DISTINCT CT2.contest_id)
        FROM group_table GT2
        INNER JOIN user_participates_group UG2 ON UG2.group_id = GT2.group_id
        INNER JOIN contest_table CT2 ON CT2.group_id = GT2.group_id
        WHERE GT2.group_name = 'Perform Group 1' AND GT2.group_name != GT1.group_name
    );
""")

result = cursor.fetchall()
for row in result:
    print(f"Group name: {row['group_name']}, ")

cursor.close()
conn.close()