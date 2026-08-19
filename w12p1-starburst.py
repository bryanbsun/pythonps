# 
# Python Problem Solver
# Week 11 Problem 2: Starburst
#

import turtle

def burst(*lengths, **style):
    t = turtle.Turtle()
    t.pencolor(style.get("colour", "black"))   # matches the slide's "colour"
    t.pensize(style.get("pensize", 2))
    t.speed(0)

    angle = 360 / len(lengths)                 # even spread, whatever the count
    for length in lengths:
        t.forward(length)                      # draw the ray out
        t.backward(length)                     # come straight back to centre
        t.right(angle)                         # rotate before the next ray

    turtle.done()

#burst(60, 100, 60, 140, 60, 100, colour="orange", pensize=3)
burst(60, 100, 60, 140, 60, 100, 75, 20, 150, 19, pensize=3)
