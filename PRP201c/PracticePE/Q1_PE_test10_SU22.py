def is_prime(n):
  if n == 1:
    return False
  if n == 2:
    return True
  if n % 2 == 0:
    return False
  for i in range(3, int(n**0.5) + 1, 2):
    if n % i == 0:
      return False
  return True

def next_prime(n):
  n = n + 1
  while not is_prime(n):
    n = n + 1
  return n

current_prime = 2

print(current_prime)

user_input = input("Type 1 if you want next prime number otherwise type 0: ")

while user_input != "0":
  
  if user_input == "1":
    current_prime = next_prime(current_prime)
    print(current_prime)
  
  else:
    print("Invalid input. Please enter either 1 or 0.")
  
  user_input = input("Type 1 if you want next prime number otherwise type 0: ")

print("Exit program!")