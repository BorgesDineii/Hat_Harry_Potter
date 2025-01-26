import random

class Hat:
    
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort (cls, name):
        print(name, "is in", random.choice(cls.houses))

Hat.sort(input(str("Insert your name to find out which house is yours: ")))