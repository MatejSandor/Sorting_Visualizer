from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title("Sorting Algorithm Visualizer")
root.maxsize(900, 600)
root.config(bg="black")

selected_alg = StringVar()


def draw_data(data):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 20
    spacing = 10

    normalized_data = [i / max(data) for i in data]

    for i, height in enumerate(normalized_data):
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill="grey")
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]))


def generate():
    print("Selected algorithm " + selected_alg.get())
    data = []

    min_value = int(min_entry.get())
    max_value = int(max_entry.get())
    size = int(size_entry.get())

    for _ in range(size):
        data.append(random.randrange(min_value, max_value+1))

    draw_data(data)


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
