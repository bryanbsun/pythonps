# 
# Python Problem Solver
# Week 7 Example 2: Optical Illusions
#

from turtle import *

speed(10)

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
drawCircle(-50, 0, 30, "purple")
drawCircle(-150, 0, 50, "black")
drawCircle(-50, 100, 50, "black")
drawCircle(50, 0, 50, "black")
drawCircle(-50, -100, 50, "black")

drawCircle(250, 0, 30, "purple")
drawCircle(310, 0, 10, "black")
drawCircle(250, -60, 10, "black")
drawCircle(190, 0, 10, "black")
drawCircle(250, 60, 10, "black")

input()

