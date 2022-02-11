from tkinter import *


root = Tk()

root.geometry("480x488")

my_entry = Entry(root, width=58)

my_entry.pack()

my_entry.insert(0, "Enter name")

my_entry.configure(state=DISABLED)


def on_click(event):
    my_entry.configure(state=NORMAL)
    my_entry.delete(0, END)


my_entry.bind("<Button-1>", on_click)

root.mainloop()
