class dog:
    animal = "Dog"

    def __init__(self, breed, colour):
        self.breed = breed
        self.colour = colour

    def details(self):
        print(" The animal is :", dog.animal)
        print("The breed is :", self.breed)
        print(" The colour is :", self.colour)

dog1 = dog(" German Shepherd", "Brown")
dog2 = dog("Labrador", "Golden")

print("Detalis of Dog 1:")
dog1.details()

print("Details of Dog 2:")
dog2.details()