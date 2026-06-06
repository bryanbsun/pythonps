# 
# Python Problem Solver
# Week 3 Problem 1: Josephus Problem
#

# Create a list to represent all soldires, 
# place 0 is not used by as a starting position
j = list(range(42))
p = 0
left = 41

# Loop until only 2 are left
while left > 2:
    # Count to 3
    for i in range(3):
        # Each time skip all dead people until 
        # a life person is found
        # Going circular from 1 - 41, use p = p % 41 + 1
        p = p % 41 + 1
        while j[p] == 0:
            p = p % 41 + 1
    # Kill the person, and decrement left people count
    j[p] = 0
    print(f"{p} is killed")
    left -= 1

# Print the survivors
for i in range(1,42):
    if j[i] != 0:
        print(f"{i} is still alive")
