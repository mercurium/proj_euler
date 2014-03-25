#NOTE TODO need to solve it
import time
start = time.time()

size = 10**2+1
mc = dict() #mc for min cost


def compute_min(l, u): #l,u for lower and upper limits
  if (l,u) in mc:
    return mc[(l,u)]
  if u <= l: 
    return 0
  if u == l+1:
    return l
  if u == l+2:
    mc[(l,u)] = l+1
    return l+1
  minz = float('inf')
  for i in xrange(l,u):
    val = compute_min(l,i-1) + i + compute_min(i+1,u)
    if val < minz:
      minz = val
  mc[(l,u)] = minz
  return minz

for i in xrange(1,101):
  compute_min(1,i)
  print i

print compute_min(1,100)
print "Time taken:", time.time()-start


#damn. this isn't going to work as expected with DP... :[
#....this works, but is slow as ...sadfacedness xD;; LOL NVM IT DOESN'T EVEN WORK... T___T
