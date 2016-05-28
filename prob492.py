#NOTE TODO need to solve it
import time
START = time.time()

MOD = 107

n = 1
values = set([1])
for i in xrange(2,10**7):
  n = (6*n**2 + 10*n+3) % MOD
  if n in values:
    print i
    break
  values.add(n)

print "Time Taken:", time.time() - START
