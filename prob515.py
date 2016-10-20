import time
from primes import ext_gcd, get_primes, m_r, ncr
START = time.time()

A = 10**6
B = 10**3
K = 10**3

def d(p,n):
  return ext_gcd(n,p)[0] % p

def D(a,b,k):
  sumz = 0
  for p in xrange(a,a+b):
    if m_r(p):
      inv = [0] + [ (ext_gcd(x, p)[0]) % p for x in xrange(1, p)]
      tempSum    = 0
      rollingNcr = 1
      for i in xrange(p-1,0,-1):
        index       = p - i
        tempSum    += inv[i] * rollingNcr
        rollingNcr  = (rollingNcr * (k + index - 1)  * inv[index]) % p
      sumz += tempSum % p
      print p, tempSum % p
  return sumz

print D(A,B,K)
print "Time Taken:", time.time() - START

"""
Time Taken: 49.0069141388 on D(10^6, 10^3, 10^3) Rip... too slow @_@

"""
