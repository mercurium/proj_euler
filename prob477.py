#NOTE TODO need to solve it

import time, math
from itertools import combinations as comb
START = time.time()
SIZE  = 10**6

def primeGen(size): #for each number n, return some factor of it.
  primes = []
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
    if factor == 1:
      return True
    if (m / factor + 3) % (factor - 1) != 0:
      return False
  return True
cpls = checkPropertyLessStupid

def prod(lst):
  return reduce((lambda x,y: x*y), lst, 1)

#maxNumPrimes = 6 # TODO fix this
#listOfPrimes = primeGen(int(SIZE**.5))
#
#sumz  = 0
#count = 0
#
#for numPrimes in xrange(1,maxNumPrimes):
#  for combo in comb(listOfPrimes, numPrimes):
#    count += 1
#    productOfPrimes = prod(combo)
#    if productOfPrimes < SIZE and cpls(productOfPrimes, combo):
#      print combo, productOfPrimes
#      sumz  += productOfPrimes
#    primeIndex = listOfPrimes.index(combo[0])
#    if prod(listOfPrimes[primeIndex: primeIndex+numPrimes]) > SIZE:
#      break


listOfPrimes = primeGen(int(SIZE**.5))
#posAns       = [(3,[3])] # product of primes, # factors in a list
#for prime in listOfPrimes[1:]:
#  posAns.extend([(x[0] * prime, x[1] + [prime]) for x in posAns])
#  posAns = filter((lambda x: x[0] < SIZE), posAns)
#
#posAns.sort()
#print "Time Taken:", time.time() - START
##START = time.time()
#
#sumz = 0
#count = 0
#for i in posAns:
#  if cpls(i[0], i[1]):
#    print i
#    sumz  += i[0]
#    count += 1


posAns       = [(1,[])] # product of primes, # factors in a list
for prime in listOfPrimes:
  posAns.extend([(x[0] * prime, x[1] + [prime]) for x in posAns])
  posAns = filter((lambda x: x[0] < SIZE), posAns)

posAns.append((2,[2]))
posAns.sort()
print "Time Taken:", time.time() - START
#START = time.time()

sumz = 0
count = 0
for i in posAns:
  if cpls(i[0], i[1]):
    print i
    sumz  += i[0]
    count += 1

print sumz, count, len(posAns)
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

  10^2 has 5  answers
  10^3 has 9  answers
  10^4 has 15 answers
  10^5 has 36 answers
  10^6 has 84 answers

"""
