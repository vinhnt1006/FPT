import sqlite3
from prettytable import PrettyTable
conn = sqlite3.connect("employee.sqlite")
cur = conn.cursor()

cur.execute('''
    DROP TABLE IF EXISTS employee;
''')
cur.execute("CREATE TABLE employee (Name TEXT, Rate REAL, Salary INTEGER, Total REAL, Tax REAL)")

tmp = 0

with open("Data.txt") as f:
    for line in f:
        tmp += 1
        if tmp < 3:
            continue
        name, rate, salary = line.split()
        rate = float(rate)
        salary = int(salary)
        total = rate * salary
        if total >= 9000000.0:
            tax = total * 0.05
        else:
            tax = 0
        cur.execute("INSERT INTO employee VALUES (?, ?, ?, ?, ?)", (name, rate, salary, total, tax))

conn.commit()

table = PrettyTable(['Name', 'Rate', 'Salary', 'Total', 'Tax'])
cur.execute("SELECT * FROM employee WHERE Rate > 3 ORDER BY Total DESC")
employee_lists = cur.fetchall()
for emp in employee_lists:
	table.add_row(emp)

print("Employee list:")
print(table)

conn.close()
