import time
from primes import gcd
from primes import *
START = time.time()
SIZE  = 10**4

# (iteration, orderTriangle, orderSide1, orderSide2, orderSide3)
countDict              = dict()
startConfig            = (1,1,0,0,0)
countDict[startConfig] = 1

primeLim               = 50

def insertIntoDict(valDict, key, value):
  if key[1] > 3:
    return # no op on numbers greater than 3
  if key in valDict:
    valDict[key] += value
  else:
    valDict[key] = value

def A(n, mod):
  return (3 * pow(4, n-1, mod) - 2 * pow(3, n-1, mod)) % mod

def appendEntry(oldEntry):
  iteration, orderTriangle, orderSide1, orderSide2, orderSide3 = oldEntry
  count = countDict[oldEntry]

  insertIntoDict(countDict, (iteration + 1, orderTriangle, orderSide1, orderSide2, orderTriangle + 1), count)
  insertIntoDict(countDict, (iteration + 1, orderTriangle, orderSide3, orderSide2, orderTriangle + 1), count)
  insertIntoDict(countDict, (iteration + 1, orderTriangle, orderSide1, orderSide3, orderTriangle + 1), count)

  insertIntoDict(countDict, (iteration + 1, orderSide1+1, orderTriangle+1, orderSide1, orderSide1), count)
  insertIntoDict(countDict, (iteration + 1, orderSide2+1, orderTriangle+1, orderSide2, orderSide2), count)
  insertIntoDict(countDict, (iteration + 1, orderSide3+1, orderTriangle+1, orderSide3, orderSide3), count)

gcdDict = dict()
count = -6 # ignore the case where size = 2
for order in xrange(2,SIZE+1):
  for key in filter((lambda key: key[0] == order-1), countDict.keys()):
    appendEntry(key)
  val1 = sum(countDict[key] for key in filter( (lambda key: key[0] == order and key[1] == 1), countDict.keys()))
  val3 = sum(countDict[key] for key in filter( (lambda key: key[0] == order and key[1] == 3), countDict.keys()))
  count += gcd(val1, val3)
  if gcd(val1, val3) > 30:
    print order, gcd(val1, val3)


print count
print "Time Taken:", time.time() - START

for value in sorted(set(gcdDict.values())):
  if not m_r(value/6):
    continue
  prime  = value / 6
  minKey = min(filter(lambda x: gcdDict[x] == value, gcdDict.keys()))
  print prime, '\t', \
      minKey, '\t', \
      modNum[prime], '\t', \
      (minKey - modNum[prime]) / (prime -1.)

"""
A(n+1) = 3 x 4^n - 2 x 3^n (  http://oeis.org/A255463 )

3 x 4^n - 2 x 3^n



by default, the gcd = 6 for most numbers
gcd(n) = 30 for n % 20 = 11
gcd(n) = 114 for n % 342 = 43. 114 = 6 x 19, 342 = 6 x 3 x 19
gcd(n) = 102 for n % 272 = 14. 102 = 6 x 17, 272 = 16 x 17

102   : 104  mod 272   (17)
114   : 43   mod 342   (19)
138   : 246  mod 253   (23)
174   : 273  mod 812   (29)
186   : 500  mod 930   (31)
246   : 64   mod 1640  (41)
258   : 1523 mod 1806  (43)
282   : 389  mod 1081  (47)
318   : 893  mod 2756  (53)
402   : don't care to compute atm (67)
438   : don't care to compute atm (73)
570   : don't care to compute atm (95)
582   : don't care to compute atm (97)
690   : don't care to compute atm (115 = 5 x 23)
1410  : 2551  (235 = 5 x 47)

Huh. Looks like the values that can be present are 6 x (1 to many unique primes).

if value = 6 x prime, then the mod value is a factor of prime.
  Ex: g(n) = 102 when n = 104 mod 272.
      102  = 6 x 17, 272 = 16 x 17

  30:   6 x  5
  20:   4 x  5

  102:  6 x 17
  272: 16 x 17

  114:  6 x 19
  342: 18 x 19

  138:  6 x 23
  253: 11 x 23

  186:  6 x 31
  930: 30 x 31

  246:   6 x 41
  1640: 40 x 41

  282:   6 x 47
  1081: 23 x 47

set([17, 19, 23, 29, 31, 41, 43, 47, 53, 67, 73, 97])
    [17, 19, 23, 29, 31, 41, 43, 47, 53, 67, 73, 79, 89, 97, 101, 103, 113, 127, 167, 173, 191, 199, 431, 439, 499, 643, 1129, 1559, 2039]
    [5,17, 19, 23, 29, 31, 41, 43, 47, 53, 67, 73, 79, 89, 97, 101, 103, 113]

    11, 16, 18, 23, 28, 30, 40, 42

    7,11,13, 37, 59, 61, 71, 83, 107, 109

for min n such that A(n) = 0 mod p
and min m such that G(m) = 0 mod 6p
  m = n mod (p-1)


5       11      3       2.0
17      104     8       6.0
19      43      7       2.0
23      246     4       11.0
29      273     21      9.0
31      500     20      16.0
41      64      24      1.0
43      1523    11      36.0
47      389     21      8.0
53      893     9       17.0
67      2469    27      37.0
73      4098    30      56.5
79      5428    46      69.0
89      6522    10      74.0
97      1219    19      12.5
113     5246    94      46.0
191     8540    85      44.5
199     8386    70      42.0
499     8839    41      17.6666666667
2039    5534    439     2.5

"""


