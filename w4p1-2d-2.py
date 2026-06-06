# 
# Python Problem Solver
# Week 4 Problem 1: the 2-D Sum, method 2
#

# Get user input of n
n = int(input("Enter n for the n*n chessboard: "))

# Define total
total = 0

# Gauss approach
# Note this is only one line, and runs only once
for i in range (1,n*n,n):
    total += (i+i+n-1)*n//2

print(total)
