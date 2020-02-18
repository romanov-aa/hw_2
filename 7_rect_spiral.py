import turtle
def rect_spiral():
    turtle.shape('turtle')
    turtle.width(3)
    c = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
    n = 20
    for i in range(360):
        turtle.color(c[i % 6])
        for j in range(10):
            turtle.forward(n)
            turtle.left(90)
            n += 10


    pass
if __name__ == "__main__":
    rect_spiral()