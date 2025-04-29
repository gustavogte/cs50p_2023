students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i+1, students[i])

print()

# Enumerate
for i, student in enumerate(students):
    print(i+1, student)

print()

e = enumerate(students)

print(e)