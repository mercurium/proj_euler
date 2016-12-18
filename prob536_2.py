import time, math
from primes import pfactor_gen, factor_given_pfactor
START = time.time()
SIZE  = 10**6

def primeGen(size): #for each number n, return some factor of it.
  primes = [2]
  factors = [0,1,2] + [1,2] *(size/2-1)
  for i in xrange(3,size,2):
    if factors[i] == 1:
      for j in xrange(i**2,size,i*2):
        if factors[j] == 1:
          factors[j] = i
      factors[i] = i
      primes.append(i)
  return primes

def checkPropertyLessStupid(m, factorization):
  for factor in factorization:
    if (m / factor + 3) % (factor - 1) != 0:
      return False
  return True

cpls = checkPropertyLessStupid
def checkPropertyStupid(m):
  for i in xrange(2,m):
    if not (pow(i,m+4, m) == i):
      return False
  return True
cps = checkPropertyStupid

START = time.time()
print "Time Taken:", time.time() - START

listOfPrimes = primeGen(int(SIZE**.5))
possibleAnswers = [1]
for prime in listOfPrimes[1:]:
  possibleAnswers.extend([x * prime for x in possibleAnswers])
  possibleAnswers = filter((lambda x: x < SIZE), possibleAnswers)

possibleAnswers.append(2)
possibleAnswers.sort()
print "Time Taken:", time.time() - START
START = time.time()

sumz = 0
count = 0
for i in possibleAnswers:
  if cps(i):
    sumz += i
    count += 1

print sumz, count, len(possibleAnswers)

print "Time Taken:", time.time() - START
