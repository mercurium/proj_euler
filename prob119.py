import time
start = time.time()
from primes import *

def sum_dig(n):
  n = str(n)
  sumz = 0
  for letter in n:
    sumz += int(letter)
  return sumz

cool_num = set()

for i in range(2,400):
  for j in range(2,30):
    n = i**j
    if sum_dig(n) == i:
      cool_num.add(n)
cool_num = list(cool_num)
cool_num.sort()
print cool_num[29], len(cool_num)

print "Time Taken: " + str(time.time()-start)
