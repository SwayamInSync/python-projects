from tkinter import *
from tkinter import filedialog, PhotoImage
from watermark import watermark

window = Tk()
image_path = filedialog.askopenfilename(title="select image", filetypes=(("png files", "*.png"),("all files", "*.*")))

def add_mark():
    watermark(image_path, text.get())

top = Toplevel()
text = Entry(top)
text.grid(column=0, row=0)
button = Button(top)
button.config(text="add", command=add_mark)
button.grid(column=0, row=1)




window.mainloop()