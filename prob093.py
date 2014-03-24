import time
start = time.time()
from itertools import permutations as perm, combinations as comb

def add(a,b): return a+b
def sub(a,b): return a-b
def div(a,b): return a/(1.0*b)
def mult(a,b): return a*b
def abs(a): return max(a,-1*a)
ops = [add,sub,div,mult]

def slow_test(digs):
  valids = set([])
  for g in perm(digs): #g for group of nums
    for a in xrange(4):
      for b in xrange(4):
        for c in xrange(4):
          val = ops[c](ops[b](ops[a](g[0],g[1]),g[2]),g[3])
          if val % 1 <= 0.1:
            valids.add(int(abs(val)))
  return valids
  
testing_vals = set([])
for group in comb(range(1,10),4):
  setz = slow_test(group)
  for i in range(1,100):
    if i not in setz:
      if i > 30: testing_vals.add((group, i))
      break


print testing_vals
print "Time Taken:", time.time() -start

