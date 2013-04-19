from primes import *
import time
start = time.time()




for i in range(9,10000,2):
  if i not in primes_few:
    j = 0
    done = 0
    while primes[j] < i and done ==0:
      n = (i-primes[j]+.5)/2
      if int(math.sqrt(n))**2==int(n):
        done = 1
      j = j+1
    if done != 1:
      print i
      break
      
print "Time Taken: " + str(time.time()-start)
