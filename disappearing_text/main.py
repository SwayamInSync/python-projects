from tkinter import *
import time

TIME = 5

window = Tk()
window.title("Don't stop writing")
window.minsize(width=400, height=400)



def check_typing(current_entry):
    global timer, time_passed
    text_box_entry = T.get("1.0", END)

    if len(text_box_entry) - len(current_entry) == 0:
        time_passed += 1
        if time_passed > 0 and time_passed % 5 == 0:
            T.delete("1.0", END)
            time_passed = 0
            timer = window.after(1000, check_typing, "")
        else:
            timer = window.after(1000, check_typing, text_box_entry)
    else:
        time_passed = 0
        timer = window.after(1000, check_typing, text_box_entry)



label = Label(text="Start writing", font=('Ariel', 20, 'normal')).grid(column=0, row=0)

T = Text(height=30, width=55, bg="light yellow")
T.grid(column=0, row=1)

check_typing("")
window.mainloop()
