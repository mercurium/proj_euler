import math
import time

start = time.time()
fa = math.factorial

size =50

r = [1] * (size+1)
g = [1] * (size+1)
b = [1] * (size+1)

r[2] = 2
r[3] = 3
g[3] = 2

for i in range(4,size+1):
  r[i] = r[i-1] + r[i-2]
  g[i] = g[i-1] + g[i-3]
  b[i] = b[i-1] + b[i-4]
  
print r[size]+g[size]+b[size]-3
print "time taken: " + str(time.time()-start)

#Answer: 20492570929
#time taken: 0.000142812728882

