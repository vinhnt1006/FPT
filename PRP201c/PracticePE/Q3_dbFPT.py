import sqlite3
con = sqlite3.connect("data1.sqlite")
cur = con.cursor()

cur.execute('''
    DROP TABLE IF EXISTS infos;
''')
cur.execute('''
    CREATE TABLE infos(
        procode INTEGER,
          deleted TEXT
    );
''')

file = open("datafile.txt")
num = 0
for line in file:
    num += 1
    if num == 1:
        continue
    data = line.rstrip().split()
    code = int(data[0].rstrip())
    ten = data[1].rstrip()
    dele = data[3].rstrip().lower()
    if (dele == "delete"):
        cur.execute(
            "insert into infos(procode,deleted) values(?,?)", (code, ten))
        con.commit()
cur.execute("select count(procode) from infos")
data = cur.fetchone()
print("so luong dong " + str(data[0]))
cur.execute("select * from infos order by procode DESC limit 3")
data = cur.fetchall()
for line in data:
    print(line)
con.commit()
con.close()
file.close()
