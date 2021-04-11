import time
from tkinter import *

root = Tk()
root.title("typing speed calculator")
paragraph = "Lets keep typing and see how much is your speed, its a very minimal program to judge your typing in words per minute"


def start(target):
    global x
    target.unbind("<KeyPress>")
    x = time.time()


def done():
    y = time.time()  # gets time everytime called
    words = paragraph.split(" ")
    number_words = len(words)
    time_taken = y - x
    words_per_min = (number_words / time_taken) * 60
    ans = round(words_per_min, 2)
    Label(root, text=ans).grid(row=4, column=0)


def start_typing():
    start_btn.destroy()
    label = Label(root, text=paragraph).grid(row=0, column=0)
    entry = Entry(width=100)
    entry.grid(row=1, column=0)
    entry.bind("<KeyPress>", lambda event: start(target=entry))
    done_btn = Button(root, text="complete", command=done)
    done_btn.grid(row=3, column=0)


start_btn = Button(root, text="click here to  begin", padx=50, pady=30, command=start_typing)
start_btn.pack()

root.mainloop()
