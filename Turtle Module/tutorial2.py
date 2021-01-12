# Shaping and Filling Colors

import turtle
import random
object = turtle.Turtle()

color = ["red","black","yellow","green","blue","grey"]

object.color("red","blue")

object.width(5)

object.begin_fill()
object.circle(50)
object.end_fill()

object.penup()
object.forward(150)
object.pendown()

object.color("yellow","black")
object.begin_fill()
for x in range(4):
    object.forward(100)
    object.right(90)
    
object.end_fill()

object.speed(10)
for x in range(6):
    randColor = random.randrange(0,len(color))
    object.color(color[randColor],color[random.randrange(0,len(color))])
    rand1 = random.randrange(-300,300)
    rand2 = random.randrange(-300,300)
    object.penup()
    object.setpos((rand1,rand2))
    object.pendown()
    object.begin_fill()
    object.circle(random.randrange(0,80))
    object.end_fill()
