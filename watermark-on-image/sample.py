
import PIL
from PIL import ImageTk, ImageDraw, ImageFont
from tkinter import filedialog
from tkinter import *

image_filetypes=[
    ('image files', '.png'),
    ('image files', '.jpg'),
    ('image files', '.tif'),
    ('image files', '.bmp'),
]

def copyright_text():
    text = text_to_add.get()
    with PIL.Image.open(file) as im:
        # Store image width and height
        w, h = im.size
        # make the image editable
        drawing = ImageDraw.Draw(im)
        font = ImageFont.truetype("Arial.ttf", 68)
        # get text width and height
        text = "© " + text + "   "
        text_w, text_h = drawing.textsize(text, font)
        pos = w - text_w, (h - text_h) - 50
        c_text = PIL.Image.new('RGB', (text_w, (text_h)), color='#000000')
        drawing = ImageDraw.Draw(c_text)
        drawing.text((0, 0), text, fill="#ffffff", font=font)
        c_text.putalpha(100)
        im.paste(c_text, pos, c_text)
        filename = filedialog.asksaveasfilename(filetypes=image_filetypes)
        im.save(filename)


def copyright_logo():
    file2 = filedialog.askopenfilename(title="Please select an logo picture", filetypes=image_filetypes)
    with PIL.Image.open(file) as im:
        im2 = PIL.Image.open(file2)
        w, h = im.size
        w1, h1 = im2.size
        pos = w - 20, (h - h1) - 50
        im2.putalpha(100)
        im.paste(im2, pos)
        filename = filedialog.asksaveasfilename(filetypes=image_filetypes)
        im.save(filename)


window = Tk()
window.title("Watermark Generator")
window.config(padx=40, pady=40)

label = Label(text="Custom Watermarkm: Add a photo to begin", width=40, bg='skyblue', font=("Arial", 18, "normal"))
label.grid(row=0, column=0, columnspan=3)

canvas = Canvas(width=600, height=400, highlightthickness=10)
file = filedialog.askopenfilename(title="Please select an image to edit", filetypes=image_filetypes)
label.config(text="Photo loaded, input a text or choose a logo")
original = PIL.Image.open(file)
original = original.resize((600, 400))
pic = ImageTk.PhotoImage(original)
canvas.create_image(0, 0, image=pic, anchor="nw")
canvas.grid(row=1, column=0, columnspan=3)

label = Label(text="Input text", width=10, font=("Arial", 14, "normal"))
label.grid(row=2, column=0)
text_to_add = Entry(width=30, )
text_to_add.insert(index=0, string="Input here")
text_to_add.grid(row=2, column=1)
button1 = Button(text="Add Text", width=10, command=copyright_text)
button1.grid(row=2, column=2)

button2 = Button(text="Add Photo", width=50, command=copyright_logo)
button2.grid(row=3, column=0, columnspan=3)

button = Button(text='Close the window', command=window.quit)

button.grid(row=4, column=0, columnspan=3)

window.mainloop()