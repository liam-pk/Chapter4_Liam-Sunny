import turtle

def draw_square(turt, side_length):
    
    for i in range(4):
        turt.forward(side_length)
        turt.right(90)

canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

jim = turtle.Turtle()
jim.color("hot pink")
jim.pensize(3)


for i in range(5):
    draw_square(jim,20)
    jim.penup()
    jim.forward(40)
    jim.pendown()

wn.mainloop()

