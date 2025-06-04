import turtle


screen = turtle.Screen()
screen.bgcolor("white")


smiley = turtle.Turtle()
smiley.speed(5)
smiley.pensize(3)

smiley.penup()
smiley.goto(0, -100)
smiley.pendown()
smiley.fillcolor("yellow")
smiley.begin_fill()
smiley.circle(100)
smiley.end_fill()

# Draw left eye
smiley.penup()
smiley.goto(-40, 40)
smiley.pendown()
smiley.fillcolor("black")
smiley.begin_fill()
smiley.circle(15)
smiley.end_fill()


smiley.penup()
smiley.goto(40, 40)
smiley.pendown()
smiley.begin_fill()
smiley.circle(15)
smiley.end_fill()


smiley.penup()
smiley.goto(-60, -20)
smiley.pendown()
smiley.setheading(-60)
smiley.circle(70, 120)


smiley.hideturtle()
turtle.done()
