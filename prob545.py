import time
from primes import get_primes, divisors, m_r
START  = time.time()
SIZE   = 10**6 * 5
LIM    = 10**5
primes = get_primes(SIZE)

div308  = divisors(308)
results = []

for p in primes:
  if len(results) > LIM: break
  if not any( [ m_r(div * p +1) for div in div308]):
    results.append(p)

print results[LIM-2] * 308, len(results)

for repetition in xrange(10):

  resultSet = set(results)
  for index, a in enumerate(results):
    if a * results[0] > results[LIM]: break

    for bIndex in xrange(index+1):
      b = results[bIndex]
      p = a*b

      if a*b > results[LIM]: break
      if not any( [ m_r(div * p +1) for div in div308]):
        if len(filter(lambda x: x not in resultSet, divisors(p)[1:-1])) == 0:
          resultSet.add(p)

  if len(results) == len(resultSet):
    break
  results = sorted(resultSet)
  print results[LIM-2] * 308, len(results)

print "Answer:", results[LIM-2] * 308
print "Time Taken:", time.time() - START

"""

Congratulations, the answer you gave to problem 545 is correct.

You are the 261st person to have solved this problem.


Answer     : 921107572
Time Taken : 3.92793607712



f(n) = 1 if n % 2 == 1
f(n) = product of all primes for which (p-1)|n
f(n/k) | f(n)

f(n) = 20010 -> n = 308 * prime

if f(a*308) works, and f(b*308) works, then maybe f(a*b*308) works too

20010 = 2 * 3 * 5 * 23 * 29
lcm(p-1) for p|20010 = 308

10^5: 11
10^6: 95
10^7: 1068

7,11,13,17,19
31,37,



"""
