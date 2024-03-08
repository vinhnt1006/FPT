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