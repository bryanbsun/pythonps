# 
# Python Problem Solver
# Week 12 Example 3: Drawing an arc
#

import turtle

def drawArc(radius,startingAngle,angle):
   myPen.setheading(startingAngle+90)
   myPen.circle(radius,angle) 

myPen = turtle.Turtle()
myPen.speed(100)
screen = turtle.Screen()
screen.setup(800, 600)
myPen.forward(25)
drawArc(165,175,-160)

input()
