import math
import string
import time
start = time.time()

count = 12951
for i in range(10**6,10**7):
  if string.join(sorted(str(i)),'') == str(i) or string.join(sorted(str(i)),'')[::-1] == str(i):
    count += 1
  if (count*1.0)/i ==.01:
    print i
    break
    
print "Time taken:" + str(time.time()-start)
