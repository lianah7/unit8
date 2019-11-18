# by Liana Hill
# last updated November, 15, 2019
# unit 8 daily exercises


from tkinter import *

root = Tk()

# # problem one
# hello_label = Label(root, text="Hello World")
# hello_label.grid(row=1, column=1)


# problem two
user_name = StringVar()
user_name = Entry(root, textvariable=user_name)
user_name.grid(row=1, column=1)


hello = Label(root)
hello.grid(row=2, column=1)
say_hello = Button(root, text="Say Hello")
say_hello.grid(row=3, column=1)
greeting = Label(root, text="Hello", )
greeting.grid(row=2, column=1)


root.mainloop()

