import tkinter as tk
from math import *
import tkinter.messagebox as msg

root = tk.Tk()
root.geometry("228x329")
root.title("Standard Calculator")
root.resizable(width=False, height=False)

screenText = tk.StringVar()
operator = screenText.get()

def buttonClick(input):
    global operator
    operator += input
    screenText.set(operator)
def clearall(input):
    global operator
    if input == "C" or input == "CE":
        screenText.set("")
        operator = ""

def backButton():
    global operator
    operator = operator[:-1]
    screenText.set(operator)

m = 0
def buttonMCc():
    global m
    m = 0

def buttonMRr():
    global m
    screenText.set(m)

def buttonMpp():
    global operator, m
    m += int(operator)
    screenText.set("")
    operator = ""

def buttonMmm():
    global operator, m
    m -= int(operator)
    screenText.set("")
    operator = ""


def buttonMMm():
    global m
    msg.showinfo("Memory", f"{m}")

def buttonSqrt():
    global operator
    screenText.set(sqrt(int(operator)))
def buttonSqr():
    global operator
    screenText.set(int(operator) ** 2)

def buttonEqual():
    global operator
    screenText.set(eval(operator))


def buttonMSs():
    pass


def plusMinus():
    pass

def aboutMe():
    msg.showinfo("Author", "Made by Vinayak Ushakola")


def Standard():
    global screen
    root.geometry("236x372")
    mainFrame = tk.Frame(root, relief="raised", bd=3)

    frame = tk.Frame(mainFrame)
    screen = tk.Entry(frame, font="helvetica 30", textvariable=screenText, width=10, relief="sunken", bd=5)
    screen.grid(row=0, column=0, columnspan=6)
    MC = tk.Button(frame, text="MC", width=4, pady=5, relief="groove", command=buttonMCc)
    MC.grid(row=1, column=0, pady=(5, 0))
    MR = tk.Button(frame, text="MR", width=4, pady=5, relief="groove", command=buttonMRr)
    MR.grid(row=1, column=1, pady=(5, 0))
    Mp = tk.Button(frame, text="M+", width=3, pady=5, relief="groove", command=buttonMpp)
    Mp.grid(row=1, column=2, pady=(5, 0))
    Mm = tk.Button(frame, text="M-", width=3, pady=5, relief="groove", command=buttonMmm)
    Mm.grid(row=1, column=3, pady=(5, 0))
    MS = tk.Button(frame, text="MS", width=4, pady=5, relief="groove", command=buttonMSs)
    MS.grid(row=1, column=4, pady=(5, 0))
    MM = tk.Button(frame, text="MM", width=4, pady=5, relief="groove", command=buttonMMm)
    MM.grid(row=1, column=5, pady=(5, 0))
    frame.grid(row=1, column=0, columnspan=4)

    per = tk.Button(mainFrame, text="%", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("%"))
    per.grid(row=2, column=0, pady=5)
    sroot = tk.Button(mainFrame, text="√", font="helvetica", width=5, pady=5, relief="groove", command=buttonSqrt)
    sroot.grid(row=2, column=1, pady=5)
    sqr = tk.Button(mainFrame, text="x²", font="helvetica", width=5, pady=5, relief="groove", command=buttonSqr)
    sqr.grid(row=2, column=2, pady=5)
    byx = tk.Button(mainFrame, text="¹/x", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("1/"))
    byx.grid(row=2, column=3, pady=5)

    CE = tk.Button(mainFrame, text="CE", font="helvetica", width=5, pady=5, relief="groove", command=lambda: clearall("CE"))
    CE.grid(row=3, column=0, pady=(0, 5))
    C = tk.Button(mainFrame, text="C", font="helvetica", width=5, pady=5, relief="groove", command=lambda: clearall("C"))
    C.grid(row=3, column=1, pady=(0, 5))
    back = tk.Button(mainFrame, text='⌫', font="helvetica", width=5, pady=5, relief="groove", command=backButton)
    back.grid(row=3, column=2, pady=(0, 5))
    div = tk.Button(mainFrame, text="÷", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("/"))
    div.grid(row=3, column=3, pady=(0, 5))

    seven = tk.Button(mainFrame, text="7", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("7"))
    seven.grid(row=4, column=0, pady=(0, 5))
    eight = tk.Button(mainFrame, text="8", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("8"))
    eight.grid(row=4, column=1, pady=(0, 5))
    nine = tk.Button(mainFrame, text="9", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("9"))
    nine.grid(row=4, column=2, pady=(0, 5))
    mul = tk.Button(mainFrame, text="×", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("*"))
    mul.grid(row=4, column=3, pady=(0, 5))

    four = tk.Button(mainFrame, text="4", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("4"))
    four.grid(row=5, column=0, pady=(0, 5))
    five = tk.Button(mainFrame, text="5", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("5"))
    five.grid(row=5, column=1, pady=(0, 5))
    six = tk.Button(mainFrame, text="6", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("6"))
    six.grid(row=5, column=2, pady=(0, 5))
    sub = tk.Button(mainFrame, text="-", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("-"))
    sub.grid(row=5, column=3, pady=(0, 5))

    one = tk.Button(mainFrame, text="1", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("1"))
    one.grid(row=6, column=0, pady=(0, 5))
    two = tk.Button(mainFrame, text="2", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("2"))
    two.grid(row=6, column=1, pady=(0, 5))
    three = tk.Button(mainFrame, text="3", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("3"))
    three.grid(row=6, column=2, pady=(0, 5))
    add = tk.Button(mainFrame, text="+", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("+"))
    add.grid(row=6, column=3, pady=(0, 5))

    sym = tk.Button(mainFrame, text="±", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("+-"))
    sym.grid(row=7, column=0)
    zero = tk.Button(mainFrame, text="0", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("0"))
    zero.grid(row=7, column=1)
    dot = tk.Button(mainFrame, text=".", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("."))
    dot.grid(row=7, column=2)
    equal = tk.Button(mainFrame, text="=", font="helvetica", width=5, pady=5, relief="groove", command=buttonEqual)
    equal.grid(row=7, column=3)

    mainFrame.grid()

def removeWidgets():
    list = root.grid_slaves()
    for l in list:
        l.destroy()


Standard()


root.mainloop()
