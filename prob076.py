import time
start = time.time()

size = 100
vals = dict()
vals[(1,1)] = 1
vals[(0,0)] = 1
vals[0] = 1
vals[1] = 1

def partitions(n):
  if n in vals:
    return vals[n]
  return sum([helper(n,k) for k in xrange(1,n+1)])
  
def helper(n,k):
  if (n,k) in vals: return vals[(n,k)]
  if n == k: return 1
  if n < k or n <= 0 or k <= 0: return 0
  vals[(n,k)] = helper(n-1,k-1) + helper(n-k,k)
  return vals[(n,k)]

print partitions(100) -1
print "Time Taken: " + str(time.time()-start)
