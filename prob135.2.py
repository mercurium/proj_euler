import time
start = time.time()
#going to come back to this later.

#problem I was facing with this code is that I have a large overhead from computing the number of sums each number has (too much wasted effort...

#i was using the fact that n = a^2 - (a-b)^2 -(a-2b)^2 = -(a-b)(a-5b) to loop through it. Very inefficient T.T;;; yeah

size = 10**3*2
lst = [0] * size
for a in range(1,size+1):
  for b in range(a/5+1, a/2):
    val = -1 * (a - b) * (a - 5*b)
    if val>0 and val < size:
      lst[val] += 1

count = 0
sumz = 0
for i in range(0,len(lst)):
  if lst[i] == 10: count += 1
  sumz+= lst[i]
print count
print sumz


print "time elapsed = " + str(time.time()-start)














