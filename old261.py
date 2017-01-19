
import time, sys
from primes import *
START = time.time()
SIZE  = 10**10

sys.setrecursionlimit(100)

def sumSq(n):
  return n*(n+1)*(2*n+1)/6

def comp(k,m,n):
  return k**2*m + k**2 - k*m**2 - k*m - (m**2*n + m*n**2 + m*n)

comps = comp

# Super simple binary search function
def binSearch(func, lowerBound, upperBound, target):
  mid = (lowerBound + upperBound) / 2
  result = func(mid)
  if result > target:
    return binSearch(func, lowerBound, (lowerBound + upperBound)/2, target)
  elif func(mid+1) < target:
    return binSearch(func, (lowerBound + upperBound)/2, upperBound, target)
  else:
    return mid

def countSmarter(size):
  pivots = set()
  for m in xrange(10, int((size/2)**.5+5)):
    k = n = 2*m**2+2*m
    if k < size:
      pivots.add(k)
      #print k,'\t', m, '\t', n
    for index in xrange(20):
      newDiff = k + n - m
      gcdN = gcd(n, newDiff)
      spot = lcm(n,newDiff) / gcdN
      if index % 2 == 1:
        spot *= m*(m+1)
      elif m == 2:
        spot *= 2
      elif m == 3:
        spot *= 4

#      if index == 0:
#        k = 8*m**3 + 10*m**2 + 3*m
#        n = 8*m**3 + 14*m**2 + 6*m
#        pivots.add(k)
#        continue
#      elif index == 1:
#        k = 32*m**4 + 56*m**3 + 28*m**2 + 4*m
#        n = 32*m**4 + 72*m**3 + 52*m**2 + 12*m
#        pivots.add(k)
#        continue
#      elif index == 2:
#        k = 128*m**5 + 288*m**4 + 216*m**3 + 60*m**2 + 5*m
#        n = 128*m**5 + 352*m**4 + 344*m**3 + 140*m**2 + 20*m
#        pivots.add(k)
#        continue

      print k, n, newDiff
      k = binSearch(lambda x: -comp(x, m, x+newDiff), k, n*newDiff, 0)
      print k,'\t', m, '\t', n, '\t', i + newDiff - spot
      pivots.add(k)
      if spot > size or i >= size -1:
        break
  return pivots


def countNum(size):
  pivots = set()
  for k in xrange(1,size):
    for n in xrange(k,size):
      if k**2 % (n+k) != 0:
        continue
      for m in xrange(1,int((size/2)**.5)+5):
        if comp(k,m,n) == 0:
          if k not in ans1:
            print k,'\t', m, '\t', n
          pivots.add(k)
  return pivots

ans1 = countSmarter(SIZE)
print sum(ans1)
print "\n\n"
ans2 = countNum(SIZE)
print "Time Taken:", time.time() - START


"""

G(10^4) = 277236
  badG(10^4)  = 239823

G(10^5) = 8376909

import sympy

  m(n+k)(n - k + m + 1) = k^2
  -> m|k^2 && (n+k)|k^2


There are results for:
  k = n = 2m(m+1)

  k = m(2m+1)(4m+3)
  n = 4m(2m+1)(m+1)

  if k,m,n is a result, then there is another k0, m0, n0 where:
    n0-k0 = k+n-m and m0 = m

120,  1080, 4368, 12240
960,  3288, 7872
2328, 4584
2256

2m^2   + 2m                         = 2m(m+1)
8m^3   + 10m^2 + 3m                 = m(2m+1)(4m+3)
32m^4  + 56m^3 + 28m^2 + 4m         = 4m(m+1)(2m+1)(4m+1)
128m^5 +288m^4 +216m^3 + 60m^2 + 5m = m(8m^2+8m+1)(16m^2+20m+5)

2m^2 + 2m
8m^3 + 14m^2 + 6m
32m^4  + 72m^3 + 52m^2 + 12m
128m^5 +352m^4 +344m^3 + 140m^2 + 20m

am^4 + bm^3 + cm^2 + dm = 120, 1080, 4368, 12240
697, 10682, 60819, 219604,

28   = lcm(7,4)
168  = lcm(28,48)/2
984  = lcm(168,287)/7
5740 = lcm(984, 1680)/12
33460= lcm(5740,9799)/41


360 = lcm(24,45)

8m(m+1)(2m+1)
2m(m+1)(4m+3)



"""
