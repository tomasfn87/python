'''
class Pet:
    pass

pet_1.name = "Bidu"
pet_1.birth = 2006
pet_1.type = "dog"

pet_2.name = "Zyg"
pet_2.birth =2020
pet_2.type = "cat"
'''
class Pet:
    def __init__(self, name, birth, species, friendly):
        self.na = name
        self.bi = birth
        self.sp = species
        self.fr = friendly

    def whois(self):
        print("%s is a %s born in %d."%(self.na, self.sp, self.bi))

    def play(self):
        if self.fr == "friendly":
            print("%s wants to play with you!"%(self.na))
        else:
            print("Unfortunately %s is %s... You will have to earn the animal's trust!"%(self.na, self.fr))

    def age(self):
        year = 2021
        if year - self.bi > 10:
            print("%s is an aged %s."%(self.na, self.sp))
        elif year - self.bi > 4:
            print("%s is an adult %s."%(self.na, self.sp))
        else:
            print("%s is a young %s."%(self.na, self.sp))

def main():
    pet_1 = Pet(
        "Bidu",
        2006,
        "dog",
        "friendly"
    )

    pet_2 = Pet(
        "Balu",
        2016,
        "dog",
        "friendly"
    )

    pet_3 = Pet(
        "Zyg",
        2020,
        "cat",
        "shy"
    )

    pet_4 = Pet(
        "Bisteca",
        2014,
        "dog",
        "friendly"
    )

    pet_5 = Pet(
        "Churrasco",
        2015,
        "dog",
        "friendly"
    )

    pets = [
        pet_1,
        pet_2,
        pet_3,
        pet_4,
        pet_5
    ]

    for pet in pets:
        Pet.whois(pet)
    print()
    for pet in pets:
        Pet.play(pet)
    print()
    for pet in pets:
        Pet.age(pet)

main()
