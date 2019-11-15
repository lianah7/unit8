# by Liana Hill
# last updated November, 15, 2019
# unit 8 daily exercises


from tkinter import *

root = Tk()

# problem one
hello_label = Label(root, text="Hello World")
hello_label.grid(row=1, column=1)


# problem two
user_name = StringVar()
user_name.grid(row=2, column=1)

root.mainloop()

