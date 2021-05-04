import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()

screen.listen()
screen.onkey(player.move, "Up")

cars = CarManager()

scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move_cars()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False


    if player.ycor() > 280:
        player.refresh()
        cars.level_up()
        scoreboard.level_on()
        








screen.exitonclick()
