# each row has : last_name, first_name, house
# the first column should be one : name

# input from existing csv=> two command arg:  name and house
# export to new csv => with first, last and house.

import sys
import csv


def main():
    check_file()
    csv2 = check_file()
    split_students(csv2)


def check_file():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif (
        sys.argv[1].strip().endswith(".csv") == False
        or sys.argv[2].strip().endswith(".csv") == False
    ):
        sys.exit("Not a CSV file")
    else:
        csv2 = sys.argv[2]
        return csv2


def split_students(csv2):
    new_students = []
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for student in reader:
                split_name = student["name"].split(",")
                new_students.append(
                    {
                        "first": split_name[1].lstrip(),
                        "last": split_name[0],
                        "house": student["house"],
                    }
                )
        #print(reader)
        #print(new_students)
    except FileNotFoundError:
        sys.exit("Could not read invalid_file.csv")

    # write new_students
    with open(csv2, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writerow({"first": "first", "last": "last", "house": "house"})
        for student in new_students:
            writer.writerow(
                {
                    "first": student["first"],
                    "last": student["last"],
                    "house": student["house"],
                }
            )
    # print(new_students)


if __name__ == "__main__":
    main()
