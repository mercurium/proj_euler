import time
from primes import get_totient
START = time.time()
SIZE  = 10**4
MOD   = 10**8

def putInDict(valsDict, key, value):
  if key in valsDict:
    valsDict[key] += value
  else:
    valsDict[key] = value

totients    = get_totient(SIZE)
numPaths    = [0] * (SIZE+1)
numPaths[6] = 1

for n in xrange(7, SIZE+1):
  for k in xrange(n-1, 5, -1):
    if totients[n] >= k:
      break
    if totients[k] < totients[n]:
      numPaths[n] += numPaths[k]
  numPaths[n] = numPaths[n] % MOD

print sum(numPaths) % MOD
print "Time Taken:", time.time() - START
