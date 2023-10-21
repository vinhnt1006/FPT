def is_valid(password):
  if len(password) < 6 or len(password) > 12:
    return False
  if not any(char.islower() for char in password):
    return False
  if not any(char.isupper() for char in password):
    return False
  if not any(char.isdigit() for char in password):
    return False
  if not any(char in "$#@" for char in password):
    return False
  return True

passwords = input("Enter passwords: ").split(",")

valid_passwords = []

for password in passwords:
  if is_valid(password):
    valid_passwords.append(password)

print("Valid passwords: ", ",".join(valid_passwords))