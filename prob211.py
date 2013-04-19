from math import *
import time
start = time.time()

lst = [1]*100000
for i in range(2,len(lst)):
  for j in range(i,len(lst),i):
    lst[j] += i**2

count = 0
for i in range(1,len(lst)):
  if int(sqrt(lst[i])+.1)**2 == lst[i]:
    print i, lst[i]
    count +=1
print count

print "time elapsed = " + str(time.time()-start)


