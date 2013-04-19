import time
start = time.time()

lst = [0] * 150000
count = 0
for i in range(2,len(lst)):
  if lst[i] == 0:
    for n in range(i*2,len(lst),i):
      lst[n]+=1
    count+=1
  if count == 10001:
    print i
    break
    
print "Time Taken: " + str(time.time()-start)
