import time
from primes import get_primes

START  = time.time()
SIZE   = 10**5 * 25
primes = get_primes(SIZE * 40)
coords = [(primes[0], primes[0])]

print "Time Taken:", time.time() - START

for i in xrange(1, SIZE):
  coords.append( (coords[-1][0] + primes[2*i] + primes[2*i-1], \
                  coords[-1][1] + primes[2*i] - primes[2*i-1]) \
                  )

totalCount = 1
maxDiff    = 10
for currentPeakIndex in xrange(1, SIZE):
  if currentPeakIndex % 10** 5 == 0:
    print currentPeakIndex, time.time() - START
  currentPeak = coords[currentPeakIndex]
  peakCount = 0
  viewAngle = 1
  for prevPeakIndex in xrange(currentPeakIndex - 1, currentPeakIndex - min(currentPeakIndex, maxDiff * 2),-1):
    prevPeak = coords[prevPeakIndex]
    nextAngle = (1.0 * currentPeak[1] - prevPeak[1]) / (currentPeak[0] - prevPeak[0])
    if nextAngle < viewAngle:
      peakCount +=1
      viewAngle = nextAngle
      maxDiff   = max(currentPeakIndex - prevPeakIndex, maxDiff)
  totalCount += peakCount

print totalCount, maxDiff
print "Time Taken:", time.time() - START


"""
Congratulations, the answer you gave to problem 569 is correct.

You are the 160th person to have solved this problem.


Answer: 21025060
Time Taken: 1258.95616102


"""
