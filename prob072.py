#wow, this solution is brilliant, but unfortunately I didn't think of it myself.

from primes import *
import time

start = time.time()
size = 10**6+1

lst = range(0,size)

for i in range(2,len(lst)):
  if i == lst[i]:
    for j in range(i,len(lst),i):
      lst[j] *= (i-1.)/i

sum = 0
for i in range(2,len(lst)):
  sum+= int(lst[i])

print sum

print "time taken:" + str(time.time()-start)


