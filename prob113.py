import time
START = time.time()
from math import factorial as fa

def ncr(n,r):
    return fa(n) / (fa(r) * fa(n-r))

def total_inc_dec(x):
    count = 0
    for i in xrange(1,x+1):
        count += ncr(i+8,i)
        count += ncr(i+9,i)
        count -= 10
        print i, count
    return count

print total_inc_dec(100)
print "Time taken:" , time.time() - START
