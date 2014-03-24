import time
start = time.time()
import sys

def gcd(a,b):
    if a == 0:
        return b
    return gcd(b%a,a)

if len(sys.argv) > 1:
    size = int(sys.argv[1])
else:
    size = 10**2

prs = range(size+1)
for i in xrange(2,size+1):
    if prs[i] == i:
        for j in xrange(i,size+1,i):
            prs[j] = (prs[j] * (i-1))/i

for j in xrange(2,size+1):
    a = j-prs[j]
    if a/gcd(a,j-1) == 1 and prs[j] != j-1:
        print j, a


print "Time Taken:", time.time() -start
