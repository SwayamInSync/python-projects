BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random

to_learn = {}
current_card = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")  # make list as ( {column : value} ) having dictionaries items


def is_known():
    global current_card, known_cards
    to_learn.remove(current_card)
    w = pandas.DataFrame(to_learn)
    w.to_csv("data/words_to_learn.csv", index=False)
    print(len(to_learn))
    next_card()


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(head, text="French")
    canvas.itemconfig(word, text=current_card["French"])
    canvas.itemconfig(card, image=front)
    canvas.itemconfig(word, fill="black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(head, text="English Translation")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(card, image=back)


window = Tk()
window.config(padx=50, pady=50)
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")
front = PhotoImage(file="images/card_front.png")
back = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=525)
card = canvas.create_image(400, 267.5, image=front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
correct_button = Button(image=right, highlightthickness=0, command=is_known)
correct_button.grid(column=1, row=1)
wrong_button = Button(image=wrong, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)
head = canvas.create_text(400, 190, text="title", font=("Ariel", 28, "normal"))
word = canvas.create_text(400, 300, text="Word", font=("Ariel", 50, "bold"))

next_card()

window.mainloop()
