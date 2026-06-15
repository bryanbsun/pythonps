# 
# Python Problem Solver
# Week 7 Example 3: Calculating Pi
#

N = int(input())

sum = 0
for n in range(1, N+1):
    sum += 1/(n*n)
answer = (sum * 6) ** .5
print(f"The {N}-th approximation of Pi is {answer}")
