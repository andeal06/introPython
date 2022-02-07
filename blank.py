import turtle

canvas = turtle.Screen()
canvas.bgcolor("Black")

t1 = turtle.Turtle()
t1.color("Aqua")
t1.speed(0)

def square():
    for i in range(4):
        t1.forward(90)
        t1.left(90)

def triangle():
    for i in range(3):
        t1.forward(90)
        t1.left(120)


for i in range(8):
    t1.penup()
    t1.forward(180)
    t1.left(45)
    t1.pendown()
    square()

t1.penup()
t1.forward(200)
t1.pendown()

triangle()


turtle.done()