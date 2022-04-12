"""Kaleido-Spirale aus 'Progammieren mit Python supereasy'(ISBN'978-3-8310-3457-4')[S.82]"""
import turtle as t
from itertools import cycle
import random as ran

#back
t.bgcolor("black")
#Turtle Speed["slowest","slow","normal","fast","fastest"]
t.speed("normal")
t.pensize(4)
colors = cycle(["red", "orange", "yellow", "green", "blue", "purple", "black"])
speed = ["normal","fast","fastest"]
speeding = "normal"

def defspeeding():
    speeding = ran.choices(speed)
    print(speeding)

def drawcircle(size, pensize, engle, shift, shape):
    #faben/pen
    t.pencolor(next(colors))
    t.bgcolor(next(colors))
    t.pensize(pensize)
    #Formen #t.circle(size)
    next_shape = ""
    if shape == "circle":
        t.circle(size)
        next_shape = "square"
    elif shape == "square":
        for i in range(4):
            t.forward(size * 2)
            t.left(90)
        next_shape = "circle"
    #speed
    defspeeding()
    t.speed(speeding)
    #Antrieb/Drehung
    t.right(engle)
    t.forward(shift)
    drawcircle(size + 5, pensize + 1, engle + 1, shift + 1, next_shape)

drawcircle(30, 4, 0, 1, "circle")