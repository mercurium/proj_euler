from primes import *
import time
start = time.time()


powz = 1777
for i in range(0,1854):
  powz = rep_sq(1777,powz,10**6)

print rep_sq(1777,powz,10**8)

print "Time Taken: " + str(time.time()-start)
