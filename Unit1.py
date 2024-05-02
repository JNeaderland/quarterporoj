import tkinter as tk
import turtle


def open_lesson(lesson):
    root.destroy()  # Close the current window
    teatcher = turtle.Turtle()
    window = turtle.Screen()
    teatcher.hideturtle()
    if lesson == "lesson 1":
        teatcher.write("Identify mathematical information from graphical, numerical, \n analytical, and/or verbal representations.", move=False, align='center', font=('Arial', 20, 'normal'))
    elif lesson == "lesson 2":
        teatcher.write("Identify mathematical information from graphical, numerical, \n analytical, and/or verbal representations.", move=False, align='center', font=('Arial', 20, 'normal'))
    elif lesson == "lesson 3":
        teatcher.write("Identify mathematical information from graphical, numerical, \n analytical, and/or verbal representations.", move=False, align='center', font=('Arial', 20, 'normal'))
    elif lesson == "lesson 4":
        teatcher.write("Identify mathematical information from graphical, numerical, \n analytical, and/or verbal representations", move=False, align='center', font=('Arial', 20, 'normal'))
    elif lesson == "lesson 5":
        teatcher.write("Apply appropriate mathematical rules or procedures, \n with and without technology. ", move=False, align='center', font=('Arial', 20, 'normal'))
    elif lesson == "lesson 6":
        teatcher.write("Identify an appropriate mathematical \n rule or procedure based on \n the classification of a given expression \n (e.g., Use the chain rule to find \n the derivative of a composite function).", move=False, align='center', font=('Arial', 20, 'normal'))
    elif lesson == "lesson 7":
        teatcher.write("Identify an appropriate mathematical \n rule or procedure based on \n the classification of a given expression \n (e.g., Use the chain rule to find \n the derivative of a composite function).", move=False, align='center', font=('Arial', 20, 'normal'))
    elif lesson == "lesson 8":
        teatcher.write("Confirm whether hypotheses orconditions of a selected definition, \n theorem, or test have been satisfied.", move=False, align='center', font=('Arial', 20, 'normal'))
    elif lesson == "lesson 9":
        teatcher.write("Identify a re-expression of mathematical information \n presented in a given epresentation.", move=False, align='center', font=('Arial', 20, 'normal'))
    else:
        teatcher.write("N/A", move=False, align='center', font=('Arial', 20, 'normal'))
        
def make_button(parent, lesson, row, column):
    button = tk.Button(parent, text=lesson, command=lambda: open_lesson(lesson))
    button.grid(row=row, column=column, padx=10, pady=10)

root = tk.Tk()
root.title("Main Launcher")

lessons = ["lesson 1", "lesson 2", "lesson 3", "lesson 4", "lesson 5", "lesson 6", "lesson 7", "lesson 8", "lesson 9", "lesson 10"]

for i, lesson in enumerate(lessons):
    make_button(root, lesson, i // 4, i % 4)

root.mainloop()
