import turtle

def nested_rectangle():
    turtle.shape('turtle')
    type1 = 20
    for i in range(10):
       for i in range(4):
          turtle.forward(type1)
          turtle.left(90)
       turtle.penup()
       turtle.right(180)
       turtle.forward(20)
       turtle.left(90)
       turtle.forward(20)
       turtle.left(90)
       turtle.pendown()
       type1 = type1 + 40

    pass


if __name__ == "__main__":
    nested_rectangle()