import time
from primes import *
import copy
start = time.time()

def primer2(n):
  if n ==1:
    return False
  for i in range(0,100):
    if n% primes[i] != 0:
      if primes[i] >= n:
        return True
      if rep_sq(primes[i],n-1,n) != 1:
        return False
  return True
  

size = 10**6
lst = [0] * size
lst2= [0] * 10
for i in range(2,len(lst)):
  if lst[i] == 0:
    for n in range(i*2,len(lst),i):
      lst[n]+=1

print "Time Taken: " + str(time.time()-start)


for i in range(10**6*4,len(lst2)):
  if lst[i] != 0 and i % 2 == 1:
    lst2[i] = primer2(i)
    if lst2[i]:
      print i
  
print "Time Taken: " + str(time.time()-start)
itemss = set()
for i in range(2,len(lst)):
  if lst[i] == 0:
    itemss.add(i)

itemss = list(itemss)
itemss.sort()
for i in range(0,len(itemss)):
  itemss[i] = str(itemss[i])
itemss = string.join(itemss,', ')
file = open('bagahh.txt','w')
file.write(itemss)




print "Time Taken: " + str(time.time()-start)







