#NOTE TODO need to solve it
import time
from primes import ncr
START     = time.time()
FRAC      = 1/2.

def probInOne(p):
  return 2 * p - p**2

def probInTwo(p):
  return (1/6. + 2 * p - p**2 - 2/3. * p**3 + p**4/2.) * (1-probInOne(p))

def addArr(a,b):
  if len(a) > len(b):
    a,b = b,a
  a = a + [0] * (len(b) - len(a))
  return [a[i] + b[i] for i in xrange(len(a))]

def scaleArr(arr, mult):
  return map(lambda x: x * mult, arr)

# integrating from i=p to i=1
def integrate(lst):
  newLst    = [0] + [ lst[i] / ( i+1. ) for i in xrange(len(lst)) ]
  newLst[0] = -1 * sum(newLst) + 1
  return newLst

def flipKToOneMinusK(lst):
  newLst = [0] * len(lst)
  for n in xrange(len(lst)):
    for r in xrange(n+1):
      newLst[r] += ncr(n,r) * lst[n] * (-1)**r
  return newLst

def plugIntoArr(arr, val):
  return sum([arr[i] * val**i for i in xrange(len(arr))])

probArr    = [1]
runningSum = 0
totalProb  = 0

for i in xrange(1,30):
  probArr = flipKToOneMinusK(probArr)
  probArr = addArr(probArr, [0] + scaleArr(probArr, -1))
  probArr = scaleArr(probArr, 2)
  probArr = integrate(probArr)
  #print probArr

  probOccur = plugIntoArr(probArr, FRAC) * (1 - totalProb)
  totalProb += probOccur

  runningSum += probOccur * i
  print str(i) + ":\t", plugIntoArr(probArr, FRAC), runningSum, totalProb

print runningSum
print "Time Taken:", time.time() - START


"""
probInOne = 1 - (1-x)^2
probInTwo =

p(2-p) -> (1-p)(2-(1-p)) = (1-p)(1+p) = 1-p^2

P[X=2] / (1 - P[X=1]) > P[X=1]

"""
