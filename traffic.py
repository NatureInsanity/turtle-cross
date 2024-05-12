from turtle import Turtle
import random

COLOR = ["red", "green", "blue", "purple", "black", "brown"]


class Traffic:
    def __init__(self):
        self.traffic_list = []
        self.lvl = 6
        self.get_traffic()
        self.accel = 0.1

    def get_traffic(self):
        chance = random.randint(1, self.lvl)
        if chance == 1:
            pen = Turtle("square")
            pen.shapesize(stretch_wid=1, stretch_len=2)
            pen.color(random.choice(COLOR))
            pen.penup()
            pen.goto(300, random.randint(-240, 240))
            self.traffic_list.append(pen)

    def move(self):
        for cars in self.traffic_list:
            cars.goto(cars.xcor() - 10, cars.ycor())

    def reset(self):
        self.accel = 0.1
        self.lvl = 6
        for cars in self.traffic_list:
            cars.goto(1000,1000)
            cars.clear()
        self.get_traffic()

    def speed_up(self):
        if self.lvl != 1:
            self.lvl -= 1
        self.accel *= 0.9
