import turtle
from time import sleep

canvas = turtle.Screen()
canvas.bgcolor("black")

t1 = turtle.Turtle()
t1.speed(5)


myColors = ["red", "orange", "yellow", "green", "blue", "purple"]

for x in range(200):
    t1.width(x//100 + 1)
    t1.pencolor(myColors[(x//18)%5])
    t1.forward(x*2)
    t1.left(108)

turtle.done()
