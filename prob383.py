#NOTE TODO need to solve it
import time
START = time.time()
SIZE = 10**8

def compute(n):
  sumz = 0
  while n > 0:
    n    /= 5
    sumz += n
  return sumz

count = 0
for i in xrange(5,SIZE+ 1,5):
  if compute(2*i-1) < 2*compute(i):
    #print i,2*i-1, compute(2*i-1), 2*compute(i), 2*compute(i) - compute(2*i-1)
    count +=1

print "There were:", count, "under", SIZE

print "Time taken:", time.time() - START

"""


"""
