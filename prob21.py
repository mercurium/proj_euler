import time
start = time.time()

size = 10**4
lst = [0]*size

for i in range(1,size):
  for j in range(2*i,size,i):
    lst[j] += i

count = 0
sum = 0
for i in range(1,size):
  if lst[i] < size and lst[lst[i]] == i and lst[i] != i:
    count += 1
    sum+= i
print sum
print "time taken: " +str(time.time()-start)
    
    
