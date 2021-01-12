# Screen and Events in Module

import turtle
from turtle import Turtle
import random


object = turtle.Turtle()

color = ["red","black","yellow","green","blue","grey","orange","brown"]

def up():
    object.setheading(90)
    object.forward(100)
def down():
    object.setheading(270)
    object.forward(100)

def left():
    object.setheading(180)
    object.forward(100)

def right():
    object.setheading(0)
    object.forward(100)

def clickleft(x,y):
    object.color(random.choice(color))

def clickright(x,y):
    object.stamp()

turtle.listen()

turtle.onscreenclick(clickleft,1)
turtle.onscreenclick(clickright,3)


turtle.onkey(up,"Up")
turtle.onkey(down,"Down")
turtle.onkey(left,"Left")
turtle.onkey(right,"Right")

turtle.mainloop()
