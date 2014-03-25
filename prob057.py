import string
import time

START = time.time()
N = 1000

a,b = 1,2
count = 0
iterations = 0
for i in xrange(N,0,-1):
    b_n = 2*b+a
    a,b = b,b_n
    if len(str(b-a)) > len(str(a)):
        count += 1
    iterations += 1
print count, iterations

print "Time Taken: " + str(time.time() - START)
