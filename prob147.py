import string, time
from primes import *

START = time.time()
N,M = 47,43

def getCount(a,b,n,m):
  c, d= a/2, b/2
  if a%2 == 0 and b%2 == 0:
    if (n-c-d) < 0 and m-c-d < 0:
      return 0
    return (n-c-d+1)*(m-c-d+1) + (n-c-d)*(m-c-d)
  elif a%2 != b%2:
    if (n-c-d) < 0 and m-c-d < 0:
      return 0
    return (n-c-d)*(m-c-d) *2
  else:
    if (n-c-d-1) < 0 and m-c-d-1 < 0:
      return 0
    return  (n-c-d)*(m-c-d-1) + (n-c-d-1)*(m-c-d)



count = 0
for n in range(1,N+1):
  for m in range(1,M+1):
    for a in range(1,max(n,m)*2):
      for b in range(1,max(n,m)*2):
        num = getCount(a,b,n,m)
        if num > 0:
          count += num
        else:
          break
    tempC = count
print count + ncr(N+2,3) * ncr(M+2,3)
print "Time Taken:", time.time() - START


"""

Congratulations, the answer you gave to problem 147 is correct.

You are the 1518th person to have solved this problem.


Time Taken: 1.40374398232
Time Taken: 0.180144786835 # used pypy on palantir mac


So... I computed the number of diagonal blocks for each size type in notes147.txt. I'll need to get around to making it just one closed formula, but if you want to see my work... it's in notes147.txt

2dx2c = (n-c-d+1)(m-c-d+1) + (n-c-d)(m-c-d)
2d+1x2c =(n-c-d)(m-c-d) +(n-c-d)(m-c-d)


2d+1x2c+1= (n-c-d)(m-c-d-1) + (n-c-d-1)(m-c-d)
2dx2c+1 =(n-c-d)(m-c-d) +(n-c-d)(m-c-d)


"""

