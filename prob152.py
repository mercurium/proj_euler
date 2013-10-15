import time
START = time.time()

MAX_SIZE = 45

inverse = [0,0] + [1./x**2 for x in range(2,MAX_SIZE+1)]
partial_sums = [ sum(inverse[-i-1:]) for i in range( len(inverse) )][::-1]

print [round(x,3) for x in partial_sums]
def recurse(n,sumz):
	if sumz > .5 or n > MAX_SIZE or sumz + partial_sums[n] < .5:
		return 0
	if sumz == .5:
		return 1
	return recurse(n+1,sumz), recurse(n+1, sumz + inverse[n])

print recurse(2,0)
print "Time Taken:", time.time() - START
