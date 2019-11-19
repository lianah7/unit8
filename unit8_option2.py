# by Liana Hill
# last updated November 19, 2019
# unit 8 option 2 project - calculator

from tkinter import *

root = Tk()

title = Label(root, text="Calculator", font="Helvetica 24")
title.grid(row=1, column=1, columnspan=4)

result_bar = Entry(root)
result_bar.grid(row=2, column=1, columnspan=4)

clear_button = Button(root, text="Clear", font="Helvetica 17", width=4)
clear_button.grid(row=3, column=1)

negative_button = Button(root, text="(-)", font="Helvetica 17", width=4)
negative_button.grid(row=3, column=2)

percent_button = Button(root, text="%", font="Helvetica 17", width=4)
percent_button.grid(row=3, column=3)

division_button = Button(root, text="/", font="Helvetica 17", width=4)
division_button.grid(row=3, column=4)

seven_button = Button(root, text="7", font="Helvetica 17", width=4)
seven_button.grid(row=4, column=1)

eight_button = Button(root, text="8", font="Helvetica 17", width=4)
eight_button.grid(row=4, column=2)

nine_button = Button(root, text="9", font="Helvetica 17", width=4)
nine_button.grid(row=4, column=3)

root.mainloop()
