import turtle
from turtle import Turtle
import random

STARTING_POSITIONS = []
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r,g,b)

class Bricks(Turtle):
    def __init__(self):
        super().__init__()
        self.all_bricks = []

    def put_bricks(self):
        for n in range(-9,10,2):
            new_brick = Turtle("square")
            new_brick.color(random_color())
            new_brick.penup()
            new_brick.shapesize(stretch_len=3, stretch_wid=1)
            x,y = 40*n , 320
            new_brick.goto(x,y)
            self.all_bricks.append(new_brick)

    def destroy_brick(self):
        self.hideturtle()


