import turtle

canvas = turtle.Screen()
canvas.bgcolor("Black")

t1 = turtle.Turtle()
t1.color("Aqua")

for size in range(20, 300, 20):
    for i in range(4):
        t1.forward(size)
        t1.left(90)
    
    t1.penup()
    t1.right(140)
    t1.forward(14)
    t1.left(140)
    t1.pendown()
    
    

turtle.done()
    
