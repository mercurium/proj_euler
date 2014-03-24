from primes import *
from math import *
import time

start = time.time()

lst = {}
limit = 5*10**7


count = 0
for i in xrange(0,24):
  if primes[i]**4 > limit:
    break
  for j in xrange(0, 100):
    if primes[i]**4+primes[j]**3 > limit:
      break
    for k in xrange(0,1000):
      sumz = primes[i]**4+primes[j]**3+primes[k]**2
      if sumz >= limit:
        break
      elif lst.get(sumz,0) == 0:
        lst[sumz] = 1

print "time taken:" + str(time.time()-start)

print len(lst)


print "time taken:" + str(time.time()-start)

