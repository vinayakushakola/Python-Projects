# ----------------------------------------------- importing modules ----------------------------------------------------
import tkinter as tk
import tkinter.messagebox as msg
import random as r
import pymysql
import datetime as d
import pandas as pd
import numpy as np


root = tk.Tk()
root.title("Activity Tracker")
root.resizable(width=False, height=False)


# Login Data
username = tk.StringVar()
password = tk.StringVar()

# Registration Data
fullnameRegister = tk.StringVar()
activityRegister = tk.StringVar()
usernameRegister = tk.StringVar()
passwordRegister = tk.StringVar()


# ------------------------------------------- Storing Resgistration data -----------------------------------------------
def registerData():
    global fullnameRegister, activityRegister, usernameRegister, passwordRegister
    global fullnameEntryR, activityEntryR, usernameEntryR, passwordEntryR
    try:
        conn = pymysql.connect(user='root', password='12345', host='localhost', db='Activity')
        cursor = conn.cursor()
        cursor.execute('insert into Activity.RegData (FullName, Activity, Username, Password) values (%s, %s, %s, %s)',
                       (fullnameRegister.get(), activityRegister.get(), usernameRegister.get(), passwordRegister.get()))
        cursor.execute("insert into Activity.users (Username, Password) Values (%s, %s)",
                       (usernameRegister.get(), passwordRegister.get()))
        registrationSuccess()
        conn.commit()
        conn.close()
        fullnameEntryR.delete(0, "end")
        activityEntryR.delete(0, "end")
        usernameEntryR.delete(0, "end")
        passwordEntryR.delete(0, "end")

    except Exception as e:
        print(e)
        usernameAlreadyRegistered()
        fullnameEntryR.delete(0, "end")
        activityEntryR.delete(0, "end")
        usernameEntryR.delete(0, "end")
        passwordEntryR.delete(0, "end")


# ------------------------------------------- Username already registered ----------------------------------------------
def usernameAlreadyRegistered():
    usernameAlreadyReg = tk.Label(root, font="helvetica 10", fg="red", text="Username already registered!")
    usernameAlreadyReg.place(relx=0.3, rely=0.9)
    root.after(1500, usernameAlreadyReg.destroy)


# ------------------------------------------------- Login Checking -----------------------------------------------------
def checkLogin():
    global result2
    global username, password
    global usernameEntry, passwordEntry

    conn = pymysql.connect(host="localhost", user="root", password="12345", db="Activity")
    cursor = conn.cursor()
    cursor.execute('select * from Activity.Regdata where Username = %s and password = %s', (username.get(), password.get()))
    result2 = cursor.fetchall()

    cursor.execute('select * from Activity.users where Username = %s And Password = %s', (username.get(), password.get()))
    result = cursor.fetchall()
    conn.close()

    if result:
        usernameEntry.delete(0, "end")
        passwordEntry.delete(0, "end")
        loginSuccess()
    else:
        usernameEntry.delete(0, "end")
        passwordEntry.delete(0, "end")
        msg.showerror("Invalid user", "Invalid username or password!")


# --------------------------------------------- To remove all widgets --------------------------------------------------
def remove_widgets():
    list = root.pack_slaves()
    list2 = root.grid_slaves()
    list3 = root.place_slaves()
    for l in list:
        l.destroy()
    for l in list2:
        l.destroy()
    for l in list3:
        l.destroy()


