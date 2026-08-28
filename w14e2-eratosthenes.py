# 
# Python Problem Solver
# Week 14 Example 2: Sieve of Eratosthenes
#

def sieve(n):
   # Create a boolean list to track the prime status of all numbers pup to n
   numbers = [True] * (n + 1)

   # 0 and 1 are not prime numbers  
   numbers[0] = False
   numbers[1] = False
   
   # Sieve of Eratosthenes algorithm
   for i in range(2,n//2 + 1):
      if numbers[i]:
         # Mark all multiples of i as non-prime
         for j in range(i*2, n + 1, i):
            numbers[j] = False

   # Combine all prime numbers in a list
   primes = []
   for i in range(2, n + 1):
      if numbers[i]:
         primes.append(i)
   
   return primes

# Main program starts here
n = 100
primes = sieve(n)
print("Prime numbers up to " + str(n) + ":")
for prime in primes:
   print(prime, end=' ')

