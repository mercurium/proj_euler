import time
from primes import ext_gcd
START = time.time()
SIZE  = 10**7
MOD   = 10**9+7

squares = set([x**2 for x in xrange(1,int((2*SIZE)**.5 + 1))])

factorials = [1] * (2*SIZE+1)
for i in xrange(2,2*SIZE+1):
  factorials[i] = factorials[i-1] * i % MOD

def ncr(n, r):
  num = factorials[n]
  div = factorials[r] * factorials[n-r]
  num = (num * ext_gcd(div,MOD)[0]) % MOD
  return num

badPoints = set()

for i in xrange(1,int(SIZE**.5)+1):
  for j in xrange(1,i):
    if i**2+j**2 in squares:
      badPoints.add((i**2,j**2))
      badPoints.add((j**2,i**2))

badPoints = sorted(badPoints) + [(SIZE, SIZE)]

paths = dict()
for index in xrange(len(badPoints)):
  point        = badPoints[index]
  paths[point] = ncr(point[0]+point[1], point[0])

  for badPointPrev in badPoints[:index]:
    if badPointPrev[1] > point[1]:
      continue
    paths[point] -= paths[badPointPrev] * \
        ncr(sum(point)-sum(badPointPrev), point[0] - badPointPrev[0])

print paths[(SIZE,SIZE)] % MOD

print "Time Taken:", time.time() - START


"""

299742733
Time Taken: 43.8476760387

Congratulations, the answer you gave to problem 408 is correct.

You are the 361st person to have solved this problem.

A path from A to B that has a middle point C that it can't go through has:
  (# paths from A to C) x (# paths from C to B) that it must exclude.

After you exclude paths through B from A to C, if you want to go from A to D, you can simply consider:
  (paths from A to D) - (paths from B to D) - (paths from C to D)

Yup yup. Since paths from A to B to D are already excluded from B to D, you don't have to do inclusion/exclusion again. Woot! \o/


"""

