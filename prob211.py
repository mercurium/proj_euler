from math import *
import time
START = time.time()
SIZE = 64*10**6

lst = [1]*SIZE
for i in xrange(2,len(lst)):
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
print "Time Taken:", time.time() - START
