from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.y_step = 10
        self.x_step = 10
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()

    def move(self):
        new_x = self.xcor() + self.x_step
        new_y = self.ycor() + self.y_step
        self.goto(new_x,new_y)

    def bounce_from_ceiling(self):
        self.y_step *= -1
        self.move()

    def bounce_from_wall(self):
        self.x_step *= -1
        self.move()
