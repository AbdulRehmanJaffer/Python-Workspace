"""class dad:
    def __init__(self, eyes, aggressive):
        self.eyes = eyes
        self.aggressive = aggressive

    def display(self):
        print("Your eye colour:", self.eyes)
        print("You are aggressive:", self.aggressive)

class son(dad):
    def __init__(self, name, age, eyes, aggressive):
        self.name = name
        self.age = age

        dad.__init__(self, eyes, aggressive)

obj = son("Hamza",13, "Hazel", True)
print(obj.display())"""

#activity 1
class person():
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
    def display(self):
        print("Your name is:", self.name)
        print("Your ID number is:", self.id_number)

class employee(person):
    def __init__(self, name, id_number, salary):
        self.salary = salary

        person.__init__(self, name, id_number)
    
obj = employee("Ali", 2, 15000)
print(obj.display())