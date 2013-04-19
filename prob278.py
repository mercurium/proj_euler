import time
start = time.time()
from bitarray import bitarray

size = 5000
tmp = bitarray('110' + '01'*(size/2))

primes = {2}
for i in xrange(3,size,2):
	if tmp[i] == 0:
		for j in xrange(i**2,size,2*i):
			tmp[j] = 1
		primes.add(i)

primes = sorted(list(primes))
sum_primes = sum(primes)
sumz = 0
for i in range(0,len(primes)-2):
	for j in range(i+1,len(primes)-1):
		sumz += sum(primes[j+1:])*(primes[i]*primes[j]*2-primes[j]-primes[i]) - len(primes[j+1:])*primes[i]*primes[j]

print sumz
print "Time Taken", time.time() - start


"""
~/Desktop/python_projects/proj_euler $python prob278.py
1228215747273908452
Time Taken 0.73316192627

Given numbers ab, bc, and ac, with ab being the smallest, we need to construct all possible numbers mod ab. This means that we need bc(a-1) + ac(b-1) to get all possible numbers mod ab. Then subtracting ab, since we don't actually want to hit all of them, we get:

bc(a-1) + ac(b-1) - ab = 2abc - ab -bc -ac


Similar idea if you consider p and q, smallest number they can not form is pq - p -q
"""
