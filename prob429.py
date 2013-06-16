import time
start = time.time()
from bitarray import bitarray

def compute(n,a):
	sumz = 0
	n /= a
	while n > 0:
		sumz += n
		n /= a
	return sumz

size = 10**3
mod  = 10**9+9
vals = bitarray('0' * (size+1))
prime_lst = [2]

for i in xrange(3,size,2):
	if vals[i] == 0:
		for j in xrange(i**2,size,i*2):
			vals[j] = 1
		prime_lst.append(i)

print len(prime_lst)
print "Time Taken:", time.time() - start

prod = 1
for prime in prime_lst:
	prod *= (pow(prime,compute(size,prime)*2,mod)+1)
	prod %= mod

print prod
print "Time Taken:", time.time() - start


"""
~/Desktop/python_projects/proj_euler $python prob429.py
5761455
Time Taken: 45.8516290188 (sieving time)
98792821
Time Taken: 50.4003789425
0.680074563 (sieving time on java)
1.088822096 (full runtime on java)


"""
