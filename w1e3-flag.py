# 
# Python Problem Solver
# Week 1 Example 3: Drawing flags using Python Turtle
#

# Import all classes and functions from Turtle
from turtle import *

# Initialise turtle

shape("arrow")
speed(10)

# Set screen background

Screen().bgcolor("#DDDDDD")

# Draw the frame for the flag

color("white")
pensize(2)
fillcolor("white")

# Position the pen in the bottom left corner

penup()
goto(-180, -120)
pendown()
begin_fill()
goto(180,-120)
goto(180,120)
goto(-180,120)
goto(-180, -120)
end_fill()  
  
#Draw the blue stripe

color("blue")
pensize(2)
fillcolor("blue")

penup()
goto(-180, -120)
pendown()
begin_fill()
goto(-60,-120)
goto(-60,120)
goto(-180,120)
goto(-180, -120)
end_fill()  

#Draw the red stripe

color("red")
pensize(2)
fillcolor("red")

penup()
goto(60, -120)
pendown()
begin_fill()
goto(180,-120)
goto(180,120)
goto(60,120)
goto(60, -120)
end_fill()  


# Adding Text...
penup()
goto(-62, -160)
color("white")
write("FRANCE", None, "left", ("Arial", 24, "bold"))

# Finish up

hideturtle()
input()
