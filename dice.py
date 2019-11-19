from tkinter import *
import random


def roll_dice():
    max = side_choice.get()
    roll = random.randint(1, max)
    roll_value.set(roll)


root = Tk()
side_choice = IntVar()
roll_value = IntVar()
side_choice.set(20)

title_label = Label(root, text="Dice Roller", font="Helvetica 20")
title_label.grid(row=1, column=1)

four_sided = Radiobutton(root, text="4-sided", variable=side_choice, value=4)
four_sided.grid(row=2, column=1, sticky="W")

six_sided = Radiobutton(root, text="6-sided", variable=side_choice, value=6)
six_sided.grid(row=3, column=1, sticky="W")

eight_sided = Radiobutton(root, text="8-sided", variable=side_choice, value=8)
eight_sided.grid(row=4, column=1, sticky="W")

ten_sided = Radiobutton(root, text="10-sided", variable=side_choice, value=10)
ten_sided.grid(row=5, column=1, sticky="W")

twenty_sided = Radiobutton(root, text="20-sided", variable=side_choice, value=20)
twenty_sided.grid(row=6, column=1, sticky="W")

roll_button = Button(root, text="Roll Die", command=roll_dice)
roll_button.grid(row=7, column=1, sticky="W")

roll_result = Label(root, textvariable=roll_value, font="Helvetica 24")
roll_result.grid(row=8, column=1)
root.mainloop()
