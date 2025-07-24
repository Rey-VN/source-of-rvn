import tkinter as tk
from tkinter import Toplevel
from PIL import Image, ImageTk
from tkinter import messagebox

#---------------------Function of common functions--------------#

#Creating Function to open button
def pillow_image_opener(path, size):
    img = Image.open(path)
    img = img.resize(size, Image.Resampling.LANCZOS)
    return img

#Creating Function to create background image
def create_background(window, pil_image):
    photo_image = ImageTk.PhotoImage(pil_image)
    label = tk.Label(window, image=photo_image)
    label.image = photo_image
    label.place(x=0, y=0, relwidth=1, relheight=1)

#Function to create buttons
def button_creator(window, image_path, size, command, relx, rely, anchor):
    pil_img = pillow_image_opener(image_path, size)
    photo_img = ImageTk.PhotoImage(pil_img)
    btn = tk.Button(window, image=photo_img, borderwidth=0, highlightthickness=0, command=command)
    btn.image = photo_img
    btn.place(relx=relx, rely=rely, anchor=anchor)
    return btn
#-----------------------------------------------------------#


#------------------------creating functions for buttons in gui--------#

#Function for quit button
def root_quit():
    print("Quit button clicked")
    root.destroy()

"""def contin():
    print("Continue button clicked")
    contin_w = Toplevel()
    contin_w.title("Mathrix")
    contin_w.geometry("1280x720")
    contin_w.resizable(False, False)

    bg_image_w = pillow_image_opener("z_Main_Math.png", (1280, 720))
    create_background(contin_w, bg_image_w)"""

#Function of start button
def levels_s():
    print("Login button clicked, Levels window")
    levels_w = Toplevel()
    levels_w.title("Mathrix_levels")
    levels_w.geometry("1280x720")
    levels_w.resizable(False, False)

    bg_lvl_image = pillow_image_opener("z_level_choosing_w.png", (1280, 720))
    create_background(levels_w, bg_lvl_image)

        # Easy button
    button_creator(levels_w, "z_Easy_lvl.png", (250, 80), lvl_w_easy, 0.47, 0.7, "center")
        # Medium button
    button_creator(levels_w, "z_medium_lvl.png", (250, 80), lvl_w_medium, 0.22, 0.6, "center")
        # Hard button
    button_creator(levels_w, "z_hard_lvl.png", (250, 80), lvl_w_hard, 0.73, 0.6, "center")


#-----------------------------Level Buttons---------------------------#
#Easy level
def lvl_w_easy():
    w_easy1 = Toplevel()
    w_easy1.title("Mathrix_easy")
    w_easy1.geometry("1280x720")
    w_easy1.resizable(False, False)

    bg_image_e_w = pillow_image_opener("z_working_bg.png", (1280, 720))
    create_background(w_easy1, bg_image_e_w)

    easy_questions = [
        {"question": "What is 2 + 2?", "answer": "4"},
        {"question": "What is 5 - 3?", "answer": "2"},
        {"question": "What is 3 x 2?", "answer": "6"},
        {"question": "What is 10 ÷ 2?", "answer": "5"},
        {"question": "What is 7 + 1?", "answer": "8"}
    ]

    current_q = [0]

    question_label = tk.Label(w_easy1, text=easy_questions[current_q[0]]["question"], font=("Just Another Hand", 40), fg="black", bg="white")
    question_label.place(relx=0.5, rely=0.2, anchor="center")

    answer_entry = tk.Entry(w_easy1, font=("Arial", 24), justify="center")
    answer_entry.place(relx=0.5, rely=0.4, anchor="center")

    feedback_text = tk.StringVar()
    feedback_label = tk.Label(w_easy1, textvariable=feedback_text, font=("Arial", 20), fg="blue", bg="white")
    feedback_label.place(relx=0.5, rely=0.5, anchor="center")

    # Function to create message box
    def create_error_window(message):
        error_window = Toplevel(w_easy1)
        error_window.title("Warning")
        error_window.geometry("250x100")
        error_label = tk.Label(error_window, text=message, fg="red", font=("Comic Sans MS", 14))
        error_label.pack(pady=20)
        
    #Function to check inputs
    def input_validator(user_input):
        if user_input.strip() == "":
            create_error_window("No Blanks!")
            return False
        elif not user_input.isdigit():
            if any(c.isalpha() for c in user_input):
                create_error_window("No Letters!")

            else:
                create_error_window("No Symbols!")
            return False
        elif len(user_input) > 6:
            create_error_window("Max 6 characters!")
            return False
        return True
    
    #Function to check answer
    def submit_answer():
        user_input = answer_entry.get()
        if not input_validator(user_input):
            return

        correct_answer = easy_questions[current_q[0]]["answer"]

        if user_input == correct_answer:
            feedback_text.set("Correct!")
        else:
            feedback_text.set(f"Wrong! Correct answer was {correct_answer}")

        current_q[0] += 1
        if current_q[0] < len(easy_questions):
            question_label.config(text=easy_questions[current_q[0]]["question"])
            answer_entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Quiz Over", "You have completed all questions.")
            w_easy1.destroy()

    button_creator(w_easy1, "z_submit_btn.png", (250, 80), submit_answer, 0.5, 0.8, "center")

