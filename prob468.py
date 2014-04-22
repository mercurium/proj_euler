import time
from bitarray import bitarray
START = time.time()
SIZE = 11
MOD = 10**9 + 993

pfactor = range(SIZE+1)
for i in xrange(2,SIZE+1):
    if pfactor[i]==i:
        for j in xrange(i**2,SIZE+1,i):
            pfactor[j] = i

def factor(n): #return all the factors of n
    factors = []
    while n > 1 and pfactor[n] != n:
        factors.append(pfactor[n])
        n /= pfactor[n]
    if n > 1:
        factors.append(n)
    return factors

sumz = SIZE
ncrDict = dict()
for r in xrange(0,SIZE/2): #Since ncr is symmetrical, only do half of the work
    """ Adding in the new factors of the next number"""
    for f in factor(SIZE-r):
        if f not in ncrDict:
            ncrDict[f] = 1
        else:
            ncrDict[f] +=1
    """ Removing the factors of the denominator"""
    for f in factor(r+1):
        ncrDict[f] -= 1
        if ncrDict[f] == 0: #We don't want to iterate over lots of 0's
            del ncrDict[f] 

    prod = 1
    for i in xrange(1,SIZE+1):
        if pfactor[i] != i or i not in ncrDict:
            sumz += prod
            if i == 2:
                print "RAWR", i, prod
            continue
        prod *= pow(i, ncrDict[i], MOD)
        sumz += prod
        if i == 2:
            print "RAWR", i, prod
        print SIZE, r, i, prod
    sumz %= MOD
    print r, ncrDict
            
print (sumz*2) % MOD
print "Time Taken:", time.time() - START
