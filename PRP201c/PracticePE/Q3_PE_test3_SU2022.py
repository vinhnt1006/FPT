import sqlite3
from prettytable import PrettyTable
conn = sqlite3.connect("Wage.sqlite")

cur = conn.cursor()

cur.execute('''
    DROP TABLE IF EXISTS Wage;
''')
cur.execute('''
    CREATE TABLE Wage (
        Name TEXT, 
        Hours INTEGER, 
        Rate INTEGER, 
        Total DOUBLE, 
        Tax DOUBLE
        );
''')

tmp = 0

with open("Database.txt", "r") as f:
    for line in f:
        tmp += 1
        if tmp == 1:
            continue
        name, hours, rate = line.split()
        hours = int(hours)
        rate = int(rate)
        total = hours * rate
        if total >= 2000000:
            tax = total * 0.1
        else:
            tax = 0
        cur.execute("INSERT INTO Wage (Name, Hours, Rate, Total, Tax) VALUES (?, ?, ?, ?, ?)", (name, hours, rate, total, tax))

conn.commit()

table = PrettyTable(['Name', 'Hours', 'Rate', 'Total', 'Tax'])
cur.execute("SELECT * FROM Wage WHERE Hours > 5 ORDER BY Hours ASC")
dns_servers = cur.fetchall()
for server in dns_servers:
	table.add_row(server)

print("Lectures wage")
print(table)

# print("Lectures wage")
# print("Name\tHours\tRate")

# cur.execute("SELECT Name, Hours, Rate FROM Wage WHERE Hours > 5 ORDER BY Hours ASC")

# rows = cur.fetchall()

# for row in rows:
#     name, hours, rate = row
#     print(name + "\t" + str(hours) + "\t" + str(rate))

cur.close()
conn.close()