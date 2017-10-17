import turtle

alex = turtle.Turtle()

for i in range(5):
    alex.forward(110)
    alex.left(216)

def draw_star():
    for i in range(5):
        alex.penup()
        alex.forward(350)
        alex.right(144)
        alex.pendown()
    
        
    