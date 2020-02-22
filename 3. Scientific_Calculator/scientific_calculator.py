import tkinter as tk
from math import *

root = tk.Tk()
root.geometry("280x382")
root.title("Scientific Calculator")
root.resizable(width=False, height=False)

screenText = tk.StringVar()
operator = ""

def buttonClick(input):
    global operator
    operator += input
    screenText.set(operator)
    if input == "C" or input == "CE":
        screenText.set("")
        operator = ""

def backButton():
    global operator
    operator = operator[:-1]
    screenText.set(operator)

def buttonMCc():
    pass
def buttonMRr():
    pass

def buttonMpp():
    pass
def buttonMmm():
    pass

def buttonMSs():
    pass
def buttonMMm():
    pass

def buttonSqrt():
    global operator
    screenText.set(sqrt(int(operator)))
def buttonSqr():
    global operator
    screenText.set(int(operator) ** 2)
    screenText.set("")

def buttonEqual():
    global operator
    screenText.set(eval(operator))

# ------------------------------------------------- Scientific ---------------------------------------------------------
def buttonUP():
    pass
def buttonXN():
    pass
def plusminus():
    pass
def buttonFact():
    pass
def buttonPi():
    pass



def Scientific():
    root.geometry("302x417")
    mainFrame = tk.Frame(root, relief="raised", bd=3)

    frame = tk.Frame(mainFrame)
    screen = tk.Entry(frame, font="helvetica 30", textvariable=screenText, width=13, relief="sunken", bd=5)
    screen.grid(row=0, column=0, columnspan=6)
    MC = tk.Button(frame, text="MC", width=5, pady=5, relief="groove", command=buttonMCc)
    MC.grid(row=1, column=0, pady=5, padx=(0, 5))
    MR = tk.Button(frame, text="MR", width=5, pady=5, relief="groove", command=buttonMRr)
    MR.grid(row=1, column=1, pady=5, padx=(0, 5))
    Mp = tk.Button(frame, text="M+", width=5, pady=5, relief="groove", command=buttonMpp)
    Mp.grid(row=1, column=2, pady=5, padx=(0, 5))
    Mm = tk.Button(frame, text="M-", width=5, pady=5, relief="groove", command=buttonMmm)
    Mm.grid(row=1, column=3, pady=5, padx=(0, 5))
    MS = tk.Button(frame, text="MS", width=5, pady=5, relief="groove", command=buttonMSs)
    MS.grid(row=1, column=4, pady=5, padx=(0, 5))
    MM = tk.Button(frame, text="MM", width=5, pady=5, relief="groove", command=buttonMMm)
    MM.grid(row=1, column=5, pady=5)
    frame.grid(row=1, column=0, columnspan=5)

    per = tk.Button(mainFrame, text="CE", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("CE"))
    per.grid(row=2, column=0, pady=(0, 5), padx=(0, 5))
    sroot = tk.Button(mainFrame, text="sin", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("sin("))
    sroot.grid(row=2, column=1, pady=(0, 5), padx=(0, 5))
    sqr = tk.Button(mainFrame, text="cos", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("cos("))
    sqr.grid(row=2, column=2, pady=(0, 5), padx=(0, 5))
    byx = tk.Button(mainFrame, text="tan", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("tan("))
    byx.grid(row=2, column=3, pady=(0, 5), padx=(0, 5))
    byx = tk.Button(mainFrame, text='⌫', font="helvetica", width=5, pady=5, relief="groove", command=backButton)
    byx.grid(row=2, column=4, pady=(0, 5))

    CE = tk.Button(mainFrame, text="C", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("%"))
    CE.grid(row=3, column=0, pady=(0, 5), padx=(0, 5))
    CE = tk.Button(mainFrame, text="log", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("%"))
    CE.grid(row=3, column=1, pady=(0, 5), padx=(0, 5))
    CE = tk.Button(mainFrame, text="Exp", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("%"))
    CE.grid(row=3, column=2, pady=(0, 5), padx=(0, 5))
    CE = tk.Button(mainFrame, text="Mod", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("%"))
    CE.grid(row=3, column=3, pady=(0, 5), padx=(0, 5))
    CE = tk.Button(mainFrame, text="√", font="helvetica", width=5, pady=5, relief="groove", command=buttonSqrt)
    CE.grid(row=3, column=4, pady=(0, 5))

    CE = tk.Button(mainFrame, text="↑", font="helvetica", width=5, pady=5, relief="groove", command=buttonUP)
    CE.grid(row=4, column=0, pady=(0, 5), padx=(0, 5))
    CE = tk.Button(mainFrame, text="x²", font="helvetica", width=5, pady=5, relief="groove", command=buttonSqr)
    CE.grid(row=4, column=1, pady=(0, 5), padx=(0, 5))
    CE = tk.Button(mainFrame, text="xⁿ", font="helvetica", width=5, pady=5, relief="groove", command=buttonXN)
    CE.grid(row=4, column=2, pady=(0, 5), padx=(0, 5))
    CE = tk.Button(mainFrame, text='10ⁿ', font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("10^"))
    CE.grid(row=4, column=3, pady=(0, 5), padx=(0, 5))
    CE = tk.Button(mainFrame, text='÷', font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("/"))
    CE.grid(row=4, column=4, pady=(0, 5))

    CE = tk.Button(mainFrame, text="π", font="helvetica", width=5, pady=5, relief="groove", command=buttonPi)
    CE.grid(row=5, column=0, pady=(0, 5), padx=(0, 5))
    CE = tk.Button(mainFrame, text="7", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("7"))
    CE.grid(row=5, column=1, pady=(0, 5), padx=(0, 5))
    CE = tk.Button(mainFrame, text="8", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("8"))
    CE.grid(row=5, column=2, pady=(0, 5), padx=(0, 5))
    CE = tk.Button(mainFrame, text="9", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("9"))
    CE.grid(row=5, column=3, pady=(0, 5), padx=(0, 5))
    CE = tk.Button(mainFrame, text="×", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("*"))
    CE.grid(row=5, column=4, pady=(0, 5))

    CE = tk.Button(mainFrame, text="n!", font="helvetica", width=5, pady=5, relief="groove", command=buttonFact)
    CE.grid(row=6, column=0, pady=(0, 5), padx=(0, 5))
    CE = tk.Button(mainFrame, text="4", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("4"))
    CE.grid(row=6, column=1, pady=(0, 5), padx=(0, 5))
    CE = tk.Button(mainFrame, text="5", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("5"))
    CE.grid(row=6, column=2, pady=(0, 5), padx=(0, 5))
    CE = tk.Button(mainFrame, text="6", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("6"))
    CE.grid(row=6, column=3, pady=(0, 5), padx=(0, 5))
    CE = tk.Button(mainFrame, text="-", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("-"))
    CE.grid(row=6, column=4, pady=(0, 5))

    CE = tk.Button(mainFrame, text="±", font="helvetica", width=5, pady=5, relief="groove", command=plusminus)
    CE.grid(row=7, column=0, pady=(0, 5), padx=(0, 5))
    CE = tk.Button(mainFrame, text="1", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("1"))
    CE.grid(row=7, column=1, pady=(0, 5), padx=(0, 5))
    CE = tk.Button(mainFrame, text="2", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("2"))
    CE.grid(row=7, column=2, pady=(0, 5), padx=(0, 5))
    CE = tk.Button(mainFrame, text="3", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("3"))
    CE.grid(row=7, column=3, pady=(0, 5), padx=(0, 5))
    CE = tk.Button(mainFrame, text="+", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("+"))
    CE.grid(row=7, column=4, pady=(0, 5))

    CE = tk.Button(mainFrame, text="(", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("{"))
    CE.grid(row=8, column=0, padx=(0, 5))
    CE = tk.Button(mainFrame, text=")", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("}"))
    CE.grid(row=8, column=1, padx=(0, 5))
    CE = tk.Button(mainFrame, text="0", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("0"))
    CE.grid(row=8, column=2, padx=(0, 5))
    CE = tk.Button(mainFrame, text=".", font="helvetica", width=5, pady=5, relief="groove", command=lambda: buttonClick("."))
    CE.grid(row=8, column=3, padx=(0, 5))
    CE = tk.Button(mainFrame, text="=", font="helvetica", width=5, pady=5, relief="groove", command=buttonEqual)
    CE.grid(row=8, column=4)

    mainFrame.grid()


Scientific()

root.mainloop()
