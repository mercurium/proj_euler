import time
from heapq import *
from primes import *
import math

START      = time.time()
#numDefects = 3
#numChips   = 7
numDefects = 2 * 10**4
numChips   = 10**6

# key   : (numDefectsLeft, numChipsLeft)
# value : numRoutes
valDict = { (numChips, numDefects) : 1 }

def insertIntoDict(valDict, key, value, heap):
  if key[0] < 0 or key[1] < 0:
    return

  if key in valDict:
    valDict[key] += value
  else:
    valDict[key] = value
    heappush(heap, (-1 * key[0], key))

heap    = []
heappush(heap, (-1 * numChips, (numChips, numDefects)))

count = 0
while len(heap) > 0:
  item                         = heappop(heap)[1]
  numChipsLeft, numDefectsLeft = item

  insertIntoDict(valDict, (numChipsLeft-1, numDefectsLeft-0), valDict[item], heap)
  insertIntoDict(valDict, \
      (numChipsLeft-1, numDefectsLeft-1), \
      valDict[item] * numDefectsLeft, \
      heap)
  insertIntoDict(valDict, \
      (numChipsLeft-1, numDefectsLeft-2), \
      valDict[item] * ncr(numDefectsLeft, 2), \
      heap)

  count += 1
  if count % 4096 == 0:
    print count, item, math.log(valDict[item], 10)

  if item != (0,0): # this is horribly inefficient. TODO: fix this
    del valDict[item]


print valDict[(0,0)]

print "Time Taken:", time.time() - START
