import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
# set the screen dim and turn animations off
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
# user turtle obj
player = Player()
# cars obj
car_manager = CarManager()
# scoreboard obj
scoreboard = Scoreboard()
# dectect if user hits up arrow to move turtle forward
screen.listen()
screen.onkey(player.go_up, "Up")
# start game
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # open the scoreboard, add a car to the list, and move the cars at a constant speed
    scoreboard.write_board()
    car_manager.create_car()
    car_manager.move_cars()

    # check for turtle/user collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.end_game_print()
            game_is_on = False
    # check if turtle/user crossed the finish line
    if player.check_end():
        player.go_to_start()
        car_manager.increase_speed()
        scoreboard.increment_level()

screen.exitonclick()
