from primes import *
import time
start = time.time()
#well... i brute forced it and it takes 14.6 seconds to run... :|

count = 0
for i in range(5,12001):
  for j in range(i/3 +1, i/2+1):
    if gcd(i,j) ==1: count +=1
print count


print "time elapsed = " + str(time.time()-start)


