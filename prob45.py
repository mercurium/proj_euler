from math import sqrt
import time
start = time.time()

for i in xrange(166,10**5):
  n = i*(3*i-1)/2
  m = int(sqrt(n/2)+1)
  if m*(2*m-1) == n:
    print n
    break

print "Time taken: " + str(time.time()-start)
