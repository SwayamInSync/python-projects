FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.goto(-280,260)
        self.update()

    def update(self):
        self.write(f"Level: {self.score}", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(-15,0)
        self.write("GAME OVER", font=FONT)