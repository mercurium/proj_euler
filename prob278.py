import time
start = time.time()
from bitarray import bitarray

size = 5000
is_prime = bitarray('001' + '10'*(size/2))

primes = {2}
for i in xrange(3,size,2):
	if is_prime[i]:
		for j in xrange(i**2,size,2*i):
			is_prime[j] = False
		primes.add(i)

primes = sorted(primes)
sum_primes = sum(primes)
sumz = 0
for i in xrange(0,len(primes)-2): # prime 1
	for j in xrange(i+1,len(primes)-1): # prime2 
		prime1, prime2 = primes[i],primes[j]
		other_primes = primes[j+1:] # Aggregate all other primes into one.
		sumz += sum(other_primes) * (2 * prime1 * prime2 - prime1 - prime2) - len(other_primes) * prime1 * prime2

print sumz
print "Time Taken", time.time() - start


"""
~/Desktop/python_projects/proj_euler $python prob278.py
1228215747273908452
Time Taken 0.73316192627

Given numbers ab, bc, and ac, with ab being the smallest, we need to construct all possible numbers mod ab. This means that we need bc(a-1) + ac(b-1) to get all possible numbers mod ab. Then subtracting ab, since we don't actually want to hit all of them, we get:

bc(a-1) + ac(b-1) - ab = 2abc - ab -bc -ac

Smallest number not possible to be constructed by ab,bc,ac is:
2abc - ab - bc - ac

Now, to avoid a triple for loop, we take primes a,b, and (c,d,e, ...) and get

( (c,d,e,...) * ( 2 * a* b - a  - b)) - ab * (len((c,d,e,...))) =

2abc - ac - bc - ab +
2abd - ad - bd - ab +
...
etc.

And yeah, that's how I solved it... :)


Similar idea if you consider p and q, smallest number they can not form is pq - p -q
"""
