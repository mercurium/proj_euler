import time
from primes import get_prime_count
SIZE = 100


def pfactor_gen(size): #for each number n, return some factor of it.
  pfactor = range(size)
  for i in xrange(2,size,2):
    pfactor[i] = 2

  for i in xrange(3,size,2):
    if pfactor[i] == i:
      for j in xrange(i**2,size,i*2):
        pfactor[j] = min(i, pfactor[j])
  return pfactor

pfactor    = pfactor_gen(SIZE+1)
pfactor[1] = 0
print sum(pfactor), len(pfactor)

for prime in sorted(set(pfactor)):
  print prime, pfactor.count(prime)
