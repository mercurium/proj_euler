import string
import time
start = time.time()

temp = open('prob22lst.txt','r')
lst = string.split(temp.read().strip(),',') 
lst.sort()

sumz = 0
for i in range(0,len(lst)):
  wd_sum = sum([ord(x) -64 if x!='"' else 0 for x in lst[i] ])
  sumz =sumz + wd_sum * (i+1)

print sumz, len(lst)
print "Time Taken: ", time.time()-start
