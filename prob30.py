import string
import math
from math import factorial
import time
start = time.time()

fifths = dict([(str(x),x**5) for x in xrange(0,10)])

def fifth_sum(n):
  return sum(  [fifths[num] for num in str(n) ] )
  

sumz = 0
for i in range(3,10**6):
  if fifth_sum(i) ==i:
    sumz = sumz + i
    print i, sumz

print sumz
print "Time Taken: " + str(time.time()-start)
