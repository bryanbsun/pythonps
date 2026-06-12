import sys
sys.setrecursionlimit(1000000000)
 
#
# Solution Template for Buried Treasure
# 
# Australian Informatics Olympiad 2025
# 
# This file is provided to assist with reading of input and writing of output
# for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#
 
# N is the number of clues.
N = 0
# L is the number of locations.
L = 0
 
# A and B contain clues. Note that the lists start from 0, and so the first
# clue is (A[0], B[0]) and the last clue is (A[N-1], B[N-1]).
A = []
B = []
 
# Read the values of N, L, and the clues.
N, L = map(int, input().strip().split())
for i in range(0, N):
  input_vars = list(map(int, input().strip().split()))
  A.append(input_vars[0])
  B.append(input_vars[1])
 
# TODO: This is where you should compute your solution. Store the number of
# locations that are consistent with all N clues into the variable answer.
 
answer = 0
 
left = 1
right = L
 
for i in range(N):
    if A[i] > left:
        left = A[i]
    if B[i] < right:
        right = B[i]
 
if left <= right:
    answer = right - left + 1
# Write the answer.
print(answer)
