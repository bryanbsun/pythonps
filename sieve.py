n = int(input("Give the upper limit of the search: "))

l = list(range(n+1))

i = 2
while (i <= n):
    while i <= n and l[i] == 0:
        i += 1
    d = i * 2
    while d <= n:
        l[d] = 0
        d += i
    i += 1

for i in range(2,n+1):
    if l[i]:
        print(l[i], end = " ")

