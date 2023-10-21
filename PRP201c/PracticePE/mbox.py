#Type until get 'done', count the number,sum,average of all even numbers.Through Exception if wrong format.
count = 0
total = 0
average = 0

while True:
    try:
        num = input("Enter a number or 'done': ")
        if num == 'done':
            break
        num = int(num)
        if num % 2 == 0:
            count += 1
            total += num
    except ValueError:
        print("Invalid input. Please enter a number or 'done'.")

if count != 0:
    average = total / count

print(f"Number of even numbers: {count}")
print(f"Sum of even numbers: {total}")
print(f"Average of even numbers: {average}")

# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# [From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008]
#Count Frequency of all emails , print out the counts.

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

# Write a program to read through the MovieList.txt and add info to database named dbmovieList.sqlite. 
# if movieID start with 'Act' then des is 'Action Movie' else des is 'Sciendtific movie'.đa

import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('dbmovieList.sqlite')
c = conn.cursor()

# Create the MovieList table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS MovieList (
                movieID TEXT,
                length INTEGER,
                Des TEXT
            )''')

# Open the file and read each line
with open('MovieList.txt', 'r') as f:
    lines = f.readlines()

# Parse each line and insert into database
for line in lines:
    # Split the line by tab characters
    fields = line.strip().split('\t')
    movieID = fields[0]
    length = int(fields[1])
    if movieID.startswith('Act'):
        des = 'Action Movie'
    else:
        des = 'Scientific Movie'
    # Insert the data into the database
    c.execute("INSERT INTO MovieList (movieID, length, Des) VALUES (?, ?, ?)", (movieID, length, des))

# Commit the changes and close the connection
conn.commit()
conn.close()


#A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. For instance, 6 has divisors 1, 2 and 3 (excluding itself), and 1+2+3 = 6, so 6 is a perfect number. 
#Write a program that repeatedly prompts a user for numbers until the user enters a positive interger number. \
#Once a valid number is entered, print out the list of perfect number from 0 to the entered number. 
#If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
#For example, enter-1, bob and 10and match the output below.
#Enter a positive integer number: -2
#the number must be positive.
#Enter a positive integer number: bob
#The number must be a positive number.
#Enter a positive integer number: 500
#The perfect numbers from 0 to 500:
#6 28 496"""

while True:
    number = input("Enter a positive number: ")
    try:
        number = int(number)
        if number < 0:
            print("The number must be positive.")
            continue
        else:
            print("The perfect numbers from 0 to", number, end=": \n")
            for i in range(6, number):
                sum = 0
                for j in range (1, int(i/2 + 1)):
                    if i % j == 0:
                        sum += j
                if sum == i:
                    print(i, end=" ")
        break
    except ValueError:
        print("The number must be a positive number.")
        continue

#Write a program that prompts for a file name, then opens that file and reads through the file DNSList.txt, looking for lines of the form:
#Location: France
#Count the number of DSN server from each country. Once you have accumulated the counts for each name, print out the counts, sorted by name.
#For example, enter a file name "DNSList.txt" or leave it blank and match the output below.
#Enter file:DNSList.txt
#DNS server list:
#Country Count
#Brazil 1
#France 6
#India 1
#United 5

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

#Write a program to read the DSN server list data from file DNSList.txt save data to the database file DNSList.sqlite using a database with the following schema to maintain the counts. CREATE TABLE DNS (IP TEXT, Reliability INTEGER, Description TEXT)
#If the reliability of an IP < 50, write "low" to description column, otherwise, write "Normal" to description column. You can take the reliability of an IP at the end of IP address line.
#The program prints all rows of the table when sorted in descending order by reliability. The output should be as follows: 

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

#Write a program that repeatedly prompts a user for numbers until the user enters a positive interger number.Once a valid number is entered, the program converts the number into a hexadecimal number and print out the result. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
#  For example, enter-1, bob and 10 and match the output below.
#Enter a positive integer number: -1
#The number must be positive.
#Enter a positive integer number: bob
#The number must be a positive number. Enter a positive integer number: 125
#125 is converted into hexadecimal: 7D
def int_to_hex(n):
  hex_digits = ""
  hex_map = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9",
             10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
  while n > 0:
    remainder = n % 16
    hex_digits = hex_map[remainder] + hex_digits
    n = n // 16
  return hex_digits

while True:
  try:
    num = int(input("Enter a positive integer number: "))
    if num > 0:
      hex_num = int_to_hex(num)
      print(f"{num} is converted into hexadecimal: {hex_num}")
      break
    else:
      print("The number must be positive.")
  except ValueError:
    print("The input must be a positive integer.")

#An ordered word is a word in which the alphabets in the word appear in the alphabetical order. 
# For Example, aam and aals are ordered words while abacus is not an ordered word. 
# Write a program to read through the file "words.txt" and print the ordered words. 
# For example, enter a file name "words.txt" or leave it blank and match the output below.
#Enter file: words.txt
#The ordered words:
#['for', 'You', 'for', 'best', 'box']
def is_ordered(word):
  word = word.lower()
  for i in range(len(word) - 1):
    if word[i] > word[i + 1]:
      return False
  return True

filename = input("Enter file: ")
file = open(filename, "r")
text = file.read()
file.close()

words = text.split()

ordered_words = []

for word in words:
  if is_ordered(word):
    ordered_words.append(word)

print("The ordered words:")
print(ordered_words)

#Write a program to manage wage of lecturers including lecturers'name, teaching hours, rate, total and tax. 
# The program reads data from the file "Database.txt" and save to the database file Wage.sqlite using the following table schema.
#Wage (Name, Hours, Rate, Total, Tax)
#Where:
#Total = Hours * Rate
#Tax = Total * 10% if Total >=2000000, otherwise, Tax=0.
#The program prints the lecturer list whose teaching hours >5 and sorted in ascending order by Hours. The output should be as follows: 
#Lectures wage
#Name    Hours    Rate
#Tuan    20    250000
#Lan    10    210000
#Hue    30    210000
#Anh    6    210000
#Toan    3    250000
#Hoang    15    250000
#An    2    250000 
import sqlite3

conn = sqlite3.connect("Wage.sqlite")

cur = conn.cursor()

cur.execute('''
    DROP TABLE IF EXISTS Wage;
