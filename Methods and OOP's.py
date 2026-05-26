"""class fruit:
    def __init__(self, fruit, colour):
        self.fruit = fruit
        self.colour = colour

    def intro(self):
        print("The fruit is: ",self.fruit)

Pineapple = fruit("Pineapple", "yellow")
Pineapple.intro()"""

"""lists = ["apple","banana","Kiwi"]

obj1 = enumerate(lists)

print(list(enumerate(lists)))"""

#activity 1
class Employee:
        def __init__(self, id, job):
            print("Contructor made!")
            self.id = id
            self.job = job

        def __del__(self):
            print("Object destroyed!")

obj = Employee(1, "restocking")
print(obj.id)
del obj
print(obj.job)

