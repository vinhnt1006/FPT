import sqlite3

conn = sqlite3.connect("Counts.sqlite")

cur = conn.cursor()

cur.execute('''
    DROP TABLE IF EXISTS Counts;
''')
cur.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")

with open("mbox-short.txt", "r") as f:
    for line in f:
        if not line.startswith("From:"):
            continue
        email = line.split()[1]
        org = email.split("@")[1]
        cur.execute("SELECT count FROM Counts WHERE org = ?", (org,))
        row = cur.fetchone()
        if row is None:
            cur.execute("INSERT INTO Counts (org, count) VALUES (?, 1)", (org,))
        else:
            cur.execute("UPDATE Counts SET count = count + 1 WHERE org = ?", (org,))

conn.commit()

print("Counts")
print("Org\tCount")

cur.execute("SELECT org, count FROM Counts ORDER BY count DESC")

rows = cur.fetchall()

for row in rows:
    org, count = row
    print(org + "\t" + str(count))

cur.close()
conn.close()