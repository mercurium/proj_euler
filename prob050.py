from primes import m_r, primes
import time
START = time.time()

SIZE           = 10**6
MAX_PRIMES_LIM = 600 # sum of [2,3,5,7, ...] first 546 primes = 997,661

maxNumPrimes = 0
for startingPrime in xrange(0, MAX_PRIMES_LIM):
  if sum(primes[startingPrime:startingPrime + maxNumPrimes]) > SIZE:
    break

  lst  = primes[:MAX_PRIMES_LIM]
  k    = startingPrime + 1
  while lst[k-1] < SIZE:
    lst[k] += lst[k-1]
    k      += 1

  for i in xrange(k-1,0,-1):
    if m_r(lst[i]):
      if maxNumPrimes < i:
        print lst[i], i
        maxNumPrimes = i
      break
print "Time taken:",time.time() -START
