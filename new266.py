import time
from primes import primes, factor
import math

START           = time.time()
MOD             = 10**16
prime_list      = primes[:42][::-1]
precision       = 141230
primeLogNoRound = [math.log(p, 10) * precision for p in prime_list]
limit           = sum(primeLogNoRound) / 2
primeLog        = [int(p) for p in primeLogNoRound]

seenBefore = dict()
def recurse(index, rollingSum, best=[]):
  if (index, rollingSum) in seenBefore:
    return seenBefore[(index, rollingSum)]

  if sum( primeLogNoRound[i] for i in best) > limit:
    return (0, [])

  if index >= len(primeLog):
    return (rollingSum, best)

  recurse1 = recurse(index+1, rollingSum + primeLog[index], best + [index])
  recurse2 = recurse(index+1, rollingSum, best)

  if sum(primeLogNoRound[i] for i in recurse1[1]) > sum(primeLogNoRound[i] for i in recurse2[1]):
    seenBefore[(index, rollingSum)] = recurse1
  else:
    seenBefore[(index, rollingSum)] = recurse2

  return seenBefore[(index, rollingSum)]

print "limit:", limit
result = recurse(0, 0, [])

print "result:", result[0]

print "primes used:", [prime_list[i] for i in result[1]]

print reduce(lambda x,y: x * y % MOD, [prime_list[i] for i in result[1]])

print "Time Taken:", time.time() - START
