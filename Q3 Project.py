#Author: Jacob Neaderland
from random import seed
from random import randint
import turtle
boxes = turtle.Turtle()
window = turtle.Screen()
letter_a = turtle.Turtle()
letter_b = turtle.Turtle()
letter_c = turtle.Turtle()
letter_d = turtle.Turtle()
letter_e = turtle.Turtle()
letter_f = turtle.Turtle()
letter_g = turtle.Turtle()
letter_h = turtle.Turtle()
letter_i = turtle.Turtle()
letter_j = turtle.Turtle()
letter_k = turtle.Turtle()
letter_l = turtle.Turtle()
letter_m = turtle.Turtle()
letter_n = turtle.Turtle()
letter_o = turtle.Turtle()
letter_p = turtle.Turtle()
letter_q = turtle.Turtle()
letter_r = turtle.Turtle()
letter_s = turtle.Turtle()
letter_t = turtle.Turtle()
letter_u = turtle.Turtle()
letter_v = turtle.Turtle()
letter_w = turtle.Turtle()
letter_x = turtle.Turtle()
letter_y = turtle.Turtle()
letter_z = turtle.Turtle()
window.screensize(1000, 1000)
words = ["House", "Water", "Chair", "Tiger", "Smile", "Earth", "Bread", "Dance", "Music", "Queen", "Apple", "Beach", "Grape", "Knife", "River", "Plant", "Happy", "Cloud", "Fruit", "Horse"]
def make_box(x, y):
    boxes.penup()
    boxes.goto(x,y)
    boxes.pendown()
    for x in range (4):
        boxes.forward(115)
        boxes.right(90)
#Row 1
make_box(-350, 300)
make_box(-225, 300)
make_box(-100, 300)
make_box(25, 300)
make_box(150, 300)
#Row 2
make_box(-350, 175)
make_box(-225, 175)
make_box(-100, 175)
make_box(25, 175)
make_box(150, 175)
#Row 3
make_box(-350, 50)
make_box(-225, 50)
make_box(-100, 50)
make_box(25, 50)
make_box(150, 50)
#Row 4
make_box(-350, -75)
make_box(-225, -75)
make_box(-100, -75)
make_box(25, -75)
make_box(150, -75)
#Row 5
make_box(-350, -200)
make_box(-225, -200)
make_box(-100, -200)
make_box(25, -200)
make_box(150, -200)
#Row 6
make_box(-350, -325)
make_box(-225, -325)
make_box(-100, -325)
make_box(25, -325)
make_box(150, -325)

