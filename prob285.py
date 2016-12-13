import time
START = time.time()
LIM   = 10
STEP  = 10**6


score = 0
for k in xrange(1,LIM+1):
  for a in xrange(0,STEP):

    upperBound  = max((k+.5)**2 - (k*a * 1.0/STEP + 1)**2, 1)
    lowerBound  = max((k-.5)**2 - (k*a * 1.0/STEP + 1)**2, 1)

    bUpper      = (upperBound**.5 - 1)
    bLower      = (lowerBound**.5 - 1)

    score      += (bUpper - bLower) / STEP

print score
print "Time Taken: ", time.time() - START

"""
integrate over two variables?

int(

    if int(.5 + ((k * a / 1000. + 1)**2 + (k * b / 1000. + 1)**2)**.5) == k:
      score += k / (1001.)**2

"""
