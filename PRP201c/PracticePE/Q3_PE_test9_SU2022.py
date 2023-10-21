import sqlite3

conn = sqlite3.connect("Wage2.sqlite")

cur = conn.cursor()

cur.execute('''
    DROP TABLE IF EXISTS Grade;
''')
cur.execute("CREATE TABLE Grade (Name TEXT, Course TEXT, NumOfAs INTEGER, Price INTEGER, Total INTEGER, Tax INTEGER)")

f = open("Database2.txt", "r")

tmp = 0

for line in f:
    tmp += 1
    if tmp == 1:
        continue
    name, course, num_of_as, price = line.split()
    num_of_as = int(num_of_as)
    price = int(price)
    total = num_of_as * price
    if total >= 2000000:
        tax = total * 0.1
    else:
        tax = 0
    cur.execute("INSERT INTO Grade VALUES (?, ?, ?, ?, ?, ?)", (name, course, num_of_as, price, total, tax))

conn.commit()

f.close()

cur.execute("SELECT * FROM Grade WHERE Course = 'Python' ORDER BY NumOfAs LIMIT 3")

rows = cur.fetchall()

print("Name\tCourse\tNumOfAs\tPrice\tTotal\tTax")
for row in rows:
  print("\t".join(str(x) for x in row))

conn.close()