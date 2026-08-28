# 
# Python Problem Solver
# Week 13 Problem 1: Square Canvas
#

N = int(input())
minx, maxx, miny, maxy = 10001, 0, 10001, 0
for i in range(N):
    x, y = map(int, input().strip().split())
    maxx = max(maxx, x)
    minx = min(minx, x)
    maxy = max(maxy, y)
    miny = min(miny, y)

side = max((maxx - minx), (maxy - miny))
print(side * side)



