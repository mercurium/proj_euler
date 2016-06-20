import time
from primes import gcd, m_r, factor
START = time.time()
SIZE  = 100

sumz = 0
for i in xrange(1,SIZE+1):
  factors = factor(i+1) + factor(i**2 - i + 1)
  biggestFactor = sorted(factors)[-1]
  print i, biggestFactor
  sumz += biggestFactor - 1

print "Answer:", sumz
print "Time Taken:", time.time() - START


"""
Congratulations, the answer you gave to problem 343 is correct.

You are the 930th person to have solved this problem.

Answer: 269533451410884183
Time Taken: 1570.37111306

Turns out that the 1/k fraction transforms into the (largest prime factor of k+1) - 1, so 1/6 -> 6, and 
  9 -> largestFactor(9+1) = 5 -> 4

"""
