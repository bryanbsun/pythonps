# 
# Python Problem Solver
# Week 13 Example 1: Art Class (2021 AIO P2)
#

N = int(input())
minx, maxx, miny, maxy = 0, 10001, 0, 10001
for i in range(N):
    x, y = map(int, input().strip().split())
    maxx = min(maxx, x)
    minx = max(minx, x)
    maxy = min(maxy, y)
    miny = max(miny, y)

print((maxx - minx) * (maxy - miny))



