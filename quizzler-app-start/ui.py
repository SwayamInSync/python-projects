THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface():
    def __init__(self, quiz_b: QuizBrain): # making sure that quiz_b should be QuizBrain class type
        self.quiz = quiz_b
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150,125,text="Some Question text",width=280 ,font=("Ariel", 20, "italic"), fill=THEME_COLOR) # setting a width will force text to wrap inside canvas
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50) # adding padding to canvas
        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)
        true_image = PhotoImage(file="images/true.png")
        self.right = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.right.grid(column=0,row=2)
        false_image = PhotoImage(file="images/false.png")
        self.wrong = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.wrong.grid(column=1,row=2)
        self.get_next_question()

        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="Quiz is Over")
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")
    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.feedback(is_right)

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000,self.get_next_question)

