class BMW():
    def __init__(self, max_speed):
        self.max_speed = max_speed
        
    def speed(self):
        print("The max speed of a BMW M4 is :", self.max_speed)

class Ferrari():
    def __init__(self, max_speed):
        self.max_speed = max_speed

    def speed(self):
        print("The Max speed of a Ferrari 250 GTO is :", self.max_speed)

speed1 = BMW(180)
speed2 = Ferrari(174)

for i in (speed1, speed2):
    print(i.speed())