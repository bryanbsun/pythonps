# 
# Python Problem Solver
# Week 10 Example 1: Street Construction 
#

n, k = map(int, input().strip().split())

"""if (n-k)%(k+1) == 0:
    print((n-k)//(k+1))
else:
    print((n-k)//(k+1)+1)
"""
print((n)//(k+1))
