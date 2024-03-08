import sqlite3
from prettytable import PrettyTable


conn = sqlite3.connect("employee.sqlite")
cur = conn.cursor()

cur.execute('''
    DROP TABLE IF EXISTS employee;
''')
cur.execute("CREATE TABLE employee (Name TEXT, rate REAL, salary INTEGER, Total INTEGER, Tax INTEGER)")

tmp = 0

with open("Datatest6.txt") as f:
    for line in f:
        tmp += 1
        if tmp == 1:
            continue
        name, rate, salary = line.split()
        rate = float(rate)
        salary = int(salary)
        total = rate * salary
        if total >= 9000000:
            tax = total * 0.05
        else:
            tax = 0
        cur.execute("INSERT INTO employee VALUES (?, ?, ?, ?, ?)", (name, rate, salary, total, tax))

conn.commit()

# print("employee list:")
# print("Name\t rate\t salary\t total\t tax")
# cur.execute("SELECT * FROM employee ORDER BY Name")
# for row in cur:
#     print("\t".join(str(x) for x in row))

# conn.close()

table = PrettyTable(['Name', 'rate', 'salary', 'total', 'tax'])
cur.execute("SELECT * FROM employee ORDER BY Name")
dns_servers = cur.fetchall()
for server in dns_servers:
	table.add_row(server)

print("employee list:")
print(table)

conn.close()