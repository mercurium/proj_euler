import time, math
from fractions import Fraction
from itertools import permutations
START = time.time()
SIZE  = 10

def addToDict(values, value):
  if value in values:
    values[value] += 1
  else:
    values[value] = 1

maps = dict()
def computeAverage(size):
  count  = 0
  values = dict()
  for lst in permutations(range(1,1+size)):
    lst         = list(lst)
    local_count = 0
    while lst != range(1,1+size):
      for i in xrange(0, len(lst) - 1):
        if lst[i] > lst[i+1]: # list is out of order.
          # doing first sort
          oldlst       = lst
          lst          = [lst[i+1]] + lst[:i+1] + lst[i+2:]
          local_count += 1
          maps[tuple(oldlst)] = lst
          break
    addToDict(values, local_count)
    count += local_count

  counts = [values[i] for i in xrange(0, 2**(size-1))]
  print Fraction(count, math.factorial(size))
  print counts[:2**(size-2)]
  print counts[2**(size-2):]


computeAverage(4)
for key in maps:
  print key, "-->", maps[key]

#for i in xrange(2, SIZE+1):
#  print i
#  computeAverage(i)

print "Time Taken:", time.time() - START



"""
123 = 0
132 -> 213 -> 123 = 2
213 -> 123 = 1
231 -> 123 = 1
312 -> 132 -> 213 -> 123 = 3
321 -> 231 -> 123 = 2


"""
