from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title("Sorting Algorithm Visualizer")
root.maxsize(900, 600)
root.config(bg="black")

frame = Frame(root, width=600, height=200, bg="grey")
frame.grid(row=0, column=0, padx=5)

canvas = Canvas(root, width=600, height=380, bg="white")
canvas.grid(row=1, column=0, padx=5, pady=5)

root.mainloop()
