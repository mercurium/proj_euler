import time
from bitarray import bitarray
from math import log
START = time.time()

SIZE = 10**3

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
cachedResult = [ [0] * (SIZE+1) for i in [0,0]]
def findShortestInt(primeIndex, compositeIndex):

    if primeIndex == SIZE and compositeIndex == SIZE:
        return 0

    """If we've put all the prime digits down, put the composite digits now"""
    if primeIndex == SIZE: 
        answer = cachedResult[primeIndex %2][compositeIndex+1]
        if answer == 0:
            answer = composites[compositeIndex]
        else:
            answer += composites[compositeIndex] * 10**int(log(answer,10)+1)
        cachedResult[primeIndex%2][ compositeIndex] = answer
        return answer

    """If we've put all the composite digits down, put the prime digits down now"""
    if compositeIndex == SIZE: 
        answer = cachedResult[(primeIndex+1)%2][compositeIndex]
        if answer == 0:
            answer = primes[primeIndex]
        else:
            answer += primes[primeIndex] * 10** int(log(answer,10)+1)
        cachedResult[primeIndex%2][ compositeIndex] = answer
        return answer

    """If both upcoming digits are the same, there's no reason to put any other digit."""
    if primes[primeIndex] == composites[compositeIndex]:
        answer = cachedResult[(primeIndex+1)%2][compositeIndex+1]
        answer += primes[primeIndex] * 10**(int(log(answer,10)+1))

        cachedResult[primeIndex%2][compositeIndex] = answer
        return answer

    """Otherwise, we should use dynamic programming to return the result with the lowest cost"""
    goPrime = cachedResult[(primeIndex+1)%2][compositeIndex]
    goPrime += primes[primeIndex] * 10** int(log(goPrime,10)+1)

    goComposite = cachedResult[primeIndex%2][compositeIndex+1]
    goComposite += composites[compositeIndex] * 10**int(log(goComposite,10)+1)

    answer = min(goPrime, goComposite)
    cachedResult[primeIndex%2][compositeIndex] =  answer
    return answer

for primeIndex in xrange(SIZE,-1,-1):
    print primeIndex, time.time() - START
    for compositeIndex in xrange(SIZE,-1,-1):
        findShortestInt(primeIndex, compositeIndex)

print cachedResult[0][0] % (10**9+7)


print "Time Taken:", time.time() - START
