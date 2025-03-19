from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

r_paddle = Paddle(370)
l_paddle = Paddle(-370)

ball = Ball()
scoreboard = Scoreboard()

screen = Screen()

screen.title("Welcome to Pong game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with upper and lower walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # Detect Right paddle misses
    if ball.xcor() > 380:
        ball.restart()
        scoreboard.l_point()

    # Detect Left paddle misses
    if ball.xcor() < -380:
        ball.restart()
        scoreboard.r_point()

screen.exitonclick()
