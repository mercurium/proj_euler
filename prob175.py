import time, string, math
from primes import factor, m_r
START = time.time()

def shortBinExpansion(n):
  counter = [1]
  binNum = bin(n)
  for dig in xrange(3, len(binNum)):
    if binNum[dig] == binNum[dig-1]:
      counter[-1] += 1
    else:
      counter.append(1)
  return string.join(map(str, counter), ',')

cache = dict()
def compute(n):
  if n == 0 or n == 1:
    return 1
  while n % 2 == 1:
    n /= 2
  if n in cache:
    return cache[n]
  if n % 4 == 0:
    cache[n] = 2 * compute(n/2) - compute(n/4)
  if n % 4 == 2:
    cache[n] = compute(n/2) + compute(n/2-1)
  return cache[n]

f = compute

for i in xrange(2,2**24,2):
  if f(i) % 3607 == 0:
    print i, f(i)

#for i in xrange(2,1000,2):
#  print i, '\t', compute(i), '\t', compute(i/2), '\t', compute(i/4), '\t', compute(i) - compute(i/2), '\t', bin(i)


print "Time Taken:", time.time() - START

"""
f(2*n+1)  = f(n)
f(2^n)    = n + 1
f(4n+2)   = f(n)       + f(2n)
f(4n)     = 2 * f(2n)  - f(n)

f(2^n +k) = f(2^(n+1) - k - 2) (k < 2^n, k even)

"""
