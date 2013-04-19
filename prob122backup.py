import time
start = time.time()

lst = range(0,200)
items = [set()]*200
for i in range(0,len(lst)/2-1):
  lst[2*i+1] = lst[i]+1
  items[2*i+1].add(i)
  items[2*i+1] = items[i].union(items[2*i+1])

for i in range(0,len(lst)-1):
  if lst[i]+1 < lst[i+1]:
    lst[i+1] = lst[i]+1
print lst[:15]

sum = 0
for i in range(1,len(lst)):
  sum += lst[i]
print sum


print "Time Taken: " + str(time.time()-start)
