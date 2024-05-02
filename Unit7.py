import tkinter as tk
import turtle

def open_lesson(lesson):
    root.destroy()  # Close the current window
    teatcher = turtle.Turtle()
    window = turtle.Screen()
    if lesson == 1:
        teatcher.write(lesson, move=False, align='center', font=('Arial', 20, 'normal'))
    elif lesson == 2:
        teatcher.write(lesson, move=False, align='center', font=('Arial', 20, 'normal'))
    elif lesson == 3:
        teatcher.write(lesson, move=False, align='center', font=('Arial', 20, 'normal'))
    elif lesson == 4:
        teatcher.write(lesson, move=False, align='center', font=('Arial', 20, 'normal'))
    elif lesson == 5:
        teatcher.write(lesson, move=False, align='center', font=('Arial', 20, 'normal'))
    elif lesson == 6:
        teatcher.write(lesson, move=False, align='center', font=('Arial', 20, 'normal'))
    elif lesson == 7:
        teatcher.write(lesson, move=False, align='center', font=('Arial', 20, 'normal'))
    elif lesson == 8:
        teatcher.write(lesson, move=False, align='center', font=('Arial', 20, 'normal'))
    elif lesson == 9:
        teatcher.write(lesson, move=False, align='center', font=('Arial', 20, 'normal'))
    else:
        teatcher.write(lesson, move=False, align='center', font=('Arial', 20, 'normal'))

def make_button(parent, lesson, row, column):
    button = tk.Button(parent, text=lesson, command=lambda: open_lesson(lesson))
    button.grid(row=row, column=column, padx=10, pady=10)

root = tk.Tk()
root.title("Main Launcher")

lessons = ["lesson 1", "lesson 2", "lesson 3", "lesson 4", "lesson 5", "lesson 6", "lesson 7", "lesson 8", "lesson 9", "lesson 10"]

for i, lesson in enumerate(lessons):
    make_button(root, lesson, i // 4, i % 4)

root.mainloop()
