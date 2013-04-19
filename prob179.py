import time
start = time.time()

lst = [0] * (10**7)

for i in range(2,len(lst)):
  for j in range(i, len(lst), i):
    lst[j] += 1

count = 0
for i in range(2,len(lst)-1):
  if lst[i] == lst[i+1]:
    count += 1
print count
print "Time Taken: " + str(time.time()-start)


#~/Desktop/python_projects/proj_euler $python prob179.py
#986262
#Time Taken: 64.1562099457
