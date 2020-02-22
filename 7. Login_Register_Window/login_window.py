# ----------------------------------importing modules-------------------------------------------------------------------
import tkinter as tk
import tkinter.messagebox as msg
import pymysql

root = tk.Tk()

# Screen width and screen height
screen_width = 350
screen_height = 270
root.geometry(f"{screen_width}x{screen_height}+200+50")


# Username and Password from user
username = tk.StringVar()
password = tk.StringVar()

# Registration data
fullname_reg = tk.StringVar()
username_reg = tk.StringVar()
password_reg = tk.StringVar()

# ----------------------------------------------To remove all widgets---------------------------------------------------
def remove_widgets():
    list = root.pack_slaves()
    for l in list:
        l.destroy()


# --------------------------------------------Storing Resgistration data------------------------------------------------
def registerData():
    global username_reg, password_reg, fullname_reg
    global fullnameEntry2, usernameEntry2, passwordEntry2

    try:
        conn = pymysql.connect(user="root", password="12345", host="localhost", db="loginwindow")
        cursor = conn.cursor()
        cursor.execute('insert into loginwindow.regData (Fullname, username, password) values (%s, %s, %s)',
                       (fullname_reg.get(), username_reg.get(), password_reg.get()))
        cursor.execute('insert into loginwindow.Users (Username, Password) values (%s, %s)',
                       (username_reg.get(), password_reg.get()))
        conn.commit()
        conn.close()
        msg.showinfo("Registration", "Registration Successfull")
        fullnameEntry2.delete(0, "end")
        usernameEntry2.delete(0, "end")
        passwordEntry2.delete(0, "end")

    except Exception as e:
        print(e)
        msg.showinfo("UsernameError", "Username already registered")

    # Delete entry
    fullnameEntry2.delete(0, "end")
    usernameEntry2.delete(0, "end")
    passwordEntry2.delete(0, "end")


# --------------------------------------------------Login Checking------------------------------------------------------
def checkLogin():
    global username, password
    global usernameEntry, passwordEntry

    conn = pymysql.connect(user="root", password="12345", host="localhost", db="loginwindow")
    cursor = conn.cursor()
    cursor.execute('select * from loginwindow.Users where username = %s and password = %s', (username.get(), password.get()))
    result = cursor.fetchall()
    conn.close()
    if result:
        # delete entry
        usernameEntry.delete(0, "end")
        passwordEntry.delete(0, "end")
        remove_widgets()
        loginSuccess()
    else:
        msg.showinfo("Invalid", "Invalid credentials!")
        # Delete entry
        usernameEntry.delete(0, "end")
        passwordEntry.delete(0, "end")


# -------------------------------------------------Register window------------------------------------------------------
def registerWindow():
    global fullnameEntry2, usernameEntry2, passwordEntry2
    remove_widgets()
    tk.Label(root, text="Register", bg="grey", fg="white", font="Helvetica 25").pack(pady=(0, 20), fill="x")

    frame = tk.Frame(root)
    fullnameLabel2 = tk.Label(frame, text="Fullname ", font='helvetica 10')
    fullnameLabel2.pack(side="left", padx=20)
    fullnameEntry2 = tk.Entry(frame, font='helvetica 10', textvariable=fullname_reg)
    fullnameEntry2.pack(side="left")
    frame.pack()

    tk.Label(root).pack()

    frame1 = tk.Frame(root)
    usernameLabel2 = tk.Label(frame1, text="Username", font='helvetica 10')
    usernameLabel2.pack(side="left", padx=20)
    usernameEntry2 = tk.Entry(frame1, font='helvetica 10', textvariable=username_reg)
    usernameEntry2.pack(side="left")
    frame1.pack()

    tk.Label(root).pack()

    frame2 = tk.Frame(root)
    passwordLabel2 = tk.Label(frame2, text="Password", font='helvetica 10')
    passwordLabel2.pack(side="left", padx=20)
    passwordEntry2 = tk.Entry(frame2, font='helvetica 10', textvariable=password_reg, show="*")
    passwordEntry2.pack(side="left")
    frame2.pack()

    tk.Label(root).pack()

    registerButton = tk.Button(root, text="Register", font="helvetica 10", width=10, command=registerData)
    registerButton.pack()

    loginButton2 = tk.Button(root, text="Login Window", font="helvetica 10", command=loginWindow)
    loginButton2.pack()


# ------------------------------------------Main window or login window-------------------------------------------------
def loginWindow():
    remove_widgets()
    global frame4, frame5
    global usernameEntry, passwordEntry
    tk.Label(root, text="Login", font="Helvetica 25").pack(pady=20, fill="x")

    frame4 = tk.Frame(root)
    usernameLabel = tk.Label(frame4, text="Username", font='helvetica 10')
    usernameLabel.pack(side="left", padx=20)
    usernameEntry = tk.Entry(frame4, font='helvetica 10', textvariable=username)
    usernameEntry.pack(side="left")
    frame4.pack()

    tk.Label(root).pack()

    frame5 = tk.Frame(root)
    passwordLabel = tk.Label(frame5, text="Password", font='helvetica 10')
    passwordLabel.pack(side="left", padx=20)
    passwordEntry = tk.Entry(frame5, font='helvetica 10', textvariable=password, show="*")
    passwordEntry.pack(side="left")
    frame5.pack()

    tk.Label(root).pack()

    loginButton = tk.Button(root, text="Login", font="helvetica 10", width=10, command=checkLogin)
    loginButton.pack()
    registerButton2 = tk.Button(root, text="Register", font="helvetica 10", width=10, command=registerWindow)
    registerButton2.pack()


# ----------------------------------------------Login Successfull-------------------------------------------------------
def loginSuccess():
    loginLabel = tk.Label(root, text="Login Successfull", font="Helvetica 25")
    loginLabel.pack(pady=30)

    logoutButton = tk.Button(root, text="Logout", font="helvetica 10", width=10, command=logout)
    logoutButton.pack()


# -------------------------------------------Registration Successfull---------------------------------------------------
# def registrationSuccess():
#     remove_widgets()
#     loginWindow()


# ----------------------------------------------------Logout------------------------------------------------------------
def logout():
    remove_widgets()
    loginWindow()


loginWindow()

root.mainloop()
