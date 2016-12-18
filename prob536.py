#NOTE TODO need to solve it

import time, math
from primes import get_primes

START        = time.time()
SIZE         = 10**6
factorDict   = {1 : [], 2: [2]}
listOfPrimes = get_primes(int(SIZE**.5))

def factor(n):
  return factorDict[n]

def checkPropertyLessStupid(m):
  for f in factor(m):
    if (m / f + 3) % (f - 1) != 0:
      return False
  return True
cpls = checkPropertyLessStupid


possibleAnswers = set([1])
for prime in listOfPrimes[1:]:
  newAnswers = set()
  for n in possibleAnswers:
    if n * prime < SIZE:
      factorDict[n*prime] = factorDict[n] + [prime]
      newAnswers.add(n*prime)
  possibleAnswers.update(newAnswers)

possibleAnswers.add(2)
possibleAnswers = sorted(possibleAnswers)
print "Time Taken:", time.time() - START

sumz  = 0
count = 0

primesUsed = set()
for i in possibleAnswers:
  if cpls(i):
    sumz  += i
    count += 1
    print i, factor(i)
    primesUsed.update(set(factor(i)))

print sumz, count, len(possibleAnswers)
print sorted(primesUsed)
print sorted(set(listOfPrimes).difference(primesUsed))

print "Time Taken:", time.time() - START


"""
  Numbers that seem to work: products of primes with no repeats (aka, p^2k does not work), and no evens besides 2.

  For each prime, p, we need the number to equal:
  m = p-4 (mod p-1)

  We can figure out which multiples of primes work for a prime by using:
  m = p(p-4 + k(p-1)) for all k >= 0

  Ex: for 7, we can have...
    7((7-4) + 0(7-1)) = 21 <-- actual answer that works
    7((7-4) + 1(7-1)) = 21 + 42 + 63. <-- Doesn't work since 63 = 3^2 * 7, but it satisfies the 7 req
    7((7-4) + 2(7-1)) = 21 + 42 + 105. <--- actual answer that works

  10^2 has 5   answers
  10^3 has 9   answers
  10^4 has 15  answers
  10^5 has 36  answers
  10^6 has 84  answers
  10^7 has 175 answers

"""

