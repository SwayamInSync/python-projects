from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0,350)
        self.color("white")


    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Ariel", 20, "normal"))