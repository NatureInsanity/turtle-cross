from turtle import Screen
from player import Player
from traffic import Traffic
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.title("Turtle Race")
screen.tracer(0)

player = Player()
traffic = Traffic()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")

game = True
while game:
    time.sleep(traffic.accel)
    screen.update()
    traffic.get_traffic()
    traffic.move()
    for cars in traffic.traffic_list:
        if cars.distance(player) < 20:
            player.reset()
            traffic.reset()
            scoreboard.refresh()
    if player.ycor() > 290:
        scoreboard.new_score()
        traffic.speed_up()
        player.reset()
    if player.ycor() < -280:
        game = False


scoreboard.save()

screen.exitonclick()
