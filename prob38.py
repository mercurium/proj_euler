from primes import *
import math


for i in range(9236,9500):
  item = str(i) + str(i*2)
  checker = 0
  for j in range(1,10):
    if str(j) in item:
      checker+=1
  if checker == 9:
    print i, 2*i
