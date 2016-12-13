from primes import *
import time
START = time.time()
SIZE  = 10**25


val   = dict()
def helper(n, twoPow):
  if n == 0:
    return 1
  if n % twoPow != 0:
    return 0
  if (n,twoPow) in val:
    return val[(n,twoPow)]


  val[(n,twoPow)] = helper(n-twoPow,   twoPow * 2) \
                  + helper(n-2*twoPow, twoPow * 2) \
                  + helper(n,          twoPow * 2)
  return val[(n,twoPow)]

def compute(n):
  return helper(n,1)

print compute(SIZE)
assert(compute(SIZE) == 178653872807)
print "Time Taken:", time.time()-START


