import time
start = time.time()
from primes import mr
import sys

sumz = 0
count = 0
size = 10**6

not_p = [11,17,19,21,23]

if len(sys.argv) > 1:
	size = int(sys.argv[1])

for i in xrange(3,28):
	a = i**2
	if mr(a+1) and mr(a+3) and mr(a+7) and mr(a+9) and mr(a+13) and mr(a+27):
		count +=1
		sumz += i
		print i

for i in xrange(30,size,10):
	if i%3==0 or i%7 == 0 or i%13 == 0:
		continue
	a = i**2
	if mr(a+1) and mr(a+3) and mr(a+7) and mr(a+9) and mr(a+13) and mr(a+27):
		pr = True
		for j in not_p:
			if mr(a+j):
				pr = False
				break
		if pr:
			count +=1
			sumz += i
			print i

print sumz, count
print "Time Taken:", time.time() -start

'""
676333270 12
Time Taken: 226.555887938
"""
