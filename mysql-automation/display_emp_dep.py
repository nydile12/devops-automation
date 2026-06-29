import mysql.connector

conn = mysql.connector.connect(
    host = '',
    port =  '',
    database = '',
    user =  '',
    password=  ''
)

cursor = conn.cursor(dictionary=True)

department = input("Enter the Department")

cursor.execute(
    "select * from employee_dummy where department = %s",(department,)
)

rows = cursor.fetchall()

if rows:
    for row in rows:
        print(row)
else:
    print("No Employee Found")

cursor.close()
conn.close()
