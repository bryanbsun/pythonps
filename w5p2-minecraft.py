# 
# Python Problem Solver
# Week 5 Problem 2: Minecraft
#

N = int(input("Input the number of cubes: "))
minimum = N * 4 + 2

for w in range(1, N+1):
    for d in range(w, N+1):
        for h in range(d, N+1):
            if w * d * h == N:
                s = w*d*2 + w*h*2 + d*h*2
                print(f"It takes {s} stickers for a cuboid W = {w}, D = {d}, H = {h}.")
                if s < minimum:
                    minimum = s

print(f"Minimum number of stickers is {minimum}.")

