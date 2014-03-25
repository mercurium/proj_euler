# NOTE this needs more refactoring too...

from bitarray import bitarray
from primes import m_r, primes
import time
START = time.time()

maxz = 0
for startingPrime in xrange(0,20):
    lst = [0]*546
    sumz = 0
    for k in xrange(startingPrime,600):
        if sumz+primes[k] < 10**6:
            sumz += primes[k]
            lst[k] = sumz
        else:
            break


    for i in xrange(k-1,0,-1):
            if m_r(lst[i]):
                if maxz < i:
                    print lst[i], i
                    maxz = i
                break
print "Time taken:",time.time() -START
