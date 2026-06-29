import mysql.connector
import csv

conn = mysql.connector.connect(
    host = '',
    port =  '',
    database = '',
    user =  '',
    password=  ''
)

cursor = conn.cursor()

cursor.execute("select * from employee_dummy")

rows = cursor.fetchall()

with open("output.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Name", "Department", "Salary"])
    writer.writerows(rows)

print("Export completed.")

cursor.close()
conn.close()
