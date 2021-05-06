import tkinter as tk
from tkinter import *


root = tk.Tk()

root.geometry("240x180")  # Used to set the size of the windDow
root.title("Adding with tkinter")
root.configure(bg='Green')

label_1 = Label(root, fg="red", text="Num 1: ")
entry_1 = Entry(root, width=20)

label_2 = Label(root, fg="red", text="Num 2: ")
entry_2 = Entry(root, width=20)

label_1.place(x=10, y=0)
entry_1.place(x=60, y=0)
label_2.place(x=10, y=50)
entry_2.place(x=60, y=50)

results_label = Label(root, fg="red", text="Answer: ")
results_entry = Entry(root, state="readonly")

results_label.place(x=10, y=80)
results_entry.place(x=60, y=80)


# A function adding two numbers.
def add_numbers():

    the_sum = float(entry_1.get()) + float(entry_2.get())
    results_entry.config(state="normal")  # set our entry to be read only when we were defining it.
    results_entry.delete(0, END)
    results_entry.insert(0, the_sum)  # use the set/insert function to a value to an entry.
    results_entry.config(state="readonly")  # we set the results value again to readonly using the config.


add_button = Button(text="ADD", command=add_numbers)
add_button.place(x=102, y=110)


def clear_inputs():
    entry_1.delete(0, END)
    entry_2.delete(0, END)
    results_entry.delete(0, END)


clear_button = Button(text="CLEAR", command=clear_inputs)
clear_button.place(x=30, y=110)


def exit_program():
    return root.destroy()


exit_button = Button(text="EXIT", command=exit_program)
exit_button.place(x=160, y=110)

root.mainloop()