''')
cur.execute('''
    CREATE TABLE Wage (
        Name TEXT, 
        Hours INTEGER, 
        Rate INTEGER, 
        Total DOUBLE, 
        Tax DOUBLE
        );
''')

tmp = 0

with open("Database.txt", "r") as f:
    for line in f:
        tmp += 1
        if tmp == 1:
            continue
        name, hours, rate = line.split()
        hours = int(hours)
        rate = int(rate)
        total = hours * rate
        if total >= 2000000:
            tax = total * 0.1
        else:
            tax = 0
        cur.execute("INSERT INTO Wage (Name, Hours, Rate, Total, Tax) VALUES (?, ?, ?, ?, ?)", (name, hours, rate, total, tax))

conn.commit()

print("Lectures wage")
print("Name\tHours\tRate")

cur.execute("SELECT Name, Hours, Rate FROM Wage WHERE Hours > 5 ORDER BY Hours ASC")

rows = cur.fetchall()

for row in rows:
    name, hours, rate = row
    print(name + "\t" + str(hours) + "\t" + str(rate))

cur.close()
conn.close()

#Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
#Invalid input
#Maximum is 10
#Minimum is 2

bigNumber = None
smallNumber = None

while True:
    number = input()
    if number == "done":
        break
    try:
        number = int(number)
        if bigNumber == None or bigNumber < number: bigNumber = number
        if smallNumber == None or smallNumber > number: smallNumber = number
    except ValueError:
        print("Invalid input")
        continue

print("Maximum is", bigNumber)
print("Minimum is", smallNumber)

#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour
d = dict()
lst = list()

fname = input('enter the file name : ')
try:
    fopen = open(fname,'r')
except:
    print('wrong file name !!!')

for line in fopen:

    stline = line.strip()
    
    if stline.startswith('From:'):
        continue
    elif stline.startswith('From'):
        spline = stline.split()
        
        time = spline[5]
        tsplit = time.split(':')
        
        t1 = tsplit[0].split()
        
        for t in t1:
            if t not in d:
                d[t] = 1
            else:
                d[t] = d[t] + 1

for k,v in d.items():
    lst.append((k,v))
lst = sorted(lst)

for k,v in lst:
    print(k,v)

#Write a program to read the mailbox data (mbox-short.txt) and count the number of email messages per organization (i.e. domain name of the email address) using a database with the following schema to maintain the counts.
#CREATE TABLE Counts (org TEXT, count INTEGER)
#mbox-short.txt 

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

#Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay should be the normal rate for hours up to 40 and time- and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. 
#The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).

def computepay(hours, rate):
  if hours > 40:
    extra_hours = hours - 40
    extra_pay = extra_hours * rate * 1.5
    pay = 40 * rate + extra_pay
  else:
    pay = hours * rate
  return pay

hours = float(input("Enter hours: "))
rate = float(input("Enter rate: "))

pay = computepay(hours, rate)

print("Pay:", pay)

#Write a program that prompts for a file name, then opens that file and reads through the file mbox-short.txt, looking for lines of the form: X-DSPAM-Confidence:           0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
#mbox-short.txt: 

fhandle = open("mbox-short.txt", "r")

count = 0
total = 0

for line in fhandle:
    if line.startswith("X-DSPAM-Confidence:"):
        value = float(line[line.find(":")+1:].strip())
        count += 1
        total += value

average = total / count

print("Average spam confidence:", average)

#Write a program to read the mailbox data (mbox.txt) and count the number of email messages per organization (i.e. domain name of the email address) using a database with the following schema to maintain the counts. CREATE TABLE Counts (org TEXT, count INTEGER)

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

#Write a program that repeatedly prompts a user for numbers until the user enters a positive interger number. Once a valid number is entered, the program converts the number into a binary number and print out the result. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. For example, enter -1 and 10 and match the output below.
#Enter a positive integer number: -1
#The number must be positive.
#Enter a positive integer number: 12
#12 is converted into binary: 1100

def decimal_to_binary(n):
  binary = ""
  while n > 0:
    binary = str(n % 2) + binary
    n = n // 2
  return binary

while True:
  try:
    num = int(input("Enter a positive integer number: "))
    if num > 0:
      print(num, "is converted into binary:", decimal_to_binary(num))
      break
    else:
      print("The number must be positive.")
  except:
    print("The input must be a valid number.")

#Write a program to read through the file "Trace.txt" and figure out the distribution by name of the providers. You can pull the name out from the 'Name' line and then splitting the string.
#Name: Microsoft-Windows-L2NACP
#Once you have accumulated the counts for each name, print out the counts, sorted by name.
#For example, enter a file name "Trace.txt" or leave it blank and match the output below.
#Enter file:Trace.txt
#Troubleshoot wired LAN related issues:
#Apple: 2
#Microsoft: 3

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
    freq = {}
    for item in mylist:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    for item in sorted(freq):
        print(str(item) + ": " + str(freq[item]))

countFreq(list)

# Write a program to manage individual tax of employees including employee'name, rate, salary, total and tax. The program reads data from the file "Data.txt" and save to the database file employee.sqlite using the following table schema. employee (Name, rate, salary, Total, Tax)
#Where:
#Total = rate * salary
#Tax Total 5% if Total >=9000000, otherwise, Tax = 0.
#The program prints the employee list whose rate > 3 and sorted in ascending order by name. The output should be as follows:
#file TXT tu tao
import sqlite3

conn = sqlite3.connect("employee.sqlite")
cur = conn.cursor()

cur.execute('''
    DROP TABLE IF EXISTS employee;
