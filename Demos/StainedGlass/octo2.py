import turtle

canvas = turtle.Screen()
canvas.bgcolor("Black")

t1 = turtle.Turtle()
t1.color("Aqua")
t1.speed(9)


#octogon with octogons

def shape(length):
    for i in range(8):
        t1.forward(length)
        t1.left(45)



for i in range(8):
    t1.penup()
    t1.forward(90)
    t1.left(45)
    t1.pendown()
    shape(50)

turtle.done()