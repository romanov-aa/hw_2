import turtle
import math

def polygon(R=10, n=3):
    turtle.shape('turtle')
    a = 2*R*math.sin(math.pi/n)
    b = 180 - (90*n - 180)/n
    print(b)
    alpha = 180*(n-2)/n
    gamma = 360/n

    turtle.left(b)
    for i in range(n):
        turtle.forward(a)
        turtle.left(gamma)
    turtle.right(b)

def regular_polygon():
    turtle.shape('turtle')
    turtle.color('green')
    turtle.width(5)
    for i in range(10):
        polygon(10+20*i, 3+i)
        turtle.penup()
        turtle.forward(20)
        turtle.pendown()



    pass
if __name__ == "__main__":
    regular_polygon()
    turtle.done()