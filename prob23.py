import string
import time
start = time.time()

lst = [1]*20162
for i in range(2,len(lst)):
  for j in range(2*i,len(lst),i):
    lst[j] += i
abu = set()
for i in range(12,len(lst)):
  if lst[i] > i:
    abu.add(i)
    
print len(abu)
abu = list(abu)
abu.sort()
set2 = set()


for i in range(0,len(abu)):
  for j in range(i,len(abu)):
    if abu[i]+abu[j] > 20162:
      break
    set2.add(abu[i]+abu[j])
set2 = list(set2)

print 20162*20163/2 - sum(set2)
print "time taken: " +str(time.time()-start)  






