from tkinter import *

root = Tk()
side_choice = IntVar()
title_label = Label(root, text="Dice Roller")
title_label.grid(row=1, column=1)

four_sided = Radiobutton(root, text="4-sided", variable=side_choice, value=4)
four_sided.grid(row=2, column=1)

six_sided = Radiobutton(root, text="6-sided", variable=side_choice, value=6)
six_sided.grid(row=3, column=1)

eight_sided = Radiobutton(root, text="8-sided", variable=side_choice, value=8)
eight_sided.grid(row=4, column=1)

ten_sided = Radiobutton(root, text="10-sided", variable=side_choice, value=10)
ten_sided.grid(row=5, column=1)

twenty_sided = Radiobutton(root, text="20-sided", variable=side_choice, value=20)
twenty_sided.grid(row=6, column=1)

roll_button = Button(root, text="Roll Dice")
roll_button.grid(row=7, column=1)

roll_result = Label(root, text="0")
roll_button.grid(row=8, column=1)

root.mainloop()