import time
from primes import m_r
from math import log

START = time.time()

def primeGen(size): #for each number n, return some factor of it.
  primes = [2]
  smallestPrimeFactor = [0,1,2] + [1,2] *(size/2-1)
  for i in xrange(3,size,2):
    if smallestPrimeFactor[i] == 1:
      primes.append(i)
      for j in xrange(i**2,size,i*2):
        smallestPrimeFactor[j] = i
      smallestPrimeFactor[i] = i
  return primes

def primeProof(n):
  for digit in xrange(1,int(log(n,10))+2):
    relevantDig = n % 10**digit - (n % 10** (digit-1))
    m           = int(n - relevantDig)
    digitChange = 10**(digit-1)
    for i in xrange(0, 10):
      if m_r(m + i* digitChange):
        return False
  return True


primes = primeGen(10**5*2)
squbes = []

for i in primes:
  for j in primes:
    if i == j:
      continue
    sqube = i**2 * j**3
    if str(sqube).find('200') != -1:
      if primeProof(sqube):
        squbes.append(sqube)

print sorted(squbes), len(squbes)
if len(squbes) > 199:
  print squbes[199]
print "Time taken:", time.time() - START
