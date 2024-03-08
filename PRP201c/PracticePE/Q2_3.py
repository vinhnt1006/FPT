import re

fname = input("Enter file:")

fhand = open(fname, 'r')

list = []

for DNS in fhand:
    DNS = DNS.strip()
    if DNS.startswith("Location: "):
        DNS = DNS[10:].split()[0]
    else:
        continue
    list.append(DNS)

def countFreq(mylist):
    freq = {}

    for item in mylist:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    
    for item in sorted(freq):
        print(str(item) + ": " + str(freq[item]))

countFreq(list)