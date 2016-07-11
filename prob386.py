import time
from primes import pfactor_gen, factor_given_pfactor
START   = time.time()
SIZE    = 10**8

pfactor = pfactor_gen(SIZE)

def factor(n):
  return factor_given_pfactor(n, pfactor)

def mapToFactorPow(n):
  factors   = factor(n)
  powCounts = [ factors.count(x) for x in set(factors)]
  return tuple(sorted(powCounts)[::-1])

primes = [2,3,5,7,11,13,17,19]
possible = dict()
def fillFactorDict(index, current=[], maxPow=1000, prod=1):
  if prod > SIZE or index >= len(primes):
    return
  if len(current) > 0:
    possible[mapToFactorPow(prod)] = 0
  fillFactorDict(index+1, \
      current, \
      current.count(primes[index]), \
      prod\
  )
  if current.count(primes[index]) < maxPow:
    fillFactorDict(index, \
        current + [primes[index]], \
        maxPow, \
        prod * primes[index] \
    )

fillFactorDict(0)
print len(possible)
print "Time taken:", time.time() - START

for i in xrange(2,SIZE+1):
  if i % 10**6 == 0:
    print i
  arrangement = mapToFactorPow(i)
  possible[arrangement] += 1

print "Time taken:", time.time() - START

'''
Theory:
  If I take the ncr that has the largest number, then that constitutes the antichain

  111 -> 3 (2)
  211 -> 4 (2)
  221 -> 5 (2)
  222 -> 7 (3)

  311 ->

4 * 9 * 25 = 900

a^2 x b^2 x c (5)
  0 1 2 3 4 5
  1 3 5 5 3 1
  a^2, b^2, ab, ac, bc

a^3 x b x c (4)
  0 1 2 3 4 5
  1 3 4 4 3 1
  a^2, b^2, ab, ac, bc

a^2 x b x c (4)
  0 1 2 3 4
  1 3 4 3 1
  a^2, ab, ac, bc

a^2 x b^2 x c^2 = 27 elements (7)
  a^2b, a^2c, b^2a, b^2c, c^2a, c^2b, abc (7)
  1, a,b,c, a^2b^2c, ab^2c^2, a^2bc^2, a^2b^2c^2
  0,1,2,3,4,5,6
  1,3,6,7,6,3,1

a^4b^2 (3)
  0,1,2,3,4,5,6
  1,2,3,3,3,2,1

a x b x c x d
  0 1 2 3 4
  1 4 6 4 1

a^2 x b x c x d (7)
  0 1 2 3 4 5
  1 4 7 7 4 1

a^4 x b^4 x c^4 (19)
  0  1  2  3  4  5  6
  1  3  6 10 15 18 19

72 = 2^3 x 3^2
  8, 12, 18

a^k x b^j = min(k,j) + 1
'''
