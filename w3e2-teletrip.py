# 
# Python Problem Solver
# Week 3 Example 2: Teletrip (AIO 2023 P1)
#

# Get input, line 1: number N, line 2: string of N instructions
n = int(input())
s = input()

# Define variables, l for leftmost house, r for rightmost house, p for current house
l = 0
r = 0
p = 0

# Loop through all instructions
for i in s[0:n]:
    if i == 'L':
        p -= 1
        if p < l:
            l = p
    elif i == 'R':
        p += 1
        if p > r:
            r = p
    elif i == 'T':
        p = 0

# Output number of houses visited
print(r - l + 1)
