import time
start = time.time()
from primes import *
from bitarray import bitarray

SIZE = 10**3

def gcd(a,b):
	if a == 0:
		return b
	return gcd(b%a,a)
def lcm(a,b):
	return a*b/gcd(a,b)

def get_plst(size):  #returns a list of numbers, each of which are a prime factor of the ith element in the list.
	lst = range(size+1)
	lst[0] = 1
	for i in xrange(2,len(lst),2):
		lst[i] = 2
	for i in xrange(3,len(lst),2):
		if lst[i] == i:
			for j in xrange(i**2,len(lst),2*i):
				lst[j] = i
	return lst

plst = get_plst(SIZE)

def pfactor(n): #returns the entire list of prime factors of n
	factors = []
	while n > 1:
		factors += [plst[n]]
		n /= plst[n]
	return sorted(factors)

def get_divisors(n): # returns all divisors of n.
	factors = pfactor(n)
	divisors = set([1])
	for f in factors:
		new_set = set()
		for d in divisors:
			new_set.add(f*d)
		for i in new_set:
			divisors.add(i)

	return sorted(list(divisors))



def rep_dig(n):
	powz = 1
	while pow(10,powz,n) != 1:
		powz +=1
	return powz
	return val

	

values = [0] * SIZE			
for i in xrange(3,SIZE,2):
	if i%1024 == 0:
		print i
	if i %5 == 0:
		values[i] = values[i/5]
		continue
	if i == pfactor[i]:  #all primes have that 10^p = 1 mod p...
		values[i] = i-1
		continue
	values[i] = rep_dig(i)

for i in xrange(2,SIZE,2):
	values[i] = values[i/2]

print sum(values)
print "time taken: " +str(time.time()-start)	


"""
For comparison sake, 139866
is the right answer for size 10^3

"""
