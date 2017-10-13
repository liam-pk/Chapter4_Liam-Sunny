##Write a program to draw this. Assume the innermost square is 20 units per side,
##and each successive square is 20 units bigger, per side, than the one inside it.
from turtle import Turtle, Screen

HYPOTENUSE = (2 ** 0.5) / 2

screen = Screen()
screen.bgcolor("lightgreen")

tess = Turtle()
tess.pencolor("hotpink")
tess.setheading(45)
tess.width(3)

for radius in range(20, 20 * 5 + 1, 20):
    tess.penup()
    tess.goto(radius/2, -radius/2)
    tess.pendown()
    tess.circle(radius * HYPOTENUSE, steps=4)

screen.exitonclick()