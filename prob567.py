import time
from primes import ncr
START    = time.time()
SIZE     = 123456789
MIN_SIZE = 100

def gameA(n):
  return sum([ (1.0 * ncr(n,k)) / k for k in xrange(1,n+1)]) / 2**n

def gameB(n):
  return sum([ (1.0) / (ncr(n,k) * k) for k in xrange(1,n+1)])

totalSum = 0
for i in xrange(1, MIN_SIZE+1):
  totalSum += gameA(i) + gameB(i)

bPrev = gameB(MIN_SIZE)
for n in xrange(MIN_SIZE+1, SIZE+1):
  bPrev = bPrev / 2 + 1. / n
  totalSum += 2 * bPrev

print "Answer:", totalSum
print "Time Taken:", time.time() - START

"""
Game A = sum( ncr(n,k) / k) / 2^n from k = 1 to k = n
Game B = sum( 1.0/(ncr(n,k) *  k))  from k = 1 to k = n

Recurrence relation:
  A(n) = A(n-1)/2 + 1/n - 1/(2^n * n)
  B(n) = B(n-1)/2 + 1/n

Given the recurrence relation, it's pretty easy to compute the next step for A and B.

As per problem 568, it's easy to see that A(n) and B(n) converge as n gets larger, which means we can save some work and just compute B(n) and double it.


11:00 EST started problem
11:20 EST figured out dumb slow way of doing problem
12:31 EST Figured out B(n) = B(n-1)/2 + 1/n
12:35 EST SOLVED IT YEAH

https://oeis.org/search?q=1%2C2%2C5%2C16%2C64%2C312

Congratulations, the answer you gave to problem 567 is correct.
You are the 9th person to have solved this problem.

jchen@jchen-mbp 9:36:22 ~/Developer/proj_euler(master) % pypy -i prob567.py
Answer: 75.448175347
Time Taken: 1.1519742012

cacheA = {1 : 0.5}
def gameA(n):
  if n in cacheA:
    return cacheA[n]
  cacheA[n] = gameA(n-1) / 2 + 1. / n - 1./ (2**n * n)
  return cacheA[n]

cacheB = {1: 1.0}
def gameB(n):
  if n in cacheB:
    return cacheB[n]
  cacheB[n] = gameB(n-1) / 2 + 1. / n
  return cacheB[n]

"""
