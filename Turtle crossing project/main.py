import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager(scoreboard)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    screen.listen()
    screen.onkey(player.go_up, "Up")

    car_manager.update()

    if player.ycor() == 280:
        scoreboard.increase_level()
        player.reset_position()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()