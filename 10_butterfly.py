import turtle


def butterfly(n=3):
    turtle.shape('turtle')
    for i in range(10):
        turtle.width(10)
        turtle.begin_fill()
        for j in range(180):
            turtle.color("blue")
            turtle.forward(n)
            turtle.left(2)
        turtle.end_fill()
        turtle.begin_fill()
        for y in range(180):
            turtle.color("yellow")
            turtle.forward(n)
            turtle.right(2)
        turtle.end_fill()
        n += 1
    pass


if __name__ == "__main__":
    butterfly()