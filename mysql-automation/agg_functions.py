import mysql.connector
from datetime import datetime

conn = mysql.connector.connect(
    host = '',
    port =  '',
    database = '',
    user =  '',
    password=  ''
)

cursor = conn.cursor()

cursor.execute("SELECT DATABASE()")
database = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM employee_dummy")
employees = cursor.fetchone()[0]

cursor.execute("SELECT MAX(salary) FROM employee_dummy")
highest = cursor.fetchone()[0]

cursor.execute("SELECT MIN(salary) FROM employee_dummy")
lowest = cursor.fetchone()[0]

cursor.execute("SELECT AVG(salary) FROM employee_dummy")
average = cursor.fetchone()[0]

print("=" * 40)
print("DATABASE HEALTH REPORT")
print("=" * 40)

print(f"Database       : {database}")
print(f"Total Employees: {employees}")
print(f"Highest Salary : {highest}")
print(f"Lowest Salary  : {lowest}")
print(f"Average Salary : {round(average,2)}")
print(f"Generated At   : {datetime.now()}")

cursor.close()
conn.close()