# ------------------------------------------------ Register window -----------------------------------------------------
def registerWindow():
    remove_widgets()
    root.geometry(f"{400}x{300}+500+100")
    global fullnameEntryR, activityEntryR, usernameEntryR, passwordEntryR
    global fullnameRegister, activityRegister, usernameRegister, passwordRegister

    label = tk.Label(root, font="helvetica 25", bg="grey", pady=15, fg="white", text="Activity Tracker")
    label.pack(fill="x")

    fullnamelLabelR = tk.Label(root, text="Fullname", font="helvetica 12")
    activitylLabelR = tk.Label(root, text="Activity", font="helvetica 12")
    usernameLabelR = tk.Label(root, text="Username", font="helvetica 12")
    passwordLabelR= tk.Label(root, text="Passowrd", font="helvetica 12")

    fullnamelLabelR.place(relx=0.15, rely=0.3)
    activitylLabelR.place(relx=0.15, rely=0.4)
    usernameLabelR.place(relx=0.15, rely=0.5)
    passwordLabelR.place(relx=0.15, rely=0.6)

    fullnameEntryR = tk.Entry(root, font="helvetica 12", textvariable=fullnameRegister)
    activityEntryR = tk.Entry(root, font="helvetica 12", textvariable=activityRegister)
    usernameEntryR = tk.Entry(root, font="helvetica 12", textvariable=usernameRegister)
    passwordEntryR = tk.Entry(root, font="helvetica 12", show="*", textvariable=passwordRegister)
    fullnameEntryR.place(relx=0.4, rely=0.3)
    activityEntryR.place(relx=0.4, rely=0.4)
    usernameEntryR.place(relx=0.4, rely=0.5)
    passwordEntryR.place(relx=0.4, rely=0.6)

    registrationButton = tk.Button(root, text="Register", width=10, command=registerData, font="helvetica 12")
    registrationButton.place(relx=0.52, rely=0.7)

    backButton = tk.Button(root, text="Back", font="helvetica 12", width=10, command=loginWindow)
    backButton.place(relx=0.52, rely=0.82)


# ----------------------------------------- Main window or login window ------------------------------------------------
def loginWindow():
    remove_widgets()
    global usernameEntry, passwordEntry

    root.geometry("400x300+500+100")

    label = tk.Label(root, font="helvetica 25", bg="grey", pady=15, fg="white", text="Activity Tracker")
    label.pack(fill="x")

    usernameLabel = tk.Label(root, text="Username", font="helvetica 12")
    passwordLabel = tk.Label(root, text="Password", font="helvetica 12")

    usernameEntry = tk.Entry(root, font="helvetica 12", textvariable=username)
    passwordEntry = tk.Entry(root, font="helvetica 12", show="*", textvariable=password)

    loginButton = tk.Button(root, text="Login", width=15, font="helvetica 12", command=checkLogin)
    registerButton = tk.Button(root, text="Register", width=10, font="helvetica 12", command=registerWindow)


    usernameLabel.place(relx=0.1, rely=0.3)
    passwordLabel.place(relx=0.1, rely=0.45)
    usernameEntry.place(relx=0.35, rely=0.3)
    passwordEntry.place(relx=0.35, rely=0.45)
    loginButton.place(relx=0.4, rely=0.6)
    registerButton.place(relx=0.1, rely=0.6)


# --------------------------------------------- Login Successfull ------------------------------------------------------
def loginSuccess():
    remove_widgets()
    root.geometry("600x600+400+50")

    label2 = tk.Label(root, text="Welcome To Activity Tracker", font="helvetica 25", pady=15, bg="grey", fg="white")
    label2.pack(fill="x", padx=10, pady=(10, 30))
    label3 = tk.Button(root, text="Logout", font="helvetica 12", width=15, height=2, command=logout)
    label3.pack()


# ------------------------------------------ Registration Successfull --------------------------------------------------
def registrationSuccess():
    regSuccessfull = tk.Label(root, font="helvetica 10", fg="green", text="Registration Sucessfull")
    regSuccessfull.place(relx=0.3, rely=0.9)
    root.after(1500, regSuccessfull.destroy)


# --------------------------------------------------- Logout -----------------------------------------------------------
def logout():
    root.destroy()


