#NOTE TODO need to solve it
import time
from primes import pfactor_gen, factor_given_pfactor
START = time.time()

SIZE = 10**3

debug = True

def test(n):
  count = 0
  nums = []
  for i in xrange(0,n,9):
    if sum(int(x) for x in str(i)) == sum(int(x) for x in str(137*i)):
      count += 1
      nums += [i]
  return (count,nums)

def factor(n):
  return factor_given_pfactor(n, pfactor)


count,lst = test(SIZE)
if debug:
  pfactor = pfactor_gen(SIZE)
  for i in lst:
    print i, i/9, factor(i/9), i * 137

print "Answer for SIZE", SIZE, "is", count
print "Time Taken:", time.time() - START
