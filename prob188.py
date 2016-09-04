import time
START = time.time()
val   = 1777

for i in xrange(0,1854):
  val = pow(1777, val, 10**6)

print "Answer is:", pow(1777, val, 10**8)
print "Time Taken: ", time.time() - START
