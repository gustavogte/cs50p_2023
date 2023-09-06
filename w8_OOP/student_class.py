class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm(self):
        if self.patronus == "Stag":
            return "🐴"
        elif self.patronus == "Otter":
            return "🦆"
        elif self.patronus == "Jach Russell terrier":
            return "🐕"
        else:
            return "🪄"


def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())
    #print(student)
    #print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)  # constructor call => intance the object.


if __name__ == "__main__":
    main()
