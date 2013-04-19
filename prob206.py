import string
import math
import time
startz = time.time()
start = 101010103
end = 138935382

done = 0
for i in range(start,end,10):
  j = str(i**2)
  if j[2]=='2' and j[4]=='3' and j[6]=='4' and j[8]=='5' and j[10]=='6' and j[12]=='7' and j[14]=='8':
   print i
   done = 1
   break
if done ==0:
  for i in range(start+4,end,10):
    j = str(i**2)
    if j[2]=='2' and j[4]=='3' and j[6]=='4' and j[8]=='5' and j[10]=='6' and j[12]=='7' and j[14]=='8':
     print i
     break

print "done"

#answer = 1389019170
print "Time Taken: " + str(time.time()-startz)
