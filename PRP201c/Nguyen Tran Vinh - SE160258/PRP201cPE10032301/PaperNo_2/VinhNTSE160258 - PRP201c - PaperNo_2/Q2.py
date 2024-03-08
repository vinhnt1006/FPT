import re

fname = input("Enter file:")

fhand = open(fname, 'r')

list = []

print("Troubleshoot wired LAN related issues:")

for line in fhand:
    line = line.rstrip()
    if line.startswith("Name: "):
        line = line[6:].split("-")[0]
    list.append(line)

def countFreq(mylist):
    tmp = 0
    freq = {}
    for item in mylist:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    for item in sorted(freq):
        tmp += 1
        if tmp == 1:
            continue
        if str(item).startswith("-"):
            break
        ans = str(item) + ": " + str(freq[item])
        ans = ans[14:].split("-")[0]
        print(ans)
        #print(str(item) + ": " + str(freq[item]))

countFreq(list)