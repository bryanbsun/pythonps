# 
# Python Problem Solver
# Week 8 Problem 2: Exact Year
#

import math

thalf = 5730
c14 = float(input("Input the current Carbon-14 to Carbon-12 ratio: "))
age = int(-(thalf / math.log(2) * math.log(c14)))

if age <= 2025:
    year = f"{2026-age}AD"
else:
    year = f"{age-2025}BC"

print(f"The age of the artefact is around {age} years, it was buried in year {year}.")
