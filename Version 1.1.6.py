"""
Author:         [Abhishek Lankapalli]
Date:           2025/06/05
Version:        1.1.1.6
Description:    This program is a math quiz for primary school students. It uses a simple Tkinter interface to ask questions, check answers,
                and give feedback to help kids practice basic and medium math skills.
Language:       Python 3.10 """

import tkinter as tk
from tkinter import Toplevel
from PIL import Image, ImageTk
from tkinter import messagebox
import json


#Function_to_postion_windows_uniformily_on_the_screen
def set_window_center(window, width, height):
    #To get dimension of screen
    win_width= window.winfo_screenwidth()
    win_height = window.winfo_screenheight()
    #Setting position,placing the window horizontally and vertically on screen
    x = (win_width - width) //2
    y = (win_height - height) // 3
    #Appying the changes to in geometry to window
    window.geometry( f"{width}x{height}+{x}+{y}")

#---------------------File_handling----------------------
#Global Variable, for tracking and storing name of current player
CURRENT_PLAYER = ""

#Function to open JSON file and save user's name, scores in each level
def save_game(player, easy=0, medium=0, hard=0):
    #Trying to read data of existing player
    try:
        with open('player_data.json') as f:
            data = json.load(f)
    #When data does not exist, this will write data with empty dictionary
    #Also update scores
    except:
        data = {}
        #Add, update scores
    data[player] = {'easy': easy, 'medium': medium,
                    'hard': hard}
    with open('player_data.json', 'w') as f:
        json.dump(data, f, indent=2)

    #Function to load saved data from JSON file
def load_player(player):
    #trying for opening and reading file for data
    try:
        with open('player_data.json') as f:
            dat = json.load(f)
            #Return specified player's data or default if not found
            return dat.get(player, {'easy': 0, 'medium': 0,'hard': 0})
        # Return default scores if any error occurs (file missing, JSON decode error, etc.)
    except:
        return {'easy': 0, 'medium': 0, 'hard': 0}

#Funtion to get only names saved in JSON file
def get_all_players():
    try:
        with open('player_data.json') as f:
            # Load the JSON data and get just the player names
            return list(json.load(f).keys())
    except:
        # Return empty list if no players found
        return []

#---------------------------------------------------------------------------------------------------------
#--------------------------Functioning_common_utilies----------
#Function for opening and resizing images, Pillow library
def pillow_image_opener(path, size):
    # Open the image from given file path
    opened_image = Image.open(path)
    #Resize the image to needed dimensions, LANCZOS for increasing quality
    img_resize = opened_image.resize(size, Image.Resampling.LANCZOS)
    #Return the resized image
    return img_resize

# Function for setting backgrounds for windows
def create_window_background(window, image):
    #Convert pillow image to photo_image for using in tkinter, and label in specified window
    image_convert = ImageTk.PhotoImage(image)
    label_img = tk.Label(window, image= image_convert)
    label_img.image = image_convert
    #Place the label from top left corner and fill 100% window width and height
    label_img.place(x=0, y=0, relwidth=1, relheight=1)


# Function to create buttons of images without border
def button_creator(window, image_path, size, command, relx, rely, anchor):
    #For opening images and parameters for file and size
    btn_img = pillow_image_opener(image_path, size)
    # Convert image for Tkinter
    img_cnvrt = ImageTk.PhotoImage(btn_img)
    btn = tk.Button(window, image=img_cnvrt, borderwidth=0,
     highlightthickness=0, command=command)
    # Keep image reference and positioning
    btn.image = img_cnvrt
    btn.place(relx=relx, rely=rely, anchor=anchor)
    #Return if needed later
    return btn


#----------------Creating_Function_for_start/continue/quit_--------------
#Funtion of quit_button in main window
def start_to_quit():
    print("Quit button clicked")
    #destroys main_window
    main_window.destroy()

