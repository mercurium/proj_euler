import time
start = time.time()
from primes import *
from bitarray import bitarray

SIZE = 10**3

def gcd(a,b):
	if a == 0:
		return b
	return gcd(b%a,a)

def lcm(a,b):
	return a*b/gcd(a,b)

pfactor = range(0,SIZE+1)
for i in xrange(2,len(pfactor)):
	if pfactor[i] == i:
		for j in xrange(i*2,len(pfactor),i):
			pfactor[j] = i


def rep_dig(n):
	if n == 1:
		return 0
	powz = 1
	while pow(10,powz,n) != 1:
		powz +=1
	return powz
	return val
	

values = [0] * SIZE			
for i in xrange(3,SIZE,2):
	if i%1024 == 0:
		print i
	if i %5 == 0:
		values[i] = values[i/5]
		continue
	if i == pfactor[i]:  #all primes have that 10^p = 1 mod p...
		values[i] = i-1
		continue

	values[i] = rep_dig(i)
	if pfactor[i] != i and values[i] != lcm(rep_dig(pfactor[i]), rep_dig(i/pfactor[i]) ):
		print i, pfactor[i], i/pfactor[i]
		print "And the values were...", rep_dig(i), rep_dig(i/pfactor[i]), rep_dig(pfactor[i])

for i in xrange(2,SIZE,2):
	values[i] = values[i/2]

print sum(values)
print "time taken: " +str(time.time()-start)	


"""
For comparison sake, 139866
is the right answer for size 10^3

"""
