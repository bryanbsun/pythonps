# 
# Python Problem Solver
# Week 5 Problem 1: ECG
#

from turtle import *

speed(15)
screensize(1600,1200)
pencolor("red")
for i in range (-600, 601,8):
    if i%20 == 0:
        pensize(2)
    else:
        pensize(1)
    penup()
    goto(i, -160)
    pendown()
    goto(i, 160)

for i in range(-160, 161, 8):
    if i%20 == 0:
        pensize(2)
    else:
        pensize(1)
    penup()
    goto(-600, i)
    pendown()
    goto(600, i)

pencolor("black")
pensize(2)
penup()
x = -600
goto(x,-9)
pendown()
speed(10)
for x in range(-600, 600, 120):
    goto(x+0, -9)
    goto(x+10, 7)
    goto(x+16, -8)
    goto(x+20, -11)
    goto(x+28, -5)
    goto(x+32, -16)
    goto(x+40, 58)
    goto(x+46, -30)
    goto(x+50, -13)
    goto(x+56, -15)
    goto(x+84, 4)
    goto(x+112, -8)
    goto(x+120, -9)
hideturtle()
