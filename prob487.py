import time
import operator as op
from primes import mr
from fractions import Fraction

START = time.time()
SIZE  = 100

def ncr(n, r):
  r = min(r, n-r)
  if r == 0: return 1
  numer = reduce(op.mul, xrange(n, n-r, -1))
  denom = reduce(op.mul, xrange(1, r+1))
  return numer//denom 

def getBernouli(n, size):
  bernouli = [Fraction(1)]
  for m in xrange(1,size+1):
    subPart = sum( [ Fraction(ncr(m,k) * bernouli[k] , (m - k + 1 )) for k in xrange(0, m)])
    bernouli.append( (pow(n,m) - subPart )  )
  return bernouli[-2:]


count = 0
print getBernouli(4, 100)


#primeMods = filter(mr, range(2*10**9, 2*10**9+2000))
#for mod in primeMods:

  
  


print "Time Taken:", time.time() - START

"""
sum( [ ((SIZE +1 - index) * index**POW) for index in range(SIZE) ] ) % MOD
def getBernouli(n, size, mod):
  bernouli = [Fraction(1)]
  for m in xrange(1,size+1):
    subPart = sum( [ (ncr(m,k) % mod) * bernouli(k) / (m - k + 1. ) for k in xrange(0, m)])
    bernouli.append( (pow(n,m,mod) - subPart ) % mod )
  return bernouli

"""
