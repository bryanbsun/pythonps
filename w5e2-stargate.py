# 
# Python Problem Solver
# Week 5 Example 2: Stargate Access Code 
#

# Get the 6-digit code
code = int(input("Input a 6-digit number: "))

# Flag if no combination can match the code
found = False

# 3-level for-loop to brute-force all 3-letter combination
for i in range(65, 91):
    for j in range(65, 91):
        for k in range(65, 91):
            product = i * j * k
            if product == code:
                print(f"Cracked the code: {chr(i)}{chr(j)}{chr(k)}")
                found = True
                break

if not found:
    print("There no combination that matches the code!")

