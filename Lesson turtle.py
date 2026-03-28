#activity 1
"""import turtle

turtle.Screen().bgcolor("Orange")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle()

num_sides = 6
side_length = 70
angles = 360.0 / num_sides

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angles)

turtle.done()"""
#activity 2
"""import turtle

turtle.Screen().bgcolor("Aqua")
board = turtle.Turtle()

board.forward(100)

board.left(120)
board.forward(100)

board.left(120)
board.forward(100)

board.penup()
board.right(150)
board.forward(50)
#second triangle
board.pendown()

board.right(90)
board.forward(100)

board.right(120)
board.forward(100)

board.right(120)
board.forward(100)

turtle.done()"""
#activity 3
"""import turtle

turtle.Screen().bgcolor("Lime")
square = turtle.Turtle()
square.fillcolor("red")

num_sides = 4
side_length = 70
angle = 90

for i in range(num_sides):
    square.forward(side_length)
    square.right(angle)

turtle.done()"""
#activity 4
"""import turtle

spiral = turtle.Turtle()
colors = ["red","orange","yellow", "green", "blue", "purple"]
spiral.speed(0)

for i in range(1000):
    spiral.pencolor(colors[i%6])
    spiral.forward(i * 2)
    spiral.right(90)
turtle.done()"""



"""import turtle

turtle.speed(1)

my_circle = turtle.Turtle()

radius = 150
i = 0

for i in range (radius):
    my_circle.circle(i)

turtle.done()"""

"""import turtle
turtle.speed(1)

screen = turtle.Screen().setup(1000,1000)
t = turtle.Turtle()
t.hideturtle() # Hide the turtle icon
t.penup()      # Lift the pen to move without drawing a line

# Move to the desired pixel coordinate (e.g., x=50, y=50)
t.goto(0, 0) 

# Draw a dot (simulated pixel) with a specified diameter (e.g., 5 pixels)
t.dot(5, "red") # Arguments are diameter and color

turtle.done() # Keep the window open"""

import turtle
import math

screen = turtle.Screen()
screen.title("My Circle")
screen.bgcolor("white")
screen.tracer(0)

turtle.penup()
turtle.goto(0,0)
turtle.dot(2,"blue")
turtle.color("blue")
turtle.speed(0)
radius = 0
angle_deg=20*360
for angle_step_deg in range(angle_deg+1):
    angle_step_rad=math.radians(angle_step_deg)
    y = radius * math.sin(angle_step_rad) # a = r*sin(theta)
    x = radius * math.cos(angle_step_rad) # b = r cos (theta)
    turtle.goto(x,y)
    turtle.dot(2,"blue")
    radius = radius + 0.05
screen.update() # Display the drawing all at once
turtle.done()


"""def draw_dotted_circle(radius, center_x, center_y, dot_size, color):
    
    #Draws a dotted circle using the turtle.dot() method and mathematical equations.

    turtle.penup() # Lift the pen to avoid drawing lines between dots
    turtle.goto(center_x, center_y - radius) # Move to the starting point on the circumference

    # Set drawing parameters
    turtle.dot(dot_size, color)
    turtle.color(color)
    turtle.speed(0) # Set speed to fastest

    # Calculate the number of points needed for a smooth circle
    # More steps result in a more continuous circle
    steps = 360
    
    for angle in range(steps + 1):
        # Convert angle from degrees to radians for math functions
        rad_angle = math.radians(angle)
        
        # Calculate x and y coordinates using the circle equation
        x = center_x + radius * math.cos(rad_angle)
        y = center_y + radius * math.sin(rad_angle)
        
        # Move the turtle to the calculated position and draw a dot
        turtle.goto(x, y)
        turtle.dot(dot_size, color)

    turtle.hideturtle() # Hide the turtle icon when finished

# --- Main execution ---
if __name__ == "__main__":
    screen = turtle.Screen()
    screen.title("Dotted Circle using Circle Equation and turtle.dot()")
    screen.bgcolor("white")

    # Define circle parameters
    RADIUS = 100
    CENTER_X = 0
    CENTER_Y = 0
    DOT_SIZE = 5
    COLOR = "red"

    draw_dotted_circle(RADIUS, CENTER_X, CENTER_Y, DOT_SIZE, COLOR)

    # Keep the window open until clicked
    screen.exitonclick()"""

