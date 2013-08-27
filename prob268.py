import time
START = time.time()
import sys
from primes import factor


SIZE = 10**2 if len(sys.argv) == 1 else int(sys.argv[1]) 
LIM = 4

primes = [2, 3, 5 , 7 ]#, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def recurse(pos,primes, count, lim):
	if count > lim:
		return 0
	if pos == len(primes):
		return 1
	v1 = recurse(pos+1,primes,count, lim) * (primes[pos]-1)
	v2 = recurse(pos+1,primes,count+1,lim)
	print primes[pos], v1,v2, count
	return v1+v2


prod = 1
for prime in primes:
	prod *= prime
ans = recurse(0,primes,0, LIM)

print ans
ans = ans/prod

print ans
print SIZE - ans 

print "Time Taken:", time.time() - START


actual_count = 0

lst = [0] * SIZE
for i in xrange(2, min(primes[-1]+1,SIZE)):
	if lst[i] == 0:
		for j in xrange(i,SIZE,i):
			lst[j] +=1

for i in range(1,SIZE):
	if lst[i] >= LIM:
		actual_count +=1

print "There were actually...", actual_count, "items... \n\n\n"

