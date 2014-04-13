import time
from bitarray import bitarray
from math import log
START = time.time()

SIZE = 10**4
MOD = 10**9+7

def digitalRoot(n):
    while n >= 10:
        n = sum([int(x) for x in str(n)])
    return n

primalityList = bitarray('0' * (SIZE*11))
for i in xrange(2,len(primalityList)):
    if primalityList[i] == 0:
        for j in xrange(i**2, len(primalityList), i):
            primalityList[j] = 1
primes = [] #Not the most efficient implementation, but also not the bottleneck so whatever.
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

primes = [digitalRoot(p) for p in primes]
composites = [digitalRoot(c) for c in composites]
cachedResult = [ [ [0,0] ] * (SIZE+1) for i in [0,0]]

def findShortestInt(primeIndex, compositeIndex):

    """After putting down all the digits, we have nothing left"""
    if primeIndex == SIZE and compositeIndex == SIZE: 
        return 0

    """If we've put all the prime digits down, put the composite digits now"""
    if primeIndex == SIZE: 
        answer = cachedResult[primeIndex %2][compositeIndex+1][:] #Using [:] to make sure we get a deep copy, not a shallow one
        answer[1]  = (answer[1] + composites[compositeIndex] * pow(10,answer[0], MOD)) 
        answer[0] +=1 
        cachedResult[primeIndex%2][compositeIndex] = answer
        return answer

    """If we've put all the composite digits down, put the prime digits down now"""
    if compositeIndex == SIZE: 
        answer = cachedResult[(primeIndex+1)%2][compositeIndex][:]
        answer[1]  = (answer[1] + primes[primeIndex] * pow(10,answer[0], MOD)) 
        answer[0] +=1 
        cachedResult[primeIndex%2][ compositeIndex] = answer
        return answer

    """If both upcoming digits are the same, there's no reason to put any other digit."""
    if primes[primeIndex] == composites[compositeIndex]:
        answer = cachedResult[(primeIndex+1)%2][compositeIndex+1][:]
        answer[1]  = (answer[1] + primes[primeIndex] * pow(10,answer[0], MOD))
        answer[0] +=1 

        cachedResult[primeIndex%2][compositeIndex] = answer
        return answer

    """Otherwise, we should use dynamic programming to return the result with the lowest cost"""
    goPrime = cachedResult[(primeIndex+1)%2][compositeIndex][:]
    goPrime[1]  = (goPrime[1] + primes[primeIndex] * pow(10,goPrime[0], MOD)) % MOD
    goPrime[0] +=1 

    goComposite = cachedResult[primeIndex%2][compositeIndex+1][:]
    goComposite[1]  = (goComposite[1] + composites[compositeIndex] * pow(10,goComposite[0], MOD)) %MOD
    goComposite[0] +=1

    if goPrime[0] < goComposite[0]: #Compare number of digits in solution first.
        answer = goPrime
    elif goPrime[0] > goComposite[0]:
        answer = goComposite
    elif primes[primeIndex] < composites[compositeIndex]: #if num digits is the same, compare first digit.
        answer = goPrime
    else:
        answer = goComposite
    cachedResult[primeIndex%2][compositeIndex] =  answer
    return answer

for primeIndex in xrange(SIZE,-1,-1):
    if primeIndex %32 == 0:
        print primeIndex, time.time() - START
    for compositeIndex in xrange(SIZE,-1,-1):
        findShortestInt(primeIndex, compositeIndex)

cachedResult[0][0][1] %= MOD
print cachedResult[0][0][1]
print "Time Taken:", time.time() - START

"""
Main idea of this problem is to find the edit distance between the two long integers. If there's a tie in the size of the edit distance, we want to return the one with a smaller sum.

Currently my bottleneck is having to deal with super large numbers... :/

Okay, so I came up with three methods to solve this problem.
1) Keep track of which sequence to add numbers to the superinteger at each step using two bit arrays, to track the three possibilites
2) Rather than storing a perfect precision number of the sequence, keep it as a double and then just retrace the path afterwards
3) Just keep track of the sum mod 10^9+7 and then since the superinteger is going to be determined by the length of the sequence and the first digit, that's all we need to know.

I went with option 3 since it seemed like the most clear choice, didn't require abstracting away details, and could be implemented as a modification to my existing code rather easily (I changed... 10-15 lines for it?)

Congratulations, the answer you gave to problem 467 is correct.

You are the 46th person to have solved this problem.
Answer is 775181359
Time Taken: 266.975491047 


"""
