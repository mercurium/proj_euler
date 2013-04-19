from primes import *
from math import *
import time

start = time.time()

lst = {}
limit = 5*10**7


count = 0
for i in range(0,24):
  if primes[i]**4 > limit:
    break
  for j in range(0, 100):
    if primes[i]**4+primes[j]**3 > limit:
      break
    for k in range(0,1000):
      sum = primes[i]**4+primes[j]**3+primes[k]**2
      if sum >= limit:
        break
      elif lst.get(sum,0) == 0:
        lst[sum] = 1

print "time taken:" + str(time.time()-start)

print len(lst)


print "time taken:" + str(time.time()-start)