def letters(letter, x, y):
    letter = letter.lower()
    if letter == "a":
        letter_a.penup()
        letter_a.goto(x, y) #centering in the screen
        letter_a.pendown()
        letter_a.pensize(10)
        letter_a.pencolor("black")

        letter_a.right(65)
        letter_a.forward(100)

        letter_a.setpos(x, y)
        letter_a.right(50)
        letter_a.forward(100)

        letter_a.penup()
        letter_a.setpos(-50,-10)
        letter_a.right(65)
        letter_a.pendown()
        letter_a.backward(50)
    elif letter == "b":
        letter_b.penup()
        #draw straight line
        letter_b.goto(x, y) #centering in the screen
        letter_b.pendown()
        letter_b.pensize(10)
        letter_b.pencolor("black")
        letter_b.right(90)
        letter_b.forward(200)
        letter_b.goto(x, y) #centering in the screen
        letter_b.pendown()
        letter_b.pensize(10)
        letter_b.pencolor("black")
        letter_b.right(90)
        letter_b.forward(200)

        letter_b.penup()
        letter_b.goto(x, y) #centering in the screen
        #draw first curve
        letter_b.pendown()
        letter_b.right(-90)
        letter_b.circle(-50,180)


        letter_b.penup()
        letter_b.goto(x, y) #centering in the screen
        #draw second curve
        letter_b.pendown()
        letter_b.right(180)
        letter_b.circle(-50,180)
    elif letter == "c":
        letter_c.penup()
        letter_c.goto(x, y) #centering in the screen
        letter_c.pendown()
        letter_c.pensize(10)
        letter_c.pencolor("black")
        letter_c.right(180)
        letter_c.backcircle(50,180)
    elif letter == "d":
        letter_d.penup()
        letter_d.goto(x, y) #centering in the screen
        letter_d.pendown()
        letter_d.pensize(10)
        letter_d.pencolor("dark gray")
        letter_d.right(90)
        letter_d.forward(200)

        letter_d.penup()
        letter_d.goto(x, y) #centering in the screen
        #draw curves
        letter_d.pendown()
        letter_d.right(-90)
        letter_d.circle(-100,180)
    elif letter == "e":
        letter_e.penup()
        letter_e.setpos(x, y) #centering in the screen
        letter_e.pendown()
        letter_e.pensize(10)
        letter_e.pencolor("dark gray")
        letter_e.forward(100)
        letter_e.backward(100)
        letter_e.right(90)
        letter_e.forward(100)
        letter_e.left(90)
        letter_e.forward(100)
        letter_e.backward(100)
        letter_e.right(90)
        letter_e.forward(100)
        letter_e.left(90)
        letter_e.forward(100)
    elif letter == "f":
        letter_f.penup()
        letter_f.setpos(x, y) #centering in the screen
        letter_f.pendown()
        letter_f.pensize(10)
        letter_f.pencolor("dark gray")
        letter_f.forward(100)
        letter_f.backward(100)
        letter_f.right(90)
        letter_f.forward(100)
        letter_f.left(90)
        letter_f.forward(100)
        letter_f.backward(100)
        letter_f.right(90)
        letter_f.forward(100)
    elif letter == "g":
        letter_g.penup()
        #draw straight line
        letter_g.goto(x, y) #centering in the screen
        letter_g.pendown()
        letter_g.pensize(10)
        letter_g.pencolor("dark gray")
        letter_g.right(180)
        letter_g.circle(50,180)
        letter_g.left(90)
        letter_g.forward(50)
        letter_g.goto(-50,0)
        letter_g.right(90)
        letter_g.forward(50)
        letter_g.right(90)
        letter_g.forward(20)
    elif letter == "h":
        letter_h.penup()
        #draw straight line
        letter_h.goto(x, y) #centering in the screen
        letter_h.pendown()
        letter_h.pensize(10)
        letter_h.pencolor("dark gray")

        letter_h.right(90)
        letter_h.forward(200)
        letter_h.goto(-30,-50)
        letter_h.goto(50,-50)
        letter_h.goto(50,50)
        letter_h.goto(50,-140)
    elif letter == "i":
        letter_i.penup()
        #draw straight line
        letter_i.goto(x, y) #centering in the screen
        letter_i.pendown()
        letter_i.pensize(10)
        letter_i.pencolor("dark gray")

        letter_i.right(90)
        letter_i.forward(100)
    elif letter == "j":
        letter_j.penup()
        #draw straight line
        letter_j.goto(x, y) #centering in the screen
        letter_j.pendown()
        letter_j.pensize(10)
        letter_j.pencolor("dark gray")

        letter_j.forward(10)
        letter_j.right(90)
        letter_j.forward(150)
        letter_j.circle(-50,180)
    elif letter == "k":
        letter_k.penup()
        #draw straight line
        letter_k.goto(x, y) #centering in the screen
        letter_k.pendown()
        letter_k.pensize(10)
        letter_k.pencolor("dark gray")

        letter_k.right(90)
        letter_k.forward(150)

        letter_k.goto(-30,-20)
        letter_k.left(45)
        letter_k.forward(100)

        letter_k.goto(-30,-20)
        letter_k.left(90)
        letter_k.forward(100)
    elif letter == "l":
        letter_l.penup()
        #draw straight line
        letter_l.goto(x, y) #centering in the screen
        letter_l.pendown()
        letter_l.pensize(10)
        letter_l.pencolor("dark gray")

        letter_l.right(90)
        letter_l.forward(150)

        letter_l.right(-90)
        letter_l.forward(70)
    elif letter == "m":
        letter_m.penup()
        #draw straight line
        letter_m.goto(x, y) #centering in the screen
        letter_m.pendown()
        letter_m.pensize(10)
        letter_m.pencolor("dark gray")

        letter_m.right(90)
        letter_m.forward(150)

        letter_m.goto(x, y)
        letter_m.goto(20,-20)
        letter_m.goto(65,50)
        letter_m.goto(65,-100)
    elif letter == "n":
        letter_n.penup()
        #draw straight line
        letter_n.goto(x, y) #centering in the screen
        letter_n.pendown()
        letter_n.pensize(10)
        letter_n.pencolor("dark gray")

        letter_n.right(90)
        letter_n.forward(150)

        letter_n.goto(x, y)
        letter_n.goto(50,-90)
        letter_n.goto(50,50)
    elif letter == "o":
        letter_o.penup()
        letter_o.goto(x, y) #centering in the screen
        letter_o.pendown()
        letter_o.pensize(10)
        letter_o.pencolor("dark gray")
        letter_o.circle(100,None,100)
    elif letter == "p":
        letter_p.penup()
        letter_p.goto(x, y) #centering in the screen
        letter_p.pendown()
        letter_p.pensize(10)
        letter_p.pencolor("dark gray")
        letter_p.right(90)
        letter_p.forward(150)
        letter_p.goto(x, y)
        letter_p.circle(50,None,100)
    elif letter == "q":
        letter_q.penup()
        letter_q.goto(x, y) #centering in the screen
        letter_q.pendown()
        letter_q.pensize(10)
        letter_q.pencolor("dark gray")
        letter_q.circle(50,None,100)

        letter_q.right(45)
        letter_q.forward(30)
    elif letter == "r":
        letter_r.penup()
        letter_r.goto(x, y) #centering in the screen
        letter_r.pendown()
        letter_r.pensize(10)
        letter_r.pencolor("dark gray")
        letter_r.right(90)
        letter_r.forward(150)
        letter_r.goto(x, y)
        letter_r.right(-90)
        letter_r.circle(-50,180,100)
        letter_r.penup()
        letter_r.goto(0,-40)
        letter_r.left(135)
        letter_r.pendown()
        letter_r.forward(70)
    elif letter == "s":
        letter_s.penup()
        letter_s.goto(x, y) #centering in the screen
        letter_s.pendown()
        letter_s.pensize(10)
        letter_s.pencolor("dark gray")
        letter_s.right(90)
        letter_s.forward(150)
        letter_s.goto(x, y)
        letter_s.right(-90)
        letter_s.circle(-50,180,100)
        letter_s.penup()
        letter_s.goto(0,-40)
        letter_s.left(135)
        letter_s.pendown()
        letter_s.forward(70)
    elif letter == "t":
        letter_t.penup()
        letter_t.goto(x, y) #centering in the screen
        letter_t.pendown()
        letter_t.pensize(10)
        letter_t.pencolor("dark gray")
        letter_t.forward(100)
        letter_t.goto(20,50)
        letter_t.right(90)
        letter_t.forward(100)
    elif letter == "u":
        letter_u.penup()
        letter_u.goto(x, y) #centering in the screen
        letter_u.pendown()
        letter_u.pensize(10)
        letter_u.pencolor("dark gray")
        letter_u.right(90)
        letter_u.forward(100)
        letter_u.circle(50,180,100)
        letter_u.forward(100)
    elif letter == "v":
        letter_v.penup()
        letter_v.goto(x, y) #centering in the screen
        letter_v.pendown()
        letter_v.pensize(10)
        letter_v.pencolor("dark gray")
        letter_v.right(65)
        letter_v.forward(100)
        letter_v.left(130)
        letter_v.forward(100)
    elif letter == "w":
        letter_w.penup()
        letter_w.goto(x, y) #centering in the screen
        letter_w.pendown()
        letter_w.pensize(10)
        letter_w.pencolor("dark gray")
        letter_w.right(65)
        letter_w.forward(100)
        letter_w.left(130)
        letter_w.forward(100)

        letter_w.right(120)
        letter_w.forward(100)
        letter_w.left(130)
        letter_w.forward(100)
    elif letter == "x":
        letter_x.penup()
        letter_x.goto(x, y) #centering in the screen
        letter_x.pendown()
        letter_x.pensize(10)
        letter_x.pencolor("dark gray")
        letter_x.right(50)
        letter_x.forward(155)
        letter_x.penup()

        letter_x.goto(50,50)
        letter_x.right(70)
        letter_x.pendown()
        letter_x.forward(150)
    elif letter == "y":
        letter_y.penup()
        letter_y.goto(x, y) #centering in the screen
        letter_y.pendown()
        letter_y.pensize(10)
        letter_y.pencolor("dark gray")
        letter_y.right(65)
        letter_y.forward(100)
        letter_y.left(130)
        letter_y.forward(100)

        letter_y.penup()
        letter_y.goto(13,-43)
        letter_y.left(25)
        letter_y.pendown()
        letter_y.backward(100)
    elif letter == "z":
        letter_z.penup()
        letter_z.goto(x, y) #centering in the screen
        letter_z.pendown()
        letter_z.pensize(10)
        letter_z.pencolor("dark gray")

        letter_z.forward(100)
        letter_z.right(130)
        letter_z.forward(130)

        letter_z.left(130)
        letter_z.forward(100)
