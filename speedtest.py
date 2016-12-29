import time
START = time.time()
SIZE  = 10**9

sumz = 0
for i in xrange(SIZE):
  sumz += i

print sumz
print "Time Taken:", time.time() - START
