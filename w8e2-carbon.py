# 
# Python Problem Solver
# Week 8 Example 2: Archaeologist's Challenge
#

import math

thalf = 5730
c14 = float(input("Input the current Carbon-14 to Carbon-12 ratio: "))
age = int(-(thalf / math.log(2) * math.log(c14)))

print(f"The age of the artefact is around {age} years.")