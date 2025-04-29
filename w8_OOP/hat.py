import random

class Hat:
    # class variables
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    # class methods (keyword "cls")
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

Hat.sort("Harry")
