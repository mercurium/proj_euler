from primes import *
import time
start = time.time() 


def trunk_r(n):
  n = n//10
  while n > 10:
    if not is_prime(n):
      return False
    n = n//10
  return True

def trunk_l(n):
  while n > 10:
    n = int(str(n)[1:])
    if not is_prime(n):
      return False
  return str(n) in '2357' or n ==0
  
count = 0
sum = 0
lst = [0]*10**6
for i in range(2,len(lst)):
  if lst[i] == 0:
    for j in range(2*i,len(lst),i):
      lst[j] += 1

p = set()
for i in range(2,len(lst)):
  if lst[i] == 0:
    p.add(i)

p = list(p)
p.sort()

for i in range(4,len(p)):
  if (not str(p[i])[0] in '14689') and trunk_r(p[i]) and trunk_l(p[i]):
    print p[i]
    count += 1
    sum += p[i]
  if count == 11:
    break
    
print sum, count

print "Time Taken: " + str(time.time() -start)

