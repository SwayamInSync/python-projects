import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
image = "blank_states_img.gif" # turtle module only process .gif type images

turtle.addshape(image) # for adding user-defined shapes to turtle 
turtle.shape(image) # now giving uder-defined shape to turtle
score = 0
while 1 > 0:
    answer = screen.textinput(title=f"{score}/50 are Correct", prompt="What's another state name? ") # producing a prompt on screen ( basically a small window )
    answer = answer.title()
    file = pandas.read_csv("50_states.csv")
    state_list = file["state"].to_list() # creating Series to a list
    if answer in state_list:
        score += 1
        row = file[file["state"] == answer] # accessing the row in dataframe
        xcor = int(row["x"]) # panda create dataframe with string entries so converting coordinates to integer
        ycor = int(row["y"])
        pen.goto(xcor, ycor) # coordinates should be integer
        pen.write(f"{answer}", align="center", font=("Courier", 8, "bold"))
    else:
        print("Think more")

