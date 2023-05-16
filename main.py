import psycopg2

connection = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='hillel_test'
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM users;")

result = cursor.fetchall()
# print(result)

for user in result:
    print(user)

cursor.close()
connection.close()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
