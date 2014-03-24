from primes import *
import time
start = time.time()


twos = tuple([2**i for i in xrange(0,84)])
val = dict()

def helper(n, tl):
  if n == 0: return 1
  if len(tl) == 0 or n%tl[0] != 0: return 0
  if (n,tl[0]) in val: return val[(n,tl[0])]
  val[(n,tl[0])] = helper(n-tl[0],tl[1:])+helper(n-2*tl[0],tl[1:]) + helper(n,tl[1:])
  return val[(n,tl[0])]
    
def compute(n):
  if n in val: return val[n]
  val[n] = helper(n,twos)
  return val[n]

print compute(10**25)
print "Time Taken: " + str(time.time()-start)


