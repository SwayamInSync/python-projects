# import colorgram
import turtle as t
import random

# colors = colorgram.extract("image.jpg", 30)
#
# rgb = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb.append(new_color)
#
# print(rgb)
t.colormode(255)
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

tim = t.Turtle()

for n1 in range(30,300,30):
    for n2 in range(10):
        chosen_color = random.choice(color_list)
        tim.dot(20, chosen_color)
        tim.penup()
        tim.forward(30)
    tim.setposition(0,n1)







screen = t.Screen()
screen.exitonclick()