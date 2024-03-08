import sqlite3

conn = sqlite3.connect("dbmovieList.sqlite")
cur = conn.cursor()

cur.execute('''
    DROP TABLE IF EXISTS MovieList;
''')
cur.execute('''
    CREATE TABLE MovieList(
        MovieID TEXT,
        length INTEGER,
        Des TEXT
    );
''')

with open("MovieList.txt") as f:
    lines = f.readlines()

tmp = 0

for line in lines:
    tmp += 1
    if tmp == 1:
        continue
    movieID, length = line.split()
    movieID = movieID.strip()
    length = length.strip()

    if movieID.startswith("Act"):
        des = "Action Movie"
    else:
        des = "Scientific Movie"

    cur.execute("INSERT INTO MovieList (movieID, length, Des) VALUES (?, ?, ?)", (movieID, length, des))

conn.commit()

cur.execute("SELECT * FROM MovieList ORDER BY length DESC LIMIT 3")

results = cur.fetchall()
for result in results:
    print(result)

conn.close()