import time
start = time.time()
from primes import mr

lst = [i**3 for i in xrange(1,578)]

candidates = set()
for i in xrange(1,len(lst)):
  for j in xrange(i-1,-1,-2):
    candidates.add(lst[i]-lst[j])
    if lst[i] -lst[j] > 10**6:
      break
print len(candidates)
count = 0
for val in candidates:
  if mr(val):
    count+= 1
print count
print "Time Taken: ", time.time() - start

"""
~/Desktop/python_projects/proj_euler $python prob131.py
4527
173
Time Taken:  0.131557941437

We only need to go up to 577

n^2(n+p)

n is cube (since n+p can't turn n^2 into a cube)
p+n is cube

n = 1
p = 7

1^3 + 1^2*7 = 8
8^3 + 8^2*19 = 3^3*4^3


p = 7,19,37,61

So basically, we need two cubes such that
a^3 - b^3 = prime < 10^6.
Reason for this, we have n^2(n+p) = cube. This means that n is a cube and n+p is a cube. So if we have n = b^3, and n+p = b^3 + prime = a^3, we're set. n^2 * (n+p) = b^6*(a^3) = cube.
"""
