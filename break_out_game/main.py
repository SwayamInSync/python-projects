import time
from turtle import Turtle, Screen
from paddle import Paddle
from bricks import Bricks
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.title("Ping Pong")
screen.bgcolor("black")
screen.setup(width=800, height=800)
screen.listen()
screen.tracer(0)

paddle = Paddle()
brick = Bricks()
brick.put_bricks()
ball = Ball()
scoreboard = Scoreboard()


screen.onkey(paddle.go_right,"Right")
screen.onkey(paddle.go_left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    if ball.ycor() >= 380:
        ball.bounce_from_ceiling()
    if ball.xcor() >= 380 or ball.xcor() <= -380:
        ball.bounce_from_wall()

    if ball.distance(paddle) < 55 and ball.ycor() < -335:
        ball.bounce_from_ceiling()

    if ball.ycor() < -380:
        ball.reset()
        ball.hideturtle()
        scoreboard.game_over()

    for block in brick.all_bricks:
        if ball.distance(block) <= 20:
            print("hit")
            block.hideturtle()



screen.exitonclick()