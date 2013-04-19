from primes import *
import time
start = time.time()


primes = tuple(primes[:100])
val = dict()

def helper(n, plst):
	if (n,plst) in val: return val[(n,plst)]
	if n==0: return 1
	if len(plst) == 0: return 1
	if plst[0] > n: return 0
	val[(n,plst)] = helper(n,plst[1:]) + helper(n-plst[0],plst)
	return val[(n,plst)]
	
def compute(n):
	val[n] = helper(n,primes)
	return val[n]

for i in xrange(1,1000):
  if compute(i) > 5000:
  	print i
  	break
  
print "Time Taken: " + str(time.time()-start)
