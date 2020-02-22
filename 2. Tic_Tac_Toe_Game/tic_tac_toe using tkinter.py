from tkinter import *
import tkinter.messagebox as msg

root = Tk()
root.title("Tic Tac Toe")
# Fixed window size
root.resizable(width=False, height=False)

# For changing player turn
btn_click = True
# For counting the turns
turn = 0

# --------------------------------------------------Player turns--------------------------------------------------------
def btn(buttons):
    global btn_click
    global turn
    if buttons['text'] == " " and btn_click == True:
        buttons['text'] = "X"
        btn_click = False
        check_winner()
        turn += 1
    elif buttons['text'] == " " and btn_click == False:
        buttons['text'] = "O"
        btn_click = True
        check_winner()
        turn += 1


# -----------------------------------------------Checking for winners---------------------------------------------------
def check_winner():
    global button1, button2, button3, button4, button5, button6, button7, button8, button9

    if (button1['text'] == "X" and button2['text'] == "X" and button3['text'] == "X" or
        button4['text'] == "X" and button5['text'] == "X" and button6['text'] == "X" or
        button7['text'] == "X" and button8['text'] == "X" and button9['text'] == "X" or
        button1['text'] == "X" and button4['text'] == "X" and button7['text'] == "X" or
        button2['text'] == "X" and button5['text'] == "X" and button8['text'] == "X" or
        button3['text'] == "X" and button6['text'] == "X" and button9['text'] == "X" or
        button1['text'] == "X" and button5['text'] == "X" and button9['text'] == "X" or
        button3['text'] == "X" and button5['text'] == "X" and button7['text'] == "X"):
        disableButton()
        msg.showinfo("Tic-Tac-Toe", "X won")


    elif (button1['text'] == "O" and button2['text'] == "O" and button3['text'] == "O" or
        button4['text'] == "O" and button5['text'] == "O" and button6['text'] == "O" or
        button7['text'] == "O" and button8['text'] == "O" and button9['text'] == "O" or
        button1['text'] == "O" and button4['text'] == "O" and button7['text'] == "O" or
        button2['text'] == "O" and button5['text'] == "O" and button8['text'] == "O" or
        button3['text'] == "O" and button6['text'] == "O" and button9['text'] == "O" or
        button1['text'] == "O" and button5['text'] == "O" and button9['text'] == "O" or
        button3['text'] == "O" and button5['text'] == "O" and button7['text'] == "O"):
        disableButton()
        msg.showinfo("Tic-Tac-Toe", "O won")


    elif turn == 8:
        disableButton()
        msg.showinfo("Tic Tac Toe", "It's a Tie!")


# ------------------------------------------------Remove widgets--------------------------------------------------------
def remove_widgets():
    list = root.grid_slaves()
    list2 = root.pack_slaves()
    list3 = root.place_slaves()
    for l in list:
        l.destroy()
    for l in list2:
        l.destroy()
    for l in list3:
        l.destroy()


# ------------------------------------------------Disable buttons-------------------------------------------------------
def disableButton():
    global button1, button2, button3, button4, button5, button6, button7, button8, button9
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)


# ----------------------------------------------Actual Game window------------------------------------------------------
def gameWindow():
    remove_widgets()
    width = 597
    height = 624
    root.geometry(f"{width}x{height}+300+20")
    global button1, button2, button3, button4, button5, button6, button7, button8, button9

    frame2 = Frame(root, width=width, height=height)
    button1 = Button(frame2, font="helvetica 80", bg="#F0F0F0", fg="#696969", width=3, height=0, text=" ", command=lambda: btn(button1))
    button1.grid(row=0, column=0)
    button2 = Button(frame2, font="helvetica 80", bg="#F0F0F0", fg="#696969", width=3, height=0, text=" ", command=lambda: btn(button2))
    button2.grid(row=0, column=1)
    button3 = Button(frame2, font="helvetica 80", bg="#F0F0F0", fg="#696969", width=3, height=0, text=" ", command=lambda: btn(button3))
    button3.grid(row=0, column=2)

    button4 = Button(frame2, font="helvetica 80", bg="#F0F0F0", fg="#696969", width=3, height=0, text=" ", command=lambda: btn(button4))
    button4.grid(row=1, column=0)
    button5 = Button(frame2, font="helvetica 80", bg="#F0F0F0", fg="#696969", width=3, height=0, text=" ", command=lambda: btn(button5))
    button5.grid(row=1, column=1)
    button6 = Button(frame2, font="helvetica 80", bg="#F0F0F0", fg="#696969", width=3, height=0, text=" ", command=lambda: btn(button6))
    button6.grid(row=1, column=2)

    button7 = Button(frame2, font="helvetica 80", bg="#F0F0F0", fg="#696969", width=3, height=0, text=" ", command=lambda: btn(button7))
    button7.grid(row=2, column=0)
    button8 = Button(frame2, font="helvetica 80", bg="#F0F0F0", fg="#696969", width=3, height=0, text=" ", command=lambda: btn(button8))
    button8.grid(row=2, column=1)
    button9 = Button(frame2, font="helvetica 80", bg="#F0F0F0", fg="#696969", width=3, height=0, text=" ", command=lambda: btn(button9))
    button9.grid(row=2, column=2)
    frame2.place(relx=0, rely=0)


# --------------------------------------------------Game start windwo---------------------------------------------------
def startGame():
    root.geometry("300x250")

    label = Label(root, text="Tic Tac Toe", font="Lucida 30", fg="white", bg="#808080", pady=15)
    label.pack(pady=(0, 35), fill="x")
    start = Button(root, text="Start", font="helvetica 10", width=25, height=2, command=gameWindow)
    start.pack()
    exit = Button(root, text="Exit", font="helvetica 10", width=25, height=2, command=root.destroy)
    exit.pack()


# -----------------------------------------------Execution of start window----------------------------------------------
startGame()

root.mainloop()
