#NOTE TODO need to solve it
import time
from primes import get_primes
START = time.time()

g      = 0.0001
n      = 100
primes = get_primes(n)

def splitIntervals(intervals, pos):
  for index,interval in enumerate(intervals):
    if interval[0] < pos < interval[1]:
      if interval[1] - pos > g:
        intervals.append((pos,interval[1]))
      if pos - interval[0] > g:
        intervals[index] = (interval[0],pos)
      else:
        del intervals[index]
      intervals.sort()
      break

for p in primes:
  intervals = [(0,1)]
  for jump in xrange(1, int(10/g)):
    splitIntervals(intervals, ((1./p)**.5 * jump) % 1)
    #print jump, len(intervals), ((1./p)**.5 * jump) % 1
    #print '\t', [(round(x[0],4),round(x[1],4)) for x in intervals]
    if len(intervals) == 0:
      print p, jump
      break
  print "Time Taken:", time.time() - START



print "Time Taken:", time.time() - START
