import time
from primes import *

START   = time.time()
SIZE    = 10**6

# This function is currently very slow for numbers with lots of factors =/
def practical_check(n):
  sumz     = 0
  for div in sorted(divisors(n)):
    if div - 1 > sumz:
      return False
    sumz += div
  return True
pc = practical_check

print "Time Taken:", time.time() - START


count = 0

for n in xrange(20,SIZE-9,20):
  if mr(n-9) and mr(n-3) and mr(n+3) and mr(n+9):
    count += 1
    print n-9, n-3,n+3,n+9
#    if all([pc(k) for k in xrange(n-8,n+9,4)]):
#      print "ANSWER:", n-8, n-4, n, n+4,n+8
#      print [factor(k) for k in xrange(n-8,n+9,4)]
print count

for n in xrange(12,SIZE-9,4):
  if all([pc(k) for k in xrange(n-8,n+9,4) ]):
    print n-8,n-4,n,n+4,n+8
    #print [factor(k) for k in xrange(n-8,n+9,4)]

#for n in xrange(20,SIZE-9,20):
#  if n % 7 not in [1,6]:
#    continue
#  if all([pc(k) for k in xrange(n-8,n+9,4) ]):
#    print n-8,n-4,n,n+4,n+8
#    print [factor(k) for k in xrange(n-8,n+9,4)]


print "Time Taken:", time.time() - START