#Function of start button in main_window,
def start_to_sign():
    #calling current player for tracking
    global CURRENT_PLAYER
    # Create sign-in window
    sign_w = Toplevel()
    sign_w.title("Mathrix.sign_in")
    set_window_center(sign_w, 1280, 720)
    sign_w.resizable(False, False)

    #Set bg
    bg_image_s = pillow_image_opener("z_signin_bg.png.", (1280, 720))
    create_window_background(sign_w, bg_image_s)

    # Function for handling close button of window(X button)
    def on_closing_s():
        closing_signin = messagebox.askyesno("exit", "do you wan to quit")
        #If user click yes, program ends immediately
        if  closing_signin:
            main_window.destroy()
    sign_w.protocol("WM_DELETE_WINDOW", on_closing_s)

    #Enrty box to type username
    username_enty = tk.Entry(sign_w, font=("Just Another Hand", 16), bg="white", fg="black",
                             relief="flat", width=20)
    username_enty.place(relx=0.49, rely=0.7, anchor='center')
    username_enty.focus_set()

    #Function of submit button in sign_in window
    def submit_in_start():
        #Global variable
        global CURRENT_PLAYER

        #Transfering entered name to global variable
        CURRENT_PLAYER = username_enty.get().strip()

        #Validator, range of 15 character, if exceeds shows warning
        if len(CURRENT_PLAYER) > 15:
            messagebox.showwarning("INVALID RANGE", "Entry should not pass more than 15 characters")
            return
        #If entry not detected, (clicked entry button without entering name)
        if not CURRENT_PLAYER:
            messagebox.showwarning("Warning", "please enter a username")
            return

        #If whitespace entry detected
        if CURRENT_PLAYER == " ":
            messagebox.showwarning("Warning", "No whitespace entry allowed")

        #If existing player detected, player redirected to continue window
        if CURRENT_PLAYER in get_all_players():
            messagebox.showinfo("Oops wrong place", f"Wrong window, you will redirected to continue window,\n spy: {CURRENT_PLAYER}")
            return start_to_continue()


        #Takes player to level window, also hide signin window
        levels()
        sign_w.withdraw()

    #Functiom for back_button in signin window, opens main_window, hides signin window
    def back_in_start():
        main_window.deiconify()
        sign_w.withdraw()

    #Buttons
    #Button-Submit_button
    button_creator(sign_w, "z_submit_btn.png", (250, 80),
                   submit_in_start, 0.489, 0.8, "center")
    #Button-Back_button
    button_creator(sign_w, "z_back_btn.png", (190, 60),
                   back_in_start, 0, 1.0, "sw")

    #Hiding main_window to keep the screen clean
    main_window.withdraw()

#continue
def start_to_continue():
    continue_w = Toplevel()
    continue_w.title("Mathrix")
    set_window_center(continue_w,1280,720)
    continue_w.resizable(False, False)

    bg_image_c = pillow_image_opener("z_continue_window.png", (1280, 720))
    create_window_background(continue_w, bg_image_c)

    # Function for handling close button of window(X button)
    def on_closing_c():
        closing_signin = messagebox.askyesno("exit", "do you want to quit")
        # If user click yes, program ends immediately
        if closing_signin:
            main_window.destroy()
    continue_w.protocol("WM_DELETE_WINDOW", on_closing_c)

    entry_in_continue = tk.Entry(continue_w, font=("Just Another Hand", 16), bg="white", fg="black",
                             relief="flat", width=20)
    entry_in_continue.place(relx=0.495, rely=0.7, anchor='center')
    entry_in_continue.focus_set()

    #Function for submit button in continue window
    def submit_in_continue():
        # Global variable
        global CURRENT_PLAYER

        # Transferring entered name to global variable
        CURRENT_PLAYER = entry_in_continue.get().strip()

        # Validator, range of 15 character, if exceeds shows warning
        if len(CURRENT_PLAYER) > 15:
            messagebox.showwarning("INVALID RANGE", "Entry should not pass more than 15 characters")
            return
        # If entry not detected, (clicked entry button without entering name)
        if not CURRENT_PLAYER:
            messagebox.showwarning("Warning", "please enter your username")
            return

        # If whitespace entry detected
        if CURRENT_PLAYER == " ":
            messagebox.showwarning("Warning", "No whitespace entry allowed")

        # If existing player detected, player redirected to continue window
        if CURRENT_PLAYER in get_all_players():
            messagebox.showinfo("WELLCOME", f"Wellcome back spy: {CURRENT_PLAYER}")

        # Takes player to level window, also hide continue_w
        levels()
        continue_w.withdraw()

    # Function for back_button in signin window, opens main_window, hides continue_w
    def back_in_continue():
        main_window.deiconify()
        continue_w.withdraw()

    # Buttons
    # Button-Submit_button
    button_creator(continue_w, "z_submit_btn.png", (250, 80),
                   submit_in_continue, 0.489, 0.8, "center")
    # Button-Back_button
    button_creator(continue_w, "z_back_btn.png", (190, 60),
                   back_in_continue, 0, 1.0, "sw")

    # Hiding main_window to keep the screen clean
    main_window.withdraw()

