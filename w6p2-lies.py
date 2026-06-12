#
# Python Problem Solver
# Week 6 Problem 1: Truth and lies
#

N = 0
L = 0
 
A = []
B = []
 
N, L = map(int, input().strip().split())
for i in range(0, N):
  input_vars = list(map(int, input().strip().split()))
  A.append(input_vars[0])
  B.append(input_vars[1])
 
Beach = [0] * (L+1)

answer = 0
 
for i in range(N):
    for j in range(A[i], B[i]+1):
        Beach[j] += 1

Beach.sort()
i = L
m = Beach[L]
while Beach[i] == m:
    i -= 1

answer = L - i

# Write the answer.
print(answer)
