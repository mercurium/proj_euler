from primes import *
import time
start = time.time() 


def trunk_r(n):
  n = n//10
  while n > 10:
    if n not in p:
      return False
    n = n//10
  return True

def trunk_l(n):
  while n > 10:
    n = int(str(n)[1:])
    if n not in p:
      return False
  return str(n) in '2357' or n ==0
  
count = 0
sumz = 0
p = set() 

lst = [0]*10**6
for i in xrange(3,len(lst),2):
  if lst[i] == 0:
    for j in xrange(i*i,len(lst),2*i):
      lst[j] = 1
    p.add(i)

print "Time Taken: " + str(time.time() -start)


for i in p:
  if (not str(i)[0] in '14689') and trunk_r(i) and trunk_l(i):
    if i > 10:
      print i
      count += 1
      sumz += i
  if count == 11:
    break
    
print sumz, count

print "Time Taken: " + str(time.time() -start)

