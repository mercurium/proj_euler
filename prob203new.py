from primes import *
import time

lst = [[0]*51 for x in range(0,51) ]

lst[0][0] = 1
for i in range(0,len(lst)):
  for j in range(
