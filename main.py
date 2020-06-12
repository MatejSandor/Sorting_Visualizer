from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title("Sorting Algorithm Visualizer")
root.maxsize(900, 600)
root.config(bg="black")

selected_alg = StringVar()


def generate():
    print("Selected algorithm " + selected_alg.get())


frame = Frame(root, width=600, height=200, bg="black")
frame.grid(row=0, column=0, padx=5)

canvas = Canvas(root, width=600, height=380, bg="white")
canvas.grid(row=1, column=0, padx=5, pady=5)

alg_menu = ttk.Combobox(frame, textvariable=selected_alg, values=['Bubble Sort', 'Merge Sort'])
alg_menu.grid(row=0, column=0, padx=5, pady=5)
alg_menu.current(0)

Button(frame, text="Generate", command=generate, bg="white").grid(row=0, column=1, padx=5, pady=5)

size_entry = Entry(frame)
size_entry.grid(row=0, column=2, padx=5, pady=5)

min_entry = Entry(frame)
min_entry.grid(row=0, column=3, padx=5, pady=5)

max_entry = Entry(frame)
max_entry.grid(row=0, column=4, padx=5, pady=5)


root.mainloop()
