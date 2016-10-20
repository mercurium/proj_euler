import time, sys
from primes import *
START = time.time()
SIZE  = 10**5

sys.setrecursionlimit(300)

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
  elif result < target:
    return binSearch(func, (lowerBound + upperBound)/2, upperBound, target)
  else:
    return mid

def countSmarter(size):
  pivots = set()
  count = 0
  for m in xrange(1, int((size/2)**.5+5)):
    k = n = 2*m**2+2*m
    pivots.add((k,m,n))
    for index in xrange(20):
      newDiff = k + n - m

      if k > size:
        break
      if index == 0:
        k = 8*m**3 + 10*m**2 + 3*m
        n = 8*m**3 + 14*m**2 + 6*m
        pivots.add((k,m,n))
        continue
      elif index == 1:
        k = 32*m**4 + 56*m**3 + 28*m**2 + 4*m
        n = 32*m**4 + 72*m**3 + 52*m**2 + 12*m
        pivots.add((k,m,n))
        continue
      elif index == 2:
        k = 128*m**5 + 288*m**4 + 216*m**3 + 60*m**2 + 5*m
        n = 128*m**5 + 352*m**4 + 344*m**3 + 140*m**2 + 20*m
        pivots.add((k,m,n))
        continue

      k = binSearch(lambda x: comp(x, m, x+newDiff), k, n*newDiff, 0)
      n = k + newDiff
      pivots.add((k,m,n))

  pivots  = set(filter(lambda x: x[0] <= SIZE, pivots))
  newElem = set()

  for pivotSet in sorted(pivots):
    k,m,n = pivotSet
    if n == k:
      continue
    count += 1
    try:
      newK = binSearch(lambda x: comp(x, n-k+m, x + 2*k-m), k, size, 0)
    except:
      continue
    pivots.add((newK, n-k+m, newK + 2*k-m))
    newElem.add((newK, n-k+m, newK + 2*k-m))

  for elem in newElem:
    k,m,n = elem
    for iteration in xrange(20):
      if k > size:
        break
      newDiff = k + n - m
      try:
        k = binSearch(lambda x: comp(x, m, x+newDiff), k, k*n,0)
        n = k + newDiff
        pivots.add((k, m, n))
      except:
        break

  pivots = set(filter(lambda x: x[0] <= SIZE, pivots))
  return pivots

def countNum(size):
  pivots = set()
  for k in xrange(1,size):
    for n in xrange(k,size):
      if k**2 % (n+k) != 0:
        continue
      for m in xrange(1,int((size/2)**.5)+5):
        if comp(k,m,n) == 0:
          if (k,m,n) not in ans1:
            print k,'\t', m, '\t', n
          pivots.add((k,m,n))
  return pivots

ans1 = countSmarter(SIZE)
print sum(set([x[0] for x in ans1]))
#ans2 = countNum(SIZE)
#print ans1.difference(ans2)
#print ans2.difference(ans1)
print "Time Taken:", time.time() - START


"""


f(10^4) = 277236
f(10^5) = 8474349
f(10^6) = 255978835

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

20 - 21 = 29
is the same as
20 - 28 = 22-29

"""
