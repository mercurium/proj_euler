#NOTE TODO need to solve it
import time
START = time.time()
import sys

MOD = 10**5
sumz = 0

LIM = int(sys.argv[1]) if len(sys.argv) > 1 else 6

def find_rep_dig(n,LIM):
    for i in xrange(len(str(n)),LIM+1):
        if pow(10,i,n) == 1:
            return 10**i / n
    return -1

for i in xrange(3,100,2):
    if i %5 == 0:
        continue
    print find_rep_dig(i,100), i




print sumz % MOD
print "Time Taken:", time.time() - START
