# 
# Python Problem Solver
# Week 2 Problem 2: I want them all!
#

# Decide if a number is a prime number

def isPrime(n):
   if n < 2:
      return False
   for i in range(2, int(n**0.5) + 1):
      if n % i == 0:
         return False
   return True


# loop all even numbers from 4 to 100
for n in range (4, 1001, 2):

    for i in range (2,n//2):
        j = n - i

        if isPrime(i) and isPrime(j):
            print(f"{n} = {i} + {j}")
            break

