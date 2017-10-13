import turtle
 
def createWindow(bgcolor, title):
       w = turtle.Screen()
       w.bgcolor(bgcolor)
       w.title(title)
       return w
 
def createTurtle(color, size):
      t = turtle.Turtle()
      t.pensize(size)
      t.color(color)
      return t
  
def draw_poly(t, n, sz):
      for i in range(n):
          t.forward(sz)
          t.left(360 / n)
  
wn = createWindow("lightgreen", "Exercises 4.3")
tess = createTurtle("hotpink", 3)
  
draw_poly(tess, 8, 50)
  
wn.mainloop()    