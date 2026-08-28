# 
# Python Problem Solver
# Week 14 Problem 3: The Stepping Stones
#

def solid_stones(n):
    if n < 2:
        return []

    # Step 1: lay out the stones — index i means stone number i.
    # True = floating (assume solid for now). Indices 0 and 1 are unused.
    floating = [True] * (n + 1)
    floating[0] = floating[1] = False

    # Steps 2-4: check each stone in turn, sinking multiples of the solid ones.
    p = 2
    while p * p <= n:               # early stop: past sqrt(n) nothing new sinks
        if floating[p]:             # p is still floating -> it's solid
            for multiple in range(p * p, n + 1, p):
                floating[multiple] = False   # watch it sink
        p += 1

    # Step 5: collect the survivors, in order.
    return [i for i in range(2, n + 1) if floating[i]]


# quick check
print(solid_stones(20))   # [2, 3, 5, 7, 11, 13, 17, 19]
print(solid_stones(10))   # [2, 3, 5, 7]
print(solid_stones(1))    # []
