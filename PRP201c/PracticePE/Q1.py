# while True:
#     try:
#         number = int(input("Enter a positive integer number: "))
#     except ValueError:
#         print("The number must be a positive number.")
#     else:
#         if number < 0:
#             print("The number must be positive.")
#             continue
#         else:
#             print("The prime numbers from 0 to", number, end=": \n")
#             for i in range(2, number):
#                 for j in range(2, int(i**0.5 + 1)):
#                     if i % j == 0:
#                         break
#                 else:
#                     print(i, end=" ")
#             break

# # while True:
# #     try:
# #         n = int(input())
# #     except ValueError:
# #         print("The number must be a positive number.")
# #         continue
# #     else:
# #         if n >= 0:
# #             print("The prime numbers from 0 to",n, end=": \n")
# #             for i in range(2, n):
# #                 for j in range(2, int((i/2) + 1)):
# #                     if(i % j) == 0:
# #                         break
# #                 else:
# #                     print(i, end = " ")
# #             break
# #         else:
# #             print("The number must be positive.")
# #             continue

while True:
    try:
        number = int(input("Enter a positive integer number: "))
    except ValueError:
        print("The number must be a positive number.")
    else:
        if number < 0:
            print("The number must be positive.")
        else:
            print("The prime numbers from 0 to", number, end=": \n")
            for i in range(2, number):
                for j in range(2, int(i**0.5 + 1)):
                    if i % j == 0:
                        break
                else:
                    print(i, end=" ")
            break