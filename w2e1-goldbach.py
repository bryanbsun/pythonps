# 
# Python Problem Solver
# Week 2 Example 1: the Goldbach Conjecture
#

# Define function to determine whether a number is Prime number
def isPrime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

# Get user to input an enen number larger than 2
n = int(input("Enter an even number greater than 2: "))
while (n % 2 == 1 or n <= 2):
    n = int(input("Enter an even number greater than 2: "))

# For any i less than n, if both i and n-i are prime, we find a match
for i in range (2, n):
    j = n - i
    if isPrime(i) and isPrime(j):
        print(f"{n} = {i} + {j}")
        break
