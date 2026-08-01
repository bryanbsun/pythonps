#Conway's Game of Life 
import turtle
import time
from random import randint

gridSize = 15
myPen = turtle.Turtle()
turtle.tracer(0)
myPen.speed(0)
myPen.color("#000000")
topLeft_x=-180
topLeft_y=180

def glider():
  grid = []
  grid.append([0,1,0,0,0,0,0,0,0,0])
  grid.append([0,0,1,0,0,0,0,0,0,0])
  grid.append([1,1,1,0,0,0,0,0,0,0])
  grid.append([0,0,0,0,0,0,0,0,0,0])
  grid.append([0,0,0,0,0,0,0,0,0,0])
  grid.append([0,0,0,0,0,0,0,0,0,0])
  grid.append([0,0,0,0,0,0,0,0,0,0])
  grid.append([0,0,0,0,0,0,0,0,0,0])
  grid.append([0,0,0,0,0,0,0,0,0,0])
  grid.append([0,0,0,0,0,0,0,0,0,0])
  return grid

# This function draws a box by drawing each side of the square and using the fill function
def box(intDim):
    myPen.begin_fill()
    # 0 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 90 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 180 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 270 deg.
    myPen.forward(intDim)
    myPen.end_fill()
    myPen.setheading(0)

#Draw the grid on screen (intDim is the width of a cell on the grid)
def drawGrid(grid,intDim):  
    global gridSize  
    #Clear the screen  
    myPen.clear()  
    for i in range(0,gridSize+1):
        myPen.penup()    
        myPen.goto(topLeft_x,topLeft_y-i*intDim)    
        myPen.pendown()    
        myPen.goto(topLeft_x+gridSize*intDim,topLeft_y-i*intDim)  
    for i in range(0,gridSize+1):    
        myPen.penup()    
        myPen.goto(topLeft_x+i*intDim,topLeft_y)
        myPen.pendown()
        myPen.goto(topLeft_x+i*intDim,topLeft_y-gridSize*intDim)
    for i in range(0,gridSize):
        myPen.penup()
        myPen.goto(topLeft_x+i*intDim+10,topLeft_y+10)
        myPen.write(chr(65+i))
    for i in range(1,gridSize+1):
        myPen.penup()
        myPen.goto(topLeft_x-15,topLeft_y-i*intDim+10)
        myPen.write(str(i))
    myPen.setheading(0)
    myPen.goto(topLeft_x,topLeft_y-intDim)
    for row in range (0,gridSize):
        for col in range (0,gridSize):
            if grid[row][col]>0:
                box(intDim)
            myPen.penup()
            myPen.forward(intDim)
            myPen.pendown()
        myPen.setheading(270)
        myPen.penup()
        myPen.forward(intDim)
        myPen.setheading(180)
        myPen.forward(intDim*gridSize)
        myPen.setheading(0)
        myPen.pendown()

def checkCell(row,col,grid):
    global gridSize
    # We will count neighbours except when at the edge of the grid 
    minRow=0
    if row>1:
        minRow=row-1
    maxRow=gridSize-1
    if row<gridSize-2:
        maxRow=row+1
    minCol=0
    if col>1:
        minCol=col-1
    maxCol=gridSize-1
    if col<gridSize-2:
        maxCol=col+1
  
    #C ount the number of neighbours
    neighbours=0-grid[row][col]  
    for nrow in range(minRow,maxRow+1):
        for ncol in range(minCol,maxCol+1):
            neighbours += grid[nrow][ncol]
    # Apply the four key rules of Conway's Game of Life
    # 1.Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
    if grid[row][col]==1 and neighbours<2:
        return 0
    #2. Any live cell with two or three live neighbours lives on to the next generation.
    elif grid[row][col]==1 and (neighbours==2 or neighbours==3):
        return 1
    #3. Any live cell with more than three live neighbours dies, as if by overpopulation.    
    elif grid[row][col]==1 and neighbours>3:
         return 0
    #4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    elif grid[row][col]==0 and neighbours==3:
        return 1
    else:
         return 0

####################### MAIN PROGRAM STARTS HERE ######################
print("##########################")
print("Select a Starting Pattern:")
print("  2: Glider")
choice = input("Your Choice (1-5)?")

if choice=="2":
    gridSize = 10
    currentgrid=glider()
else:
    print("Invalid Choice!")
# Initialise the nextgrid
nextgrid = []
for row in range(0, gridSize):
    nextgrid.append([])
    for col in range(0, gridSize):
        nextgrid[row].append(0)

#Start animating the grid
while True:
    drawGrid(currentgrid, 25) #25 is the width of each square on the grid
    myPen.getscreen().update()	
    time.sleep(0.5)
    # Generate Next Grid using the four key rules of Conway's Game of Life
    for row in range(0, gridSize):
        for col in range(0, gridSize):
            nextgrid[row][col] = checkCell(row, col, currentgrid)  
    # Swap grids (nextgrid becomes currentgrid)
    tmpgrid = currentgrid
    currentgrid = nextgrid
    nextgrid = tmpgrid