# ------------------------------------------------- Popup Window -------------------------------------------------------
def popu():
    now = d.datetime.now()
    presentTime = now.strftime("%H:%M:%S")
    now_plus_10 = now + d.timedelta(minutes=10)
    futureTime = now_plus_10.strftime("%H:%M:%S")


    root2 = tk.Toplevel(root)
    root2.resizable(width=False, height=False)
    screenwidth = 300
    screenheight = 215
    root2.geometry(f"{screenwidth}x{screenheight}+500+100")
    def nextCaptcha():
        global captchaScreen
        canvas.delete("all")
        captchaScreen = []
        for i in range(5):
            captchaScreen.append(chr(r.randint(65, 90)))

        color = ["black", "red", "yellow", "blue", "brown", "grey", "pink", "cyan"]
        font = ['lucida', 'verdana', 'helvetica', 'papyrus', 'Arial', 'Calibri']

        t1 = canvas.create_text(40 + r.randint(0, 10), 40 + r.randint(0, 10), text=captchaScreen[0],
                           font=font[r.randint(0, 5)] + " 28 bold", fill=color[r.randint(0, 7)])
        t2 = canvas.create_text(80 + r.randint(0, 10), 40 + r.randint(0, 10), text=captchaScreen[1],
                           font=font[r.randint(0, 5)] + " 28 bold", fill=color[r.randint(0, 7)])
        t3 = canvas.create_text(120 + r.randint(0, 10), 40 + r.randint(0, 10), text=captchaScreen[2],
                           font=font[r.randint(0, 5)] + " 28 bold", fill=color[r.randint(0, 7)])
        t4 = canvas.create_text(160 + r.randint(0, 10), 40 + r.randint(0, 10), text=captchaScreen[3],
                           font=font[r.randint(0, 5)] + " 28 bold", fill=color[r.randint(0, 7)])
        t5 = canvas.create_text(200 + r.randint(0, 10), 40 + r.randint(0, 10), text=captchaScreen[4],
                           font=font[r.randint(0, 5)] + " 28 bold", fill=color[r.randint(0, 7)])

        for i in range(0, 5):
            lines = canvas.create_line(r.randint(5, 295), r.randint(5, 195), r.randint(5, 295), r.randint(5, 195),
                                  fill=color[r.randint(0, 6)], width=r.randint(1, 3))

    def verifyCaptcha():
        global captchaScreen
        captchaScreen2 = ""
        for i in captchaScreen:
            captchaScreen2 += i

        if screen_text.get() in captchaScreen2:
            activityEntry()
            root2.destroy()
        else:
            canvas.delete("all")
            screen_text.set("")
            nextCaptcha()

    def activityEntry():
        global result2
        for data in result2:
            data
        name = data[0]
        now = d.datetime.now()
        time = now.strftime("%H:%M:%S")
        date = now.strftime("%d/%m/%y")
        conn = pymysql.connect(user='root', password="12345", host="localhost", db="Activity")
        cursor = conn.cursor()
        cursor.execute("insert into Activity.data (Name, Date, Time) values (%s,%s,%s)", (name, date, time))
        cursor.execute("select * from activity.data")
        userActivityData = cursor.fetchall()
        conn.commit()
        conn.close()
        df = pd.DataFrame(userActivityData, columns=['Name', 'Date', 'Time'])
        df.to_csv('userActivityData.csv')


    screen_text = tk.StringVar()
    root2.configure(background="#00FFFF")
    canvas = tk.Canvas(root2, width=screenwidth, height=100, bg="white")
    captchaEntry = tk.Entry(root2, font="helvetica 20", width=30, textvariable=screen_text)
    canvas.pack(pady=10, padx=10)
    captchaEntry.pack(padx=10)

    frame = tk.Frame(root2, width=screenwidth, bg="#00FFFF")
    frame.pack(padx=10, pady=10)
    nextButton = tk.Button(frame, text="Next", width=10, font="Helvetica 13", command=nextCaptcha)
    verifyButton = tk.Button(frame, text="verify", width=10, font="helvetica 13", command=verifyCaptcha)

    verifyButton.pack(side="left", padx=(0, 39))
    nextButton.pack(side="left", padx=(39, 0))

    nextCaptcha()


loginWindow()


root.mainloop()
