import turtle

def koch_curve(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        koch_curve(t, length / 3, depth - 1)
        t.left(60)
        koch_curve(t, length / 3, depth - 1)
        t.right(120)
        koch_curve(t, length / 3, depth - 1)
        t.left(60)
        koch_curve(t, length / 3, depth - 1)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.speed(0)
    t.up()
    t.goto(-150, 0)
    t.down()
    koch_curve(t, 300, 4)
    myWin.exitonclick()

main()