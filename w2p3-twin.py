# 
# Python Problem Solver
# Week 2 Problem 3: Twin Primes
#

# Decide if a number is a prime number

def isPrime(n):
   if n < 2:
      return False
   for i in range(2, int(n**0.5) + 1):
      if n % i == 0:
         return False
   return True

# record the last prime number found
lastlastprime = 0
lastprime = 0
# loop all number from 2 to 1000
for n in range (2, 1000001):
    if isPrime(n):
        if lastprime and lastlastprime and lastprime == n - 2 and lastlastprime == n - 4:
            print(f"{lastlastprime}, {lastprime}, {n}")
        lastlastprime = lastprime
        lastprime = n

