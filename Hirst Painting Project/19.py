from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def rotate_clockwise():
    tim.circle(50, 90)


def rotate_counter_clock():
    tim.circle(-50, 90)


def clear_draw():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="W", fun=move_forwards)
screen.onkey(key="S", fun=move_backwards)
screen.onkey(key="A", fun=rotate_counter_clock)
screen.onkey(key="D", fun=rotate_clockwise)
screen.onkey(key="C", fun=clear_draw)
screen.exitonclick()