# MEdium Level
def lvl_w_medium():
    w_med1 = Toplevel()
    w_med1.title("Mathrix_medium")
    w_med1.geometry("1280x720")
    w_med1.resizable(False, False)

    bg_image_m_w = pillow_image_opener("z_working_bg.png", (1280, 720))
    create_background(w_med1, bg_image_m_w)

    medium_questions = [
        {"question": "What is 15 + 28?", "answer": "43"},
        {"question": "Calculate 45 - 19", "answer": "26"},
        {"question": "What is 8 x 7?", "answer": "56"},
        {"question": "Divide 144 by 12", "answer": "12"},
        {"question": "What is 25% of 200?", "answer": "50"}
    ]

    current_q = [0]

    question_label = tk.Label(w_med1, text=medium_questions[current_q[0]]["question"], font=("Just Another Hand", 40), fg="black", bg="white")
    question_label.place(relx=0.5, rely=0.2, anchor="center")

    answer_entry = tk.Entry(w_med1, font=("Arial", 24), justify="center")
    answer_entry.place(relx=0.5, rely=0.4, anchor="center")

    feedback_text = tk.StringVar()
    feedback_label = tk.Label(w_med1, textvariable=feedback_text, font=("Arial", 20), fg="blue", bg="white")
    feedback_label.place(relx=0.5, rely=0.5, anchor="center")

    #Message box
    def create_error_window(message):
        error_window = Toplevel(w_med1)
        error_window.title("Warning")
        error_window.geometry("250x100")
        error_label = tk.Label(error_window, text=message, fg="red", font=("Comic Sans MS", 14))
        error_label.pack(pady=20)
        
    #Validator
    def input_validator(user_input):
        if user_input.strip() == "":
            create_error_window("No Blanks!")
            return False
        elif not user_input.isdigit():
            if any(c.isalpha() for c in user_input):
                create_error_window("No Letters!")
            else:
                create_error_window("No Symbols!")
            return False
        elif len(user_input) > 6:
            create_error_window("Max 6 characters!")
            return False
        return True
    
    #Answer Checker
    def submit_answer():
        user_input = answer_entry.get()
        if not input_validator(user_input):
            return

        correct_answer = medium_questions[current_q[0]]["answer"]

        if user_input == correct_answer:
            feedback_text.set("Correct!")
        else:
            feedback_text.set(f"Wrong! Correct answer was {correct_answer}")

        current_q[0] += 1
        if current_q[0] < len(medium_questions):
            question_label.config(text=medium_questions[current_q[0]]["question"])
            answer_entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Quiz Over", "You have completed all questions.")
            w_med1.destroy()

    button_creator(w_med1, "z_submit_btn.png", (250, 80), submit_answer, 0.5, 0.8, "center")

# Hard Level
def lvl_w_hard():
    w_hard1 = Toplevel()
    w_hard1.title("Mathrix_hard")
    w_hard1.geometry("1280x720")
    w_hard1.resizable(False, False)

    bg_image_h_w = pillow_image_opener("z_working_bg.png", (1280, 720))
    create_background(w_hard1, bg_image_h_w)

    hard_questions = [
        {"question": "What is 35 x 14?", "answer": "490"},
        {"question": "Calculate 125 ÷ 5", "answer": "25"},
        {"question": "What is the result of 15 + (-8)?", "answer": "7"},
        {"question": "If you subtract 17 from 83, what do you get?", "answer": "66"},
        {"question": "Calculate 12.5% of 240", "answer": "30"}
    ]

    current_q = [0]

    question_label = tk.Label(w_hard1, text=hard_questions[current_q[0]]["question"], font=("Just Another Hand", 40), fg="black", bg="white")
    question_label.place(relx=0.5, rely=0.2, anchor="center")

    answer_entry = tk.Entry(w_hard1, font=("Arial", 24), justify="center")
    answer_entry.place(relx=0.5, rely=0.4, anchor="center")

    feedback_text = tk.StringVar()
    feedback_label = tk.Label(w_hard1, textvariable=feedback_text, font=("Arial", 20), fg="blue", bg="white")
    feedback_label.place(relx=0.5, rely=0.5, anchor="center")
    #Message Box
    def create_error_window(message):
        error_window = Toplevel(w_hard1)
        error_window.title("Warning")
        error_window.geometry("250x100")
        error_label = tk.Label(error_window, text=message, fg="red", font=("Comic Sans MS", 14))
        error_label.pack(pady=20)
    #Validator
    def input_validator(user_input):
        if user_input.strip() == "":
            create_error_window("No Blanks!")
            return False
        try:
            float(user_input)
        except ValueError:
            create_error_window("Please enter a valid number!")
            return False
        if len(user_input) > 10:
            create_error_window("Max 10 characters!")
            return False
        return True
    
    #Answer checker
    def submit_answer():
        user_input = answer_entry.get().strip()
        if not input_validator(user_input):
            return

        correct_answer = hard_questions[current_q[0]]["answer"]
        #Considering Float to increase diffulty
        try:
            user_val = float(user_input)
            correct_val = float(correct_answer)
        except ValueError:
            feedback_text.set("Invalid numeric answer format.")
            return

        if user_val == correct_val:
            feedback_text.set("Correct!")
        else:
            feedback_text.set(f"Wrong! Correct answer was {correct_answer}")

        current_q[0] += 1
        if current_q[0] < len(hard_questions):
            question_label.config(text=hard_questions[current_q[0]]["question"])
            answer_entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Quiz Over", "You have completed all questions.")
            w_hard1.destroy()

    button_creator(w_hard1, "z_submit_btn.png", (250, 80), submit_answer, 0.5, 0.8, "center")


# ---------------------- Main Window ------------------------

root = tk.Tk()
root.title("Mathrix")
root.geometry("1280x720")
root.resizable(False, False)

bg_image = pillow_image_opener("z_Main_Math.png", (1280, 720))
create_background(root, bg_image)

# Start button
button_creator(root, "Z_Start_m.png", (250, 80), levels_s, 0.494, 0.8, "center")

# Continue button
#Continue_button will be added in the final version, because the developer is currently understanding more about file handling

# Quit button
button_creator(root, "z_Quit_m.png", (250, 80), root_quit, 0.0, 1.0, "sw")

root.mainloop()

