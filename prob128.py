import time
start = time.time()
from primes import m_r

rings = [1] + [3*x*(x-1)+2 for x in xrange(1,100000)]

sol = [0,1]
for i in xrange(2,len(rings)-2):
	val = m_r(rings[i+1] - rings[i] +1) + \
		m_r(rings[i+2] -rings[i] -1) + \
		m_r(rings[i+1] - rings[i] -1)
	if val == 3:
		sol += [rings[i]]

for i in xrange(2,len(rings)-2):
	a = rings[i] -1
	val = m_r(a - rings[i-1]) + \
		m_r(a -rings[i-2]) + \
		m_r(rings[i+1] - 2 - a) 
	if val == 3:
		sol += [a]

sol.sort()
print len(sol)
if len(sol) > 2000:
	print sol[1999]
print sol[:10]
print "Time Taken:", time.time() - start

"""
13:57 ~/Desktop/python_projects/proj_euler $ python prob128.py 
2635
14516824220
[0, 1, 8, 19, 20, 37, 61, 128, 217, 271]
Time Taken: 1.24889087677

Interesting thing to note, the only time it has a chance of 3 prime differences is when it's at the very beginning or very end of a loop... :x. After that, rest is easy.

"""
