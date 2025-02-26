# import colorgram
#
# colors = colorgram.extract('HirstPainting.jpg', 10)
#
# total = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     case = (r,g,b)
#     total.append(case)
#
# print(total)

import turtle
import random

color_list = [ (182, 65, 34), (213, 149, 97), (14, 245, 42), (55, 137, 233), (239, 208, 94), (25, 234, 142), (237, 62,
                                                                                                             33),(157, 26, 19)]

turtle.colormode(255)
tim = turtle.Turtle()
tim.speed(0)
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle.Screen()
screen.exitonclick()