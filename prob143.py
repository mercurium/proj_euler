#NOTE unsolved TODO

import time
from math import *
START = time.time()
SIZE = 1000

count = 0
for i in xrange(1,SIZE):
    for j in xrange(1,i+1):
        for k in xrange(i-j+1,j+1) :
            if acos((i**2-j**2-k**2)/(2*j*k)) > 2*pi/3:
               break
            count +=1
    print i, count

print "Time Taken:", time.time() - START
