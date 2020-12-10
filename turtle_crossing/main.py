import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
score = Scoreboard()

car_manager = CarManager()


screen.listen()

screen.onkey(turtle.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_new_cars()
    car_manager.move_car()

    if turtle.ycor() >= 280:
        turtle.goto(0, -280)
        # increase car speed
        car_manager.increase_speed()

        # increase level on scoreboard

        score.increase_score()
    for cars in car_manager.all_cars:
        if turtle.distance(cars) < 15:
            car_manager.stop()
            score.game_over()
            game_is_on = False



screen.exitonclick()