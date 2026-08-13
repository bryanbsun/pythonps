# 
# Python Problem Solver
# Week 12 Example 4: Circular Maze
#

import turtle

myPen = turtle.Turtle()
#myPen.speed(100)
screen = turtle.Screen()
screen.setup(800, 600)
screen.bgpic("images/circular-maze.png")
myPen.pensize(3)
myPen.color("#cc0088")
myPen.penup()
myPen.goto(-190,20)
myPen.pendown()
myPen.setheading(0)

def drawArc(radius,startingAngle,angle):
   myPen.setheading(startingAngle+90)
   myPen.circle(radius,angle) 

#Completing the maze...
myPen.forward(25)
drawArc(165,175,-160)
myPen.setheading(195)
myPen.forward(40)	
drawArc(125,20,165)
myPen.setheading(190)
myPen.forward(50)

# Complete the code from here...
input()
