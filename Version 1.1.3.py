import tkinter as tk
from tkinter import Toplevel
from PIL import Image, ImageTk
import random

def root_quit():
    print("quit button clicked")
    root.destroy()
def contin():
    print("conti button clicked")
def login_btn():
    login
    
def start_c():
    start_w = tk.Toplevel()
    start_w.title("Mathrix")
    start_w.geometry("1280x720")
    start_w.resizable(False, False)

    bg_image = Image.open(r"C:\Users\24705\OneDrive - Lynfield College\3PAD\Assessment 91906 and 91907\Checkpoit 1\IMAGES\Main_Math.png")
    bg_image = bg_image.resize((1280, 720), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = tk.Label(start_w, image=bg_photo)
    bg_label.image = bg_photo
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    #Levels
    def levels_s():
        levels_w = tk.Toplevel()
        levels_w.title("Mathrix")
        levels_w.geometry("1280x720")
        levels_w.resizable(False, False)

        bg_lvl_image = Image.open(r"C:\Users\24705\OneDrive - Lynfield College\3PAD\Assessment 91906 and 91907\Checkpoit 1\IMAGES\level_choosing_w.png")
        bg_lvl_image = bg_lvl_image.resize((1280, 720), Image.Resampling.LANCZOS)
        bg_lvl_photo = ImageTk.PhotoImage(bg_lvl_image)

        bg_lvl_label = tk.Label(levels_w, image=bg_lvl_photo)
        bg_lvl_label.image = bg_lvl_photo
        bg_lvl_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        #Easy button
        easy_img = Image.open(r"C:\Users\24705\OneDrive - Lynfield College\3PAD\Assessment 91906 and 91907\Checkpoit 1\IMAGES\Easy_lvl.png")
        easy_img = easy_img.resize((250, 80), Image.Resampling.LANCZOS) 
        easy_photo = ImageTk.PhotoImage(easy_img)

        easy_btn = tk.Button(levels_w, image=easy_photo, borderwidth=0, command=root_quit)
        easy_btn.image = easy_photo  
        easy_btn.place(relx=0.47, rely=0.7, anchor="center")

        #Medium button
        Medium_img = Image.open(r"C:\Users\24705\OneDrive - Lynfield College\3PAD\Assessment 91906 and 91907\Checkpoit 1\IMAGES\Easy_lvl.png")
        Medium_img = Medium_img.resize((250, 80), Image.Resampling.LANCZOS) 
        Medium_photo = ImageTk.PhotoImage(Medium_img)

        Medium_btn = tk.Button(levels_w, image=Medium_photo, borderwidth=0, command=root_quit)
        Medium_btn.image = Medium_photo  
        Medium_btn.place(relx=0.47, rely=0.7, anchor="center")
        
   
    
    #entry box
    username_entry = tk.Entry(start_w, font=("Arial", 16), width=30, justify="center")
    username_entry.place(relx=0.5, rely=0.6, anchor="center")


    #login button
    login_img = Image.open(r"C:\Users\24705\OneDrive - Lynfield College\3PAD\Assessment 91906 and 91907\Checkpoit 1\IMAGES\login_1s.png")
    login_img = login_img.resize((250, 80), Image.Resampling.LANCZOS) 
    login_photo = ImageTk.PhotoImage(login_img)

    logn_btn = tk.Button(start_w, image=login_photo, borderwidth=0, command=levels_s)
    logn_btn.image = login_photo  
    logn_btn.place(relx=0.5, rely=0.7, anchor="center")
    

# main window
root = tk.Tk()
root.title("Mathirix")
root.geometry("1280x720")
root.resizable(False, False)
bg_image = Image.open(r"C:\Users\24705\OneDrive - Lynfield College\3PAD\Assessment 91906 and 91907\Checkpoit 1\IMAGES\Main_Math.png")
bg_image = bg_image.resize((1280, 720), Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(bg_image)

label = tk.Label(root, image=photo)
label.place(x=0, y=0, relwidth=1, relheight=1)

# Buttons
button_img = tk.PhotoImage(file=r"C:\Users\24705\OneDrive - Lynfield College\3PAD\Assessment 91906 and 91907\Checkpoit 1\IMAGES\Start_m.png")
strt_button = tk.Button(root, image=button_img, borderwidth=0000, command=start_c)
strt_button.place(relx=0.494, rely=0.7, anchor="center")

buttn_img = tk.PhotoImage(file=r"C:\Users\24705\OneDrive - Lynfield College\3PAD\Assessment 91906 and 91907\Checkpoit 1\IMAGES\Continue_w.png")
conti_button = tk.Button(root, image=buttn_img, borderwidth=0, command=contin)
conti_button.place(relx=0.5, rely=0.9, anchor="center")

butn_img = tk.PhotoImage(file=r"C:\Users\24705\OneDrive - Lynfield College\3PAD\Assessment 91906 and 91907\Checkpoit 1\IMAGES\Quit_m.png")
quit_button = tk.Button(root, image=butn_img, borderwidth=0, command=root_quit)
quit_button.place(relx=0.00, rely=1.0, anchor="sw")



root.mainloop()
