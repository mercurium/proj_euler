import time
START = time.time()

n = 290797
MOD = 50515093
SIZE = 10**6

sumz = 0
min_val = [] # (value, index)
next_val = (n**2)% MOD
for i in xrange(SIZE):
	for j in xrange(len(min_val)):
		if min_val[j][0] > next_val:
			min_val = min_val[:j]
			break
	min_val.append((next_val,i))

	for num in xrange(len(min_val)-1,0,-1):
		sumz += min_val[num][0] * (min_val[num][1] - min_val[num-1][1])
	sumz += min_val[0][0] * (min_val[0][1]+1)

	next_val = (next_val**2)%MOD


print sumz
print "Time Taken:", time.time() - START

