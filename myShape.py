import turtle

canvas = turtle.Screen()
canvas.bgcolor("Black")

t1 = turtle.Turtle()
t1.color("Aqua")
t1.speed(8)

def myShape():
    for i in range(4):
        t1.forward(90)
        t1.left(90)


myShape()

turtle.done()