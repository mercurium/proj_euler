#NOTE TODO need to solve it
import time
START = time.time()

def gcd(a,b):
	while a != 0:
		a,b = b%a,a
	return b

SIZE = 10000
sumz = 0
for i in xrange(1,SIZE+1):
	for j in xrange(i+1,SIZE+1):
		if gcd(i,j) == 1:
			sumz += (1./(i*j))* (min(i+j,SIZE) - j+1)

print sumz
print "Time taken:", time.time() - START
