# 
# Python Problem Solver
# Week 9 Example 2: Bubble Sort
#

N = int(input("Input the number of elements to sort: ").strip())
a = list(map(int, input("Input the elements: ").strip().split()))

for i in range(N):
    for j in range(N-1,i,-1):
        if a[j] < a[j-1]:
            t = a[j]
            a[j] = a[j-1]
            a[j-1] = t

for i in range(0,N-1):
    print(a[i], end=", ")
print(a[N-1])