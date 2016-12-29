import time
from primes import gcd
START = time.time()
SIZE  = 1000


sumz = 0
for i in xrange(1,int(SIZE**.5)+1):
    sumz += i
    for j in xrange(i+1, SIZE/i+1):
        sumz += gcd(i,j) * 2


print "Answer:", sumz
print "Time Taken:", time.time() - START


"""
def f(n) = sum( gcd(n, d) for d in xrange(1,n+1))

f(p) = 2p - 1 if p is a prime
f(pq)  = (2p-1)(2q-1) if p,q are primes

f(p^2) = p(3p-2) if p is a prime
f(p^3) = p^2(4p-3) if p is a prime

f(p^n) = p^(n-1) * ((n+1)p-n)

f(nm) = f(n) * f(m) if gcd(n,m) = 1


"""
