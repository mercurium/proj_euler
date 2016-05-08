import time, math
START = time.time()
SIZE  = 1001
LIM   = 10**12

#the way to get the next item in the list is such:
# A' = a*B -A
# B' = (d-A'*A')/B
# a' = int((math.sqrt(d)+A')/B')
def transform(A,B,a,d):
  A = a*B-A
  B = (d-A*A)/B
  a = int((math.sqrt(d)+A)/B)
  return [A,B,a]

def transformTuples(tuples,d):
  A,B,a = tuples
  return transform(A,B,a,d)

def computeDenom(inputs):
  denom = [1,inputs[-1][2]]
  for denom_val in inputs[-2:0:-1]:
    denom.append(denom[-1] * denom_val[2] + denom[-2])
  return denom[-1]



denom_sum = 0
for d in xrange(2,SIZE):
  if int(math.sqrt(d+.2))**2 == d: #skipping squares
    continue

  inputs = [(0,1,int(math.sqrt(d)))]
  for i in xrange(1000):
    nextVals  = transformTuples(inputs[-1], d)
    nextDenom = computeDenom(inputs + [nextVals])
    if nextDenom > LIM:
      currentDenom = nextDenom
      inputs[-1][2] += 200
      while nextDenom > LIM:
        inputs[-1][2] -=  1
        nextDenom = computeDenom(inputs)
      break
    inputs.append(nextVals)

  nextDiff    = int(nextDenom * math.sqrt(d) + .1) * 1.0 / nextDenom - math.sqrt(d)
  currentDiff = int(currentDenom * math.sqrt(d) + .1) * 1.0 / currentDenom - math.sqrt(d)

  if abs(nextDiff) < abs(currentDiff):
    print d
    currentDenom = nextDenom

  denom_sum += currentDenom


print denom_sum
print "Time Taken:", time.time() - START


"""
continued fractions are the best approximation for their area, but not the best overall (go figure, limited denominators -> limited precision).

How can I get a fraction, a/b, such that abs(math.sqrt(d) - p/q) > abs(math.sqrt(d) - a/b)?

Assume that math.sqrt(d) > p/q and math.sqrt(d) > a/b. Then

answer to 1 to 1000 is
561480917932597
I'm getting:
428383607390799
5426051998674302


"""
