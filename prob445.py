#NOTE TODO need to solve it
import time
from primes import m_r, pfactor_gen, factor_given_pfactor, ext_gcd
START = time.time()
SIZE  = 10**7
MOD   = 10**9 +7


pfactor = pfactor_gen(SIZE)

def factor(n):
  return factor_given_pfactor(n, pfactor)

def multInverse(n, mod):
  return ext_gcd(n, mod)[0] % mod

def addToDict(valDict, key, value):
  if key in valDict:
    valDict[key] += value
    if valDict[key] == 0:
      del valDict[key]
  else:
    valDict[key] = value

valDict = {}
count   = 0
prod    = 1

for n in xrange(1,SIZE/2+1):
  changes  = dict()

  # Add on the factors from the top
  for f in factor(SIZE-n+1):
    addToDict(changes, f, 1)

  for f in factor(n):
    addToDict(changes, f, -1)

  for f in changes.keys():
    if f in valDict:
      prod = multInverse(1 + pow(f, valDict[f], MOD), MOD) * prod % MOD
      if valDict[f] + changes[f] != 0:
        prod = (1 + pow(f, valDict[f] + changes[f], MOD)) * prod % MOD
    else:
      prod = (1 + pow(f, changes[f], MOD)) * prod % MOD

  for f in changes.keys():
    addToDict(valDict, f, changes[f])

  # The cases for n are symmetric, so only do half the work

  count = (count + prod*2) % MOD

  # Progress counter
  if n% 1024 == 0:
    print n, time.time() - START

count -= prod # We don't want to count the middle case twice!

# accounting for the sum of the numbers themselves
count = (count - pow(2,SIZE,MOD)+2) % MOD

print "Answer is:", count
print "Time Taken:", time.time() - START


"""
The number of retractions that a certain base has is equal to the sum of its divisors, excluding itself.

Sum of divisors is (1+p1^k1) * (1+p2^k2) * (1 + pm^km)

ax + b = a(ax+b) + b mod n
a^2 = a mod n
ab  = 0 mod n

ex: 6x + 5 mod 15
-> 6(6x + 5) + 5 mod 15 = 36x + 35 mod 15 = 6x + 5


Congratulations, the answer you gave to problem 445 is correct.
You are the 212th person to have solved this problem.

Answer is: 659104042
Time Taken: 49.5843429565
Time Taken: 40.5066130161 Minor optimizations
Time Taken: 39.6483750343 Printing every 1024 instead of every 100




"""
