import time, math
from primes import *
START = time.time()

def iterate(lst, pos):
  toPlace = lst[pos]
  lst[pos] = 0
  for spot in xrange(pos+1, pos+toPlace+1):
    lst[spot % len(lst)] += 1
  return (pos + toPlace) % len(lst)

def getSteps(size):
  if size == 1:
    return 0
  lst   = [0,2] + [1] * (size - 2)
  steps = 1
  pos   = 1
  while lst != [1] * size:
    steps += 1
    pos = iterate(lst, pos)
  return steps



diffs = dict()
prev  = 0
for i in xrange(1,257):
  gs   = getSteps(i)
  gs1  = prev
  diff = gs - gs1
  print i, gs, diff
  diffs[diff] = diffs.get(diff,0) + 1
  prev = gs

print "\n\n"
for key in sorted(diffs.keys()):
  print key, diffs[key]

