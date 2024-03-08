def gcd(a, b):
  if b == 0:
    return (a, 1, 0)
  else:
    d, x, y = gcd(b, a % b)
    x, y = y, x - (a // b) * y
    return (d, x, y)

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

d, x, y = gcd(num1, num2)
print(f"GCD of {num1}, {num2} is {d}")
