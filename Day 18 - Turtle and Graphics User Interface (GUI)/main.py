# from turtle import Turtle, Screen
#
# tim = Turtle()
# timmy_the_turtle.shape('turtle')
# timmy_the_turtle.color('green')
# timmy_the_turtle.square(50)
import random
# Draw a square using Turtle
# Long way
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)

# Shortcut
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)


# Ways to import libraries

# import turtle
# tim = turtle.Turtle()


# from turtle import Turtle
# tim = Turtle()

# Importing everything from turtle module
# from turtle import *

# Alias Module
# import turtle as t
# tim = t.Turtle()

from turtle import Turtle, Screen

tim = Turtle()


# Create a dotted line using turtle (for function refer documentations)
# for _ in range(50):
#     tim.pendown()
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)


# Draw square, pentagon, hexagon and so on

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


colors = ["CornflowerBlue", "DarkOrchid",
          "IndianRed", "DeepSkyBlue", "LightSeaGreen",
          "wheat", "SlateGray", "SeaGreen"]

# Draw different polygon using same side
for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()
