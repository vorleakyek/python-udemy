import turtle
from turtle import Turtle, Screen
import random

turtle1 = Turtle()
turtle.colormode(255)
turtle1.shape("turtle")
turtle1.color("DarkCyan")


def square_path():
    for _ in range(4):
        turtle1.forward(100)
        turtle1.right(90)


def dashed_line_path():
    for _ in range(5):
        turtle1.forward(10)
        turtle1.penup()
        turtle1.forward(10)
        turtle1.pendown()


def tri_to_oct_path():
    for num_sides in range(3, 11):
        random_color()
        draw_shape(num_sides)


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        turtle1.right(angle)
        turtle1.forward(100)


def random_color():
    r = random.randint(0,225)
    g = random.randint(0,225)
    b = random.randint(0,225)
    random_color_rgb = (r, g, b)
    return random_color_rgb


def random_path():
    turtle1.speed('fast')
    turtle1.pensize(5)
    steps = 35
    direction = [0, 90, 180, 270]

    for _ in range(100):
        turtle1.color(random_color())
        angle = random.choice(direction)
        turtle1.setheading(angle)
        turtle1.forward(steps)


def circular_path(size_of_gap):
    turtle1.speed('fastest')
    for _ in range(int(360 / size_of_gap)):
        turtle1.color(random_color())
        turtle1.circle(100)
        current_heading = turtle1.heading()
        turtle1.setheading(current_heading + size_of_gap)


# square_path()
# dashed_line_path()
# tri_to_oct_path()
# random_path()
circular_path(10)
screen = Screen()
screen.exitonclick()
