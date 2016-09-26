#NOTE TODO need to solve it
import time, math
from primes import gcd, rep_sq_sqrt, multInverse
from primes import *

START = time.time()
MOD   = 987898789
SIZE  = 40

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

# I can do better than this... derp
def compute2(a,c):
  valDict = { c%2 : 2*a }
  for b in xrange(a, 0, -2*twoPowerList[a]):
    addToDict(valDict, pow(c, gcd(a,b), MOD-1), 2)
    addToDict(valDict, c%2, -2)
  addToDict(valDict, pow(c,a,MOD-1), -1)

  return sum([f(key) * valDict[key] for key in valDict.keys()])

sumz = 0
for a in xrange(1,SIZE+1):
  #print a, len(prevComputed)
  for c in xrange(1,SIZE+1):
    sumz += compute2(a,c)

print sumz % MOD
print "Time Taken:", time.time() - START

"""
T(n) = T(k) * T(n-k) + T(k-1) * T(n-k-1)

comp(45,47,c) = c
comp(45,49,c) = c
comp(46,50,c) = c**2
comp(47,49,c) = c
comp(39,45,c) = c**3

2 4
3 8
4 16
5 32
6 4 / 64
7 128
8 256
9 8 / 512

970746056
Time Taken: 650.409888983
Time Taken: 383.118942976 # removed some excessive calculations



Congratulations, the answer you gave to problem 440 is correct.

You are the 212th person to have solved this problem.

"""
