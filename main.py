from tkinter import *
import random

window = Tk()
window.config(
    bg="#282828"
)

window.geometry("360x400")

CL = ["yes","no"]

def pick():
    label["text"] = CL[random.randrange(0,2)]

label = Label(
    text="",
    font=("Arial",30,"bold"),
    bg="#282828",
    fg="#ffffff"
)

button = Button(
    text="pick",
    font=("Arial",30,"bold"),
    bg="#282828",
    fg="#ffffff",
    bd=1,
    command=pick
)

button.pack(side="bottom",pady=40)

label.pack(side="top",pady=60)

window.mainloop()