def drawing ():
    attempt = 1
    if attempt == 1:
        (-292.5 , 242.5)
        attempt += 1
    elif attempt == 2:
        (-167.5, 242.5)
        attempt += 1
    elif attempt == 3:
        (-42.5, 242.5)
        attempt += 1
    elif attempt == 4:
        (82.5, 242.5)
        attempt += 1
    elif attempt == 5:
        (207.5, 242.5)
        attempt += 1
    elif attempt == 6:
        (-292.5, 117.5)
        attempt += 1
    elif attempt == 7:
        (-167.5, 117.5)
        attempt += 1
    elif attempt == 8:
        (-42.5, 117.5)
        attempt += 1
    elif attempt == 9:
        (82.5, 117.5)
        attempt += 1
    elif attempt == 10:
        (207.5, 117.5)
        attempt += 1
    elif attempt == 11:
        (-292.5, -7.5)
        attempt += 1
    elif attempt == 12:
        (-167.5, -7.5)
        attempt += 1
    elif attempt == 13:
        (-42.5, -7.5)
        attempt += 1
    elif attempt == 14:
        (82.5, -7.5)
        attempt += 1
    elif attempt == 15:
        (207.5, -7.5)
        attempt += 1
    elif attempt == 16:
        (-292.5, -132.5)
        attempt += 1
    elif attempt == 17:
        (-167.5, -132.5)
        attempt += 1
    elif attempt == 18:
        (-42.5, -132.5)
        attempt += 1
    elif attempt == 19:
        (82.5, -132.5)
        attempt += 1
    elif attempt == 20:
        (207.5, -132.5)
        attempt += 1
    elif attempt == 21:
        (-292.5, -257.5)
        attempt += 1
    elif attempt == 22:
        (-167.5, -257.5)
        attempt += 1
    elif attempt == 23:
        (-42.5, -257.5)
        attempt += 1
    elif attempt == 24:
        (82.5, -257.5)
        attempt += 1
    elif attempt == 25:
        (207.5, -257.5)
        attempt += 1
    elif attempt == 26:
        (-292.5, -382.5)
        attempt += 1
    elif attempt == 27:
        (-167.5, -382.5)
        attempt += 1
    elif attempt == 28:
        (-42.5, -382.5)
        attempt += 1
    elif attempt == 29:
        (82.5, -382.5)
        attempt += 1
    elif attempt == 30:
        (207.5, -382.5)
        attempt += 1
window.mainloop()