from math import log
import time
START = time.time()

logValues = [0] + [log(x,10) for x in xrange(1,101)]


count = 0
for i in xrange(23,101):
  for j in xrange(0,i):
    if sum(logValues[i-j+1:i+1]) - sum(logValues[0:j+1]) > 6:
      count = count +1

print count
print "Time Taken:", time.time()-START
