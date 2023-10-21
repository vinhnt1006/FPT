while True:
    number = input("Enter a positive integer number: ")
    try:
        number = int(number)
        if number < 0:
            print("The number must be positive.")
            continue
        else:
            print("Sum of fractions of", number, ":")
            sum = 0.00
            ans = ""
            for i in range(1,number+1):
                sum = sum + 1/i
            if number == 1:
                print("1=1")
            else:
                ans = ans + "1+"
                for i in range(2,number):
                    ans = ans + "1/" + str(i) + "+"
                ans = ans + "1/" + str(number) + "="
                print(ans,end="")
                tmp = int(sum)
                sum = sum - tmp
                sum = sum * 1000
                if sum % 10 > 4:
                    res = sum / 10 + 1
                else: res = sum / 10
                res = int(res)
                print(tmp,end=".")
                print(res)
        break
    except ValueError:
        continue