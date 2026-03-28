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
import turtle

spiral = turtle.Turtle()
colors = ["red","orange","yellow", "green", "blue", "purple"]
spiral.speed(0)

for i in range(100):
    spiral.pencolor(colors[i%6])
    spiral.forward(i * 2)
    spiral.right(90)
turtle.done()