# 
# Python Problem Solver
# Week 1 Example 4: the Goldbach Conjecture
#

# Decide if a number is a prime number

def isPrime(n):
   if n < 2:
      return False
   for i in range(2, int(n**0.5) + 1):
      if n % i == 0:
         return False
   return True

""""# Get an input and tell if      
number = int(input("Enter a whole number"))
if isPrime(number):
   print("This number is a prime number!")
else:
   print("This number is a not a prime number!")
"""

n = int(input("Enter an even number greater than two: "))
while n%2 == 1 or n <= 2:
    n = int(input("Enter an even number greater than two: "))

for i in range (2,n):
    j = n - i

    if isPrime(i) and isPrime(j):
        print(f"{n} = {i} + {j}")
        break

