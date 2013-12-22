import time
START = time.time()
from primes import m_r
SIZE = 10**5

def pfactor_gen(size): #for each number n, return some factor of it.
	stuff = [0,1,2] + [1,2] *(size/2-1)
	for i in xrange(3,size,2):
		if stuff[i] == 1:
			for j in xrange(i**2,size,i*2):
				stuff[j] = i
			stuff[i] = i
	return stuff

pfactor = pfactor_gen(SIZE+1)

def factor(n): #simple factoring method, put one of the factors of n onto the list until we run out of factors
	if n == 1:
		return []
	if pfactor[n] == n:
		return [n]
	factors = []
	while pfactor[n] != 1:
		factors.append(pfactor[n])
		n /= pfactor[n]
	return factors	
print "Time Taken:", time.time() - START


START = time.time()
sumz = 0
for i in xrange(3, SIZE+1):
	if pfactor[i] == i:
		sumz +=1
		continue
	sval = sumz
	factors = factor(i)
	for j in xrange(i-factors[-1],i//2-1, -factors[-1]):
		if j+2 != i and ((j+1)**2 -1) % i == 0:
			sumz +=j+1
			#print i,j+1
			break
		if ((j-1)**2 -1) % i == 0:
			sumz +=j-1
			#print i,j-1
			break
	if sval == sumz:
		sumz +=1
		#print i, 1
print sumz

print "Time Taken:", time.time() - START

"""
Solve the problem of... x^2 = 1 mod n...
(x+1)(x-1) = 0 mod n... dammit. I should have something in my book about this T.T....


"""
