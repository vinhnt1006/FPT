import sqlite3

conn = sqlite3.connect("Scholar.sqlite")

cur = conn.cursor()

cur.execute('''
    DROP TABLE IF EXISTS Student;
''')
cur.execute("CREATE TABLE Student (Name TEXT, term INTEGER, grade REAL, Scholar TEXT)")

tmp = 0

with open("Data2.txt", "r") as f:
    for line in f:
        tmp += 1
        if tmp == 1:
            continue
        name, term, grade = line.split()
        term = int(term)
        grade = float(grade)
        if grade >= 8:
            scholar = "A"
        elif grade >= 7:
            scholar = "B"
        else:
            scholar = None
        cur.execute("INSERT INTO Student (Name, term, grade, Scholar) VALUES (?, ?, ?, ?)", (name, term, grade, scholar))

conn.commit()

cur.execute("SELECT * FROM Student ORDER BY grade DESC")

rows = cur.fetchall()

print("Scholar list:")

print("Name\tterm\tgrade\tScholar")
for row in rows:
    print("\t".join(str(x) for x in row))

cur.close()
conn.close()