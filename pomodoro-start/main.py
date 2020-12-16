from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    title_label.config(text="Work")
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    if (reps + 1) % 2 == 0 and (reps + 1) < 8:
        title_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    elif (reps + 1) == 8:
        title_label.config(text="Long Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    if count == 0:
        reps += 1
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✓"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
title_label = Label(text="Timer", font=(FONT_NAME, 40, "normal"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)
check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", bg=YELLOW, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", bg=YELLOW, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
