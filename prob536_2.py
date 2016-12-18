import time, math
from primes import pfactor_gen, get_primes

START = time.time()
SIZE  = 10**6

factorDict = {1 : [], 2: [2]}

def factor(n):
  return factorDict[n]

def checkPropertyLessStupid(m):
  for f in factor(m):
    if (m / f + 3) % (f - 1) != 0:
      return False
  return True
cpls = checkPropertyLessStupid


def checkPropertyStupid(m):
  for i in xrange(2,m):
    if not (pow(i,m+4, m) == i):
      return False
  return True
cps = checkPropertyStupid

print "Time Taken:", time.time() - START

listOfPrimes    = get_primes(int(SIZE**.5))
possibleAnswers = set([1])
for prime in listOfPrimes[1:]:
  newAnswers      = set()
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
    #print i, factor(i)
    primesUsed.update(set(factor(i)))

print sumz, count, len(possibleAnswers)

print "Time Taken:", time.time() - START
