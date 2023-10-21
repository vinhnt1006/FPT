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