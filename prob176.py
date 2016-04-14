from primes import gcd, factor
import time

START          = time.time()
TEST_SIZE      = 10**3
TEST_MULT_SIZE = TEST_SIZE**2
MAX_TRI_SIZE   = 10**4
MIN_LIM        = 45
TARGET_NUM     = 5040

# cathetus dictionary containing count of how many triangles have a length as cathetus
catDict = dict()

def insertOrIncrement(n):
  if n in catDict:
    catDict[n] += 1
  elif n < MAX_TRI_SIZE:
    catDict[n] = 1

for m in xrange(2,TEST_SIZE):
  for n in xrange(1,m):
    if 2 * m * n > MAX_TRI_SIZE:
       break
    if gcd(m,n) != 1:
      continue
    for k in xrange(1,TEST_MULT_SIZE):
      if (m**2 - n**2) * k > MAX_TRI_SIZE or \
          2 * m * n * k > MAX_TRI_SIZE:
           break
      tripletSum = 2*m*k*(m+n)
      insertOrIncrement(2*m*n*k)

for key in catDict.keys():
  if catDict[key] >= MIN_LIM:
    print key, catDict[key], factor(key)
print max(catDict.values())
print "Time Taken:", time.time() - START

"""
Suppose that the number b is even. Why does that guarantee a solution for:
    b = k_2 x (m_2^2 - n_2^2)
  if a solution for:
    b = 2mnk
        m_1 > n_1
  exists?

  2mnk:
    m = (m_2^2-n_2^2)
    n = 1
    k = k_2/2

a = k(m^2 - n^2)
b = k(2mn)
c = k(m^2 + n^2)

12 = m: 6, n: 1 k: 1 (2 x 6 x 1)    35,12, 37
12 = m: 3, n: 2 k: 1 (2 x 3 x 2)     5,12, 13
12 = m: 2, n: 1 k: 4 4x(2^2 - 1^2)  12,16, 20
12 = m: 3, n: 1 k: 2 (2(2 x 3 x 1)) 16,12, 20
12 = m: 2, n: 1 k: 3 (3(2 x 2 x 1)), 9,12, 15

840: 20 + 33
1680: 14 + 45
2520: 22 + 37
2640: 12 + 35
3360: 8 + 47
5040: 13 + 43

840 86 [2, 2, 2, 3, 5, 7]
1680 104 [2, 2, 2, 2, 3, 5, 7]
2520 96 [2, 2, 2, 3, 3, 5, 7]
2640 82 [2, 2, 2, 2, 3, 5, 11]
3360 102 [2, 2, 2, 2, 2, 3, 5, 7]
5040 99 [2, 2, 2, 2, 3, 3, 5, 7]


840 53 [2, 2, 2, 3, 5, 7]
1680 59 [2, 2, 2, 2, 3, 5, 7]
2520 59 [2, 2, 2, 3, 3, 5, 7]
3360 55 [2, 2, 2, 2, 2, 3, 5, 7]
5040 56 [2, 2, 2, 2, 3, 3, 5, 7]
"""
