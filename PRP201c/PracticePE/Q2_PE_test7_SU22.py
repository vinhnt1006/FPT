fname = input("Enter file name: ")

fhandle = open(fname)

count = 0
total = 0

for line in fhandle:
    if line.startswith("X-DSPAM-Confidence:"):
        value = float(line[line.find(":")+1:].strip())
        count += 1
        total += value

average = total / count

print("Average spam confidence:", average)