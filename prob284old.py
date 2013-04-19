import time
start = time.time()
from math import log

def base14(num):
  base = ''
  while num != 0:
    n = num%14
    if n > 9: n = chr(n+87)
    n = str(n)
    base = n + base
    num/=14
  return base

sumz = 0
for i in xrange(1,10001):
  dig = int(log(i,14)+1)
  if (i**2 % 14**dig) == i:
    print i, base14(i)
    n = i
    while n > 0:
      sumz += n%14
      n/=14

print base14(sumz)
print "Time Taken:", time.time() - start
