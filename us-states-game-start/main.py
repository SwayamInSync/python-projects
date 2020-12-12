import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
image = "blank_states_img.gif"

turtle.addshape(image)
turtle.shape(image)
score = 0
while 1 > 0:
    answer = screen.textinput(title=f"{score}/50 are Correct", prompt="What's another state name? ")
    answer = answer.title()
    file = pandas.read_csv("50_states.csv")
    state_list = file["state"].to_list()
    if answer in state_list:
        score += 1
        row = file[file["state"] == answer]
        xcor = int(row["x"])
        ycor = int(row["y"])
        pen.goto(xcor, ycor)
        pen.write(f"{answer}", align="center", font=("Courier", 8, "bold"))
    else:
        print("Think more")

