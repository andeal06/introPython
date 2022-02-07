import turtle
from time import sleep


canvas = turtle.Screen()
canvas.title("Turtle Playground")

t1 = turtle.Turtle()
t1.speed(0)

canvas.bgcolor("black")


myAngles = [71, 73, 80, 83, 91, 96, 98, 100, 102, 103, 106, 108, 118, 126, 127, 128, 129, 130, 131, 132, 134, 135, 136, 137, 138, 139, 140, 143, 145, 149, 150, 160, 162, 192, 194, 196, 206, 209, 210, 214, 218, 220, 229, 233, 249, 252, 285, 286, 287, 289, 299, 303, 310, 320, 330]
myColors = ["red", "orange", "yellow", "green", "blue", "violet"]

for angle in myAngles:
    for x in range(150):
        t1.pencolor(myColors[(x%6)])
        t1.width(x//100 +1)
        t1.forward(x*2)
        t1.left(angle)

    print(angle)
    sleep(3)
    canvas.clearscreen()
    t1 = turtle.Turtle()
    t1.speed(0)
    canvas.bgcolor("black")
    


turtle.done()




