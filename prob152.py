import time
START = time.time()

MAX_SIZE = 35

inverse = [0,0] + [1./x**2 for x in range(2,MAX_SIZE+1)]
partial_sums = [ sum(inverse[-i-1:]) for i in range( len(inverse) )][::-1]

primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]

print [round(x,3) for x in partial_sums]
def recurse(n,sumz):
	if sumz > .5 or n > MAX_SIZE or sumz + partial_sums[n] < .5:
		return 0
	if sumz == .5:
		return 1
	if n > MAX_SIZE//2 and n in primes:
		return recurse(n+1,sumz)
	return recurse(n+1,sumz), recurse(n+1, sumz + inverse[n])

print recurse(2,0)
print "Time Taken:", time.time() - START
