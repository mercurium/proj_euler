from primes import *
import string
import math
import time
start = time.time()

def rot_check(item):
  j = len(str(item))  
  for i in range(0,j):
    if lst[item/10**i + (item % 10**i)*(10**(j-i))] != 0:
      return False
  return True

lst = [0]*10**6

count = 0
for i in range(2,len(lst)): #this marks the nonprimes
  if lst[i] == 0:
    for j in range(2*i,len(lst),i):
      lst[j]+=1 #lst[j] is marked as not prime

for i in range(2,len(lst)):
  if lst[i] == 0 and rot_check(i):
    count+=1
#    print i
print count

print "Time Taken: " + str(time.time()-start)
