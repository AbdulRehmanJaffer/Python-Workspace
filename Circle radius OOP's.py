class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
            print(3.14*self.radius**2)

    def perimeter(self):
            print(2*3.14*self.radius)


circle1 = circle(32)
circle1.radius
circle1.area()
circle1.perimeter()
