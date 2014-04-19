import time
from bitarray import bitarray
START = time.time()
SIZE = 11
MOD = 10**9 + 993

import operator as op
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    num = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return num//denom

pfactor = range(SIZE+1)

for i in xrange(2,SIZE+1):
    if pfactor[i]==i:
        for j in xrange(i**2,SIZE+1,i):
            pfactor[j] = i
pfactor[1] =0

def factor(n):
    factors = []
    while n != 1 and pfactor[n] != n:
        factors.append(pfactor[n])
        n /= pfactor[n]
    return factors

sumz = SIZE
cnr = 1
for r in xrange(0,SIZE/2):
    cnr = (cnr * (SIZE-r))/(r+1)
    prod = 1
    c = cnr
    for i in xrange(1,SIZE+1):
        if pfactor[i] != i:
            sumz += prod
            continue
        while c  % i == 0:
            prod *= i
            c /= i
        sumz += prod
    sumz %= MOD
    print r
            
print (sumz*2) % MOD
print "Time Taken:", time.time() - START
