from turtle import *  # from this we can import everything we want
import random
# import turtle as t  # this gives the module a name
tim = Turtle()  # object

tim.shape("turtle")  # This shape method set the shape to a turtle
tim.color("red")  # set the color of turtle to red

colormode(255)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0,255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


tim.speed("fastest")

tim.pensize(2)


def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.color(random_colour())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()  # method makes the screen to stay until we don't click
