import turtle


def spring():
    turtle.shape('turtle')
    turtle.left(90)
    turtle.width(4)
    c = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
    for a in range(7):
        turtle.color(c[a % 6])
        for i in range(180):
            turtle.forward(1)
            turtle.right(1)
        for j in range(36):
           turtle.forward(1)
           turtle.right(5)
    pass

if __name__ == "__main__":
    spring()