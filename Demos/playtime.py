import turtle

canvas = turtle.Screen()
canvas.title("Playtime Fun")


t1 = turtle.Turtle()
t1.speed(0)

for x in range(75):
    t1.width(0.5)
    t1.forward(200)
    t1.left(150)
    t1.forward(50)
    t1.left(80)
    t1.forward(32)
    t1.right(152)

turtle.done()

