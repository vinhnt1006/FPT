file = open("mbox-short.txt")
counts = dict()

for line in file:
    line = line.strip()
    if line.startswith('From: '):
        continue
    elif line.startswith('From '):
        words = line.split()
        time = words[5]
        parts = time.split(":")
        hour = parts[0]
        counts[hour] = counts.get(hour, 0) + 1

lst = list(counts.items())

lst.sort()

for hour, count in lst:
    print(hour, count)