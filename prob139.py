import time
import math
start = time.time()

size = 10**6
py_trip = set()
count = 0


for m in xrange(1,size):
  if 2*m*(m+1) > size:
    break
    
  diff = 2 if m%2 == 0 else 1
  val2 = size/2/m - m
  
  for n in xrange(1,min(m,val2+1),diff):
        
    d,f = m*m,n*n
    a,b,c = d-f,2*m*n,d+f
    if a+b+c >= size: break
    a,b = min(a,b), max(a,b)
      
      
    if c %(b-a) == 0:
      for k in xrange(1,size/(2*m*(m+n))+1):
        py_trip.add((a*k,b*k,c*k))

print len(py_trip)
print "Time Taken:", time.time()-start


"""

~/Desktop/python_projects/proj_euler $python prob139.py
10057761
Time Taken: 253.662650108 (slow, naive method)
Time Taken: 26.9965119362 (reordered the loops)

Method of attack: a = m^2-n^2,b = 2mn, c = m^2 +n^2
So we know that since we can tile the square, we have (b-a)|c.
After this, we only need to check the k's when we have a valid equation... :x



"""
