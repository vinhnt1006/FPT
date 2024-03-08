while True:
    try:
        number = int(input("Enter a positive integer number: "))
    except ValueError:
        print("The number must be a positive number.")
    else:
        if number < 0:
            print("The number must be positive.")
        else:
            print("The Fibonacci sequence of", number, end=": \n")
            print(0, 1, end = " ")
            f1 = 0
            f2 = 1
            for i in range(2, number):
                # #print(f2, end = " ")
                # f1 = f1 + f2
                # f2 = f1 + f2
                # print(f1, f2, end = " ")
                print(f1 + f2, end = " ")
                f2 += f1
                f1 = f2 - f1
        break