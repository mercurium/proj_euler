import time
START = time.time()
def compute(n):
	sumz = 0
	n /= 5
	while n > 0:
		sumz += n
		n/= 5
	return sumz

count = 0
SIZE = 10**3
for i in xrange(5,SIZE+ 1,5):
	if compute(2*i-1) < 2*compute(i):
		print i,2*i-1, compute(2*i-1), 2*compute(i), 2*compute(i) - compute(2*i-1)
		count +=1

print "There were:", count, "under", SIZE

print "Time taken:", time.time() - START
