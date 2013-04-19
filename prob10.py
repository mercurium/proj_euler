import time
start = time.time()

lst = [0]*(2*10**6)

sum = 0
count = 0
for i in range(2,len(lst)):
  if lst[i] == 0:
    sum+=i
    for j in range(2*i,len(lst),i):
      lst[j]+= 1
    count +=1
      
print count
print sum

print "Time Taken: " + str(time.time()-start)
