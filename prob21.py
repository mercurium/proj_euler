import time
start = time.time()

size = 10**4
lst = [0]*size

for i in xrange(1,size):
  for j in xrange(2*i,size,i):
    lst[j] += i

count = 0
sumz = 0
for i in xrange(1,size):
  if lst[i] < size and lst[lst[i]] == i and lst[i] != i:
    count += 1
    sumz+= i
print sumz
print "time taken: " +str(time.time()-start)
    
    
