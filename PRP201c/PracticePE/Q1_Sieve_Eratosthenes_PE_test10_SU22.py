def sieve_of_eratosthenes(limit):
  prime = [True for i in range(limit + 1)]
  p = 2
  while p * p <= limit:
    if prime[p]:
      for i in range(p * p, limit + 1, p):
        prime[i] = False
    p += 1
  
  return [p for p in range(2, limit + 1) if prime[p]]

def next_prime(n):
  n = n + 1
  while True:
    primes = sieve_of_eratosthenes(n)
    if n in primes:
      return n
    else:
      n += 1

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