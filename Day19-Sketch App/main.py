import turtle
from turtle import Turtle, Screen
tim = Turtle()


def forward():
    tim.forward(10)

def backward():
    tim.backward(10)

def left():
    # new_heading = tim.heading() + 10
    # tim.setheading(new_heading)
    tim.left(10)

def right():
    # new_heading = tim.heading() - 10
    # tim.setheading(new_heading)
    tim.right(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen = Screen()
screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
