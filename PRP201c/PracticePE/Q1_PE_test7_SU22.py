def Anagram(s1, s2):
  s1 = s1.lower()
  s2 = s2.lower()
  s1 = sorted(s1)
  s2 = sorted(s2)
  if s1 == s2:
    return True
  else:
    return False

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

result = Anagram(s1, s2)

print(f"Anagram('{s1}', '{s2}'):", result)