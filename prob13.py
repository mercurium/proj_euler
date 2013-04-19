import string
temp = open('prob13lst.txt','r')

import time
start = time.time()

strz = temp.read()
lst = string.split(strz, '\n')
sum = 0
for i in range(0,len(lst)-1):
  lst[i] = int(lst[i])
  sum = sum + lst[i]
  
print sum / 10**40

print "Time Taken: " + str(time.time()-start)
