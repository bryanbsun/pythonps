# 
# Python Problem Solver
# Week 15 Example 2: Reverse the digits
#

with open("reverse.txt","r") as f:
    l = list(map(int,f.read().strip().split()))
    for n in l:
        while n > 0:
            print(n%10, end="")
            n//= 10
        print(" ", end="")
    print()
