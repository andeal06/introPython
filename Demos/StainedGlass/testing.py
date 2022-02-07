import turtle

canvas = turtle.Screen()
canvas.bgcolor("Black")

t1 = turtle.Turtle()
t1.color("Aqua")
t1.speed(0)


def octo():
    for i in range(8):
        t1.forward(90)
        t1.left(45)

for i in range(4):
    t1.penup()
    t1.forward(90)
    t1.left(90)
    t1.pendown()
    octo()


turtle.done()