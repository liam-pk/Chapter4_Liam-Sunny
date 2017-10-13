import turtle

def drawFivePointStar(t):
    for i in range(5):
        t.forward(100)
        t.left(216)

wolfram = turtle.Turtle()
drawFivePointStar(wolfram)