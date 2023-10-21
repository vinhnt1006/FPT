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