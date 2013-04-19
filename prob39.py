import time
from math import sqrt
start = time.time()

lst = [0] * (1+10**3)

for i in range(2,501):
  for j in range(1,i+1):
    n = sqrt(i**2+j**2)
    if i+j+n > 1000:
      break
    if int(n) == n:
      lst[i+j + int(n)] += 1
print max(lst), lst.index(max(lst))  

print "Time Taken: " + str(time.time()-start)

