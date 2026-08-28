# 
# Python Problem Solver
# Week 14 Example 3: Level Ground (2022 AIO P2) 
#

N = 0
A = []
answer = 0

# Read the value of N.
N = int(input().strip())

# Read the altitudes.
A = list(map(int, input().strip().split()))

lastheight = 0
intensity = 0

for height in A:
    if height  == lastheight:
        intensity += height
    else: 
        intensity = height
    answer = max(answer, intensity)
    lastheight = height

# Write the answer.
print(answer)
