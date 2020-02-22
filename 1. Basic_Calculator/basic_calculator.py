author = "Vinayak Ushakola"

from tkinter import *


class Calculator(Tk):

    def __init__(self):
        super().__init__()
        self.geometry("308x439")
        self.title("Calculator")
        self.resizable(width=False, height=False)

        self.screenValue = StringVar()
        self.operator = ""

        self.frame = Frame(self, relief="raised", bd=5)

        self.screenE = Entry(self.frame, font="helvetica 40", width=10, relief="sunken", bd=4, textvariable=self.screenValue)
        self.screenE.grid(row=0, columnspan=4, pady=(0, 5))

        self.clearB = Button(self.frame, text="C", font="helvetica 13", width=7, height=3, relief=GROOVE, command=self.buttonDel)
        self.clearB.grid(row=1, column=0)
        self.clearB = Button(self.frame, text="x²", font="helvetica 13", width=7, height=3, relief=GROOVE, command=self.buttonSqr)
        self.clearB.grid(row=1, column=1)
        self.clearB = Button(self.frame, text="√", font="helvetica 13", width=7, height=3, relief=GROOVE, command=self.buttonSqrt)
        self.clearB.grid(row=1, column=2)
        self.clearB = Button(self.frame, text="⌫", font="helvetica 13", width=7, height=3, relief=GROOVE, command=self.buttonBack)
        self.clearB.grid(row=1, column=3)

        self.clearB = Button(self.frame, text="1", font="helvetica 13", width=7, height=3, relief=GROOVE, command=lambda: self.buttonClick("1"))
        self.clearB.grid(row=2, column=0)
        self.clearB = Button(self.frame, text="2", font="helvetica 13", width=7, height=3, relief=GROOVE, command=lambda: self.buttonClick("2"))
        self.clearB.grid(row=2, column=1)
        self.clearB = Button(self.frame, text="3", font="helvetica 13", width=7, height=3, relief=GROOVE, command=lambda: self.buttonClick("3"))
        self.clearB.grid(row=2, column=2)
        self.clearB = Button(self.frame, text="/", font="helvetica 13", width=7, height=3, relief=GROOVE, command=lambda: self.buttonClick("/"))
        self.clearB.grid(row=2, column=3)

        self.clearB = Button(self.frame, text="4", font="helvetica 13", width=7, height=3, relief=GROOVE, command=lambda: self.buttonClick("4"))
        self.clearB.grid(row=3, column=0)
        self.clearB = Button(self.frame, text="5", font="helvetica 13", width=7, height=3, relief=GROOVE, command=lambda: self.buttonClick("5"))
        self.clearB.grid(row=3, column=1)
        self.clearB = Button(self.frame, text="6", font="helvetica 13", width=7, height=3, relief=GROOVE, command=lambda: self.buttonClick("6"))
        self.clearB.grid(row=3, column=2)
        self.clearB = Button(self.frame, text="x", font="helvetica 13", width=7, height=3, relief=GROOVE, command=lambda: self.buttonClick("*"))
        self.clearB.grid(row=3, column=3)

        self.clearB = Button(self.frame, text="7", font="helvetica 13", width=7, height=3, relief=GROOVE, command=lambda: self.buttonClick("7"))
        self.clearB.grid(row=4, column=0)
        self.clearB = Button(self.frame, text="8", font="helvetica 13", width=7, height=3, relief=GROOVE, command=lambda: self.buttonClick("8"))
        self.clearB.grid(row=4, column=1)
        self.clearB = Button(self.frame, text="9", font="helvetica 13", width=7, height=3, relief=GROOVE, command=lambda: self.buttonClick("9"))
        self.clearB.grid(row=4, column=2)
        self.clearB = Button(self.frame, text="-", font="helvetica 13", width=7, height=3, relief=GROOVE, command=lambda: self.buttonClick("-"))
        self.clearB.grid(row=4, column=3)

        self.clearB = Button(self.frame, text=".", font="helvetica 13", width=7, height=3, relief=GROOVE, command=lambda: self.buttonClick("."))
        self.clearB.grid(row=5, column=0)
        self.clearB = Button(self.frame, text="0", font="helvetica 13", width=7, height=3, relief=GROOVE, command=lambda: self.buttonClick("0"))
        self.clearB.grid(row=5, column=1)
        self.clearB = Button(self.frame, text="=", font="helvetica 13", width=7, height=3, relief=GROOVE, command=self.buttonEqual)
        self.clearB.grid(row=5, column=2)
        self.clearB = Button(self.frame, text="+", font="helvetica 13", width=7, height=3, relief=GROOVE, command=lambda: self.buttonClick("+"))
        self.clearB.grid(row=5, column=3)

        self.frame.grid()

    def buttonClick(self, input):
        self.operator += input
        self.screenValue.set(self.operator)

    def buttonEqual(self):
        self.screenValue.set(eval(self.operator))

    def buttonDel(self):
        self.screenE.delete(0, END)
        self.operator = ""

    def buttonSqr(self):
        self.screenValue.set(int(self.operator)**2)

    def buttonSqrt(self):
        self.screenValue.set(int(self.operator)**0.5)

    def buttonBack(self):
        self.operator = self.operator[:-1]
        self.screenValue.set(self.operator)


if __name__ == '__main__':
    root = Calculator()
    root.mainloop()
