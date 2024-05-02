import tkinter as tk

def open_unit(unit):
    root.destroy()  # Close the current window
    if unit == "a1":
        import Unit1
    elif unit == "b2":
        import Unit2
    elif unit == "c3":
        import Unit3
    elif unit == "d4":
        import Unit4
    elif unit == "e5":
        import Unit5
    elif unit == "f6":
        import Unit6
    elif unit == "g7":
        import Unit7
    elif unit == "h8":
        import Unit8
    elif unit == "i9":
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