#-------------------Working_window(easy/medium/hard)----------------
#Working Function of easy button in level.w
def working_wind_easy():
    #window set up
    working_easy_w = Toplevel()
    working_easy_w.title(f"Mathrix Easy Mode - {CURRENT_PLAYER}")
    set_window_center(working_easy_w, 1280,720)
    working_easy_w.resizable(False, False)

    # Background setup
    bg_image_w_easy = pillow_image_opener("z_working_bg.png", (1280, 720))
    create_window_background(working_easy_w, bg_image_w_easy)

    # Function for handling close button of window(X button)
    def on_closing_easy():
        closing_signin = messagebox.askyesno("exit", "do you wan to quit")
        # If user click yes, program ends immediately
        if closing_signin:
            main_window.destroy()
    working_easy_w.protocol("WM_DELETE_WINDOW", on_closing_easy)

    # Quiz questions for easy level, easy.w
    #creating dictionary named easy_questions, which stores answer and questions
    easy_questions = [
        {"q": "5 + 3 = ?", "a": 8},
        {"q": "10 - 4 = ?", "a": 6},
        {"q": "2 × 4 = ?", "a": 8},
        {"q": "9 ÷ 3 = ?", "a": 3},
        {"q": "7 + 6 = ?", "a": 13}
    ]

    #Easy level game essential variables
    SCORE_OF_EASY = 0
    CURRENT_Q = 0

    #Labels, Question,score labels and entry box
    #Labeling score in working_w_easy(will grt updated)
    score_label = tk.Label(working_easy_w, text=f"Score: {SCORE_OF_EASY}",
                           font=("Arial", 24), bg="#FFD700")
    score_label.place(relx=0.1, rely=0.1, anchor="center")

    # Labeling easy_questions in working_w_easy(will get updated)
    question_label = tk.Label(working_easy_w, text="",
                              font=("Arial", 36), bg="white")
    question_label.place(relx=0.5, rely=0.3, anchor="center")

    #Labeling entry_box in working_w_easy
    answer_entry = tk.Entry(working_easy_w, font=("Arial", 24), width=10)
    answer_entry.place(relx=0.5, rely=0.5, anchor="center")
    answer_entry.focus_set()

    #Function to show and switch question
    def show_question_easy():
        #For keeping track on question
        nonlocal CURRENT_Q
        #Check if more questions remaining
        if CURRENT_Q < len(easy_questions):
            # Update question label with current question text
            question_label.config(text=easy_questions[CURRENT_Q]["q"])
            #For clearing previous answer
            answer_entry.delete(0, tk.END)
        #if no question remaining end game
        else:
            end_game()

    #Checking answer for easy question entered by player, and switching question
    def check_answer_easy():
        #For tracking
        nonlocal SCORE_OF_EASY, CURRENT_Q
        try:
            #Collecting answer entered by player
            user_answer = int(answer_entry.get())
            #Checking the answer from dictionary
            correct_answer = easy_questions[CURRENT_Q]["a"]

            # Check if answer is right
            if user_answer == correct_answer:
                #Adding 20 points in to score , if answer is correct
                SCORE_OF_EASY += 20
                messagebox.showinfo("Correct!", "Well done! +20 points")

            if len(str(user_answer)) > 15:
                messagebox.showwarning("INVALID RANGE", "Enty should not pass more than 15 characters")
                return answer_entry.delete(0, tk.END)


                #Informing user have entered wrong answer
            if user_answer != correct_answer:
                messagebox.showerror("Incorrect", "The answer you have entered is wrong+ ")
                answer_entry.delete(0, tk.END)


            # Updating score label and moving to next question
            score_label.config(text=f"Score: {SCORE_OF_EASY}")
            CURRENT_Q += 1
            #Show the next question (or end game if finished)
            show_question_easy()
        #If player's entry is not in integer form, shows error
        except ValueError:
            messagebox.showerror("Error", "Please enter a number only!")

    #Handing game when program ends, saving score and showing results
    def end_game():
        # Load the player's existing scores from file
        current_scores = load_player(CURRENT_PLAYER)
        #Updating score of easy mode only
        save_game(CURRENT_PLAYER,
                  easy=SCORE_OF_EASY,
                  medium=current_scores['medium'],
                  hard=current_scores['hard'])
        #Close the game window
        working_easy_w.destroy()

        # Create result window
        result_window_e = Toplevel()
        result_window_e.title("Game Results")
        result_window_e.geometry("1280x720")
        result_window_e.resizable(False, False)

        # Function for handling close button of window(X button)
        def on_closing_result_e():
            closing_e_r = messagebox.askyesno("exit", "do you wan to quit")
            # If user click yes, program ends immediately
            if closing_e_r:
                main_window.destroy()
        result_window_e.protocol("WM_DELETE_WINDOW", on_closing_result_e)

        # Determine win/lose background
        if SCORE_OF_EASY >= 50:
            bg_image_m = pillow_image_opener("z_win_scorebord.png", (1280, 720))
        else:  # Lose condition
            bg_image_m = pillow_image_opener("z_lose_scorebord.png", (1280, 720))

        create_window_background(result_window_e, bg_image_m)

        # Display player name and score
        name_label = tk.Label(result_window_e, text=CURRENT_PLAYER,
                              font=("Arial", 36), bg="green", fg="white")
        name_label.place(relx=0.45, rely=0.6, anchor="center")

        score_display = tk.Label(result_window_e, text=f"Score: {SCORE_OF_EASY}",
                                 font=("Arial", 36), bg="green", fg="white")
        score_display.place(relx=0.56, rely=0.6, anchor="center")

        # Restart button (returns to level selection)
        button_creator(result_window_e, "z_restart_btn.png", (250, 80),
                       lambda: [result_window_e.destroy(), levels()],
                       0.4, 0.9, "center")

        # Quit button
        button_creator(result_window_e, "z_quit_3.png", (200, 70),
                       main_window.destroy, 0.6, 0.9, "center")

        working_easy_w.withdraw()
    def back_in_e():
        working_easy_w.destroy()
        levels()

    # Submit button
    button_creator(working_easy_w, "z_submit_btn.png", (240, 90),
                   check_answer_easy, 0.5, 0.8, "center")

    # Quit button
    button_creator(working_easy_w, "z_quit_2.png", (150, 50),
                   main_window.destroy, 0.89, 1.0, "sw")

    button_creator(working_easy_w, "z_back_btn.png", (150, 50),
                   back_in_e, 0.0, 1.0, "sw")

    # Start the game
    show_question_easy()
    #--------------------------------------------------#
