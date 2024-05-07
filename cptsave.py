import tkinter as tk

def open_unit(unit):
    root.destroy()  # Close the current window
    if unit == "Unit 1":
        import Unit1
    elif unit == "Unit 2":
        import Unit2
    elif unit == "Unit 3":
        import Unit3
    elif unit == "Unit 4":
        import Unit4
    elif unit == "Unit 5":
        import Unit5
    elif unit == "Unit 6":
        import Unit6
    elif unit == "Unit 7":
        import Unit7
    elif unit == "Unit 8":
        import Unit8
    elif unit == "Unit 9":
        import Unit9
    else:
        import Unit10

def make_button(parent, unit, row, column):
    button = tk.Button(parent, text=unit, command=lambda: open_unit(unit))
    button.grid(row=row, column=column, padx=10, pady=10)

root = tk.Tk()
root.title("Main Launcher")

units = ["Unit 1", "Unit 2", "Unit 3", "Unit 4", "Unit 5", "Unit 6", "Unit 7", "Unit 8", "Unit 9", "Unit 10"]

for i, unit in enumerate(units):
    make_button(root, unit, i // 4, i % 4)

root.mainloop()

"""
import turtle
from tkinter import *

boxes = turtle.Turtle()
window = turtle.Screen()
CURSOR_SIZE = 20
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
BOX_WIDTH = 125
BOX_HEIGHT = 125A
BUTTON_HEIGHT = 25

def open_unit(t):
    window.bye()
    if t == "a1":
        import Unit1
    elif t == "b2":
        import Unit2
    elif t == "c3":
        import Unit3
    elif t == "d4":
        import Unit4
    elif t == "e5":
        import Unit5
    elif t == "f6":
        import Unit6
    elif t == "g7":
        import Unit7
    elif t == "h8":
        import Unit8
    elif t == "i9":
        import Unit9
    else:
        import Unit10

def make_box(a, b, u, i):
    boxes.penup()
    boxes.goto(a, b)
    boxes.pendown()
    for _ in range(4):
        boxes.forward(BOX_WIDTH)
        boxes.right(90)
    boxes.penup()
    boxes.goto(a + BOX_WIDTH / 2, b - BOX_HEIGHT / 2)
    boxes.pendown()
    boxes.write(str(u), move=False, align='center', font=('Arial', 20, 'normal'))
    canvas = window.getcanvas()
    frame = Frame(canvas.master)
    frame.pack()
    button = Button(frame, text="                 ", command=lambda: open_unit(i))
    button.grid(row=0, column=0)
    frame.place(x=(a + CANVAS_WIDTH / 2 - CURSOR_SIZE) + BOX_WIDTH / 4 + 10,
                y=((CANVAS_HEIGHT / 2 - b) - CURSOR_SIZE - BOX_HEIGHT / 3 + BUTTON_HEIGHT - 15) + 150)
    boxes.hideturtle()

make_box(-350, 300, "Unit 1", "a1")
make_box(-200, 300, "Unit 2", "b2")
make_box(-50, 300, "Unit 3", "c3")
make_box(100, 300, "Unit 4", "d4")
make_box(-350, 150, "Unit 5", "e5")
make_box(-200, 150, "Unit 6", "f6")
make_box(-50, 150, "Unit 7", "g7")
make_box(100, 150, "Unit 8", "h8")
make_box(-200, 0, "Unit 9", "i9")
make_box(-50, 0, "Unit 10", "j10")

window.mainloop()
"""
