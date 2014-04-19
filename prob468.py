import time
START = time.time()
SIZE = 11

import operator as op
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    num = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return num//denom

primeChecker = [True] * (SIZE+1)
primes = []
for i in xrange(2,SIZE+1):
    if primeChecker[i] == True:
        primes.append(i)
        for j in xrange(i**2,SIZE+1,i):
            primeChecker[j] = False
primeChecker[1] = False

sumz = 0
for r in xrange(0,SIZE+1):
    cnr = ncr(SIZE,r)
    prod = 1
    for i in range(1,SIZE+1):
        if not primeChecker[i]:
            sumz += prod
            continue
        while cnr  % i == 0:
            prod *= i
            cnr /= i
        sumz += prod
            
print sumz
print "Time Taken:", time.time() - START
