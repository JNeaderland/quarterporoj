import turtle
window = turtle.Screen()
boxes = turtle.Turtle()
def make_box(x, y):
    boxes.penup()
    boxes.goto(x,y)
    boxes.pendown()
    for x in range (4):
        boxes.forward(115)
        boxes.right(90)
#Row 1
box1 = make_box(-350, 300)

turtle.color('gray')
style = ('Courier', 30, 'italic')
turtle.write('Hello!', font=style)
turtle.hideturtle()
window.mainloop()