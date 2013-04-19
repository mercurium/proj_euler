from primes import *
from math import factorial
import time
start = time.time()


lst = [-1]*(10**7+1)
lst[1] = lst[2] = 1
lst[169] = lst[363601]=lst[1454]=3
lst[871] = lst[45361] = 2
lst[872] = lst[45362] = 2

def fact_sum(n):
  if n == 0:
    return 0
  return factorial(n%10) + fact_sum(n/10)

def grab(i):
  if lst[i] == -1:
    if i == fact_sum(i):
      lst[i] = 0
    else:
      temp = 1 + grab(fact_sum(i))
      lst[i] = temp
  return lst[i]

sum = 0
for i in range(1,10**6):
  if grab(i) == 60:
    sum+=1
print sum


print "Time Taken: " + str(time.time()-start)
  
