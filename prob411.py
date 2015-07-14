import time
from bisect import bisect_right
START = time.time()

def getLongestPath(size):
  funcStart = time.time()
  points = set()
  newPoint = (1,1)
  for i in xrange(0, 2 * size + 1):
    newPoint = ( (newPoint[0] * 2) % size, (newPoint[1] * 3) % size)
    if newPoint in points:
      break
    points.add(newPoint)

  points      = [tup[1] for tup in sorted(points)]
  longestPath = [0]

  sortTime = time.time() - funcStart
  print "Sort time:", sortTime

  for point in points:
    insertionPoint = bisect_right(longestPath, point)
    if insertionPoint == len(longestPath):
      longestPath.append(point)
    else:
      longestPath[insertionPoint] = point

  print "computeTime:", time.time() - funcStart - sortTime

  return len(longestPath)-1

sumz = 0
for i in xrange(1,31):
  newLongestPath = getLongestPath(i**5)
  sumz          += newLongestPath
  print "The longest path for size", i, "was:", newLongestPath
  print "Time Taken:", time.time() - START

print "The overall answer was:", sumz
print "Time Taken:", time.time() - START


"""

The overall answer was: 9936352
Time Taken: 824.641003132
Time Taken: 376.311254025 (This was done after realizing that the sort time was taking way longer than the compute time)
Time Taken: 306.173972845 (Computing the next point cummulatively instead of stupid stuff like (pow(2,i,size),pow(3,i,size))

Congratulations, the answer you gave to problem 411 is correct.

You are the 338th person to have solved this problem.

Okay, cool. For this problem, I first computed all the points that were relevant, sorted them by their x-coordinate, seeing the longest subsequence of length k (for k = 1 to as long as k could go).

With each additional point, it could either lower the max size required for a sequence, or it could extend a sequence. Each additional point made exactly one change, and at the end, the array would have a list of the minimum value needed at the end for a run of length k. Returning the length of the array would then give the longest possible run.

I realized after timing each step that the setup step (sorting /computing points) was way slower than the actual algorithm for computing the answer. Given that the sort is (n log n), while each step in the algorithm is log(k), and k grows slowly, the actual algorithm does much better than n log(k). Thus, there needs to be work done to optimize the sort to make this go faster

"""
