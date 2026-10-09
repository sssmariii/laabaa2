import turtle
import random

def tree(branchLen, t):
    if branchLen > 5:
        t.pensize(branchLen / 10)
        
        if branchLen < 20:
            t.pencolor("green")
        else:
            t.pencolor("brown")
            
        t.forward(branchLen)
        
        angle = random.randint(15, 45)
        t.right(angle)
        tree(branchLen - random.randint(5, 15), t)
        
        t.left(angle * 2)
        tree(branchLen - random.randint(5, 15), t)
        
        t.right(angle)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.speed(0)
    tree(75, t)
    myWin.exitonclick()

main()