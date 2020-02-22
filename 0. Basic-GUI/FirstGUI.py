import tkinter
def fun():
    a = text1.get() + " " + text2.get()
    text3.set(a)
    print(a)
root = tkinter.Tk()
text1 = tkinter.StringVar()
text2 = tkinter.StringVar()
text3 = tkinter.StringVar()

# Creating my title
root.title("My first GUI")

#display
l = tkinter.Label(root,text= "Enter your name")
l.grid(row = 0, column = 0)
e = tkinter.Entry(root, width = 20,textvariable = text1)
e.grid(row = 0, column = 1)

l2 = tkinter.Label(root,text= "Enter your surname")
l2.grid(row = 1, column = 0)
e2 = tkinter.Entry(root,width = 20,textvariable = text2)
e2.grid(row = 1, column = 1)

b = tkinter.Button(root,text = "Submit",command = fun)
b.grid(row = 2,column =1)

l3 = tkinter.Label(root,text= "Displaying your name")
l3.grid(row = 4, column = 0)

l4 = tkinter.Label(root,width = 20,textvariable = text3)
l4.grid(row = 4, column = 1)
root.mainloop()