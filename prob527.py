import time, math
START = time.time()
SIZE  = 10**10

def costBinary(n):
  cost = 0
  numRemaining = n
  for i in xrange(1,int(math.log(n,2)+3)):
    numToRemove   = min(2**(i-1), numRemaining)
    cost         += numToRemove * i
    numRemaining -= numToRemove
  return cost * 1.0 / n

def costRandom(n):
  cost = 0
  for i in xrange(2,n+2):
    cost += 1.0 / i
  cost = 2 * ((n+1.0)/n) * cost - 1
  return cost

randomCost = costRandom(SIZE)
print randomCost, costBinary(SIZE), randomCost - costBinary(SIZE)

print "Time Taken:", time.time() - START

"""
44.2061331947 32.2820130851 11.9241201096
Time Taken: 154.49310708 (used pypy)
Time Taken: 45.4874811172 (removed the mod print statements... wtf)

"""
