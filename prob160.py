import time
START = time.time()
from math import factorial as fact, log
from primes import crt, ext_gcd

POWER   = 12
MOD_POW = 5
MOD5    = 5**MOD_POW
MOD2    = 2**MOD_POW
MOD     = 10**MOD_POW
SIZE    = 10**POWER

def faMod(n, modNum, ignoreModNum=False):
  if n == 0 or n == 1:
    return 1
  prod = 1
  for i in xrange(2,n+1):
    number = i
    if number % modNum == 0 and ignoreModNum:
      continue
    while number % modNum == 0:
      number    /= modNum
    prod = prod * number % (modNum ** MOD_POW)
  return prod

# find the largest power of 5 that SIZE divides
fivePow     = sum([SIZE/5**x for x in xrange(1,int(log(SIZE,5))+1)])

# solution  = b * k + 3125 * m, where b * k + 3125 * m = 0 mod 32, finding m
# b is 2^(-fivePow) mod 3125

# finding k here:
fiveMod     = faMod(2**12*5**4,5)

# finding b here:
twoMultiple = pow(2,fivePow, MOD5)
twoInverse  = ext_gcd(twoMultiple, MOD5)[0] % MOD5

# b * k here
numMod5Pow  = fiveMod * twoInverse % MOD5

modPower    = (ext_gcd(MOD5, 2**5)[0] * -1 * numMod5Pow) % MOD2

print "Solution is:", modPower * MOD5 + numMod5Pow
print "Time taken:", time.time() - START

"""
Congratulations, the answer you gave to problem 160 is correct.

You are the 2222nd person to have solved this problem.


jchen@jchen-mbp 17:15:06 ~/Developer/proj_euler(master) % pypy prob160new.py
Solution is: 16576
Time taken: 0.117702960968

Cool things to note:
  If we know what fa(10^12) % 2^5 and fa(10^12) % 5^5 are, we can find fa(10^12) % 10^5.
  Since the power of 2 >>> power of 5 in fa(10^12), we know that fa(10^12) mod 2^10000000 = 0.

  Thus, we just need to compute fa(10^12) % 5^5.
  There's a pretty cool trick though, in that fa(5**k * c) = fa(5**(k-1) * c) mod 5^5, for k >= 5, so we have

  fa(10^12) mod 5^5 = fa(2^12 * 5^4) mod 5^5, which is computable.

  Since I just removed all the powers of 5, I also needed to remove an equivalent number of powers of 2,
    which I just used the extended_gcd algorithm to do.

"""