##Working Function of medium button in level.w
def working_wind_medium():
    # Window setup for medium mode
    working_medium_w = Toplevel()
    working_medium_w.title(f"Mathrix Medium Mode - {CURRENT_PLAYER}")
    set_window_center(working_medium_w, 1280, 720)
    working_medium_w.resizable(False, False)

    # Background setup
    bg_image_w_medium = pillow_image_opener("z_working_bg.png", (1280, 720))
    create_window_background(working_medium_w, bg_image_w_medium)

    # Handle window closing (X button)
    def on_closing_medium():
        closing_med = messagebox.askyesno("exit", "do you wan to quit")
        # If user click yes, program ends immediately
        if closing_med:
            main_window.destroy()

    working_medium_w.protocol("WM_DELETE_WINDOW", on_closing_medium)

    # Medium difficulty questions, dictionary
    medium_questions = [
        {"q": "12 × 4 = ?", "a": 48},
        {"q": "√144 = ?", "a": 12},
        {"q": "15% of 200 = ?", "a": 30},
        {"q": "3² + 4² = ?", "a": 25},
        {"q": "2³ × 3 = ?", "a": 24}
    ]

    # Medium level game essential variables
    SCORE_M = 0
    CURRENT_Q_M = 0
    WINNING_SCORE = 70

    # Score display label
    score_label = tk.Label(working_medium_w, text=f"Score: {SCORE_M}",
                           font=("Arial", 24), bg="#FFD700")
    score_label.place(relx=0.1, rely=0.1, anchor="center")

    # Question display label
    question_label = tk.Label(working_medium_w, text="",
                              font=("Arial", 36), bg="white")
    question_label.place(relx=0.5, rely=0.3, anchor="center")

    # Answer entry box
    answer_entry = tk.Entry(working_medium_w, font=("Arial", 24), width=10)
    answer_entry.place(relx=0.5, rely=0.5, anchor="center")
    answer_entry.focus_set()

    # Function to show and switch question
    def show_question_medium():
        # For keeping track on question
        nonlocal CURRENT_Q_M
        # Check if more questions remaining
        if CURRENT_Q_M < len(medium_questions):
            # Update question label with current question text
            question_label.config(text=medium_questions[CURRENT_Q_M]["q"])
            # For clearing previous answer
            answer_entry.delete(0, tk.END)
        # If no question remaining end game
        else:
            end_game()

    def check_answer_medium():
        # For tracking score and question number
        nonlocal SCORE_M, CURRENT_Q_M
        try:
            # Collecting answer entered by player
            user_answer = int(answer_entry.get())
            # Checking the answer from dictionary
            correct_answer = medium_questions[CURRENT_Q_M]["a"]

            # Check if answer is right
            if user_answer == correct_answer:
                # Adding 20 points to score if answer is correct
                SCORE_M += 20
                messagebox.showinfo("Correct!", "Well done! +20 points")

            # Validate answer length
            if len(str(user_answer)) > 15:
                messagebox.showwarning("INVALID RANGE", "Entry should not pass more than 15 characters")
                return answer_entry.delete(0, tk.END)

            # Handle wrong answers
            if user_answer != correct_answer:
                messagebox.showerror("Incorrect", "The answer you have entered is wrong")
                answer_entry.delete(0, tk.END)

            # Update display and move to next question
            score_label.config(text=f"Score: {SCORE_M}")
            CURRENT_Q_M += 1
            # Show next question or end game
            show_question_medium()

        # Handle non-number inputs
        except ValueError:
            messagebox.showerror("Error", "Please enter a number only!")

    def end_game():
        # Load player's existing scores
        current_scores = load_player(CURRENT_PLAYER)
        # Update only medium score
        save_game(CURRENT_PLAYER,
                  easy=current_scores['easy'],
                  medium=SCORE_M,
                  hard=current_scores['hard'])

        # Close game window
        working_medium_w.destroy()

        # Create result window
        result_window_m = Toplevel()
        result_window_m.title("Game Results")
        set_window_center(result_window_m, 1280, 720)
        result_window_m.resizable(False, False)

        # Handle result window closing
        def on_closing_result_m():
            closing_m_r = messagebox.askyesno("exit", "do you wan to quit")
            if closing_m_r:
                main_window.destroy()

        result_window_m.protocol("WM_DELETE_WINDOW", on_closing_result_m)

        # Set win and lose background
        if SCORE_M >= WINNING_SCORE:
            bg_image_m = pillow_image_opener("z_win_scorebord.png", (1280, 720))
        else:
            bg_image_m = pillow_image_opener("z_lose_scorebord.png", (1280, 720))
        create_window_background(result_window_m, bg_image_m)

        # Display player info
        name_label = tk.Label(result_window_m, text=f" SPY: {CURRENT_PLAYER}",
                              font=("Just Another Hand", 36), bg="green", fg="white")
        name_label.place(relx=0.46, rely=0.6, anchor="center")

        score_display = tk.Label(result_window_m, text=f"Score: {SCORE_M}",
                                 font=("Just Another Hand", 36), bg="green", fg="white")
        score_display.place(relx=0.56, rely=0.6, anchor="center")

        # Restart button
        button_creator(result_window_m, "z_restart_btn.png", (250, 80),
                       lambda: [result_window_m.destroy(), levels()],
                       0.4, 0.9, "center")

        # Quit button
        button_creator(result_window_m, "z_quit_3.png", (200, 70),
                       main_window.destroy, 0.6, 0.9, "center")

    # Back button function
    def back_in_m():
        working_medium_w.destroy()
        levels()

    # Create game control buttons
    button_creator(working_medium_w, "z_submit_btn.png", (240, 90),
                   check_answer_medium, 0.5, 0.8, "center")

    button_creator(working_medium_w, "z_quit_2.png", (150, 50),
                   main_window.destroy, 0.89, 1.0, "sw")

    button_creator(working_medium_w, "z_back_btn.png", (150, 50),
                   back_in_m, 0.0, 1.0, "sw")

    # Start the game
    show_question_medium()
    #__________________________________________________________________#


