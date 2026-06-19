# 
# Python Problem Solver
# Week 7 Problem 2: More Illusions
#

from turtle import *

speed(10)

def drawRectangle(x, y, width, height, colour):
    penup()
    goto(x, y)
    fillcolor(colour)
    pendown()
    begin_fill()
    goto(x + width, y)
    goto(x + width, y - height)
    goto(x, y - height)
    goto(x, y)
    end_fill()
    penup()

def drawLine(xFrom, yFrom, xTo, yTo, colour):
    penup()
    goto(xFrom, yFrom)
    pencolor(colour)
    pendown()
    goto(xTo, yTo)
    penup

def drawCircle(x, y, r, c):
    penup()
    pencolor(c)
    fillcolor(c)
    goto(x, y - r)
    pendown()
    begin_fill()
    circle(r)
    end_fill()
    penup()
    hideturtle()

# Pay attention to all the coordinates are calcuated

drawRectangle(-250, 100, 280, 200, "black")

for y in range(-100, 101, 40):
    if y == -100 or y == 100:
        pensize(10)
    else:
        pensize(5)
    
    drawLine(-250, y, 30, y, "grey")

for x in range(-250, 31, 40):
    if x == -250 or x == 30:
        pensize(10)
    else:
        pensize(5)
    
    drawLine(x, -100, x, 100, "grey")

for x in range(-210, -9, 40):
    for y in range(-60, 61, 40):
        drawCircle(x, y, 3, "white")

x, y = 180, 100

penup()
pencolor("black")
pensize(3)
goto(x, y)
pd()
setheading(240)
fd(200)
lt(120)
fd(170)
lt(120)
fd(110)

pu()
goto(x,y)
setheading(0)
pd()
fd(30)
rt(120)
fd(170)
lt(120)
fd(110)

pu()
goto(x,y)
setheading(0)
fd(30)
pd()
rt(60)
fd(200)
rt(60)
fd(30)
rt(120)
fd(170)
lt(120)
fd(110)

up()
goto(x,y)
setheading(240)
fd(200)
pd()
lt(60)
fd(30)
lt(60)
fd(200)

hideturtle()
input()