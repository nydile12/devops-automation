import mysql.connector

conn = mysql.connector.connect(
    host = '',
    port =  '',
    database = '',
    user =  '',
    password=  ''
)

cursor = conn.cursor()

department = input("Enter the Department")
Salary = float(input("Enter the amount"))

query = """
update employee_dummy
set salary = salary+%s
where department = %s
"""

cursor.execute(query, (Salary, department))
conn.commit()

print(f"{cursor.rowcount} employees updated.")

cursor.close()
conn.close()