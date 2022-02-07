import turtle
from time import sleep


#canvas = turtle.Screen()


t1 = turtle.Turtle()

t1.forward(180)
t1.right(90)
t1.forward(180)
t1.right(90)
t1.forward(180)
t1.right(90)
t1.forward(180)


#creates same thing, but much simpler to read
for i in range(4):
    t1.forward(100)
    t1.left(90)
    sleep(7)





turtle.done()

