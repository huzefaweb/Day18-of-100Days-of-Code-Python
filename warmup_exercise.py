from turtle import *  # from this we can import everything we want
import random
# import turtle as t  # this gives the module a name
tim = Turtle()  # object

tim.shape("turtle")  # This shape method set the shape to a turtle
tim.color("red")  # set the color of turtle to red

#------------ square -----------
# for _ in range(4):
#     turtle.forward(100)
#     turtle.left(90)

# ------------ dash line --------------
# for i in range(30):
#     tim.pendown()
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)

colors = ["light steel blue", "sky blue", "dark cyan", "medium spring green", "gold", "goldenrod"]

# --------------- shapes -------------
# def sides(num_sides):
#     degree_sides = 360/num_sides
#     for i in range(num_sides):
#         tim.forward(100)
#         tim.right(degree_sides)
#
#
# for num in range(3, 11):
#     tim.color(random.choice(colors))
#     sides(num)

# --------- random walk ---------
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")
#
# for i in range(200):
#     tim.color(random.choice(colors))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
