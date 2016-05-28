#NOTE TODO need to solve it

import time
START = time.time()
from primes import factor


factorsDict = { \
    2 : 9, \
    3 : 5, \
    7 : 1, \
    11: 1 }

factors = []
for f in factorsDict.keys():
  factors += [f] * factorsDict[f]

divisors = {2}
for f in factors:
  divisors = set( [x * f for x in divisors] + list(divisors))

print len(divisors)
for d in divisors:
  if d % 100 == 12:
    print d, factor(d)

print "Time taken:", time.time() - START
