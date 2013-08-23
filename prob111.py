import time
START = time.time()
from primes import mr

mult = 1111111111
successes = set()
sumz = 0
for big_dig in xrange(9,0,-1):
	n = big_dig * mult
	for dig in xrange(0,10):
		for diff in xrange(big_dig-9,big_dig+1):
			m = n - diff*10**dig
			if mr(m) and m > 10**9:
				successes.add(big_dig)
				sumz += m
print "Digits we've seen:", successes
print "Time taken:", time.time() - START

for big_dig in xrange(9,0,-1):
	if big_dig in successes:
		continue
	n = big_dig * mult
	test = False
	for dig in xrange(0,10):
		for dig2 in xrange(0,dig):
			for diff in xrange(big_dig-9,big_dig+1):
				for diff2 in xrange(big_dig-9,big_dig+1):
					m = n - diff*10**dig - diff2*10**dig2
					if mr(m) and m > 10**9:
						successes.add(big_dig)
						sumz += m

print "Digits we've seen:", successes
print "Time taken:", time.time() - START

for dig1 in xrange(1,10):
	n = dig1 * 10**9
	for pow2 in xrange(9):
		for dig2 in xrange(0,10):
			m = n + dig2 * 10**pow2
			if mr(m):
				sumz += m

print sumz
print "Time taken:", time.time() - START
"""
9 can have 9 nines
8 can have 8 eights
7 can have 9 sevens
6 can have 8 sixes
5 can have 8 fives

Congratulations, the answer you gave to problem 111 is correct.
You are the 3407th person to have solved this problem.


"""
