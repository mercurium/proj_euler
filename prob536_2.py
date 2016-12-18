import time, math
from primes import get_primes
from heapq import *

START        = time.time()
SIZE         = 10**8
factorDict   = {1 : [], 2: [2]}
listOfPrimes = get_primes(int(SIZE**.5))

def factor(n):
  return factorDict[n]

def checkPropertyLessStupid(m, factors=None):
  if not factors:
    factors = factor(m)
  for f in factors:
    if (m / f + 3) % (f - 1) != 0:
      return False
  return True
cpls = checkPropertyLessStupid


possibleAnswers = set([1])
primesUsed = set()
answers    = set()

firstTime  = True

#possibleAnswers = []
#heapify(possibleAnswers)

for prime in listOfPrimes[1:]:
  print prime, len(possibleAnswers)
  newAnswers = set()

  if prime**3 > SIZE:
    for n in possibleAnswers:
      if n > prime and n * prime < SIZE:
        if cpls(n*prime, factorDict[n] + [prime]):
          answers.add(n*prime)

    # stupid minor optimization
    if prime % 100 == 37:
      for n in sorted(possibleAnswers):
        if n*prime > SIZE:
          if cpls(n):
            answers.add(n)
          possibleAnswers.remove(n)
    continue

  for n in possibleAnswers:
    if n * prime < SIZE:
      if n * prime**2 > SIZE:
        if cpls(n*prime, factorDict[n] + [prime]):
          answers.add(n*prime)
          #primesUsed.update([prime] + factor(n))
      else:
        factorDict[n*prime] = factorDict[n] + [prime]
        newAnswers.add(n*prime)
  possibleAnswers.update(newAnswers)



possibleAnswers.add(2)
possibleAnswers = sorted(possibleAnswers)
print "Time Taken:", time.time() - START

for i in possibleAnswers:
  if cpls(i):
    answers.add(i)
    #print i, factor(i)
    primesUsed.update(set(factor(i)))


print sum(answers), len(answers), len(possibleAnswers)
#print sorted(answers)
print sorted(primesUsed)

print "Time Taken:", time.time() - START


"""
  Numbers that seem to work: products of primes with no repeats (aka, p^2k does not work), and no evens besides 2.

  For each prime, p, we need the number to equal:
  m = p-4 (mod p-1)

  We can figure out which multiples of primes work for a prime by using:
  m = p(p-4 + k(p-1)) for all k >= 0

  Ex: for 7, we can have...
    7((7-4) + 0(7-1)) = 21 <-- actual answer that works
    7((7-4) + 1(7-1)) = 21 + 42 = 63. <-- Doesn't work since 63 = 3^2 * 7, but it satisfies the 7 req
    7((7-4) + 2(7-1)) = 21 + 84 = 105. <--- actual answer that works

  10^2 has 5    answers
  10^3 has 9    answers
  10^4 has 15   answers
  10^5 has 36   answers
  10^6 has 84   answers
  10^7 has 175  answers
  10^8 has 1038 answers

"""
