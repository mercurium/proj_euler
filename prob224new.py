import time, math
from primes import factor
START = time.time()
SIZE = 10**2 * 4

def get_divisors(factors):
  factors = filter(lambda x: x > 1, factors)
  divisors = set([1])
  for f in factors:
    divisors = divisors.union(set([ x*f for x in divisors]))
  return sorted(divisors)

count = 0

for a in xrange(2, SIZE/3):
  if math.sqrt(2 * a**2 + 1) + 2*a > SIZE:
    break

  div = get_divisors(factor(a**2+1))

  # a+b+c = a + (a^2 - 1)/k, which has to be less than the lim
  # also, c - b < a
  kLowerLim = (a**2 + 1) / (SIZE - a)
  div = filter(lambda k: k < a and k > kLowerLim, div)

  # b = (a^2 - k^2 - 1)/2k. We need to make sure b is an int
  # tangent: c = (a^2 + k^2 - 1)/2k. If b is an int, then so is c
  div = filter(lambda k: (a+k) % 2 == 1 , div)
  div = filter(lambda k: \
       (a % 2 == 0) or \
       ((a**2 + 1) % (2*k) == 0) \
      , div)

  # make sure that a <= b
  div = filter(lambda k: a <= (a**2 - k**2 + 1) / (2*k), div)

  for k in div:
    b = (a**2 - k**2 + 1) / (2*k)
    c = b+k
    print a, b,c, k

  count += len(div)

print "Answer:", count
print "Time Taken:", time.time() - START

"""
a^2 + b^2 = c^2 - 1

a^2 + b^2 = (b+k)^2 - 1
-> a^2 = 2bk + k^2 - 1
-> b   = (a^2 - k^2 + 1) / 2k
-> c   = (a^2 + k^2 + 1) / 2k

So we need k|(a^2 + 1)

2a^2 - 1 in squares

a^2 + (a+k)^2 = c^2 - 1
2a^2 + 2ak + k^2 = c^2 - 1




"""

