import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

the_player = Player()
the_car = CarManager()
the_scoreboard = Scoreboard()

screen.listen()
screen.onkey(the_player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    the_car.generate_car()
    the_car.move_cars()

    # detect collision with car
    # note that cars are 40x20
    for car in the_car.all_cars:
        if car.distance(the_player) < 20:
            game_is_on = False
            the_scoreboard.game_over()

    # turtle/the_player crosses successfully
    if the_player.at_finish_line():
        the_player.go_to_start()
        the_car.level_up()
        the_scoreboard.increase_level()

screen.exitonclick()
