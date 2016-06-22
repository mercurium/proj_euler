import time, math
from primes import pfactor_gen, factor_given_pfactor
START = time.time()
SIZE = 25 * 10**6

def get_divisors(factors):
  factors = filter(lambda x: x > 1, factors)
  divisors = set([1])
  for f in factors:
    divisors = divisors.union(set([ x*f for x in divisors]))
  return sorted(divisors)

pfactor = pfactor_gen(SIZE)

def factor(n):
  return factor_given_pfactor(n, pfactor)

count       = (SIZE-1) / 2

for a in xrange(2, SIZE/3):
  if a % 16384 == 0:
    print a, count

  if math.sqrt(2 * a**2 - 1) + 2*a > SIZE:
    break

  div = get_divisors(sorted(factor(a-1) + factor(a+1)))

  # a+b+c = a + (a^2 - 1)/k, which has to be less than the lim
  # also, c - b < a
  kLowerLim = (a**2 - 1) / (SIZE - a)
  div = filter(lambda k: k < a and k > kLowerLim, div)

  # b = (a^2 - k^2 - 1)/2k. We need to make sure b is an int
  # tangent: c = (a^2 + k^2 - 1)/2k. If b is an int, then so is c
  div = filter(lambda k: (a+k) % 2 == 1 , div)
  div = filter(lambda k: \
       (a % 2 == 0) or \
       ((a**2 - 1) % (2*k) == 0) \
      , div)

  # make sure that a <= b
  div = filter(lambda k: a <= (a**2 - k**2 - 1) / (2*k), div)

  count += len(div)

print "Answer:", count
print "Time Taken:", time.time() - START


"""

Congratulations, the answer you gave to problem 223 is correct.

You are the 982nd person to have solved this problem.

Answer: 61614848
Time Taken: 632.266522884

"""