''')
cur.execute("CREATE TABLE employee (Name TEXT, rate REAL, salary INTEGER, Total INTEGER, Tax INTEGER)")

tmp = 0

with open("Data.txt") as f:
    for line in f:
        tmp += 1
        if tmp == 1:
            continue
        name, rate, salary = line.split()
        rate = float(rate)
        salary = int(salary)
        total = rate * salary
        if total >= 9000000:
            tax = total * 0.05
        else:
            tax = 0
        cur.execute("INSERT INTO employee VALUES (?, ?, ?, ?, ?)", (name, rate, salary, total, tax))

conn.commit()

print("employee list:")
print("Name\t rate\t salary\t total\t tax")
cur.execute("SELECT * FROM employee WHERE rate > 3 ORDER BY Name")
for row in cur:
    print("\t".join(str(x) for x in row))

conn.close()

#Write a program in the python programming language using data from the datafile.txt. The result is saved to the database file dbFPT.sqlite. Create the table with information: CREATE TABLE INFos (ProCode INTEGER, Deleted TEXT)
#The program prints the number of processed records, the first 3 rows of the table when sorted in descending order by ProjectCode.
import sqlite3
con=sqlite3.connect("data1.sqlite")
cur=con.cursor()
script="""
     drop table if exists infos;
     create table infos(
          procode INTEGER,
          deleted TEXT
     );
"""
cur.executescript(script)
con.commit()
file=open("datafile.txt")
num=0
for line in file:
    num+=1
    if num==1 : continue
    data=line.rstrip().split()
    code=int(data[0].rstrip())
    ten=data[1].rstrip()
    dele= data[3].rstrip().lower()
    if(dele=="delete"):
        cur.execute("insert into infos(procode,deleted) values(?,?)",(code,ten))
        con.commit()
cur.execute("select count(procode) from infos")
data=cur.fetchone()
print("so luong dong "+ str(data[0]))
cur.execute("select * from infos order by procode DESC limit 3")
data=cur.fetchall()
for line in data:
    print(line)
con.commit()
con.close()
file.close()

#The greatest common divisor (GCD) refers to the greatest positive integer that is a common divisor for a given pair of positive integers. Write a program that repeatedly prompts a user for numbers until the user enters two positive interger numbers. Once two valid numbers are entered, the program finds the GCD of the entered numbers and print out the result. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. For example, enter -1, bob and 10, 15 and match the output below.

def gcd(a, b):
  if b == 0:
    return a
  else:
    return gcd(b, a % b)

num1 = None
num2 = None

while num1 is None or num2 is None:
  try:
    num = int(input("Enter a positive integer number: "))
    if num > 0:
      if num1 is None:
        num1 = num
      else:
        num2 = num
        break
    else:
      print("The number must be positive.")
  except ValueError:
    print("The number must be a positive number.")

print(f"GCD of {num1}, {num2} is {gcd(num1, num2)}")

#Given an list of integer numbers in the text file "List.txt". Write a program to read through the file and compute the average of even numbers. For example, enter a file name "List.txt" or leave it blank and match the output below.
#Enter file: List.txt
#Avg = 5.0

file = open("List.txt", "r")

text = file.read()

numbers = text.split()

sum = 0
count = 0
avg = 0

for number in numbers:
    num = int(number)
    if num % 2 == 0:
        sum += num
        count += 1

if count != 0:
    avg = sum / count

print("Avg =", avg)

file.close()

# Write a program to manage wage of grading assignments including name, course, number of assignments, price per assignment, total and tax. The program reads data from the file "Database.txt" and save to the database file Wage.sqlite using the following table schema.
#Grade (Name, Course, NumOfAs, Price, Total, Tax)
#Where:
#Total NumOfAs * Price
#Tax = 10% of Total if Total >= 2000000, otherwise, Tax =0.
#The program prints the wage of grading Python and sorted in ascending order by NumOfAs. The output should be as follows:

import sqlite3

conn = sqlite3.connect('Wage.sqlite')

conn.execute('''CREATE TABLE IF NOT EXISTS Grade
             (Name TEXT,
             Course TEXT,
             NumOfAs INTEGER,
             Price REAL,
             Total REAL,
             Tax REAL)''')

with open('Database.txt', 'r') as f:
    for line in f:
        data = line.strip().split('\t')
        name, course, num_of_as, price = data[0], data[1], int(data[2]), float(data[3])
        total = num_of_as * price
        tax = 0 if total < 2000000 else total * 0.1
        conn.execute("INSERT INTO Grade VALUES (?, ?, ?, ?, ?, ?)",
                     (name, course, num_of_as, price, total, tax))
conn.commit()

cursor = conn.execute("SELECT * FROM Grade WHERE Course='Python' ORDER BY NumOfAs ASC")
print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format("Name", "Course", "NumOfAs", "Price", "Total", "Tax"))
for row in cursor:
    name, course, num_of_as, price, total, tax = row
    print("{:<10} {:<10} {:<10} {:<10,.1f} {:<10,.1f} {:<10,.1f}".format(name, course, num_of_as, price, total, tax))

cursor = conn.execute("SELECT SUM(Tax) FROM Grade")
tax = cursor.fetchone()[0]
print("Total Tax: {:,.1f}".format(tax))

conn.close()

#Write a program that prints out the first prime number (3) and the repeatedly prompts a use for numbers until the user enters to stop. If the user enters number rather than 0, the program will print out the next prime number
#For example:
#2
#Type 1 if u want next prime number otherwise type it: 1
#3
#Type 1 if u want next prime number otherwise type it: 1
#5

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

print("DNS server list\nCountry Count")

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

# Write a program that prompts for a file name, then opens that file and reads through the file DNSList.txt, looking for lines of the form Location: France
#Count the number of DSN server from each country. Once you have and the
#counts for each name, print out the counts, sorted by name
#For example, enter a file name "DNSList.txt" or leave it blank and match the output below.
#Enter file: DNSList.txt
#DNS server list
#Country Count
#Brazil     1
#France   6
#India       1
#United   5

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

print("DNS server list\nCountry Count")

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

#Write a program to manage product selling including name, product quantity, price, total and discount. The program read data from the file "Txt" and save to the database file Product.sqlite using the following the schemma
#Product (Name, Quantity, Price, Total, Discount)
#Where:
#Total=Quantity Price
#Discount=10% of Total 70000000, otherwise, Discount
#The program prints the list of product and sorted in descending onder by quantity. The output should be as follows:
#Product list
#Name      Quantity   Price                       Total               Discount
#Iphone11   5                 140000000         70000000    7000000

import sqlite3

conn = sqlite3.connect('Product.sqlite')

conn.execute('''CREATE TABLE IF NOT EXISTS Product
             (Name TEXT,
             Quantity INTEGER,
             Price REAL,
             Total REAL,
             Discount REAL)''')

with open('data.txt', 'r') as f:
    for line in f:
        data = line.strip().split('\t')
        name, quantity, price = data[0], int(data[1]), float(data[2])
        total = quantity * price
        discount = 0.1 * total if total >= 70000000 else 0
        conn.execute("INSERT INTO Product VALUES (?, ?, ?, ?, ?)",
                     (name, quantity, price, total, discount))

conn.commit()

cursor = conn.execute("SELECT * FROM Product ORDER BY Quantity DESC")
print("{:<10} {:<10} {:<10} {:<10} {:<10}".format("Name", "Quantity", "Price", "Total", "Discount"))
for row in cursor:
    name, quantity, price, total, discount = row
    print("{:<10} {:<10} {:<10,.1f} {:<10,.1f} {:<10,.1f}".format(name, quantity, price, total, discount))

conn.close()

#Write a grogram to check whether two strings are anagrams or not and return True or False respectively. One string is an anagram of another if the second is simply a rearrangement of the first
#For example:
#Anagram('heart, 'earth')→ True 
#Anagram('python', 'typhon')→ True 
#Anagram ('Foot', 'tooth')→ False
def Anagram(s1, s2):
  s1 = s1.lower()
  s2 = s2.lower()
  s1 = sorted(s1)
  s2 = sorted(s2)
  if s1 == s2:
    return True
  else:
    return False

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

result = Anagram(s1, s2)

print(f"Anagram('{s1}', '{s2}'):", result)

#Write a program to manage scholarship of students including name m grade, scholar. The program reads data from the file "Data.txt" and save to the des file Scholar .sqlite using the following table schemma
#Student (Name, term, grade, Scholar)
#Where:
#Scholar = A if grade >= 8, else if grade >= 7 scholar =B otherwise none
#The program prints the scholar list and sorted in descending order by grade The ouput should be as follows
#Scholar list:
#Name  term  grade  Scholar
#Tuan     1          8.0       A
#Son       1          7.0       B
#Dat        1         5.0

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

