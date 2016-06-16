import time, math
from fractions import Fraction
START = time.time()
SIZE  = 10**6

vals = [0.0, 1., 1., 1., 2.]

for i in xrange(5, SIZE+1):
  prob = (2*vals[-5] + (i-4)*vals[-1] + 2) / (i-3.)
  vals.append(prob)
  vals.pop(0)

print vals

a = vals[-1]
k = SIZE

print a -((k-4)*(k-1) * a + 2*(k-5)*a + 2*k)/(k*(k-3.))

print [1 -vals[i] / (SIZE-len(vals) + i + 1) for i in xrange(len(vals))]
print "Time Taken:", time.time() - START




"""

0 1 2 3 4

2 3 4

2 -> () / (4)

3 -> () / ()



xrange(1,3) -> [1,2]

"""
