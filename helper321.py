import time, string
from heapq import *
START = time.time()


def computePath(n):
  # e = empty, r = red, b = blue
  # n % 4 = column, n/4 = row
  startConfig = tuple('r' * n + 'e' + 'b' * n)
  endConfig   = tuple('b' * n + 'e' + 'r' * n)

  # Path Dict fields:
  # shortest path to position
  pathDict              = dict()
  pathDict[startConfig] = 0
  pqueue                = []

  heappush(pqueue, (0,startConfig))

  def insertIntoDict(position, numStepsToPos):
    if position not in pathDict:
      pathDict[position] = numStepsToPos
      heappush(pqueue, (numStepsToPos, position))

  def nextStep(position, move):
    emptySpot     = position.index('e')
    newPosition   = list(position)
    numStepsToPos = pathDict[position]

    newPosition[emptySpot]        = newPosition[emptySpot + move]
    newPosition[emptySpot + move] = 'e'
    newPosition                   = tuple(newPosition)

    insertIntoDict(newPosition, numStepsToPos + 1)

  while len(pqueue) > 0 and endConfig not in pathDict:
    nextPos   = heappop(pqueue)[1]
    emptySpot = nextPos.index('e')
    if emptySpot != 0     : nextStep(nextPos, -1)
    if emptySpot >= 2     : nextStep(nextPos, -2)
    if emptySpot != 2*n   : nextStep(nextPos, 1)
    if emptySpot <= 2*n-2 : nextStep(nextPos, 2)

  return pathDict[endConfig]

for i in xrange(1,20):
  print i, computePath(i)
