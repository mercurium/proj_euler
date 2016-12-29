#NOTE TODO need to solve it
import time
from primes import *

START  = time.time()
SIZE   = 3800
primes = get_primes(SIZE)
count  = 0

for p in primes:
  for A in xrange((p-1)//2+1, p*10):
    B = abs(A - p)
    if gcd(A,B) != 1:
      continue
    for index in xrange(len(primes)):
      if A*B % primes[index] != 0:
        break
    if A-B > primes[index]**2:
      continue
    if A+B > primes[index]**2 and A < p:
      continue
    count += A
    print p, A, B, factor(A), factor(B)
    break

print count
print "Time Taken:", time.time() - START
