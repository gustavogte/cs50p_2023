"""
with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
"""
import csv
students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})

#print(students)
#print(type(students))

def get_name(student):
    return student["name"]

def get_house(student):
    return student["home"]

"""
print(student.keys())
print(student)
print(get_name(student))
print(get_house(student))
"""

for student in sorted(students, key=lambda student: student["name"], reverse=False):
    print(f"{student['name']} is from {student['home']}")

#print(get_name(student))
#print(get_house(student))
