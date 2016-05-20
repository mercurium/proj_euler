import time, math, primes
from itertools import combinations as comb
from primes import factor

START      = time.time()
SIZE       = 10**16
prime_num  = [2,3,5,7,11,13,17,19,23,29,31,37,41,43]
answer     = 0
# I don't get why (0,0,0,....) = .5, but it makes the answer consistent
seenBefore = { (): 0.5, (1,) : 1, (1,1): 3 }

def prodPows(powers):
  product = 1
  for index in xrange(len(powers)):
    product *= prime_num[index] ** powers[index]
  return product

def computePow(powers):
  totalVal = 0
  for numElem in xrange(1,len(powers)+1):
    for positions in comb(xrange(len(powers)), numElem):

      # set up the elements that should be subtracted
      positionSpots = [0] * len(powers)
      for num in positions:
        positionSpots[num] = -1

      number = [powers[x] + positionSpots[x] for x in xrange(len(powers))]
      number = tuple(sorted(filter(None, number))[::-1])
      totalVal += 2 * pow(-1, numElem + 1) * seenBefore[number]

  seenBefore[powers] = int(totalVal)
  return totalVal


def getChain(prevEntries):
  # can ignore lists of prime powers that are too big
  if len(prevEntries) > len(prime_num) or \
      prodPows(prevEntries) > SIZE:
    return None

  # no need to recompute powers
  if prevEntries not in seenBefore:
    computePow(prevEntries)

  # add in a new prime factor
  getChain(prevEntries + (1,))

  # always have the prime powers in descending order
  if len(prevEntries) == 1 or prevEntries[-1] < prevEntries[-2]:
    # increment latest prime factor by one
    prevCopy      = prevEntries[:-1] + (prevEntries[-1] + 1,)
    getChain(prevCopy)

def collapseNumIntoFactorPowers(number):
  factors = primes.factor(number)
  powerDict = dict()
  for f in factors:
    try:
      powerDict[f] += 1
    except KeyError:
      powerDict[f] = 1
  return tuple(sorted(powerDict.values()))[::-1]

getChain((1,))

print "Time Taken for part 1:", time.time() - START
chainsSmallEnough = sorted(filter( lambda x: x < SIZE, set(seenBefore.values())))
chainsSmallEnough.pop(0) # derp, pop off that random 0.5 in the set

for chainSetLen in chainsSmallEnough:
  powerOfChainSetLen = collapseNumIntoFactorPowers(chainSetLen)
  if seenBefore[powerOfChainSetLen] == chainSetLen:
    answer += chainSetLen

# lol derp, 1 is excluded earlier
answer += 1


print "Answer:", answer
print "Time Taken:", time.time() - START

"""

Congratulations, the answer you gave to problem 548 is correct.

You are the 219th person to have solved this problem.

jchen@jchen-mbp 14:52:09 ~/Developer/proj_euler(master|●1✚6…) % pypy prob548.py
12144044603581281
Time Taken: 9.50624489784

so this was a pretty sweet problem, and I'm glad I got to solve it.
An interesting first observation that can be made for this problem is that the actual numbers don't matter for the chain length, besides their prime factorization. For example, 12 and 18 have the same number of chains since 12 = 2^2 * 3 and 18 = 2 * 3^2. As a result, we can reduce down the number of cases we need to care about dramatically.

The next observation you can realize is that since we're looking for all g(n) for which g(n) = n, we can first compute all possible g(n) and *then* figure out which ones are equal to n.

Definition: We define f(a,b,c,...) to be the number of chains for a number n = p_0^a * p_1 ^ b * p_2 ^ c * ... (with f(a) = f(a,0,0,0,0,...))

Example: 12 = 2^2 * 3, so 12 => f(2,1)

After this, the next step would be to realize that f(a,b,....) = sum(f(a0,b0,c0,...)) where a0 <= a, b0 <= b, ... and sum(a0,b0,....) < sum(a,b,c,...). This is due to the fact that for any f(a0,b0,...) less than f(a,b,c....) can be used to generate a unique solution based on the number that is right before n. Since this is a bit difficult to explain without an example, here's one below:

  12 = f(2,1)
  Valid chains for 12 are:
  f(1) = 1
  (1,12)      # one solution ending with '1' before going to 12

  f(1) = 1
  (1,2,12)    # one solution ending with '2' before going to 12

  f(1)  = 1
  (1,3,12)    # one solution ending with '3' before going to 12

  f(2)  = 2
  (1,4,12)    # two solutions ending with '4' before going to 12
  (1,2,4,12)

  f(1,1) = 3
  (1,6,12)    # three solutions ending with '6' before going to 12
  (1,2,6,12)
  (1,3,6,12)

  Since the number right before the 'target', in this case 12 can be 1,2,3,4, or 6, we get that:
    g(12) = f(2,1) = f(2,0) + f(1,0) + f(1,1) + f(0,1) + f(0,0) = 2 + 1 + 3 + 1 + 1 = 8 = g(12)

Also, since the entire matrix of prime factors is symmetrical, f(4,3,1) = f(1,3,4) = f(3,1,4), etc.

Beyond that,  we can notice that:
  f(a)   = 2^(a-1)  # This for some reason causes f(0,0,0, ...) to be 0.5. Very weird, but it fits the formula
  f(a,b) = 2(f(a-1, b) + f(a, b - 1) - f(a-1,b-1))

You can figure out the formula for f(a,b) by using the following observation:
  f(a,b) = f(a-1,b) + f(a-2,b) + .... + f(a-1,b-1) + f(a-2,b-1) + ... etc
  But, you remember that f(a-1,b) = f(a-1,b-1) + f(a-1,b-2) + ...
  And so, since f(a-1,b) and f(a,b-1) are sums of most of the table that you need to sum up, you can add them together, then subtract their overlap, aka f(a-1,b-1).

And the three dimensional and higher cases work in exactly the same way; add up the parts that are one less than your current position, and subtract their overlap using the inclusion exclusion principle

At this point, you have all possible g(n) for n < SIZE, and you want to check them to see if any g(n) = n. Easy stuff. Just factor n, plug it in as f(a,b,...), and see if that equals n. If it does, then add it to the running sum, otherwise exclude it. And you're done :)


"""

