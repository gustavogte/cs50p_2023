# each row has : last_name, first_name, house
# the first column should be one : name

# input from existing csv=> two command arg:  name and house
# export to new csv => with first, last and house.

import sys
import csv
#from tabulate import tabulate

def main():
    check_file()
    csv2 = check_file()
    split_students(csv2)


def check_file():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].strip().endswith(".csv") == False or sys.argv[2].strip().endswith(".csv") == False:
        sys.exit("Not a CSV file")
    else:
        csv2 =sys.argv[2]
        return csv2


def split_students(csv2):
    try:
        students = []
        with open (sys.argv[1]) as file:
            reader = csv.DictReader(file, fieldnames=["name","house"])
            for student in reader:
                students.append(student)
        new_students = []
        for student in students:
            house = student["house"]
            name = student["name"].split(",")
            if len(name) > 1 :
                first = name[1].strip()
            else:
                first = "first"
            last = name[0]
            if last == "name":
                last = "last"
            new_student = {"first": first, "last": last, "house": house}
            new_students.append(new_student)
    except(FileNotFoundError):
        sys.exit("Could not read invalid_file.csv")
    for student in new_students:
        print(f'{student["first"]}, {student["last"]}, {student["house"]}')
        with open(csv2, "a") as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            writer.writerow({"first": student["first"], "last": student["last"], "house": student["house"]})
    print(new_students)


if __name__ == "__main__":
    main()

