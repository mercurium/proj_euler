import time, math
from primes import get_primes

START        = time.time()
NUM_PRIMES   = 47
LIM          = 10**12 * 2
small_primes = get_primes(NUM_PRIMES)

smooths = set([1])
for p in small_primes:
  next_batch = set( filter(lambda y: y <= LIM, [p * x for x in smooths]))
  smooths.update(next_batch)
  for power in xrange(2, int(math.log(LIM, p))+1):
    next_batch = set( filter(lambda y: y <= LIM, [p * x for x in next_batch]))
    smooths.update(next_batch)

print "Time Taken:", time.time() - START

sumz  = 0
for num in smooths:
  if num+1 in smooths:
    sumz += num

print "Answer is:", sumz
print "Time Taken:", time.time() - START

"""
Congratulations, the answer you gave to problem 581 is correct.

You are the 81st person to have solved this problem.

1502 2227616372734
Time Taken: 12.0912189484

(Cheatingly adjusted my bounds)
1502 2227616372734
Time Taken: 7.02477192879

Kind of sad that I couldn't prove that I had gotten all of them before I had solved the problem


Looks like https://en.wikipedia.org/wiki/St%C3%B8rmer%27s_theorem is relevant

"""
