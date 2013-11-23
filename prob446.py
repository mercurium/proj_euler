import time
from primes import m_r
START = time.time()

count = 0
SIZE = 1024
mod = 10**9 +7


def gcd(a,b):
	while a != 0:
		a,b = b%a, a
	return b

def pollard_rho(n):
	def func(x):
		return (x**2+1)%n
	def func2(x):
		return (x**2+3)%n
	x,y = 2,2
	d = 1
	while d==1: 
		x = func(x)
		y = func(func(y))
		d = gcd(abs(x-y),n)
	
	
	if d==n:
		d=1
		while d==1:
			x = func2(x)
			y = func2(func2(y))
			d = gcd(abs(x-y),n)
	return d

small_primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,113,127,131,137,139,149,151,157,163,167]

def factor(n):
	if m_r(n):
		return [n]
	factor_lst = []
	for i in small_primes:
		while n % i == 0:
			factor_lst.append(i)
			n /= i
	while n != 1:
		if m_r(n):
			return (factor_lst + [n])
		d = pollard_rho(n)
		while n % d == 0:
			factor_lst.append(d)
			n /= d
	return factor_lst


for n in range(1,SIZE+1):
	val_dict = dict()
	a, b = n**2 - 2*n +2, n*n +2*n+2
	factors = factor(a) + factor(b)
	for p in factors:
		if p in val_dict:
			val_dict[p] +=1
		else:
			val_dict[p] = 1
	prod = 1
	for f in val_dict.keys():
		prod = ((1 + pow(f, val_dict[f],mod)) * prod) % mod
	count += prod - (n**4+4)% mod
	if n% 1024 == 0:
		print n, time.time() - START

print count %mod
print "Time Taken:", time.time() - START
