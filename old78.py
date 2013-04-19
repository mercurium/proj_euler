import time
start = time.time()

size = 10**4
vals = {(1,1):1,(0,0):1,0:1,1:1}

def partitions(n):


  def helper(n,k):
    if (n,k) in vals: return vals[(n,k)]
    if n == k: return 1
    if n < k or n <= 0 or k <= 0: return 0
    vals[(n,k)] = (helper(n-1,k-1) + helper(n-k,k) ) %size
    return vals[(n,k)]


  if n in vals:
    return vals[n]
  return sum([helper(n,k) for k in xrange(1,n+1)])
  

part = 1
i = 10
while part % size != 0:
  i+=1
  part = partitions(i)
  print i
print i, "DONE!!! :D :D :D"
print "Time Taken: " + str(time.time()-start)


#19, 74, 449, 599
