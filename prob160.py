import time
START = time.time()
from math import factorial as fact

POWER   = 12
MOD_POW = 5
MOD     = 10**MOD_POW
MOD5    = 5 **MOD_POW
SIZE    = 10**POWER

def fa(num, ignore10=False, ignore2Pow=False):
  prod      = 1
  twoCount  = 0
  for i in xrange(1, num + 1):
    if ignore10 and i % 10 == 0:
      continue
    number = i
    while number % 5 == 0:
      number    /= 5
      twoCount  -= 1
    while number % 2 == 0:
      number    /= 2
      twoCount  += 1
    prod = prod * number % MOD

  if not ignore2Pow:
    prod = prod * 2**twoCount % MOD
  return prod

#second parameter is for if we want to ignore the multiples of 5
def fa5(n, ignore5=False):
  if n == 0 or n == 1:
    return 1
  prod = 1
  for i in xrange(2,n+1):
    number = i
    while number % 5 == 0:
      number    /= 5
    prod = prod * number % MOD5
  return prod

print fa5(5**3)
print fa5(5**2,True)**5 * fa5(5**2, False) % MOD5

print "Time Taken:", time.time() -START



"""
"""
