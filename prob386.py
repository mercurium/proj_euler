import time, string
from primes import pfactor_gen, factor_given_pfactor
from itertools import combinations

START   = time.time()
SIZE    = 10**8
pfactor = pfactor_gen(SIZE)
primes  = [2,3,5,7,11,13,17,19]

def factor(n):
  return factor_given_pfactor(n, pfactor)

def mapToFactorPow(n):
  factors   = factor(n)
  powCounts = [ factors.count(x) for x in set(factors) ]
  return tuple(sorted(powCounts)[::-1])

def getMaxOptions(distro):
  lettersMerged = string.join([str(i) * num for i,num in enumerate(distro)], '')
  return len(set( combinations( \
      lettersMerged, \
      len(lettersMerged)/2 )))

gmo = getMaxOptions

possible = dict()
def fillFactorDict(index, current = [], maxPow = 1000, prod = 1):
  if prod > SIZE or index >= len(primes):
    return
  if len(current) > 0:
    possible[mapToFactorPow(prod)] = 0
  fillFactorDict(index+1, \
      current, \
      current.count(primes[index]), \
      prod \
  )
  if current.count(primes[index]) < maxPow:
    fillFactorDict(index, \
        current + [primes[index]], \
        maxPow, \
        prod * primes[index] \
    )

fillFactorDict(0)
print "Time taken:", time.time() - START

for i in xrange(2,SIZE+1):
  if i % 10**6 == 0:
    print i
  arrangement = mapToFactorPow(i)
  possible[arrangement] += 1

total = 1
for key in possible:
  total += gmo(key) * possible[key]

print total
print "Time taken:", time.time() - START

"""

Answer: 528755790
Time taken: 193.456457853

Congratulations, the answer you gave to problem 386 is correct.

You are the 482nd person to have solved this problem.
"""
