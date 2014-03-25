from primes import primes
from math import *
import time

START = time.time()
setz = set()
SIZE = 5*10**7


count = 0
for fourthPow in xrange(0,int(SIZE**(1/4.))):
  if primes[fourthPow]**4 > SIZE:
    break
  for thirdPow in xrange(0, int(SIZE**(1/3.))):
    if primes[fourthPow]**4+primes[thirdPow]**3 > SIZE:
      break
    for secondPow in xrange(0,int(SIZE**(1/2.))):
      sumz = primes[fourthPow]**4+primes[thirdPow]**3+primes[secondPow]**2
      if sumz >= SIZE:
        break
      setz.add(sumz)

print "The answer is:", len(setz)
print "Time Taken:", time.time() - START

"""
Pretty simple solution here, just iterate through all possible combinations. There's not that many that satisfy it since prime fourth powers get pretty big pretty fast so it only takes ~.91 seconds to find all 1,097,343 of them.
"""
