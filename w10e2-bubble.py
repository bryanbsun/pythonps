# 
# Python Problem Solver
# Week 10 Example 2: Bubble Sort
#

N = int(input("Input the number of elements to sort: ").strip())
a = list(map(int, input("Input the elements: ").strip().split()))

for i in range(N):
    for j in range(N-1):
        if a[j] > a[j+1]:
            t = a[j]
            a[j] = a[j+1]
            a[j+1] = t

for i in range(N):
    print(a[i], end=" ")
print()
