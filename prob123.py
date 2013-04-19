from primes import *

for i in range(6000,len(primes)):
  if (i+1) * primes[i] * 2 > 10**10 and i %2 ==0:
    print i+1
    break


