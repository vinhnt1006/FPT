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