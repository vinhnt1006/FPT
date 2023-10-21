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