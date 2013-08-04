import time
start = time.time()

SIZE = 10**6
LIM = 1000

pfactor = range(SIZE)
for i in xrange(4,SIZE,2):
	pfactor[i] = 2
for i in xrange(3,SIZE,2):
	if pfactor[i] == i:
		for j in xrange(i**2,SIZE,2*i):
			pfactor[j] = i

def factor(n):
	factors = []
	while n > 1:
		factors.append(pfactor[n])
		n /= pfactor[n]
	return sorted(factors)


for num in xrange(3,SIZE):
	if num == pfactor[num]:
		continue
	factors = factor(num)
	factor_map = dict()
	factor_set = set(factors + [2,3,5,7])
	factor_map[2] = 5
	factor_map[3] = 3
	factor_map[5] = 3
	factor_map[7] = 3
	for f in factors:
		if f not in factor_map:
			factor_map[f] = 3
		else:
			factor_map[f] +=2	
	prod = 1
	numz = 1
	for f in factor_set:
		prod *= factor_map[f]
		numz *= f**(factor_map[f]-1)
	if prod/2 >= LIM:
		print prod, int(numz**.5+ .5)
		break
print "Time Taken:", time.time() - start


"""
WOWWW I was being stupid... ;___;

Congratulations, the answer you gave to problem 108 is correct.

You are the 6407th person to have solved this problem.

13:54 ~/Desktop/python_projects/proj_euler $ python prob108.py 
2025 180180
Time Taken: 0.944803953171
"""
