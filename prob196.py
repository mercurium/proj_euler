import time
START = time.time()
from primes import m_r

pos = [8,9] # 5678027

def neighbors(n,row):
	row_start = row*(row-1)/2 + 1
	pos = n - row_start
	lower, upper = (row-1)*(row-2)/2 +1, row*(row+1)/2+1
	if pos != 0:
		neighbors = [lower+pos-1, lower+pos, lower+pos+1, upper+pos-1, \
				upper+pos, upper + pos +1]
	else:
		neighbors = [lower,lower+1,upper,upper+1]
	return neighbors	

sumz = 0
for p in pos:
	for i in xrange(p*(p-1)/2+1, p*(p+1)/2):
		if m_r(i):
			neigh_sum = sum([m_r(x) for x in neighbors(i,p)])
			if neigh_sum >= 2:
				sumz += i
				print i
print sumz
print "Time Taken:", time.time() - START
