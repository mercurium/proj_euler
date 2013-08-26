import time
START = time.time()
from bitarray import bitarray

def compute(n,a): # This computes what power of a^k is a divisor of n.
	sumz = 0
	n /= a
	while n > 0:
		sumz += n
		n /= a
	return sumz

SIZE = 10**3
MOD  = 10**9+9
is_prime = bitarray('1' * (SIZE+1))
prime_lst = [2]

for i in xrange(3,SIZE,2):  #generic sieve function, as usual, evens aren't worth considering.
	if is_prime[i]:
		for j in xrange(i**2,SIZE,i*2):
			is_prime[j] = False
		prime_lst.append(i)

print len(prime_lst)
print "Time Taken:", time.time() - START

prod = 1
for prime in prime_lst:
	prod *= ( pow(prime,compute(SIZE,prime) * 2, MOD) + 1) # doubling the power since it's a square, and adding 1 since it can divide that square, or it won't
	prod %= MOD

print prod
print "Time Taken:", time.time() - START


"""
~/Desktop/python_projects/proj_euler $python prob429.py
5761455
Time Taken: 45.8516290188 (sieving time)
98792821
Time Taken: 50.4003789425
0.680074563 (sieving time on java)
1.088822096 (full runtime on java)


Okay, cool, so the thing to note about this problem is that if n = p1^k1 * p2^k2 * ... pn^kn, then the divisors d of n such that d and n/d have a gcd of 1 can have all of one power, or not at all. This means that the factors with all powers of pi is either 1 (for pi) or pi^ki. Thus, we take:

(1 + p1^k1) * (1 + p2^k2) * (1 + p3^k3) * .... * (1 + pn^kn) = sum of d satisfying earlier said constraints. Beyond this, the rest of the math is pretty trivial.


"""
