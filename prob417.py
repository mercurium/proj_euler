import time
start = time.time()
import sys

if len(sys.argv) > 1:
	SIZE = int(sys.argv[1])
else:
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

def get_totient(size):  #gives you the totients of all numbers i <= size
	lst = range(size+1)
	lst[0] = 1
	for i in xrange(2,len(lst)):
		if lst[i] == i:
			for j in xrange(i,len(lst),i):
				lst[j] = (lst[j] * (i-1))/i 
	return lst
totient = get_totient(SIZE)


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
	potential_pows = get_divisors(totient[n])
	for powz in potential_pows:
		if pow(10,powz,n) == 1:
			return powz

values = [0] * SIZE
values[3] = 1
for i in xrange(5,SIZE,2):
	if i %1024 == 1:
		print i
	if i %5 == 0:
		values[i] = values[i/5]
		continue
	values[i] = rep_dig(i)

for i in xrange(2,SIZE,2):
	values[i] = values[i/2]

print sum(values)
print "time taken: " +str(time.time()-start)	


"""
For comparison sake, 94288
is the right answer for size 10^3

17:43 ~/Desktop/python_projects/proj_euler $ python prob417.py 1000000
55535191115
time taken: 22.1281189919


446572970925740 (answer)
time taken: 4837.17608619
For comparison sake... LOL, 7200ish seconds on school computer (via ssh) 7214.40327597


"""
