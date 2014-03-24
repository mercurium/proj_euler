import string
import time
start = time.time()

temp = open('prob22inputz.txt','r')
inputz = string.split(temp.read().strip(),',') 
inputz.sort()

sumz = 0
for i in xrange(0,len(inputz)):
    wd_sum = sum([ord(x) -64 if x!='"' else 0 for x in inputz[i] ])
    sumz =sumz + wd_sum * (i+1)

print sumz, len(inputz)
print "Time Taken: ", time.time()-start
