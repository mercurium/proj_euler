import time
from bitarray import bitarray
from math import log
START = time.time()

SIZE = 10

def digitalRoot(n):
    while n >= 10:
        n = sum([int(x) for x in str(n)])
    return n

primalityList = bitarray('0' * (SIZE*11))
for i in xrange(2,len(primalityList)):
    if primalityList[i] == 0:
        for j in xrange(i**2, len(primalityList), i):
            primalityList[j] = 1
primes = []
for i in xrange(2,len(primalityList)):
    if len(primes) == SIZE:
        break
    if primalityList[i] == 0:
        primes.append(i)
composites = []
for i in xrange(2,len(primalityList)):
    if len(composites) == SIZE:
        break
    if primalityList[i] == 1:
        composites.append(i)

primes = [digitalRoot(prime) for prime in primes]
composites = [digitalRoot(c) for c in composites]

cachedResult = dict()
def findShortestInt(primeIndex, compositeIndex):
    """If already computed, don't recompute"""
    if (primeIndex, compositeIndex) in cachedResult: 
        return cachedResult[primeIndex, compositeIndex]

    """If we've put all the prime digits down, put the composite digits now"""
    if primeIndex == SIZE: 
        answer = 0
        for i in xrange(compositeIndex, SIZE):
            answer *= 10
            answer += composites[i]
        cachedResult[primeIndex, compositeIndex] = answer
        return answer

    """If we've put all the composite digits down, put the prime digits down now"""
    if compositeIndex == SIZE: 
        answer = 0
        for i in xrange(primeIndex, SIZE):
            answer *= 10
            answer += primes[i]
        cachedResult[primeIndex, compositeIndex] = answer
        return answer

    """If both upcoming digits are the same, there's no reason to put any other digit."""
    if primes[primeIndex] == composites[compositeIndex]:
        answer = findShortestInt(primeIndex+1,compositeIndex+1)
        answer += primes[primeIndex] * 10**(int(log(answer,10)+1))

        cachedResult[primeIndex, compositeIndex] = answer
        return cachedResult[primeIndex, compositeIndex]

    """Otherwise, we should use dynamic programming to return the result with the lowest cost"""
    goPrime = findShortestInt(primeIndex+1, compositeIndex) 
    goPrime += primes[primeIndex] * 10** int(log(goPrime,10)+1)

    goComposite = findShortestInt(primeIndex, compositeIndex+1) 
    goComposite += composites[compositeIndex] * 10**int(log(goComposite,10)+1)

    cachedResult[primeIndex, compositeIndex] =  min(goPrime, goComposite)
    return cachedResult[primeIndex, compositeIndex]

for primeIndex in xrange(SIZE,0,-1):
    print primeIndex
    for compositeIndex in xrange(SIZE,0,-1):
        findShortestInt(primeIndex, compositeIndex)

print findShortestInt(0,0) #% (10**9+7)


print "Time Taken:", time.time() - START
