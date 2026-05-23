"""class student:
    def __init__(self, id, name, section):
        self.id = id
        self.name = name
        self.section = section
#functions
    def enroll(self):
        print(self.name, self.id, "Hey welcome to XYZ school")

#objects 
student_1 = student("01", "Ali", "C")
student_1.enroll()

student_1 = student("03", "Ayesha", "D")
student_1.enroll()

student_1 = student("02", "Ahmed", "A")
student_1.enroll()"""

#activity 1

class Vehicle:
    def __init__(self, max_speed, mileage):

        self.max_speed = max_speed
        self.mileage = mileage

car = Vehicle("130", "560km")
print(car.max_speed, car.mileage)