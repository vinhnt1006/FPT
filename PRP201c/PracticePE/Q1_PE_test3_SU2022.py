def int_to_hex(n):
  hex_digits = ""
  hex_map = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9",
             10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
  while n > 0:
    remainder = n % 16
    hex_digits = hex_map[remainder] + hex_digits
    n = n // 16
  return hex_digits

while True:
  try:
    num = int(input("Enter a positive integer number: "))
    if num > 0:
      hex_num = int_to_hex(num)
      print(f"{num} is converted into hexadecimal: {hex_num}")
      break
    else:
      print("The number must be positive.")
  except ValueError:
    print("The input must be a positive integer.")