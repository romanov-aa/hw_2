import turtle

turtle.speed(100)
def spider():
    turtle.shape('turtle')
    n=50
    for i in range(n):
       turtle.left(360/n)
       turtle.forward(90)
       turtle.stamp()
       turtle.backward(90)


    pass


if __name__ == "__main__":
    spider()