# 
# Python Problem Solver
# Week 4 Problem 2: Chart the time
#

from turtle import *

speed(10)
screensize(800,400)

penup()
pencolor("grey")
pensize(1)
for y in range(-120,121,30):
    goto(-360,y)
    pendown()
    goto(-90, y)
    penup()

for x in range(-360,-89,30):
    goto(x,-120)
    pendown()
    goto(x,120)
    penup()

pensize(3)
pencolor("purple")

goto(-360,-120)
pendown()
goto(-360,150)
goto(-370,140)
penup()
goto(-360,150)
pendown()
goto(-350,140)
penup()

goto(-360,-120)
pendown()
goto(-60,-120)
goto(-70,-130)
penup()
goto(-60,-120)
pendown()
goto(-70,-110)
penup()

goto(-320,-160)
write("Constant Algorithm", move=False, align="left", font=("Arial", 16, "normal"))

goto(-380,150)
write("Execution\nTime", move=False, align="center", font=("Arial", 16, "normal"))

goto(-360,0)
pendown()
goto(-75,0)
penup()
write("O(1)", move=False, align="left", font=("Arial", 16, "normal"))

penup()
pencolor("grey")
pensize(1)
for y in range(-120,121,30):
    goto(90,y)
    pendown()
    goto(360, y)
    penup()

for x in range(90,361,30):
    goto(x,-120)
    pendown()
    goto(x,120)
    penup()

pensize(3)
pencolor("purple")

goto(90,-120)
pendown()
goto(90,150)
goto(80,140)
penup()
goto(90,150)
pendown()
goto(100,140)
penup()

goto(90,-120)
pendown()
goto(390,-120)
goto(380,-130)
penup()
goto(390,-120)
pendown()
goto(380,-110)
penup()

goto(130,-160)
write("Linear Algorithm", move=False, align="left", font=("Arial", 16, "normal"))

goto(70,150)
write("Execution\nTime", move=False, align="center", font=("Arial", 16, "normal"))

goto(90,-120)
pendown()
goto(375,135)
penup()
write("O(n)", move=False, align="left", font=("Arial", 16, "normal"))


input()
