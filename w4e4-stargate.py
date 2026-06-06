# 
# Python Problem Solver
# Week 4 Example 4: Stargate Access Code 
#

import sys

print("    ___________________________________")
print("   /                                   \\")
print("   |    Stargate Door Access Panel     |")
print("   \\___________________________________/")
print()

# Get 6-digit code
accessCode = int(input(" >> Input 6-digit code you see: "))

print(" >> 6-digit Access Code: " + str(accessCode))
print(" >>")
print(" >> Starting Brute Force Code Breaking Algorithm to retrieve 3-Letter combination...")

# 3-level loop to find all combinations of (d1, d2, d3)
for d1 in range(65, 91):
    for d2 in range(65, 91):
        for d3 in range(65, 91):
            if d1 * d2 * d3 == accessCode:
                print(" >> Code cracked: ", end="")
                print(chr(d1)+chr(d2)+chr(d3))
                sys.exit()
