# 
# Python Problem Solver
# Week 15 Example 3: Octal numbers
#

with open("octal.txt","r") as f:
    l = list(map(int,f.read().strip().split()))
    for n in l:
        value = 0
        while n > 0:
            value *= 8
            value += n%10
            n//= 10
        print(value, end=" ")
    print()
