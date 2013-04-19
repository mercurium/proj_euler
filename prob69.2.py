import time
start = time.time()
size = 10**6
lst = range(0,size+1)

for i in xrange(2,len(lst)):
  if i == lst[i]:
    for j in xrange(i,len(lst),i):
      lst[j] = lst[j]/i *(i-1)

print "Time Taken: ", time.time() - start
#and lst is now your list of totients

maxz, m = 0,0
for i in xrange(2,len(lst)):
  if i*1./lst[i] > maxz:
    maxz = i*1./lst[i]
    m = i

print m, maxz
print "Time Taken: ", time.time() - start
