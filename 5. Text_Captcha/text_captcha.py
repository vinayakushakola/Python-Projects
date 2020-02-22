import tkinter as tk
import tkinter.messagebox as msg
import random as r

root = tk.Tk()

# Window size
screenwidth = 300
screenheight = 215
root.geometry(f"{screenwidth}x{screenheight}+500+100")
root.title("Captcha ")

# Window background color
root.configure(background="#00FFFF")

screen_text = tk.StringVar()


# ---------------------------------------------------For next captcha---------------------------------------------------
def nextCaptcha():
    global screenCaptcha
    global canvas
    # To delete alphabets on canvas screen
    canvas.delete("all")

    # Storing Alphabets
    screenCaptcha = []
    for i in range(5):
        # 65 - 90 is Ascii numbers for capital alphabets
        screenCaptcha.append(chr(r.randint(65, 90)))

    # Colors for alphabet
    color = ["black", "red", "yellow", "blue", "brown", "grey", "pink", "cyan"]
    # Font for alphabet
    font = ['lucida', 'verdana', 'helvetica', 'papyrus', 'Arial', 'Calibri']

    # To show alphabet on canvas screen
    t1 = canvas.create_text(40 + r.randint(0, 10), 40 + r.randint(0, 10), text=screenCaptcha[0],
                            font=font[r.randint(0, 5)] + " 28 bold", fill=color[r.randint(0, 7)])
    t2 = canvas.create_text(80 + r.randint(0, 10), 40 + r.randint(0, 10), text=screenCaptcha[1],
                            font=font[r.randint(0, 5)] + " 28 bold", fill=color[r.randint(0, 7)])
    t3 = canvas.create_text(120 + r.randint(0, 10), 40 + r.randint(0, 10), text=screenCaptcha[2],
                            font=font[r.randint(0, 5)] + " 28 bold", fill=color[r.randint(0, 7)])
    t4 = canvas.create_text(160 + r.randint(0, 10), 40 + r.randint(0, 10), text=screenCaptcha[3],
                            font=font[r.randint(0, 5)] + " 28 bold", fill=color[r.randint(0, 7)])
    t5 = canvas.create_text(200 + r.randint(0, 10), 40 + r.randint(0, 10), text=screenCaptcha[4],
                            font=font[r.randint(0, 5)] + " 28 bold", fill=color[r.randint(0, 7)])

    # Printing canvas lines on screen
    for i in range(0, 5):
        lines = canvas.create_line(r.randint(5, 295), r.randint(5, 195), r.randint(5, 295), r.randint(5, 195),
                                   fill=color[r.randint(0, 6)], width=r.randint(1, 3))


# ----------------------------------------------Verification of Captcha-------------------------------------------------
def verifyCaptcha():
    global screenCaptcha
    storeScreenCaptcha = ""
    for i in screenCaptcha:
        storeScreenCaptcha += i

    if screen_text.get() == storeScreenCaptcha:
        msg.showinfo("Verification", "Verification successfull")
        # Verification successfull destroy window
        root.destroy()
    else:
        msg.showinfo("Verification", "Verification unsuccessfull!")
        # Delete captcha if not matched
        canvas.delete("all")
        screen_text.set("")
        # Verification not successfull show next captcha
        nextCaptcha()


# ----------------------------------------Captcha window or Main window-------------------------------------------------
def mainWindow():
    global canvas
    canvas = tk.Canvas(root, width=screenwidth, height=100, bg="white")
    canvas.pack(fill="x", padx=10, pady=10)

    textEntry = tk.Entry(root, font="helvetica 20", width=30, textvariable=screen_text)
    textEntry.pack(padx=10)

    frame = tk.Frame(root, width=screenwidth, height=screenheight, bg="#00FFFF")
    verifyButton = tk.Button(frame, text="Verify", width=10, font="helvetica 13", command=verifyCaptcha)
    verifyButton.pack(side="left", padx=(0, 39))

    nextButton = tk.Button(frame, text="Next", width=10, font="Helvetica 13", command=nextCaptcha)
    nextButton.pack(side="left", padx=(39, 0))
    frame.pack(padx=10, pady=10)

    nextCaptcha()


mainWindow()

root.mainloop()
