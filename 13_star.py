import turtle

turtle.shape("turtle")

def star(n=5):
    turtle.color('red')
    turtle.begin_fill()
    if n % 2 != 0:
        for i in range(n):
            turtle.forward(100)
            a = n // 2 * 360 / n
            turtle.left(a)
    turtle.end_fill()


star()
turtle.done()