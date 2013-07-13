import time
start = time.time()

lst = [0]*(2*10**6)

sumz = 0
count = 0
for i in xrange(3,len(lst),2):
  if lst[i] == 0:
    sumz+=i
    for j in xrange(i**2,len(lst),2*i):
      lst[j]+= 1
    count +=1
      
print count
print sumz

print "Time Taken: " + str(time.time()-start)
