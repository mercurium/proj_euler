import time
start = time.time()
from bitarray import bitarray

SIZE = 500

def gcd(a,b):
        if a == 0:
                return b
        return gcd(b%a,a)

primes = bitarray('11'+'0' *(SIZE-1))
for i in xrange(2,501):
        if primes[i] == 0:
                for j in xrange(2*i,(SIZE+1),i):
                        primes[j] = 1


seq = bitarray('000011000100101')
squares = [0] + [1] * SIZE 
new = [0] * (SIZE+1)
div = 3**15 * SIZE * 2**15


for i in xrange(0,15):
        new[1] = squares[2]
        new[SIZE] = squares[SIZE-1]
        for j in xrange(2,SIZE):
                new[j] = squares[j-1] + squares[j+1]

        for j in xrange(1,SIZE+1):
                if seq[i] == primes[j]:
                        new[j] *= 2
        squares = new[:]
        new = [0]*(SIZE+1)

a = sum(squares)
shared = gcd(a,div)
a,div = a/shared, div/shared
print str(a) + '/' + str(div)

print "Time Taken:", time.time() - start

