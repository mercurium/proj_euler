#NOTE TODO need to solve it
import time
from primes import ext_gcd, get_primes, m_r, ncr, multInverse
START = time.time()

A = 10**6
B = 10**3
K = 10**3

def d(p,n):
    return multInverse(n, p)

def dFast(p, k):
    sumz = 0
    for m in xrange(k+1, p-1):
        sumz += ncr(m-1, k) * multInverse(m, p) % p
    return sumz % p

def D(a,b,k):
    sumz = 0
    for p in xrange(a,a+b):
        if m_r(p):
            inv = [0] + [ multInverse(x,p) for x in xrange(1, p)]
            tempSum    = 0
            rollingNcr = 1
            for i in xrange(p-1,k-2,-1):
                index      = p - i
                tempSum   += inv[i] * rollingNcr
                rollingNcr = (rollingNcr * (k + index - 1) * inv[index]) % p
            sumz += tempSum % p
            print p, tempSum % p
    return sumz

print D(A,B,K)
print "Time Taken:", time.time() - START

"""
Time Taken: 49.0069141388 on D(10^6, 10^3, 10^3) Rip... too slow @_@

d(p,p-1,k) = sum( ncr(m-1,k) * m^-1 from m = k to m = p-1)

"""
