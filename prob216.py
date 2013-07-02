import time
start = time.time()
from bitarray import bitarray
from primes import factor, mr
import sys

size = 10**2
if len(sys.argv) > 1:
	size = int(sys.argv[1])


lst = bitarray('0' * (size+1))

count = 0

for i in xrange(2,size+1):
	if i%10240 == 0:
		print i
	if lst[i] == 0:
		if not mr(2*i*i - 1):
			if i < size//500:
				a = set(factor(2*i**2-1)[:-1])
				for j in a:
					for k in xrange((-i)%j+j,size+1,j):
						lst[k] = 1
					for k in xrange(i,size+1,j):
						lst[k] = 1
			count +=1
	else:
		count +=1

print size -1 - count
print "Time Taken:", time.time() - start


"""
~/Desktop/python_projects/proj_euler $python prob216.py 1000000
141444
Time Taken: 11.5162708759
~/Desktop/python_projects/proj_euler $python prob216.py 50000000
5437849
Time Taken: 924.391628981
"""