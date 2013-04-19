from primes import *
import time
start = time.time()


def rep_dig(n):
  if n == 1:
    return 0
  j = 10
  val = 1
  while j%n != 1:
    j*= 10
    val+=1
  return val
  
      
largest = 0
big_n = 0
for i in xrange(3,1000,2):
  if i%2!=0 and i%5 != 0:
    val = rep_dig(i)
    if largest < val:
      largest = val
      big_n = i
print big_n, largest

print "time taken: " +str(time.time()-start)  
