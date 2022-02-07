import turtle

canvas = turtle.Screen()

t1 = turtle.Turtle()

sizes = [10, 30, 50 ,70 ,90, 110, 130, 150]

for size in sizes:
    for i in range(4):
        t1.forward(size)
        t1.left(90)

turtle.done()