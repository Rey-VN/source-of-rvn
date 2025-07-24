import tkinter as tk
from tkinter import Toplevel
from PIL import Image, ImageTk
import random

def root_quit():
    print("quit button clicked")
    root.destroy()

def start_c():
    print("Start Button Clicked")

    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    app = tk.Toplevel(root)
    app.title("Math Quiz")
    app.geometry("300x300")
    app.resizable(False, False)

    # State variables
    current_q = tk.StringVar()
    feedback_text = tk.StringVar()

    # generate the first number
    def generate_question():
        num1 = random.choice(num)
        num2 = random.choice(num)
        current_q.set(f"{num1} + {num2}")
        app.num1 = num1
        app.num2 = num2
        feedback_text.set("") 

    def resultPLUS():
        return app.num1 + app.num2

    def create_error_window(message):
        error_window = Toplevel(app)
        error_window.title("Warning")
        error_window.geometry("250x100")
        error_label = tk.Label(error_window, text=message, fg="red", font=("Comic Sans MS", 14))
        error_label.pack(pady=20)

    def input_validator(user_input):
        if user_input.strip() == "":
            create_error_window("No Blanks!")
            return False
        elif not user_input.isdigit():
            if any(c.isalpha() for c in user_input):
                create_error_window("No Letters!")
            elif " " in user_input:
                create_error_window("No Whitespace!")
            else:
                create_error_window("No Symbols!")
            return False
        elif len(user_input) > 6:
            create_error_window("Max 6 characters!")
            return False
        return True

    def submit_answer():
        user_input = entry.get()
        if not input_validator(user_input):
            return

        if int(user_input) == resultPLUS():
            feedback_text.set("Correct!")
        else:
            feedback_text.set("Wrong!")

    # working out window
    tk.Label(app, textvariable=current_q, font=("Courier", 18)).pack(pady=10)
    entry = tk.Entry(app, font=("Courier", 14))
    entry.pack(pady=10)
    tk.Button(app, text="Submit", command=submit_answer).pack(pady=5)
    tk.Label(app, textvariable=feedback_text, font=("Courier", 14)).pack(pady=10)
    tk.Button(app, text="Try Again", command=generate_question).pack(pady=5)

    generate_question()

def contin():
    print("Continue button clicked")

# main window
root = tk.Tk()
root.title("Mathirix")
root.geometry("1280x720")
root.resizable(False, False)
bg_image = Image.open(r"C:\Users\24705\OneDrive - Lynfield College\3PAD\Assessment 91906 and 91907\Checkpoit 1\IMAGES\Mathrix_main.png")
bg_image = bg_image.resize((1280, 720), Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(bg_image)

label = tk.Label(root, image=photo)
label.place(x=0, y=0, relwidth=1, relheight=1)

# Buttons
button_img = tk.PhotoImage(file=r"C:\Users\24705\OneDrive - Lynfield College\3PAD\Assessment 91906 and 91907\Checkpoit 1\IMAGES\StartMbttn.png")
strt_button = tk.Button(root, image=button_img, borderwidth=0, command=start_c)
strt_button.place(relx=0.5, rely=0.7, anchor="center")

buttn_img = tk.PhotoImage(file=r"C:\Users\24705\OneDrive - Lynfield College\3PAD\Assessment 91906 and 91907\Checkpoit 1\IMAGES\continueMbttn.png")
conti_button = tk.Button(root, image=buttn_img, borderwidth=0, command=contin)
conti_button.place(relx=0.5, rely=0.9, anchor="center")

butn_img = tk.PhotoImage(file=r"C:\Users\24705\OneDrive - Lynfield College\3PAD\Assessment 91906 and 91907\Checkpoit 1\IMAGES\quitmbttn.png")
quit_button = tk.Button(root, image=butn_img, borderwidth=0, command=root_quit)
quit_button.place(relx=0.00, rely=1.0, anchor="sw")

root.mainloop()
