import turtle

def draw_mountain(t, x, y, width, height, depth):
    if depth == 0:
        t.up()
        t.goto(x, y)
        t.down()
        t.goto(x + width / 2, y + height)
        t.goto(x + width, y)
        t.goto(x, y)
    else:
        t.up()
        t.goto(x, y)
        t.down()
        t.goto(x + width / 2, y + height)
        t.goto(x + width, y)
        t.goto(x, y)
        
        draw_mountain(t, x, y, width / 2, height / 2, depth - 1)
        draw_mountain(t, x + width / 2, y, width / 2, height / 2, depth - 1)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.speed(0)
    draw_mountain(t, -200, -100, 400, 300, 4)
    myWin.exitonclick()

main()