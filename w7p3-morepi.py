# 
# Python Problem Solver
# Week 7 Problem 3: More Formula
#

N = int(input("Input N for Leibniz formula: "))

sum = 0
for n in range(1, N+1):
    if n%2 == 0:
        sum -= 1/(2*n-1)
    else:
        sum += 1/(2*n-1)
answer = 4 * sum
print(f"The Leibniz formula: the {N}-th approximation of Pi is {answer}")

N = int(input("Input N for Nilakantha formula: "))

sum = 3
for n in range(1, N+1):
    if n%2 == 0:
        sum -= 4/(2*n*(2*n+1)*(2*n+2))
    else:
        sum += 4/(2*n*(2*n+1)*(2*n+2))
answer = sum
print(f"The Nilakantha formula: the {N}-th approximation of Pi is {answer}")
