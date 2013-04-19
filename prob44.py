import string
import math
import time
start = time.time()

items = set()
for i in range(1,50000):
  items.add(i*(3*i-1)/2)
print "Time Taken: " + str(time.time()-start)

done = 0
for i in range(2,10000):
  for j in range(1,i):
    a = i*(3*i-1)/2
    b = j*(3*j-1)/2
    if a+b in items and a-b in items:
      print a-b, a, b, a+b
      print i,j
      done = 1
      break
  if done:
    break

print "Time Taken: " + str(time.time()-start)
