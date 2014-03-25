import math, time
from bitarray import bitarray

START = time.time()
SIZE = 20

#Find the number of semiprimes less than size. 
def findNumSemiprimes(size):
    numSemiprimes = 0 
    isPrime1 = bitarray(SIZE) #(0,0) = untouched. (0,1) = one prime so far
    isPrime2 = bitarray(SIZE) #(1,0) = two primes, (1,1) = more than two distinct prime factors

    for i in xrange(SIZE): #sadly, need to do this to avoid running low on memory
        isPrime1[i] = 0
        isPrime2[i] = 0 

    def getVal(i):
        return isPrime1[i]*2+isPrime2[i]
    def setVal(i, val):
        if val > 3:
            val = 3
        isPrime1[i] = val/2
        isPrime2[i] = val%2

    for i in xrange(2,SIZE):
        if getVal(i) == 2:
            numSemiprimes+=1
        elif getVal(i) == 0:
            for j in xrange(2*i,SIZE,i):
                setVal(j, getVal(j)+1)
        else:
            pass #We don't care about the number if it's not a semiprime or a prime
    return numSemiprimes

answer = findNumSemiprimes(SIZE)
print "The answer is:", answer
print "Time Taken:", time.time() - START


#Since we have four states to deal with, prime, notseen yet, 2 distinct factors, and more than two distinct factors, we need two bits per number to store them. This unfortunately requires two bitarrays instead of one, but at least the memory cost is relatively cheap.
