import turtle
turtle = turtle.Turtle()
def draw_square():
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)
        
turtle.penup()
turtle.goto(-200, 100)
turtle.pendown()
draw_square()


def draw_triangle():
    for _ in range(3):
        turtle.forward(100)
        turtle.left(120)
        
turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
draw_triangle()


def draw_circle():
    turtle.circle(50)
    
turtle.penup()
turtle.goto(200, 100)
turtle.pendown()
draw_circle()


def draw_rectangle():
    for _ in range(2):
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(75)
        turtle.right(90)
        
turtle.penup()
turtle.goto(-150, -100)
turtle.pendown()
draw_rectangle()


def draw_pentagon():
    for _ in range(5):
        turtle.forward(100)
        turtle.right(72)
        
turtle.penup()
turtle.goto(100, -100)
turtle.pendown()
draw_pentagon()
   
