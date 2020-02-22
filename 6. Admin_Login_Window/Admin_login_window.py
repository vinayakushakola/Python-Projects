# ----------------------------------importing modules-------------------------------------------------------------------
import tkinter as tk
import os

root = tk.Tk()

# Screen width and screen height
screen_width = 350
screen_height = 250
root.geometry(f"{screen_width}x{screen_height}+200+50")
root.title("Admin Login")

# Username and Password from user
username = tk.StringVar()
password = tk.StringVar()


# ----------------------------------------------To remove all widgets---------------------------------------------------
def remove_widgets():
    list = root.pack_slaves()
    for l in list:
        l.destroy()


# --------------------------------------------------Login Checking------------------------------------------------------
def checkLogin():
    # global usernameEntry
    # global passwordEntry

    # if login.txt is not exsist then this will create one
    if not (os.path.exists('login.txt')):
        with open('login.txt', 'w')as f:
            f.write("Admin\n")  # Writing username in text file
            f.write("Admin")  # Writing password in text file

    # To open login text file where username and password is stored
    with open('login.txt', 'r')as r1:
        username_password = r1.readlines()
        username_logintext = username_password[0].rstrip()
        password_logintext = username_password[1].rstrip()

        # Username Password checking
        if (username.get() == username_logintext) and (password.get() == password_logintext):
            # deleting entry
            usernameEntry.delete(0, "end")
            passwordEntry.delete(0, "end")
            remove_widgets()
            loginSuccess()

        # If username password is not matched
        else:
            Invalid = tk.Label(root, text="Invalid credentials entered!", font="helvetica 10", fg="red")
            Invalid.pack(pady=20)
            root.after(1500, Invalid.destroy)
            # Deleting entry
            usernameEntry.delete(0, "end")
            passwordEntry.delete(0, "end")



# ------------------------------------------Main window or login window-------------------------------------------------
def loginWindow():
    global usernameEntry
    global passwordEntry
    tk.Label(root, text="Admin Login", font="Helvetica 25").pack(pady=20, fill="x")

    frame = tk.Frame(root)
    usernameLabel = tk.Label(frame, text="Username", font='helvetica 10')
    usernameLabel.pack(side="left", padx=20)
    usernameEntry = tk.Entry(frame, font='helvetica 10', textvariable=username)
    usernameEntry.pack(side="left")
    frame.pack()

    tk.Label(root).pack()

    frame1 = tk.Frame(root)
    passwordLabel = tk.Label(frame1, text="Password", font='helvetica 10')
    passwordLabel.pack(side="left", padx=20)
    passwordEntry = tk.Entry(frame1, font='helvetica 10', textvariable=password, show="*")
    passwordEntry.pack(side="left")
    frame1.pack()

    tk.Label(root).pack()

    loginButton = tk.Button(root, text="Login", font="helvetica 10", width=10, command=checkLogin)
    loginButton.pack()


# ----------------------------------------------Login Successfull-------------------------------------------------------
def loginSuccess():
    loginLabel = tk.Label(root, text="Login Successfull", font="Helvetica 25")
    loginLabel.pack(pady=30)

    logoutButton = tk.Button(root, text="Logout", font="helvetica 10", width=10, command=logout)
    logoutButton.pack()


# ----------------------------------------------------Logout------------------------------------------------------------
def logout():
    remove_widgets()
    loginWindow()


loginWindow()

root.mainloop()
