import mysql.connector

conn = mysql.connector.connect(
    host = '',
    port =  '',
    database = '',
    user =  '',
    password=  ''
)

cursor =conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employee_dummy (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(30),
    salary DECIMAL(10,2)
)
""")

employees = [
    ("John", "IT", 60000),
    ("Alice", "HR", 45000),
    ("Bob", "Finance", 70000),
    ("David", "Sales", 55000),
    ("Emma", "IT", 80000)
]

sql = """
INSERT INTO employee_dummy(name, department, salary)
VALUES(%s,%s,%s)
"""
cursor.executemany(sql, employees)

conn.commit()

print(f"{cursor.rowcount} records inserted.")
cursor.close()
conn.close()