from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(height=400, width=500)
is_game_on = False
user_input = screen.textinput(title="What's your bet", prompt="Which Turtle will win? Enter a color ")
colors = ["red", "yellow", "orange", "green", "blue", "purple"]
turtles = []
if user_input:
    is_game_on = True

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=100 - (i * 40))
    turtles.append(new_turtle)


while is_game_on:
    for turtle in turtles:
        if turtle.xcor()>230:
            is_game_on = False
            if turtle.pencolor() == user_input:
                print(f"You Won {turtle.pencolor()} is win")
            else:
                print(f"You lost {turtle.pencolor()} is Won ")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)





















screen.exitonclick()