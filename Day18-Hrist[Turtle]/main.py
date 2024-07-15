# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("image.png",30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)


import turtle
from turtle import Screen
import random
turtle.colormode(255)

tim = turtle.Turtle()
colors = [(203, 155, 102), (70, 107, 129), (163, 77, 49), (123, 154, 169), (237, 244, 241), (234, 238, 242), (116, 83, 99), (132, 173, 156), (225, 197, 135), (50, 36, 20), (180, 94, 109), (159, 137, 74), (186, 128, 144), (22, 41, 54), (81, 117, 114), (82, 166, 132), (210, 101, 77), (232, 167, 164), (30, 74, 87), (38, 33, 35), (11, 28, 26), (148, 35, 29), (107, 122, 158), (92, 139, 152), (133, 36, 41), (222, 172, 177), (171, 203, 192), (39, 74, 72)]
tim.setheading(225)
tim.speed("fastest")

tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots+1):
    tim.dot(20, random.choice(colors))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = Screen()
screen.exitonclick()
