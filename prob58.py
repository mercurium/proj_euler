import string
from primes import *
import time
start = time.time()
#the four diagonals are 4n^2-2n+1, 4n^2+1,4n^2+2n+1,
# and (2n+1)^2

count = 0
j = 1


for i in range(1,100000):
  a = 4 * i*i +1
  j = 2* i
  count += mr(a+j) + mr(a) + mr(a-j)
  if count * 1.0 / (4*i+1) < .1:
    print i, count, count / (i *4.0+1)
    break
    
print j+1, count / (j*2.0+1)
print "Time taken: " + str(time.time() -start)


"""

LOL. I revisited this problem on 1/20/2013. I ran it with the original prime checking algorithm, then I ran it with the miller rabin primality test.

Original time: 
Time taken: 31.7114129066
New time:
Time taken: 0.593687772751
"""