def working_wind_hard():
    # Setting up window
    working_hard_w = Toplevel()
    working_hard_w.title(f"Mathrix Hard Mode - {CURRENT_PLAYER}")
    set_window_center(working_hard_w, 1280, 720)
    working_hard_w.resizable(False, False)

    # Background setup
    bg_image_w_hard = pillow_image_opener("z_working_bg.png", (1280, 720))
    create_window_background(working_hard_w, bg_image_w_hard)

    # Function for handling close button of window(X button)
    def on_closing_h():
        closing_h = messagebox.askyesno("exit", "do you want to quit")
        #If user entered yes, program ends immediately
        if closing_h:
            main_window.destroy()
    working_hard_w.protocol("WM_DELETE_WINDOW", on_closing_h)

    # Hard question, stored in dictionary
    hard_questions = [
        {"q": "Solve for x: 5(3x - 2) = 65", "a": 5},
        {"q": "What is the GCD of 84 and 126?", "a": 42},
        {"q": "If x² - 10x + 21 = 0, find the larger root", "a": 7},
        {"q": "Volume of a cube with surface area 150cm²?", "a": 125},
        {"q": "Sum of the first 12 prime numbers?", "a": 197},
        {"q": "If 4ⁿ = 64, what is 3ⁿ⁺¹?", "a": 81},
        {"q": "A car travels 360km in 4.5 hours. Speed in km/h?", "a": 80}
    ]

    # Hard window variables, these variables called with unlocal
    SCORE_H = 0
    CURRENT_QH = 0
    TIME_LIMIT = 80
    TIME_REMAINING = TIME_LIMIT
    TIMER_H = None
    PENALTY_GIVEN = False

    # labelling score on hard window
    score_label = tk.Label(working_hard_w, text=f"Score: {SCORE_H}",
                           font=("Arial", 24),bg="#FFD700")
    score_label.place(relx=0.1, rely=0.1, anchor="center")
    #Labelling time on hard window
    timer_label = tk.Label(working_hard_w, text=f"Time: {TIME_REMAINING}",
                           font=("Arial", 24), bg="#FF6347")
    timer_label.place(relx=0.9, rely=0.1, anchor="center")
    #Labelling question
    question_label = tk.Label(working_hard_w, text="",
                              font=("Arial", 36), bg="white")
    question_label.place(relx=0.5, rely=0.3, anchor="center")

    # Entry box for collecting user entry
    answer_entry = tk.Entry(working_hard_w, font=("Arial", 24), width=15)
    answer_entry.place(relx=0.5, rely=0.5, anchor="center")
    answer_entry.focus_set()
    # Function for updating timer, hard window
    def update_timer():
        # Variables called unlocally, will be used to track, time,score etc
        nonlocal TIME_REMAINING, TIMER_H, SCORE_H, PENALTY_GIVEN
        # Decrease time by 1 second
        TIME_REMAINING -= 1
        timer_label.config(text=f"Time: {TIME_REMAINING}")

        # Check if time exceeds
        if TIME_REMAINING <= 0:

            # Point deduction for exceeding time limit
            if not PENALTY_GIVEN:
                SCORE_H = max(0, SCORE_H - 10)
                score_label.config(text=f"Score: {SCORE_H}")
                messagebox.showwarning("Time's Up!",
                                       "10 points deducted from reward for\n exceeding time!")
                timer_label.config(text="Time: 0", fg="red")
                #If the deduction gave once , this will stops giving  same question
                PENALTY_GIVEN = True
                next_question()
            return

        # Continue countdown after in 1 millisecond after clicking ok
        TIMER_H = working_hard_w.after(1000, update_timer)

    # Function to reset timer for new question
    def reset_timer():
        nonlocal TIME_REMAINING, TIMER_H, PENALTY_GIVEN
        # Cancel existing timer if running
        if TIMER_H:
            working_hard_w.after_cancel(TIMER_H)

        # Resets timer variables
        TIME_REMAINING = TIME_LIMIT
        timer_label.config(text=f"Time: {TIME_LIMIT}",
                           fg="black")
        PENALTY_GIVEN = False

        # Starts new countdown
        update_timer()

    # Function to display current question
    def show_question():

        #Checks for question is remaining or not
        if CURRENT_QH < len(hard_questions):

            # Display question and clears previous answer
            question_label.config(text=hard_questions[CURRENT_QH]["q"])
            answer_entry.delete(0, tk.END)
            reset_timer()

        else:
            #Ending game
            end_game()

    # Function for checking answer
    def check_answer():
        nonlocal SCORE_H, CURRENT_QH, PENALTY_GIVEN
        try:
            # Validates answer entered
            user_answer = int(answer_entry.get())
            correct_answer = hard_questions[CURRENT_QH]["a"]
            # Check if answer is correct
            if user_answer == correct_answer:
                #Reward points for correct answer and informs player
                SCORE_H += 20
                messagebox.showinfo("Correct!", "Well done! +20 points")
            else:
                # If answer is wrong, informs player the entered answer is wrong
                messagebox.showerror("Incorrect", "The answer you entered is wrong")
                

            # Update score and move to next question
            score_label.config(text=f"Score: {SCORE_H}")
            CURRENT_QH += 1
            next_question()
        #If the entry is not a number, error window pops up
        except ValueError:
            messagebox.showerror("Error", "Please use only numbers!")
            return

    # Function to proceed to next question
    def next_question():
        # Cancel current timer before moving to next question
        if TIMER_H:

            working_hard_w.after_cancel(TIMER_H)
        show_question()

    # Function to handle game when it ends
    def end_game():
        # Load player's saved scores
        current_scores = load_player(CURRENT_PLAYER)
        # Update scores for only hard mode
        save_game(CURRENT_PLAYER,
                  easy=current_scores['easy'],
                  medium=current_scores['medium'],
                  hard=SCORE_H)

        # Close game window
        working_hard_w.destroy()

        # Create result window for hard
        result_window = Toplevel()
        result_window.title("Game Results")
        set_window_center(result_window, 1280, 720)
        result_window.resizable(False, False)

        # Set win/lose background based on score
        if SCORE_H >= 80:
            bg_image_r = pillow_image_opener("z_win_scorebord.png", (1280, 720))
        else:  # Lose condition
            bg_image_r = pillow_image_opener("z_lose_scorebord.png", (1280, 720))
        create_window_background(result_window, bg_image_r)

        # Display player name and score on the window
        name_label = tk.Label(result_window, text=f"SPY: {CURRENT_PLAYER}",
                              font=("Just Another Hand", 36), bg="green", fg="white")
        name_label.place(relx=0.46, rely=0.6, anchor="center")

        score_display = tk.Label(result_window, text=f"Score: {SCORE_H}",
                                 font=("Just Another Hand", 36), bg="green", fg="white")
        score_display.place(relx=0.56, rely=0.6, anchor="center")

        # Restart button (returns to level selection)
        button_creator(result_window, "z_restart_btn.png", (250, 80),
                       lambda: [result_window.destroy(), levels()],
                       0.4, 0.9, "center")

        # Quit button
        button_creator(result_window, "z_quit_3.png", (200, 70),
                       main_window.destroy, 0.6, 0.9, "center")

    # Function to return to level selection
    def back_to_levels():
        # Cancel timer if running
        if TIMER_H:
            working_hard_w.after_cancel(TIMER_H)
        working_hard_w.destroy()
        levels()

    # Create buttons
    # Submit answer button
    button_creator(working_hard_w, "z_submit_btn.png", (240, 90),
                   check_answer, 0.5, 0.8, "center")

    # Quit game button
    button_creator(working_hard_w, "z_quit_2.png", (150, 50),
                   main_window.destroy, 0.89, 1.0, "sw")

    # Back to levels button
    button_creator(working_hard_w, "z_back_btn.png", (150, 50),
                   back_to_levels, 0.0, 1.0, "sw")
    # Start the game by showing first question
    show_question()


