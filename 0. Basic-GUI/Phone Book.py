import tkinter

def phonebook():
    with open('phonebook.text', 'a')as f:
        f.write(f"Name: {name.get()} | Phone number: {phone.get()}\n")

root = tkinter.Tk()

frame = tkinter.Frame(root)
frame.pack(padx=20, pady=20)
tkinter.Label(frame, text="Phonebook", font='helvetica 20 bold').grid()

name = tkinter.StringVar()
phone = tkinter.StringVar()

l1 = tkinter.Label(frame, text="Name")
l2 = tkinter.Label(frame, text="Phone")
e1 = tkinter.Entry(frame, textvariable=name)
e2 = tkinter.Entry(frame, textvariable=phone)

l1.grid(row=1, column=0)
l2.grid(row=2, column=0)
e1.grid(row=1, column=1)
e2.grid(row=2, column=1)

tkinter.Button(frame, text="Submit", comman=phonebook).grid(row=3, column=1)

root.mainloop()