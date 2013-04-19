import time
start = time.time()
from math import factorial as fa
import string

val_dict = dict()
min_val = dict()
max_comp = 0

def f(n):
  return sum([fa(int(i)) for i in str(n) ])

def sf(n):
  return sum( [int(i) for i in str(f(n) ) ])

def g(n):
  if n in min_val:
    return min_val[n]
  valz = 0
  lim = 0
  while valz != n:
    lim +=1
    valz = sf(lim)
    val_dict[lim] = valz
    if valz not in min_val:
      min_val[valz] = lim
  return lim

def sg(n):
  return sum( [int(i) for i in str(g(n)) ])

lim = 1
sumz = 0
for i in range(1,150+1):
  print i, sg(i)
  sumz += sg(i)
print sumz
