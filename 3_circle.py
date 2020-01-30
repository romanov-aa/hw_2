import turtle

def circle():
    turtle.shape('turtle')
    for i in range(360):
        turtle.forward(2)
        turtle.left(1)
    pass
if __name__ == "__main__":
    circle()