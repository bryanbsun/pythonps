# 
# Python Problem Solver
# Week 10 Problem 1: Fountain Ring
#

n, k = map(int, input().strip().split())

"""if (n-k)%(k) == 0:
    print((n-k)//(k))
else:
    print((n-k)//k+1)
"""
print(n//k)
