import tkinter
root = tkinter.Tk()
def phone():
    set1 = 1234
    if set1 == get.get():
        print("phne unlock")
        c = "Phone Unlocked"
        b.set(c)
    else:
        print("ph unlock fail")
        c = "Phone Unlock Fail!"
        b.set(c)

get = tkinter.IntVar()
b = tkinter.StringVar()
label = tkinter.Label(root, text="Enter password")
label.grid(row=0,column=0)
e = tkinter.Entry(root, textvariable=get)
e.grid(row=0,column=1)

b1 = tkinter.Button(root, text="Submit", command=phone)
b1.grid(row=1, column=1)

label2 = tkinter.Label(root, textvariable=b)
label2.grid(row=2,column=0)
root.mainloop()
