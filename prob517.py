import time, math, unittest as ut
from primes import m_r, mod_inverse
START = time.time()
LOWER_LIM = 10**7
UPPER_LIM = 10**7 + 10**4
MOD       = 10**9 + 7

# f(n) = f(n-1) + f(n-a)
def f(n,a):
  sumz = 0
  for i in xrange(0,int(math.ceil(n/a))+1):
    sumz += ncr(int(math.ceil(n-1 - i * (a-1))), i)
  return sumz

def ncr(n, r):
  if n < r: return 0
  r = min(r, n-r)
  if r == 0: return 1
  prod  = 1
  denom = 1
  for i in xrange(n, n-r, -1):
    prod = (prod * i) % MOD
  for i in xrange(1,r+1):
    denom = (denom * i) % MOD

  return (prod * mod_inverse(denom, MOD)) % MOD

def unit_tests():
  tc = ut.FunctionTestCase('==')
  tc.assertEquals(f(10,2), 55)
  tc.assertEquals(f(10,3), 19)
  tc.assertEquals(f(2, math.sqrt(2)), 2)
  tc.assertEquals(f(90, math.sqrt(90)), 7564511)
  print "small test cases pass! trying the bigger numbers now!"

def main():
  sumz = 0
  for i in xrange(LOWER_LIM, UPPER_LIM):
    if m_r(i):
      result = f(i, math.sqrt(i))
      sumz += result
      print i, result, '\t', time.time() - START
  print sumz % MOD

unit_tests()
main()

print "Time taken:", time.time() - START

"""
f(n) = f(n-1) + f(n-a), but we can do much better than an O(2^n) search.

main insight for this problem is that... you can use f(n,a) = sum( ncr(n-1 - k * (a-1), k) from k =1 to k=n//a)

Time taken: 580.698855162



"""
