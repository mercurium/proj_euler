from primes import *
import time
START = time.time()

for i in xrange(len(primes)):
    if (i+1) * primes[i] * 2 > 10**10 and i %2 ==0:
        print i+1
        break

print "Time Taken:", time.time() - START
