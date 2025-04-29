import csv
students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        #students.append({"name": row["name"], "home": row["home"]})
        students.append(row)

for student in sorted(students, key=lambda student: student["name"], reverse=False):
    print(f"{student['name']} is from {student['home']}")
