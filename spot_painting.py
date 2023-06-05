# import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

from turtle import *
import random
colormode(255)
tim = Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(206, 163, 101), (148, 68, 43), (240, 244, 241), (58, 102, 131), (169, 152, 37), (239, 240, 244), (220, 203, 136), (135, 34, 22), (208, 89, 67), (131, 165, 185), (47, 115, 78), (100, 80, 89), (240, 173, 158), (141, 183, 145), (69, 51, 45), (61, 50, 53), (13, 102, 73), (92, 143, 151), (88, 154, 113), (162, 141, 160), (17, 90, 94), (39, 58, 81), (78, 69, 46), (48, 63, 82), (83, 133, 175), (93, 48, 53), (183, 204, 169), (37, 63, 52)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
numbers_of_dots = 100
for dot_count in range(1, numbers_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()
