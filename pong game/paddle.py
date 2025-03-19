from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, pos_x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(pos_x, 0)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    # paddle1 = Turtle()
    # paddle1.shape("square")
    # paddle1.color("white")
    # paddle1.shapesize(stretch_wid=5, stretch_len=1)
    # paddle1.penup()
    # paddle1.speed(0)
    # paddle1.goto(360, 0)
    #
    # def go_up():
    #     new_y = paddle1.ycor() + 20
    #     paddle1.goto(paddle1.xcor(), new_y)
    #
    # def go_down():
    #     new_y = paddle1.ycor() - 20
    #     paddle1.goto(paddle1.xcor(), new_y)
