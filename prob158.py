import string
from math import *
from primes import *

maxz = 0
vals = []
lst = []
for i in range(0,26):
  vals += [2**i-i-1]
  lst += [factorial(26) /(factorial(i)*factorial(26-i))]
  print vals[i], lst[i], vals[i]*lst[i]
  if maxz < vals[i]*lst[i]:
    maxz = vals[i]*lst[i]


print maxz
