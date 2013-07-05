import time
start = time.time()
import sys

mod = 10**5
sumz = 0
if len(sys.argv) > 1:
	lim = int(sys.argv[1])
else:
	lim = 6

for n in xrange(1,lim):
	for i in xrange(10**n, 10**(n+1)/2):
		a = i/10 + (i%10)*10**n
		if a%i == 0:
			print i, a
			sumz += i

print sumz % mod
print "Time Taken:", time.time() - start
