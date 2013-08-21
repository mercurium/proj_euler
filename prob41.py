from primes import mr
import time
from itertools import permutations
import string


START = time.time()

#sum from 1 to 8 = 36, sum from 1 to 9 is 45, so if we went from 1 to 8 or 1 to 9, it would be divisible by 3.
permutation = permutations(['1','2','3','4','5','6','7'],7)
maxz = 0
for perm in permutation:
	n = int(string.join(perm, ''))
	if n > maxz and mr(n):
		maxz = n
print maxz
print "Time Taken:", time.time() -START
