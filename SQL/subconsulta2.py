import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="rootpassword",
    database="codeforces-db"
)

cursor = conn.cursor()

print("======Quantidade de contests que um usuario criador de um grupo ja criou======")

query = """
    SELECT
    u.id,
    u.user_name,
    (
        SELECT COUNT(*)
        FROM contest_table c
        WHERE c.user_id_creator = u.id  
    ) AS quantidade_contests_criados
    FROM
    user_table u
    WHERE
    EXISTS ( 
        SELECT 1
        FROM group_table g
        WHERE g.user_id_creator = u.id
    );
    """

cursor.execute(query)
results = cursor.fetchall()

for i in range(len(results)):
    print(f"Id: {results[i][0]}, Nome: {results[i][1]}, Quantidade Contests criados: {results[i][2]}")


cursor.close()
conn.close()

