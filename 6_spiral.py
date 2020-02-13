import turtle

def spiral():
    turtle.shape('turtle')
    for i in range(100):
        turtle.forward(6)
        turtle.left(5)
    pass


if __name__ == "__main__":
    spiral()