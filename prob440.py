import time, math
from primes import gcd, rep_sq_sqrt, multInverse

START = time.time()
MOD   = 987898789
SIZE  = 2000

def mult(a,b): #multiplying numbers which share a square root (sqrt)
  full = a[0] * b[0] + a[1] * b[1] * a[2]
  frac = a[1] * b[0] + a[0] * b[1]
  return (full, frac, a[2])

prevComputed = dict()
def f(n):
  n = n % (MOD - 1)
  if n in prevComputed:
    return prevComputed[n]
  a    = (26,  5, 26)
  b    = (26, -5, 26)

  aPow = (5, 1,26)
  bPow = (5,-1,26)

  partAPow = rep_sq_sqrt(aPow, n, MOD)
  partBPow = rep_sq_sqrt(bPow, n, MOD)

  ans = (mult(a, partAPow)[0] \
       + mult(b, partBPow)[0])\
       * multInverse(52, MOD) % MOD

  prevComputed[n] = ans
  return ans

twoPowerList = [1] * (SIZE+1)
for twoPow in xrange(1, int(math.log(SIZE+1,2)+1)):
  for i in xrange(2**twoPow, SIZE+1, 2**twoPow):
    twoPowerList[i] *= 2

def compute(a,b,c):
  if (a-b) % (2 * twoPowerList[b]) == 0:
    return pow(c, gcd(a,b), MOD-1)
  return c % 2

def addToDict(valDict, key, value):
  if key in valDict:
    valDict[key] += value
  else:
    valDict[key] = value

def computeBetter(a):
  valDict = { 0 : 2*a }
  for b in xrange(a, 0, -2*twoPowerList[a]):
    addToDict(valDict, gcd(a,b), 2)
    addToDict(valDict, 0, -2)
  addToDict(valDict, a, -1)

  sumz = (f(1) + f(0)) * valDict[0] * SIZE /2
  del valDict[0]

  for c in xrange(1,SIZE+1):
    sumz += sum([f(pow(c,key, MOD-1)) * valDict[key] for key in valDict.keys()])
  return sumz

sumz = 0
for a in xrange(1,SIZE+1):
  print a
  sumz += computeBetter(a)

print sumz % MOD
print "Time Taken:", time.time() - START


"""
T(n) = T(k) * T(n-k) + T(k-1) * T(n-k-1)

970746056
Time Taken: 650.409888983
Time Taken: 383.118942976 # removed some excessive calculations
Time Taken: 106.342717886 # merged some computation


Congratulations, the answer you gave to problem 440 is correct.

You are the 212th person to have solved this problem.

"""
