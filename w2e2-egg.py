# 
# Python Problem Solver
# Week 2 Example 2: the Egg Farmer's Puzzle
#

# Get user to input a positive integer
n = int(input("Number of eggs: "))
while (n < 1):
    n = int(input("Number off eggs: "))

# Find number of large cartons
c1 = n // 12
if c1 > 0:
    print(f"You will need {c1} cartons of 12")
n -= c1 * 12

# Find number of small cartons
c2 = n // 6
if c2 > 0:
    print(f"You will need {c2} cartons of 6")
n -= c2 * 6 

# Find number of loose eggs
if n > 0:
    print(f"You will have {n} eggs for breakfast!")
