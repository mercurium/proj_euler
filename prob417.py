import time, sys
START = time.time()

SIZE = 10**3 if len(sys.argv) <= 1 else int(sys.argv[1])


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

def rep_dig(n): #Gives the first power of 10 such that 10^k = 1 mod n.
	potential_pows = get_divisors(totient[n])
	for powz in potential_pows:
		if pow(10,powz,n) == 1:
			return powz

values = [0] * SIZE
values[3] = 1
for i in xrange(5,SIZE,2): #Evens are easy to compute, do it later
	if i %1024 == 1: # My counter, once every 1024 to not add too much time to overall computation.
		print i
	if i %5 == 0: # multiples of 5 add no extra digits from the factor of 5.
		values[i] = values[i/5]
		continue
	values[i] = rep_dig(i)

for i in xrange(2,SIZE,2):
	values[i] = values[i/2]

print sum(values)
print "Time Taken:", time.time() - START

"""
For comparison sake, 94288
is the right answer for size 10^3

17:43 ~/Desktop/python_projects/proj_euler $ python prob417.py 1000000
55535191115
time taken: 22.1281189919


446572970925740 (answer)
time taken: 4837.17608619
For comparison sake... LOL, 7200ish seconds on school computer (via ssh) 7214.40327597

Okay, cool. So for this problem, I used the fact that a fraction, 1/n repeats after we can find a 'k' value such that 10^k = 1 mod n. This can be seen to be true since, supposing we have 5 repeating digits for 1/n. Then
1/n = .abcdeabcdeabcde.... And that means that 10^5/n = abcde.abcdeabcde.... Then 99999/n = abcde. This means that 99999 = 0 mod n, and so 10^5 = 1 mod n.

Now that we've established why we need to find 10^k = 1 mod n for all n, we can use Fermat's Little Theorem (a generalization) to tell us that a^k = 1 mod n if and only if 'k' is a divisor of totient(n). Computing this for all numbers, we get the algorithm that we desire. Wins :)

"""
