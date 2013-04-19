import math
import time

start = time.time()


size =50

f = [1] * (size+1)
f[2] = 2
f[3] = 4
f[4] = 8
for i in range(5,len(f)):
  f[i] = f[i-1]+f[i-2]+f[i-3]+f[i-4]      

print f[size]
print "time taken: " + str(time.time()-start)

#100808458960497
#100808382058055

