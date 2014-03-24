from math import *
import time
start = time.time()
import sys

size = 10**5
if len(sys.argv) > 1:
    size = int(sys.argv[1])

lst = [1]*size
for i in xrange(2,len(lst)):
    if i%1024 == 0:
        print i
    a = i**2
    for j in xrange(i,len(lst),i):
        lst[j] += a

count = 0
sumz = 0
for i in xrange(1,len(lst)):
    if int(sqrt(lst[i])+.1)**2 == lst[i]:
        print i, lst[i]
        count +=1
        sumz +=i
print count
print sumz
print "time elapsed = " + str(time.time()-start)


