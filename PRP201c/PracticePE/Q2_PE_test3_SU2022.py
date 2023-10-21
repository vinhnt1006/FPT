def is_ordered(word):
  word = word.lower()
  for i in range(len(word) - 1):
    if word[i] > word[i + 1]:
      return False
  return True

filename = input("Enter file: ")
file = open(filename, "r")
text = file.read()
file.close()

words = text.split()

ordered_words = []

for word in words:
  if is_ordered(word):
    ordered_words.append(word)

print("The ordered words:")
print(ordered_words)