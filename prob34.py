import string
import math
from math import factorial
import time
start = time.time()



def fact_sum(n):
  if n == 0:
    return 0
  return factorial(n%10) + fact_sum(n/10)
  

sum = 0
for i in range(3,10**6):
  if fact_sum(i) ==i:
    sum = sum + i
    print i, sum

print sum

print "Time Taken: " + str(time.time()-start)
