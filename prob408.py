#NOTE TODO need to solve it
import time
start = time.time()
import operator as op
import sys

precompute = dict()
def extended_gcd(a, b): #returns c,d such that ac+bd =1
	if b == 0:
		return (1, 0)
	if b== MOD and a in precompute:
		return precompute[a]
	else:
		q, r = a/b, a%b
		s, t = extended_gcd(b, r)
		if b == MOD:
			precompute[a] = (t,s-q*t)
		return (t, s - q * t)
ext_gcd = extended_gcd


def ncr(n, r):
	r = min(r, n-r)
	if r == 0: return 1
	num = 1
	for i in xrange(1,r+1):
		num = (num * (n-i+1)) % MOD
		num = (num * ext_gcd(i,MOD)[0])
	return num


MOD = 10**9 + 7
lst = []
vals = dict()
count = 0
SIZE = 1000 if len(sys.argv) < 2 else int(sys.argv[1])
for i in range(1, int(SIZE**.5)+1):
	I = i**2
	for j in range(1,i):
		J = j**2
		if (I + J)**.5 %1 == 0:
			count +=1
			lst.append((I,J))
			sumz = 0
			for a,b in vals.keys():
				if a <= J and b <= I:
					sumz += (vals[(a,b)] * ncr((I-b) + (J-a), J-a)) % MOD
				if b <= J and a <= I:
					sumz += (vals[(a,b)] * ncr((I-a) + (J-b), (J-b))) % MOD
			vals[(I,J)] = (ncr(I+J,J) - sumz) % MOD
			print I, J, vals[(I,J)], len(vals.keys()), len(precompute.keys())

print "There are", count*2, "inadmissible points"
print "Time Taken:", time.time() - start

sumz = 0
for a,b in lst:
	sumz += (vals[(a,b)] * (ncr(2*SIZE-a-b,SIZE-a) + ncr(2*SIZE-a-b,SIZE-b))) % MOD
	print (a,b)
print (ncr(SIZE*2,SIZE) - sumz) % MOD


print "Time Taken:", time.time() - start