#--------------------------------------------Level_Window_--------------------
# The level window
def levels():
    # window, title, position setup
    level_w = Toplevel()
    level_w.title("Mathrix")
    set_window_center(level_w, 1280, 720)
    level_w.resizable(False, False)

    # Creating bg for level
    bg_image_lvl = pillow_image_opener("z_level_choosing_w.png", (1280, 720))
    create_window_background(level_w, bg_image_lvl)

    # Function for handling close button of window(X button)
    def on_closing_l():
        closing_level = messagebox.askyesno("exit", "do you wan to quit")
        if closing_level:
            main_window.destroy()

    level_w.protocol("WM_DELETE_WINDOW", on_closing_l)

    # Function of back button in level window
    def back_in_levels():
        level_w.destroy()
        main_window.deiconify()

    def quit_in_level():
        main_window.destroy()

    # -------------Button functions--------------------------
    def easy_in_levels():
        level_w.withdraw()
        working_wind_easy()

    def medium_in_levels():
        level_w.withdraw()
        working_wind_medium()

    def hard_in_levels():
        level_w.withdraw()
        working_wind_hard()

    # ----------------------------------------------------#

    # Create the actual buttons for each level
    button_creator(level_w, "z_easy_lvl.png", (250, 80),
                   easy_in_levels, 0.47, 0.74, "center")
    button_creator(level_w, "z_medium_lvl.png", (250, 80),
                   medium_in_levels, 0.22, 0.6, "center")
    button_creator(level_w, "z_hard_lvl.png", (250, 80),
                   hard_in_levels, 0.73, 0.6, "center")

    # Back button
    button_creator(level_w, "z_back_btn.png", (200, 70),
                   back_in_levels, 0, 1.0, "sw")
    button_creator(level_w, "z_quit_2.png", (200, 70),
                   quit_in_level, 0.85, 1.0, "sw")
    # Hiding main window
    main_window.withdraw()

#____________________________________________________________Main_Window_______________________________________________________________#
#--------------------------------------------------------------------------------------------------------------------------------------#
#Main Window set up
main_window = tk.Tk()
main_window.title("Mathrix")
set_window_center(main_window, 1280,720)
main_window.resizable(False, False)

# Bg set up
bg_image = pillow_image_opener("z_Main_Math.png", (1280, 720))
create_window_background(main_window, bg_image)

#Waring when click on close button
def on_closing():
    answer = messagebox.askyesno("exit", "You sure to quit")
    if not answer:
        return
    else:
        main_window.destroy()
main_window.protocol("WM_DELETE_WINDOW", on_closing)

# Start button
button_creator(main_window, "Z_Start_m.png", (250, 80),
               start_to_sign, 0.494, 0.7, "center")


# Continue button
button_creator(main_window, "z_Continue_w.png", (250, 80),
               start_to_continue, 0.5, 0.9, "center")

# Quit button
button_creator(main_window, "z_Quit_m.png", (150, 60),
               start_to_quit, 0.0, 1.0, "sw")

#For looping whole program
main_window.mainloop()


