import time
from fractions import Fraction
from primes import gcd

START = time.time()
LIMIT = 10**4

count = 0
for denominator in xrange(1, LIMIT):
  numer_range = xrange(1, denominator / 100) if denominator % 2 == 1 else xrange(1, denominator / 100, 2)
  for numerator in numer_range:
    if gcd(numerator, denominator) != 1:
      continue
    if gcd(numerator - 1, denominator) != 1 and gcd(numerator +1, denominator) != 1:
      count += 1
      #print Fraction(numerator, denominator)

print count
print "Time Taken:", time.time() - START



"""

i want to get the set of all numer, denom where:
  numer < denom / 100
  gcd(numer, denom)    = 1
  gcd(numer-1, denom) != 1
  gcd(numer+1, denom) != 1

how the hell do I get the overlap of the two groups of:
  gcd(numer-1, denom) != 1
  gcd(numer+1, denom) != 1
?

"""
