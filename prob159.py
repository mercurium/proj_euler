import time
start = time.time()

size = 10**3
pfactor = [0] + [1,2]*(size//2)
for i in xrange(3,size,2):
	if pfactor[i] == 1:
		pfactor[i] = i
		for j in xrange(i**2,size,i*2):
			pfactor[j] = i

def factor(n):
	if n == 0 or n == 1:
		return []
	facts = []
	while n > 1:
		facts += [pfactor[n]]
		n /= pfactor[n]
	return sorted(facts)

def drs(n):
	if n < 10:
		return n
	sumz = 0
	r = 9
	while n > 1 and r > 1:
		while n% r == 0:
			sumz += r
			n /= r
		r -= 1
	val = factor(n)
	for i in xrange(len(val)):
		val[i] = sum([int(x) for x in str(val[i])])
	sumz += sum(val)
	return sumz

def main():
	sumz = 0
	for i in xrange(2,size):
		sumz += drs(i)
		if i %1024 == 0:
			print i
	return sumz
print main() 
print "Time Taken:", time.time() - start
"""
Never mind, this method is not going to work....

"""
