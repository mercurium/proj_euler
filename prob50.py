from bitarray import bitarray
from primes import *
import time
start = time.time()

maxz = 0
for j in xrange(0,20):
  lst = [0]*546
  sumz = 0
  for k in xrange(j,600):
    if sumz+primes[k] < 10**6:
      sumz += primes[k]
      lst[k] = sumz
    else: break
  for i in xrange(k-1,0,-1):
      if m_r(lst[i]):
        if maxz < i:
          print lst[i], i
          maxz = i
        break
print "Time Taken: " + str(time.time()-start)
