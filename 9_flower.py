import turtle
from circle import circle
turtle.speed(100)
def flower():
    turtle.shape('turtle')
    for i in range(20):
        circle()
        turtle.left(8)
    pass


if __name__ == "__main__":
    flower()