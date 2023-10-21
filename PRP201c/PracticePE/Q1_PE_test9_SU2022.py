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