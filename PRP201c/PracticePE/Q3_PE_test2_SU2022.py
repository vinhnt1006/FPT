import sqlite3
from prettytable import PrettyTable

conn = sqlite3.connect('DNSList.sqlite')
cursor = conn.cursor()

cursor.executescript('''
	DROP TABLE IF EXISTS DNS;
	
	CREATE TABLE DNS(
		IP TEXT NOT NULL,
		Reliability INTEGER,
		Description TEXT
)''')


with open('DNSList.txt') as f:
	lines = f.readlines()

insert_query = "INSERT INTO DNS VALUES(?, ?, ?)"
for line in lines:
	if line.startswith("IP"):
		data3 = line.split(":")
		data4 = data3[1]
	if line.startswith("Reliability:"):
		data = line.split()
		data1 = data[1].split("%")
		if int(data1[0]) < 50:

			cursor.execute(insert_query, (data4, data[1], "Low"))

		else:
			cursor.execute(insert_query,(data4,data[1],"Normal"))

table = PrettyTable(['IP', 'Reliability','Description'])
cursor.execute("SELECT * FROM DNS ORDER BY Reliability DESC;")
dns_servers = cursor.fetchall()
for server in dns_servers:
	table.add_row(server)

print("DNS server list:")
print(table)