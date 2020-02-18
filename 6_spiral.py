import turtle
import math
def spiral(n=10, h=10, m=60, r=10):
    turtle.shape('turtle')
    turtle.width(10)
    turtle.color("red")
    c = ['red', 'green', 'yellow', 'blue', 'violet', 'brown']
    for i in range(n):

        for _ in range(m):
            turtle.color(c[_ % 6])
            r += 1
            a =2*r*math.sin(math.pi/m)
            turtle.forward(a)
            turtle.right(360/m)
    pass


if __name__ == "__main__":
    spiral()