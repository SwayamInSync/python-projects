from tkinter import *
from tkinter import filedialog
import fitz
from gtts import gTTS
from playsound import playsound


root = Tk()
root.title("convert pdf to audiobook")
root.geometry("500x500")

# Creating a textbox
my_text = Text(root, height=30, width=60)
my_text.pack(pady=10)


def clear_text():
    my_text.delete(1.0, END)


def open_pdf():
    open_file = filedialog.askopenfilename(
        initialdir="/Users/swayam/Downloads/",
        title="Open PDF file",
        filetypes=(
            ("PDF Files", "*.pdf"),
            ("All Files", "*.*")
        )
    )

    if open_file:
        doc = fitz.Document(open_file)
        page = doc.load_page(0)
        page_content = page.get_textpage()
        content = page_content.extractText()
        my_text.insert(1.0, content)

def play_sound():
    text = my_text.get(1.0, END)
    tts = gTTS(text, lang='en')
    tts.save("audio.mp3")
    playsound("audio.mp3")


# creating menu

my_menu = Menu(root)
root.config(menu=my_menu)

# adding dropdowns

file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_pdf)
file_menu.add_command(label="clear", command=clear_text)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

play_btn = Button(text="Play", command=play_sound)
play_btn.pack(pady=20)

root.mainloop()