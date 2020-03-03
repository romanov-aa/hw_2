import turtle
from circle import circle

def smile():
    turtle.shape("turtle")
    turtle.width(3)
    turtle.color('yellow')
    turtle.begin_fill()
    circle()
    turtle.end_fill()
    turtle.left(90)
    turtle.penup()
    turtle.forward(140)
    turtle.left(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.pendown()
    turtle.color('blue')
    turtle.begin_fill()
    for i in range(90):
        turtle.forward(2)
        turtle.left(4)
    turtle.end_fill()
    turtle.penup()
    turtle.right(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.pendown()
    turtle.begin_fill()
    for j in range(90):
        turtle.forward(2)
        turtle.right(4)
    turtle.end_fill()
    turtle.color('black')
    turtle.penup()
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.pendown()
    turtle.width(7)
    turtle.forward(40)
    turtle.penup()
    turtle.forward(45)
    turtle.pendown()
    turtle.left(90)
    turtle.width(3)
    turtle.color('red')
    for m in range(80):
        turtle.forward(1)
        turtle.left(1)
    for t in range(160):
        turtle.backward(1)
        turtle.right(1)
    for n in range(80):
        turtle.forward(1)
        turtle.left(1)






    pass

if __name__ == "__main__":
    smile()
    turtle.down()