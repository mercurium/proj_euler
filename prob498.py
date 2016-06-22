import time, math
from primes import ncr, ext_gcd

START = time.time()
MOD   = 10**9 - 63

def coefficient(n, m, d):
  numerator = faMod(n / MOD, MOD) * faMod(n % MOD, MOD)
  denom     = (n-d) * faMod(d, MOD) \
                * faMod((n-m)/MOD, MOD) * faMod((n-m)% MOD, MOD) \
                * faMod((m-d-1)/MOD, MOD) * faMod((m-d-1) % MOD, MOD)

  return (numerator * ext_gcd(denom, MOD)[0]) % MOD

def faMod(n, modNum):
  prod = 1
  for i in xrange(2,n+1):
    prod = prod * i % MOD
  return prod

print "Answer:", coefficient(10**13, 10**12, 10**4)
print "Time Taken:", time.time() - START



"""
Answer = n! / ( (n-m)! * (m-1-d)! * (n-d))

Congratulations, the answer you gave to problem 498 is correct.

You are the 274th person to have solved this problem.

Answer: 472294837
Time Taken: 0.0224871635437

"""
