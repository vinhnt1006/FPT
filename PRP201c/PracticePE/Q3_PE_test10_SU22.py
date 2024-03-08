import sqlite3
from prettytable import PrettyTable

conn = sqlite3.connect("Product.sqlite")

cur = conn.cursor()

cur.execute('''
    DROP TABLE IF EXISTS Product;
''')
cur.execute("CREATE TABLE Product (Name TEXT, Quantity INTEGER, Price REAL, Total REAL, Discount REAL)")

cur.execute("DELETE FROM Product")

tmp = 0

with open("data.txt", "r") as f:
    f.readline()
    for line in f:
        tmp += 1
        if tmp == 1:
            continue
        tmp2 = line.split()
        price = float(tmp2[len(tmp2)-1])
        quantity = int(tmp2[len(tmp2)-2])
        name = ""
        qq = 0
        for c in tmp2:
            name = name + c
            qq += 1
            if qq == len(tmp2) - 2:
                break
        total = quantity * price
        if total >= 70000000:
            discount = 0.1 * total
        else:
            discount = 0
        cur.execute("INSERT INTO Product (Name, Quantity, Price, Total, Discount) VALUES (?, ?, ?, ?, ?)", (name, quantity, price, total, discount))

conn.commit()

# print("Product list")
# print("Name\tQuantity\tPrice\tTotal\tDiscount")

# cur.execute("SELECT * FROM Product ORDER BY Quantity DESC")

# rows = cur.fetchall()

# for row in rows:
#     name, quantity, price, total, discount = row
#     print(f"{name}\t{quantity}\t{price}\t{total}\t{discount}")

# cur.close()
# conn.close()


table = PrettyTable(['Name', 'Quantity', 'Price', 'Total', 'Discount'])
cur.execute("SELECT * FROM Product ORDER BY Quantity DESC;")
dns_servers = cur.fetchall()
for server in dns_servers:
	table.add_row(server)

print("Product list:")
print(table)