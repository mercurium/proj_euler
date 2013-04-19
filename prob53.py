from math import log
import string
import time
start = time.time()


vals = range(0,101)
for i in range(1,len(vals)):
  vals[i] = log(vals[i],10)


count = 0
for i in range(23,101):
  for j in range(0,i):
    if sum(vals[i-j+1:i+1]) - sum(vals[0:j+1]) > 6:
      count = count +1

print count
print "Time Taken: ",time.time()-start 
