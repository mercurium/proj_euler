import time
from heapq import *
START = time.time()
MOD   = 10**8 + 7

# e = empty, r = red, b = blue
# n % 4 = column, n/4 = row
startConfig = ('e','r','b','b', \
    'r','r','b','b', \
    'r','r','b','b', \
    'r','r','b','b')

endConfig   = ('e','b','r','b', \
    'b','r','b','r', \
    'r','b','r','b', \
    'b','r','b','r')

# Path Dict fields:
# shortest path to position
# number of shortest paths
# checksum sum of shortest paths
pathDict              = dict()
pathDict[startConfig] = (0,1,[""])
pqueue                = []

heappush(pqueue, (0,startConfig))

def insertIntoDict(position, numStepsToPos, numPathsToPos, routes):
  if position not in pathDict:
    pathDict[position] = (numStepsToPos, numPathsToPos, routes)
    heappush(pqueue, (numStepsToPos, position))
    return True

  dictNumStepsToPos, dictNumPathsToPos, dictRoutes = pathDict[position]
  # Will never be pushing on a shorter path due to the priority queue
  if dictNumStepsToPos < numStepsToPos:
    return False # this is a non optimal way of routing.
  else:
    pathDict[position] = (numStepsToPos, \
                          numPathsToPos + dictNumPathsToPos, \
                          routes + dictRoutes)
    return True

def nextStep(position, action):
  emptyAbsSpot                         = position.index('e')
  emptySpot                            = (emptyAbsSpot / 4, emptyAbsSpot % 4)
  newPosition                          = list(position)
  numStepsToPos, numPathsToPos, routes = pathDict[position]
  routes                               = [route + action for route in routes]

  if action == 'R':
    newPosition[emptyAbsSpot]   = newPosition[emptyAbsSpot-1]
    newPosition[emptyAbsSpot-1] = 'e'

  if action == 'L':
    newPosition[emptyAbsSpot]   = newPosition[emptyAbsSpot+1]
    newPosition[emptyAbsSpot+1] = 'e'

  if action == 'U':
    newPosition[emptyAbsSpot]   = newPosition[emptyAbsSpot+4]
    newPosition[emptyAbsSpot+4] = 'e'

  if action == 'D':
    newPosition[emptyAbsSpot]   = newPosition[emptyAbsSpot-4]
    newPosition[emptyAbsSpot-4] = 'e'

  newPosition = tuple(newPosition)
  insertIntoDict(newPosition, numStepsToPos + 1, numPathsToPos, routes)

def computeChecksum(checksumString):
  checksum = 0
  for letter in checksumString:
    checksum = (ord(letter) + 243 * checksum) % MOD
  return checksum

while len(pqueue) > 0 and endConfig not in pathDict:
  nextPos      = heappop(pqueue)[1]
  emptyAbsSpot = nextPos.index('e')
  emptySpot    = (emptyAbsSpot / 4, emptyAbsSpot % 4)
  if emptySpot[1] != 0: nextStep(nextPos, 'R')
  if emptySpot[1] != 3: nextStep(nextPos, 'L')
  if emptySpot[0] != 3: nextStep(nextPos, 'U')
  if emptySpot[0] != 0: nextStep(nextPos, 'D')

print pathDict[endConfig]
print sum([computeChecksum(checksum) for checksum in pathDict[endConfig][2]])
print "Time Taken:", time.time() - START

"""
There's only nCr(16,8) * 8 possible arrangements here. Think it should be pretty easy to DP through.


Congratulations, the answer you gave to problem 244 is correct.

You are the 905th person to have solved this problem.


jchen@jchen-mbp 18:06:48 ~/Developer/proj_euler(master) % pypy prob244.py
(32, 1, ['LLURRDLLLURRDLUURULDLURDRRULDDRD'])
96356848
Time Taken: 1.60516309738



"""
