import string
import time
start = time.time()
#run time of 42.229 second ;___;
lst = range(0,10**7)

for i in range(2, len(lst)):
  if lst[i] == i:
    for j in range(i,len(lst),i):
      lst[j] *= (i-1.0)/i

print "Time Taken: " + str(time.time()-start)

min = 500
min_i = 0
for i in range(2,len(lst)):
  lst[i] = int(lst[i])
  if i%2 !=0  and i%3 != 0 and i%5 != 0:
    if sorted( str(lst[i]) ) ==sorted( str(i) ):
      if i*1.0/lst[i] < min:
        min = i*1.0/lst[i]
        min_i = i
        print i, lst[i], i*1.0/lst[i]
print min_i, min
print "Time Taken: " + str(time.time()-start)
