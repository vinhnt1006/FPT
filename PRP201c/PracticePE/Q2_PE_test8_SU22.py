# class Student:
#     def __init__(self, name, age, scores):
#         self.name = name
#         self.age = age
#         self.scores = scores

#     def __str__(self):
#         return f"Name= {self.name}, Age= {self.age}, Scores= {self.scores}"

#     def __lt__(self, other):
#         return self.name < other.name

# students = [
#     Student("John", 20, 80),
#     Student("Anish", 21, 50),
#     Student("Berry", 22, 87),
#     Student("Patrick", 20, 90),
#     Student("Alexa", 19, 84),
#     Student("Cindy", 25, 96),
#     Student("Sandy", 16, 76),
#     Student("Tom", 18, 75),
#     Student("Jerry", 17, 79)
# ]

# print("Before Sorting")
# for student in students:
#     print(student)

# students.sort()

# print("\nAfter Sorting")
# for student in students:
#     print(student)

class Student:
    def __init__(self, name, age, scores):
        self.name = name
        self.age = age
        self.scores = scores

    def __repr__(self):
        return f"Name= {self.name}, Age= {self.age}, Scores= {self.scores}"

students = [
    Student("John", 20, 80),
    Student("Anish", 21, 50),
    Student("Berry", 22, 87),
    Student("Patrick", 20, 90),
    Student("Alexa", 19, 84),
    Student("Cindy", 25, 96),
    Student("Sandy", 16, 76),
    Student("Tom", 18, 75),
    Student("Jerry", 17, 79)
]

print("Before Sorting")
print(*students, sep="\n")

students.sort(key=lambda student: student.name)

print("\nAfter Sorting")
print(*students, sep="\n")