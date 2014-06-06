#NOTE TODO need to solve it
from itertools import permutations
import time
START = time.time()

for lenz in range(1,11):
	count = [0,0,0,0,0,0,0,0,0]

	for perm in permutations('0123456789'[:lenz]):
		vals = set()
		maxz = 0
		size = 0
		for i in perm:
			vals.add(int(i))
			size +=1
			if int(i)-1 in vals:
				size -=1
			if int(i)+1 in vals:
				size -=1
			if size > maxz:
				maxz = size
		count[maxz] +=1
	print lenz, '\t', count[1:-3]


"""
1 	[1, 0, 0, 0, 0]
2 	[2, 0, 0, 0, 0]
3 	[4, 2, 0, 0, 0]
4 	[8, 16, 0, 0, 0]
5 	[16, 92, 12, 0, 0]
6 	[32, 472, 216, 0, 0]
7 	[64, 2312, 2520, 144, 0]
8 	[128, 11104, 24480, 4608, 0]
9 	[256, 52880, 216432, 90432, 2880]
10 	[512, 250912, 1815264, 1418112, 144000]

size = k
first term is 2^(k-1)
last term for odd numbers is ((k+1)/2)! * ((k-1)/2)! 
For evens, last term = 2(k/2)! * (k/2-1)! *(k/2)^2

"""

