from turtle import Turtle

import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_CREATION_INTERVAL = 10


class CarManager:

    def __init__(self, scoreboard):
        self.all_cars = []
        self.frame_count = 0
        self.scoreboard = scoreboard

    def create_car(self):
        if self.frame_count % CAR_CREATION_INTERVAL == 0:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.setposition(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_cars(self):
        for seg in self.all_cars:
            seg.setx(seg.xcor() - STARTING_MOVE_DISTANCE - MOVE_INCREMENT * self.scoreboard.level)
            if seg.xcor() < -290:
                seg.hideturtle()
                self.all_cars.remove(seg)

    def update(self):
        self.frame_count += 1
        self.create_car()
        self.move_cars()
