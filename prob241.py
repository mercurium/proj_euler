import time
from primes import divisors, factor, pfactor_gen
START = time.time()
SIZE  = 10**6

factors = pfactor_gen(SIZE)

for i in xrange(2,SIZE,2):
  if sum(divisors(i)) % i == i/2:
    print i, factor(i)

print "Time Taken:", time.time() - START


"""
2: 1,3,7,15,31,65,129
3: 1,4,10,40,121,364
5: 1,6,31,156,781,3906

p(2)    = 3/2 -> 1 1/2
p(24)   = (13 * 4)/8 = 6 1/2
p(4320) = (63 * 40 * 6) = 3 1/2
        -> 2^4 * 3^3 * 5 * 7
  4320  = 2^5 * 3^3 * 5



2 [2]
24 [2, 2, 2, 3]
4320 [2, 2, 2, 2, 2, 3, 3, 3, 5]
4680 [2, 2, 2, 3, 3, 5, 13]
26208 [2, 2, 2, 2, 2, 3, 3, 7, 13]


"""
