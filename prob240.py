import time
start = time.time()

size = 6
lst1 = [1]*size + [0]*(100-size)
lst2 = [0]*100



for k in range(1,3): #counting distribution of pete
  for i in range(1,size+1):
    for j in range(0,len(lst1)-i):
      lst2[i+j] += lst1[j]
  lst1 = lst2[:]
  lst2 = [0]*(100)
print lst1[14]



print "Time Taken: " + str(time.time() -start)
