import turtle

def spider():
    turtle.shape('turtle')
    for i in range(12):
       turtle.forward(90)
       turtle.stamp()
       turtle.backward(90)
       turtle.right(30)

    pass


if __name__ == "__main__":
    spider()