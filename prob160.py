#NOTE TODO need to solve it
import time
START = time.time()
from math import factorial as fact


POWER = 12 
MOD_POW = 5
MOD = 10**MOD_POW
SIZE = 10**POWER

#second parameter is for if we want to ignore the multiples of 10. 1=ignore,0 = don't ignore.
def fa(n, ignore_10=0): 
	if n == 0 or n == 1:
		return 1
	prod = 1
	two_count = 0
	for i in xrange(2,n+1):
		a = i
		if i%10==0 and ignore_10:
			continue
		while a%2 == 0:
			a /= 2
			two_count += 1
		while a%5 == 0:
			a /= 5
			two_count -= 1
		prod = (prod * a)% MOD
	prod = (pow(2,two_count,MOD) * prod)% MOD
	return prod


val = fa(MOD,1)
print val

POWER_NECS = sum(10**x for x in xrange(POWER-MOD_POW+1))
print POWER_NECS
vals_after = fa(MOD/10)
print (pow(val,POWER_NECS,MOD) * vals_after)%MOD 
print "Time Taken:", time.time() -start



"""
ahh, dammit >.>;; The reason for the incongrinuity... is because if we have like... 12300000000, it becomes 123, not another random number we cancel out... T___T
okay, so I'm going to test first ignoring all numbers that are divisible by 10, then move up to ignoring those divisible by 100, then 1000, etc.
"""
