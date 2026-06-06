# 
# Python Problem Solver
# Week 4 Example 3: Election II (AIO 2022 P1)
#

import sys
sys.setrecursionlimit(1000000000)

# N is the number of votes.
N = 0

# votes contains the sequence of votes.
votes = ""

answer = None

# Read the value of N and the votes.
N = int(input().strip())
votes = input().strip()

# TODO: This is where you should compute your solution. Store the winning
# candidate ('A', 'B' or 'C'), or 'T' if there is a tie, into the variable
# answer.

a = 0
b = 0 
c = 0

for v in votes[:N]:
    if v == 'A':
        a += 1
    elif v == 'B':
        b += 1
    elif v == 'C':
        c += 1

if a > b and a > c:
    answer = 'A'
elif b > a and b > c:
    answer = 'B'
elif c > a and c > b:
    answer = 'C'
else:
    answer = 'T'

# Write the answer.
print(answer)
