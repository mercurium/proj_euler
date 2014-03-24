import time
start = time.time()

sumz = 0
for a in xrange(10**2):
    for b in xrange(10**2):
        sumz += min(a,b) /10**3.

print sumz

print "Time Taken:", time.time() - start
