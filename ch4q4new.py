##Draw this pretty pattern.

import turtle

def draw_square(turtle):
    for i in range(0,4):
        turtle.forward(100) 
        turtle.right(90)           

def draw_art():        
 
    window = turtle.Screen()
    window.bgcolor("lightgreen")     

    
    brad = turtle.Turtle()
    brad.shape("turtle")      
    brad.color("blue")      
    brad.speed(50)             

    
    for i in range (0, 20):
        draw_square(brad)
        brad.right(18)

    
    window.exitonclick()      


draw_art()