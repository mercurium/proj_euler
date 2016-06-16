import time, math
from primes import get_primes
START         = time.time()
SIZE          = 10**6
MAX_THREE_POW = int(math.log(SIZE,3))+1

primes = get_primes(SIZE)

def incrValDict(valDict, value):
  if value in valDict:
    valDict[value] += 1
  else:
    valDict[value] = 1

values = dict()
def recurse(threePow, twoPow, runningSum):
  if threePow >= MAX_THREE_POW:
    incrValDict(values, runningSum)
    return

  for i in xrange(0, twoPow):
    nextPartitionItem = 2**i * 3**threePow
    if nextPartitionItem + runningSum > SIZE:
      break
    recurse( threePow +1, i, runningSum + nextPartitionItem)
  recurse(threePow +1, twoPow, runningSum)


recurse(0, int(math.log(SIZE, 2) + 1), 0)

sumz = 0
for p in primes:
  if p in values and values[p] == 1:
    sumz += p

print sumz
print "Time Taken:", time.time() - START

"""
Congratulations, the answer you gave to problem 333 is correct.

You are the 610th person to have solved this problem.

3053105
Time Taken: 69.4968202114

For this problem, valid solutions have partitions of the form 2^i * 3^j, and all numbers in the partition have the trait that i1 > i2 iff j1 < j2. Then, this means that we just need to find all possible decreasing subsequences and we get our answer.

"""
