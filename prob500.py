import time
import math
from Queue import PriorityQueue as pq

START   = time.time()
SIZE    = 10**7
NUM_DIV = 500500
MOD     = 500500507

def pfactor_gen(size): #for each number n, return some factor of it.
  primes = [2]
  stuff  = [0,1,2] + [1,2] *(size/2-1)
  for i in xrange(3,size,2):
    if stuff[i] == 1:
      primes.append(i)
      for j in xrange(i**2,size,i*2):
        stuff[j] = i
      if len(primes) > 500500:
        break
  return primes

primes   = pfactor_gen(SIZE)
divisors = pq()

solution = 1

for prime in primes:
  divisors.put(prime)

for i in range(NUM_DIV):
  num      = divisors.get()
  solution = (num * solution) % MOD
  if num < SIZE:
    divisors.put(num**2)

print solution
print "Time Taken:", time.time() - START


"""
Answer    : 35407281
Time Taken: 8.43801283836

Easy problem haha. The thing to note for this is that the number of factors that a number of the form p1^q1 * p2^q2 * ... pn^qn is: (1+q1)(1+q2)...(1+qn).

Then the powers that we need are one less than a power of 2. For each prime, 'p' increases the number of factors by 2x, 'p^3' by 4x, 'p^7' by 8x, and etc.

Then we just keep adding on the smallest factor that will increase the number of divisors by a power of two until we're done.

"""
