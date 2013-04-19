import time
start = time.time()
from math import *
fa = factorial
from primes import factor

size = 20
knapErr = 10.

def log10(n):
  return log(n)/log(10)

total = sum([log(n) for n in range(2,size+1)])
total = int(knapErr*total+.5)/knapErr

vals = [int(knapErr*log(n)+.5)/knapErr for n in factor(fa(size))[:-1]]


print total
print vals, sum(vals)

goal_val = total/3.
prev_seen = {}

def helper(a,b,c,pos):
  #already seen case
  if (a,b,c,pos) in prev_seen:
    return ((a,b,c,pos),10**a+10**b+10**c)
  
  #end case
  if pos == len(vals):
    return (max(abs(a-c),abs(a-b),abs(b-c)),10**a+10**b+10**c)
  
  #recursive case
  a_n,am = helper(a+vals[pos],b,c,pos+1)
  b_n,bm = helper(a,b+vals[pos],c,pos+1)
  c_n,cm = helper(a,b,c+vals[pos],pos+1)
  
  return_val = am
  if a_n > b_n: return_val = bm
  if c_n < b_n and c_n < a_n: return_val = cm
  
  prev_seen[(a,b,c,pos)] = min(a_n,b_n,c_n)
  return (prev_seen[(a,b,c,pos)],return_val)

print helper(0,0,0,0)
#we will proceed to attempt this problem using knapsack.

#each item can go into one of three sacks, and we will make the recursive cases reflect this. The old way of thinking has been put into old418.py



