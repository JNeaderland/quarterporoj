import turtle
from tkinter import *
from tkinter import font as W1
from random import seed
from random import randint

seed = 100301
randi = randint(0, 19)
boxes = turtle.Turtle()
window = turtle.Screen()
window.screensize(1000, 100)
FW=Tk() ; FW.withdraw() # a must but don't need a window
leng = 0
letters = []
wordw = []
wordr = []
wordc = []
wordu = []
words = ["House", "Water", "Chair", "Tiger", "Smile", "Earth", "Bread", "Dance", "Music", "Queen", "Apple", "Beach", "Grape", "Knife", "River", "Plant", "Happy", "Cloud", "Fruit", "Horse"]
for x in words:
    wordu.append(x.upper())
randword = wordu[randi]
guess = 0
fullwordguessed = 1

def make_box(x, y):
    boxes.penup()
    boxes.goto(x, y)
    boxes.pendown()
    for _ in range(4):
        boxes.forward(115)
        boxes.right(90)

# Function to calculate center coordinates of each box
def calculate_center(x, y, text, font):
    width = leng
    height = font[1]  # Assuming font[1] represents font size
    return x + (115 - width) / 2, y - (115 + height) / 2
def LENGTH(Text) :
    W2 = W1.Font(family='Courtier' , size = 50)
    leng = W2.measure(Text)

# Font style
style = ('Courier', 50, 'italic')

# Iterate through each box and let the user choose a letter
for y_coord in range(300, -351, -125):
    for x_coord in range(-350, 151, 125):
        make_box(x_coord, y_coord)
        text = turtle.textinput("Input", f"Enter a letter for this box at position ({x_coord}, {y_coord}): ").upper()
        letters.append(text)
        if len(letters)%5 == 0:
            wordg = letters[guess : guess + 5]
            for letter in range(5):
                find = randword.find(wordg[letter])
                if find == -1:
                    wordw.append(wordg[letter])
                elif find != letter:
                    wordc.append(wordg[letter])
                else:
                    wordr.append(wordg[letter])
            guess += 5
            fullwordguessed += 1

        center_x, center_y = calculate_center(x_coord - 5, y_coord - 15, text, style)
        turtle.penup()
        turtle.goto(center_x, center_y)
        turtle.write(text, align='center', font=style)

turtle.hideturtle()
window.mainloop()
