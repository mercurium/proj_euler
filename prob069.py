import sys

import time
start = time.time()
size = 10**6
lst = range(0,size+1)

for i in xrange(2,len(lst)):
  if i == lst[i]:
    for j in xrange(i,len(lst),i):
      lst[j] = lst[j]/i *(i-1)

print "Time Taken: ", time.time() - start
#and lst is now your list of totients

maxz, m = 0,0
for i in xrange(2,len(lst)):
  if i*1./lst[i] > maxz:
    maxz = i*1./lst[i]
    m = i

print m, maxz
print "Time Taken: ", time.time() - start

def factor_rec(val, count):
  while(val >= count):
    if val % count == 0:
       return count
    count = count + 1


def factor(val):
  if val == 1:
    return [1]
  temp = factor_rec(val, 2)
  return [temp] + factor(val/temp)
  
def totient(n):
  lst = factor(n)[:-1]
  print lst
  result = 1.0
  for i in range(0,len(lst)):
    if i==0 or lst[i] != lst[i-1]:
      result = result * (lst[i]-1)
    else:
      result = result * lst[i]
  return result


