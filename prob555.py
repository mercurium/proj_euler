import time
from primes import gcd, pfactor_gen, get_divisors_given_pfactor
START = time.time()
SIZE  = 10**6
p     = 10**6


pfactor = pfactor_gen(SIZE)

def sumInterval(start, end):
  return (end*(end+1))/2 - (start -1)*start/2

def divisors(n):
  # want to exclude the number itself
  return get_divisors_given_pfactor(n, pfactor)[:-1]

ans = 0
for k in xrange(1,p+1):
  for div in divisors(k):
    s    = k - div
    ans += sumInterval(SIZE + 1 - s, SIZE + k - 2*s)

print ans
print "Time taken:", time.time() - START


"""
number goes from 16 to 30 for m=p = 30, k = 30

For a number m, k, and s,

if (k-s) | k, then there are (k-s) numbers that work, specifically (m+k)


Congratulations, the answer you gave to problem 555 is correct.

You are the 263rd person to have solved this problem.

~/proj_euler $pypy prob555.py 
208517717451208352
Time taken: 5.01386809349

This problem is actually pretty darn straightforward. It's clear that a pair (k,s) only has solutions if (k-s) | k, and then it'll have exactly (k-s) solutions from (m + 1 - s) to (m + k - 2*s).

Summing the numbers is super easy too, slowest part is almost definitely getting the divisors, but I wrote the code for that part a while back


"""
