import time
import math
start = time.time()

size = 10**6
py_trip = set()
count = 0

for k in xrange(1,size//4):
  val = size/(2*k)
  for m in xrange(1,size):
    if m*(m+1) > val:
      break
    diff = 2 if m%2 == 0 else 1
    val2 = val/m - m
    for n in xrange(1,min(m,val2+1),diff):
        
      d,f = k*m*m,k*n*n
      a,b,c = d-f,2*k*m*n,d+f
      a,b = min(a,b), max(a,b)
      
      
      if c %(b-a) == 0:
        py_trip.add((a,b,c))

print len(py_trip)
print "Time Taken:", time.time()-start


"""

~/Desktop/python_projects/proj_euler $python prob139.py
10057761
Time Taken: 253.662650108 (slow, naive method)
"""
