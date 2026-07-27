a = list(map(int,input().strip().split()))
n = len(a)

for i in range(n):
    for j in range(n-1):
        if a[j] > a[j+1]:
            t = a[j+1]
            a[j+1] = a[j]
            a[j] = t
    print(a)
            
