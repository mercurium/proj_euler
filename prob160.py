import time
START = time.time()
from math import factorial as fact

def fa(n, ignore = False):
	if n == 0 or n == 1:
		return 1
	prod = 1
	for i in xrange(2,n+1):
		if ignore and i % 10 == 0:
			continue
		prod *= i
		while prod % 10 == 0:
			prod /= 10
		prod = prod % (10**5)
	return prod

val = fa(10**5, True)
#last 4 digits of factorial(10**5) are 2496
print val
print pow(val,10**7,10**10)
print "Time Taken:", time.time() -START



#ahh, dammit >.>;; The reason for the incongrinuity... is because if we have like... 12300000000, it becomes 123, not another random number we cancel out... T___T


#okay, so I'm going to test first ignoring all numbers that are divisible by 10, then move up to ignoring those divisible by 100, then 1000, etc.
