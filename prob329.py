import time
start = time.time()
from bitarray import bitarray

def gcd(a,b):
        if a == 0:
                return b
        return gcd(b%a,a)

primes = bitarray('11'+'0' *499)
for i in xrange(2,501):
        if primes[i] == 0:
                for j in xrange(2*i,501,i):
                        primes[j] = 1


seq = bitarray('000011000100101')
squares = [0] + [1] * 500
new = [0] * 501
div = 3**15 * 500 * 2**15


for i in xrange(0,15):
        new[1] = squares[2]
        new[500] = squares[499]
        for j in xrange(2,500):
                new[j] = squares[j-1] + squares[j+1]

        for j in xrange(1,501):
                if seq[i] == primes[j]:
                        new[j] *= 2
        squares = new[:]
        new = [0]*501

a = sum(squares)
shared = gcd(a,div)
a,div = a/shared, div/shared
print str(a) + '/' + str(div)

print "Time Taken:", time.time() - start

