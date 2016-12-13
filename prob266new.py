import time
from primes import factor, get_primes
START = time.time()

SIZE   = 100
primes = get_primes(SIZE)[::-1]
LIM    = reduce(lambda x,y: x*y, primes)**.5

def prod(lst):
  if lst == []:
    return 1
  return reduce(lambda x,y: x*y, lst)

valid_set = set([1])
for index in xrange(len(primes)):
  prime         = primes[index]
  remainingProd = prod(primes[index+1:])
  maxElem       = max(valid_set)
  print prime, len(valid_set), "Time Taken:", time.time() - START

  valid_set.update(  \
      set(filter(lambda x: x < LIM and x * remainingProd > maxElem, \
      [prime * val for val in valid_set])))
  valid_set = set(filter( lambda x: x < LIM and x * remainingProd >= maxElem, valid_set))


print LIM - max(valid_set)

print "Time Taken:", time.time() - START
