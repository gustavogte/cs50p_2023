students = ["Hermione", "Harry", "Ron"]

# List Comprehension => List of Dict Objects
#gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]


# Dict Comprehension => One Dict Object
gryffindors = {student: "Gryffindor" for student in students}


print(gryffindors)