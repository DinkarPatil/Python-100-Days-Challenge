# Code to extract colors rgb code from image

# import colorgram
#
# colors = colorgram.extract('NY-Madison-Avenue.jpg', 10)
#
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)


color_list = [(235, 223, 201), (210, 154, 95), (189, 60, 29), (225, 212, 111), (234, 215, 224),
              (209, 147, 178), (177, 157, 44), (222, 225, 237), (224, 233, 226), (92, 103, 187)]

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



